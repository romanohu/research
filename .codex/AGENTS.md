# `fill Author` Operational Guide

## Purpose
When the user issues `fill Author` (or a short equivalent instruction with the same intent), perform the full workflow in one pass:

- append author information to paper notes under `03_research/*`
- create or update author pages under `03_research/Authors/*`
- add/update cross-links between paper notes and author pages
- A task is not complete if only the first author has been added for a multi-author paper.

## Trigger
Run this workflow when:

- the user explicitly says `fill Author`
- or the user clearly intends something like “fill author information from paper notes and link them to Authors”

## Scope
- Paper notes:
  - `03_research/**/papers.md`
  - `03_research/MARL/*_papers.md`
- Author pages:
  - `03_research/Authors/japanese/*.md`
  - `03_research/Authors/overseas/*.md`
- Author index:
  - `03_research/Authors/index.md`

## Required Workflow
1. Collect paper entries from `papers.md`.
   - Prioritize papers under `####` headings.

2. For each paper, identify the official source page and confirm the author list.
   - Prefer official sources such as arXiv, publisher pages, OpenReview, or conference/workshop websites.
   - Do not rely on guesswork when an official source is available.

3. Extract and record the authors.
   - **If multiple authors are available from the source, you MUST include all of them.**
   - **Never stop at the first author only.**
   - **This rule is mandatory and must be followed strictly.**

4. Add an author line immediately below each paper heading.
   - Format:
     - Overseas authors:
       - `[Name](../Authors/overseas/NameFile.md) [Name2](../Authors/overseas/Name2File.md) ...`
     - Japanese authors:
       - `[氏名](../Authors/japanese/氏名.md)`
   - Do **not** add a `著者:` prefix.

5. Create or update author pages.
   - Template:
     - `# 著者名`
     - `## 論文`
     - `### 年`
     - `- [論文タイトル](../../<分野>/papers.md#アンカー)`

6. Add author links to `03_research/Authors/index.md`.
   - Preserve the Japanese / Overseas classification.
   - Do not delete existing entries.
   - Avoid duplicates only.

7. Verify cross-links.
   - Confirm that links from `papers.md` to `../Authors/...` point to real files.
   - Confirm that links from `Authors/*.md` to `../../.../papers.md#...` point to existing paper anchors.

## Formatting Rules
- Do not break the existing file style.
  - Preserve heading levels, full-width / half-width character usage, and relative link style.
- Do not overwrite an existing author line unnecessarily.
  - If needed, only append or correct it.
- If there is ambiguity, do not introduce new naming variations.
  - Reuse existing filenames and notation whenever possible.

## Non-Negotiable Rule for Author Coverage
- When author information is found, **all listed authors must be added**.
- Adding only the first author is არას acceptable.
- Even if the paper has many authors, do not truncate the list unless the source itself is incomplete.
- If the available source is incomplete, use the best official source you can find and record as many confirmed authors as possible.

## Completion Criteria
Completion is achieved only when:

- the target paper entries have author lines
- the corresponding author pages exist
- the authors are reachable from `Authors/index.md`
- there are no major broken links in the main cross-reference paths