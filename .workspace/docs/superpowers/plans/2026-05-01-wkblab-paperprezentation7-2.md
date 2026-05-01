# wkblab_paperprezentation7-2 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a new TMU-CS Marp deck that explains why fine-tuning usually reuses pretrained capabilities rather than creating brand-new ones.

**Architecture:** Reuse the existing `tmu-cs` paper-presentation pattern, keep the deck self-contained, and use only inline equations plus bibliography citations. The talk is theory-first, so the slides emphasize a single narrative over experimental detail.

**Tech Stack:** Marp, `marp-theme-tmu-cs`, BibTeX

---

### Task 1: Create the new deck files

**Files:**
- Create: `prezentaion/wkblab_paperprezentation7-2/slides.md`
- Create: `prezentaion/wkblab_paperprezentation7-2/references.bib`

- [ ] Add front matter aligned with the existing `wkblab_paperprezentation7` deck.
- [ ] Add a 7-minute slide flow: question, geometry intuition, paper map, three evidence slides, conclusion, references.
- [ ] Add bibliography entries for the four cited papers.

### Task 2: Make the math and claims beginner-friendly

**Files:**
- Modify: `prezentaion/wkblab_paperprezentation7-2/slides.md`

- [ ] Keep one core equation per slide.
- [ ] Explain symbols in plain Japanese immediately below each equation.
- [ ] Explicitly label the geometry slide as intuition rather than a direct FT theorem.

### Task 3: Verify rendering

**Files:**
- Verify: `prezentaion/wkblab_paperprezentation7-2/slides.md`

- [ ] Run `npm run html -- wkblab_paperprezentation7-2/slides.md` from `prezentaion/`.
- [ ] Check that citations, section pages, and math render without overflow.
- [ ] Fix slide density if any page becomes too crowded.

