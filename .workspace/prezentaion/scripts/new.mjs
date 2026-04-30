import { cpSync, existsSync, mkdirSync, statSync } from "node:fs";
import path from "node:path";

const sampleDir = process.argv[2];
const targetDirName = process.argv[3];

function printUsage() {
  console.error("Usage:");
  console.error("  npm run new -- <sample-directory> <new-directory-name>");
  console.error("");
  console.error("Examples:");
  console.error("  npm run new -- samples/paper-review paper-review-2026-04-30");
  console.error("  npm run new -- samples/basic seminar-01");
}

if (!sampleDir || !targetDirName) {
  printUsage();
  process.exit(1);
}

if (!existsSync(sampleDir)) {
  console.error(`Error: sample directory not found: ${sampleDir}`);
  process.exit(1);
}

if (!statSync(sampleDir).isDirectory()) {
  console.error(`Error: sample path is not a directory: ${sampleDir}`);
  process.exit(1);
}

if (
  targetDirName.includes("/") ||
  targetDirName.includes("\\") ||
  targetDirName === "." ||
  targetDirName === ".."
) {
  console.error("Error: new directory name must be a simple directory name, not a path.");
  console.error("");
  console.error("Good:");
  console.error("  npm run new -- samples/paper-review my-review");
  console.error("");
  console.error("Bad:");
  console.error("  npm run new -- samples/paper-review ../my-review");
  console.error("  npm run new -- samples/paper-review nested/my-review");
  process.exit(1);
}

const targetDir = path.resolve(process.cwd(), targetDirName);

if (existsSync(targetDir)) {
  console.error(`Error: target directory already exists: ${targetDirName}`);
  process.exit(1);
}

mkdirSync(path.dirname(targetDir), { recursive: true });

cpSync(sampleDir, targetDir, {
  recursive: true,
  errorOnExist: true,
  force: false
});

console.log(`Created: ${targetDirName}`);
console.log(`From:    ${sampleDir}`);
console.log("");
console.log("Next:");
console.log(`  npm run pdf -- ${targetDirName}/slides.md`);