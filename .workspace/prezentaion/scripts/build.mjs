import { spawnSync } from "node:child_process";
import { existsSync, mkdirSync } from "node:fs";
import path from "node:path";

const mode = process.argv[2];
const input = process.argv[3];

const allowedModes = new Set(["html", "pdf", "pptx", "standalone"]);

if (!allowedModes.has(mode)) {
  console.error("Usage:");
  console.error("  npm run pdf -- <path/to/slides.md>");
  console.error("  npm run html -- <path/to/slides.md>");
  console.error("  npm run pptx -- <path/to/slides.md>");
  console.error("  npm run standalone -- <path/to/slides.md>");
  process.exit(1);
}

if (!input) {
  console.error("Error: Markdown file path is required.");
  console.error("");
  console.error("Example:");
  console.error("  npm run pdf -- seminar/slides.md");
  process.exit(1);
}

if (!existsSync(input)) {
  console.error(`Error: File not found: ${input}`);
  process.exit(1);
}

const parsed = path.parse(input);
const dirName = path.basename(parsed.dir || ".");
const baseName = parsed.name;

const outDir = "dist";
mkdirSync(outDir, { recursive: true });

const ext =
  mode === "pdf" ? "pdf" :
  mode === "pptx" ? "pptx" :
  "html";

const output = path.join(outDir, `${dirName}-${baseName}.${ext}`);

const args = [];

if (mode === "pdf") {
  args.push("--pdf");
}

if (mode === "pptx") {
  args.push("--pptx");
}

if (mode === "standalone") {
  args.push("--standalone");
}

args.push(input, "-o", output);

console.log(`Building: ${input}`);
console.log(`Output:   ${output}`);

const result = spawnSync("marp-tmu-cs", args, {
  stdio: "inherit",
  shell: process.platform === "win32"
});

process.exit(result.status ?? 1);