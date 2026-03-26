# Autonomous Literature Explorer (priority: highest)

## Purpose
- Elicit the user’s research intent, then autonomously search for relevant papers and record findings in `03_research/**/papers.md` without pausing for permission mid-run.

## Trigger
- User asks to know/learn/explore research topics.

## Clarification Loop
- Up to 3 focused turns to narrow domain/keywords; end earlier if the user says “OK” or the agent can name a single domain with top keywords and announces search start.

## Sources and Cadence
- Sources: arXiv, OpenReview, ACM, IEEE, Springer, Google Scholar.
- Fetch in 5-minute batches; skip duplicates by anchor/title against existing notes.

## Destination Rules
- Choose the best-fit existing `papers.md` file; may add new subheadings (survey/subtopic) matching current style.
- If domain is new, append to `03_research/Others/papers.md`; upon stop, propose a new domain placement to the user.

## Writing Task (subtask)
- Follow existing `papers.md` heading/order style.
- For each new paper add a concise note covering: 1) what it is, 2) what’s novel vs prior work, 3) core technical idea, 4) how it’s validated, 5) open debates, 6) next papers to read (also use as next-search hints), plus paper info/link.

## fill Author Integration
- Run `fill Author` in batches every 20 papers or every 30 minutes (whichever comes first) during the session.

## Stop Conditions
- Chat remaining context < 20%; or explicit user stop; or rolling 7-day token counter exceeds 10% of weekly budget (default: cumulative weekly budget from latest user guidance).

## Budget & Persistence
- Track per-call token usage from API metadata; maintain rolling 7-day counter.
- Store state and per-site cool-downs in `.codex/workspace/litsearch_state.json`.
- Use `.codex/workspace/litsearch_notes-YYYY-MM-DD.md` as scratch to offload context; keep files.

## Rate Limits
- If a source rate-limits, record a cool-down for that source in state and skip it until expiry, then resume.

## Behavior
- Do not ask for permission mid-run; continue until a stop condition fires.

# `fill Author` Operational Guide
Priority: lower than Autonomous Literature Explorer.

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
   - Add a short bio section immediately under the name with concise facts and **include source links** for each fact (e.g., homepages, scholar profiles); keep it brief and sourced.

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
