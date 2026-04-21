---
description: Session-close checklist for the research dossier. Run before ending any session that touched research content.
---

Run these checks in order. Skip a step only if no work in the session touched that area. Do not skip the final `research-log.md` append — it is mandatory.

## 1. Research content changes — durable capture

If the session produced new research findings (new sources, revised narratives, resolved dates, updated source tiers), make sure they landed in the right canonical location:

- New primary source → `appendices/primary-sources/{slug}/`
- Updated case facts → `cases/{slug}.md` (and check its Tier/Confidence tags)
- Cross-case pattern or revision → `analysis/connection-analysis.md` or `analysis/hypotheses.md`
- Country-level coverage update → `appendices/foreign-coverage/{country}.md`

**Exclude** meta discussion about the repo, agent, or process — those belong in the research-log's Decisions section, not in case/analysis files.

## 2. Integrity artifacts — keep them current

- **Contradictions** — If the session introduced, resolved, or sharpened a contradiction, update [logs/contradictions.md](../../logs/contradictions.md).
- **Known unknowns** — If the session revealed a new analytical gap or closed an existing one, update [logs/known-unknowns.md](../../logs/known-unknowns.md).
- **Dossier sync** — If a case narrative changed materially, check that the dossier case index and executive summary still reflect reality. `dossier.md` rots silently.

## 3. Tier consistency

If any source tier was changed in this session, propagate the change across all files that cite that source: `cases/`, `analysis/`, `dossier.md`, `appendices/`. Tier drift is a recurring bug (see the 7→8 migration in `prompts/build/prompt-retag-tiers.md`).

## 4. Navigation and routing

- If a new artifact type was created (new folder, new file class), update [NAVIGATION.md](../../NAVIGATION.md).
- If an existing pointer is now wrong, fix it.
- If nothing meaningful to routing changed, do nothing. Do not bump dates for no reason.

## 5. Actionables reconciliation ([TODO-research.md](../../TODO-research.md))

- Any TODO items completed this session → strike through or remove.
- Any new TODOs discovered → add with enough context that a future agent can pick them up cold.
- If the file has grown unwieldy, flag it — do not silently archive.

## 6. Session progress append — mandatory

Append a new dated section to [logs/progress.md](../../logs/progress.md). This is the **single durable record** of every agent session — research, website, tooling, whatever. Do **not** skip this step.

```
## YYYY-MM-DD — <brief description>

**What changed:**
- <specific bullets: files touched, decisions made, commits/pushes, with paths and SHAs>

**Further work:**
- <anything half-finished, deferred, or worth picking up next session>
```

Rules: specific over general; include file paths and commit SHAs; a trivial session can be two lines. If the session also touched research content, **additionally** append to [logs/research-log.md](../../logs/research-log.md) with research-specific detail (searches run, sources found, tier changes).

## 7. Status and changelog

- If the session closed out a prompt run or a major milestone, update [STATUS.md](../../STATUS.md).
- If the session resulted in a versionable change to the dossier or analysis, append to [CHANGELOG.md](../../CHANGELOG.md).

## 8. Final report

Summarize to the user in one paragraph: what the session produced, where it went, and any flags for the next session.
