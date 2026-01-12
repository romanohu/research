# AGENT.md — Marp Slide Generation Agent

## Purpose
Read user instructions and/or provided Markdown (notes, drafts, specs) and generate a **Marp-compatible presentation Markdown**.  
Whenever possible, **embed CSS and (if needed) JavaScript into a single `.md` file** to keep distribution and maintenance simple.

## Inputs
- User instructions (e.g. goal, audience, duration, tone, slide count, structure, key messages)
- Reference Markdown (optional: existing docs, meeting notes, design memos, README, etc.)
- Style requirements if any (company template, colors, fonts, logo, spacing, chart policy)

## Outputs
- `*.md` (Marp format)
  - Front matter at the top (`marp: true`, etc.)
  - **Embedded `<style>` for CSS** (theme and overrides)
  - **Embedded `<script>` for JS if required** (mainly for HTML output)
- outputfolder
  - `.workspace/`

## Default Principles
- One slide = one message.
- Keep information density low.
- Structure slides as: Heading → 3 key points → optional details.
- Prefer short sentences and bullet points; keep terminology consistent.
- Always include at least: Title / Agenda / Section breaks / Summary / Q&A.
- Use Mermaid for diagrams when appropriate and allowed.

## Generation Workflow
1. Respect explicitly provided **goal, audience, and duration**.  
   If missing, assume:
   - 10 minutes → 10–12 slides
   - 20 minutes → 15–20 slides
2. If reference Markdown is provided, extract an outline and key points.
3. Convert the outline into slides, removing redundancy and adding examples/diagrams where useful.
4. Apply layout and readability adjustments via CSS (spacing, code, tables, images).
5. Add JavaScript only when truly necessary (interactive elements, demos, light animations).
6. Final pass: align tone, terminology, notation, and pagination.

## Marp Front Matter Template
Use this at the top of generated files unless instructed otherwise:

---
marp: true
theme: default
paginate: true
size: 16:9
---

Notes:
- Prefer `default`, `gaia`, or `uncover` themes unless specified.

## Embedded CSS (Single-file Operation)
Marpit/Marp treats `<style>` blocks inside Markdown as theme CSS, enabling **single-file operation without external CSS**.

Example (place right after front matter):

<style>
/* Base adjustments */
section {
  font-size: 28px;
}
h1 { letter-spacing: 0.02em; }
ul { margin-top: 0.6em; }
code { font-size: 0.9em; }
</style>

Guidelines:
- Prioritize readability (font size, line height, spacing).
- Code blocks and tables should be larger with generous spacing.
- For Japanese or dense text, avoid overpacking—use whitespace.

## Embedded JavaScript (Only If Necessary)
Marp Markdown can include client-side JavaScript when rendered as HTML.  
Note: **JS is usually disabled or ignored in PDF exports**, so clearly state when HTML output is required and provide a non-JS fallback if possible.

Example (HTML-oriented):

<script>
document.addEventListener('DOMContentLoaded', () => {
  // Example: lightweight slide-specific behavior
});
</script>

## Constraints & Notes
- There is no standard front-matter directive for loading external CSS; for single-file usage, embedding `<style>` is recommended.
- Prefer relative paths for images. Depending on distribution, consider embedding images as data URIs.
- The output must remain **valid Marp-compatible Markdown** (proper slide separators `---`, directives, etc.).

## Recommended Slide Structure
1. Title (topic / presenter / date)
2. Agenda (3–6 items)
3. Main content with section divider slides
4. Summary (3 key takeaways)
5. Next actions (if any)
6. Q&A

## Final Checklist
- No slide is too text-heavy.
- Terminology and phrasing are consistent.
- Diagrams, tables, and code are readable at presentation size.
- Conclusions match the initial objectives.

---
(This agent generates Marp presentation Markdown according to this AGENT.md.)
