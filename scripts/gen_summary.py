#!/usr/bin/env python3
"""
Generate SUMMARY.md for mdBook by enumerating .md files in ascending order.

Rules:
- Only .md files
- Skip SUMMARY.md itself and the root index.md (handled separately)
- Exclude directories: book, config/templates, .git, target, node_modules, __pycache__
- Directory entries are shown as plain titles (no link); files are linked
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import List, Optional

EXCLUDE_DIRS = [
    "book",
    "config/templates",
    ".git",
    ".codex",
    ".workspace",
    "01_dailymemo",
    "target",
    "node_modules",
    "__pycache__",
]


def read_title(md_path: Path) -> str:
    """Extract first level-1 heading; fallback to filename stem."""
    heading_re = re.compile(r"^#\s+(.*)\s*$")
    link_re = re.compile(r"\[(?P<text>[^\]]+)\]\([^)]+\)")
    try:
        with md_path.open("r", encoding="utf-8") as f:
            for _ in range(50):  # avoid reading huge files
                line = f.readline()
                if not line:
                    break
                m = heading_re.match(line)
                if m:
                    title = m.group(1).strip()
                    title = link_re.sub(r"\g<text>", title)
                    if title:
                        return title
    except OSError:
        return md_path.stem
    return md_path.stem


def node_title(md_path: Path, parent_name: Optional[str] = None) -> str:
    if md_path.name == "index.md" and parent_name:
        heading = read_title(md_path)
        return heading if heading and heading != md_path.stem else parent_name
    return read_title(md_path)


def is_excluded(path: Path, root: Path) -> bool:
    resolved = path.resolve()
    for ex in EXCLUDE_DIRS:
        if resolved.is_relative_to((root / ex).resolve()):
            return True
    return False


def build_tree(directory: Path, root: Path) -> Optional[dict]:
    if directory.name.startswith(".") or is_excluded(directory, root):
        return None

    children: List[dict] = []
    entries = sorted(directory.iterdir(), key=lambda p: (p.is_file(), p.name))

    index_file = directory / "index.md"
    index_exists = index_file.exists() and not is_excluded(index_file, root)

    for entry in entries:
        if entry.is_dir():
            node = build_tree(entry, root)
            if node and node.get("children"):
                children.append(node)
        else:
            if entry.suffix != ".md":
                continue
            if entry.name.startswith("."):
                continue
            if entry.name in {"SUMMARY.md", "index.md"}:
                continue
            if is_excluded(entry, root):
                continue
            children.append(
                {
                    "title": node_title(entry, parent_name=entry.parent.name),
                    "path": entry.relative_to(root),
                    "children": [],
                    "is_dir": False,
                }
            )

    if not children and not index_exists:
        return None

    if index_exists:
        node_path = index_file.relative_to(root)
        children_for_node = children
        title = node_title(index_file, parent_name=directory.name)
    else:
        node_path = children[0]["path"] if children else None
        children_for_node = [c for c in children if c.get("path") != node_path]
        title = directory.name

    return {
        "title": title,
        "path": node_path,
        "children": children_for_node,
        "is_dir": True,
    }


def render_tree(node: dict, depth: int = 0) -> List[str]:
    lines: List[str] = []
    indent = "  " * depth
    if node["is_dir"]:
        if node["path"]:
            rel = node["path"].as_posix()
            lines.append(f"{indent}- [{node['title']}]({rel})")
        else:
            lines.append(f"{indent}- {node['title']}")
        for child in node["children"]:
            lines.extend(render_tree(child, depth + 1))
    else:
        rel = node["path"].as_posix()
        lines.append(f"{indent}- [{node['title']}]({rel})")
    return lines


def write_summary(root: Path, output: Path) -> int:
    nodes: List[dict] = []
    entries = sorted(root.iterdir(), key=lambda p: (p.is_file(), p.name))
    for entry in entries:
        if entry.is_dir():
            node = build_tree(entry, root)
            if node:
                nodes.append(node)
        else:
            if entry.suffix != ".md":
                continue
            if entry.name in {"SUMMARY.md", "index.md"}:
                continue
            nodes.append(
                {
                    "title": node_title(entry, parent_name=root.name),
                    "path": entry.relative_to(root),
                    "children": [],
                    "is_dir": False,
                }
            )

    lines: List[str] = ["# Summary", ""]
    index_path = root / "index.md"
    index_title = node_title(index_path, parent_name=root.name) if index_path.exists() else root.name
    lines.append(f"- [{index_title}](index.md)")

    count = 1  # index.md
    for node in nodes:
        lines.extend(render_tree(node, depth=1))
        # count file nodes in rendered subtree
        def count_files(n: dict) -> int:
            if n["is_dir"]:
                return sum(count_files(c) for c in n["children"])
            return 1

        count += count_files(node)

    output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return count


def main():
    parser = argparse.ArgumentParser(description="Generate SUMMARY.md for mdBook")
    parser.add_argument("--root", type=Path, default=Path("book_src"), help="Root directory containing mdBook content")
    parser.add_argument("--output", type=Path, default=Path("book_src/SUMMARY.md"), help="Output SUMMARY.md path")
    args = parser.parse_args()

    root = args.root.resolve()
    output = args.output.resolve()

    count = write_summary(root, output)
    print(f"Wrote {count} entries to {output.relative_to(root)}")


if __name__ == "__main__":
    main()
