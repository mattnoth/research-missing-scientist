# Project History

How this research repository was built, from conception through execution. Written for transparency and reproducibility — if someone wants to understand how this was made, or replicate the approach for a different investigation, this is the document.

---

## Origins and motivation

In mid-April 2026, news broke that the Trump White House and FBI had confirmed a "holistic review" of approximately 11 U.S. scientists and officials — tied to nuclear, aerospace, military, and advanced research — who had died or disappeared under unusual circumstances since 2022. The House Oversight Committee opened its own investigation. Media coverage ranged from careful reporting to rampant speculation. There was no single authoritative public source that compiled the evidence with source discipline, evaluated the competing hypotheses, and clearly separated what was documented from what was alleged from what was speculated.

This project set out to build that resource: a structured, rigorously sourced research dossier maintained entirely through AI-assisted research workflows. The author (Matt Noth) designed and wrote the prompts; Claude Code (Anthropic's CLI agent) executed them.

## Architecture: the prompt pipeline

The core design decision was to structure the entire research process as a **pipeline of five sequential prompts**, each executed as a standalone Claude Code session via `claude -p --dangerously-skip-permissions`. Each prompt reads the filesystem left behind by the previous one — the repo itself is the shared state between sessions. There is no database, no API, no persistent agent memory between prompts.

### Why prompts instead of a single long session?

1. **Context window management.** A single session researching 11 cases, writing analysis, producing structured data, generating PDFs, and building a website would blow past any context limit. Breaking into phases keeps each session focused.
2. **Idempotency.** Each prompt checks for existing work before starting. If a session fails partway (which happened — see "The rate limit incident" below), you can re-run it without losing completed work.
3. **Separation of concerns.** Research (prompt 001) is walled off from rendering (prompts 002/003). The research repo is the source of truth; everything else is a derived artifact.
4. **Auditability.** Each prompt is a self-contained spec. You can read exactly what the agent was told to do, then compare the git history to see what it actually did.

### The five prompts

| Prompt | Purpose | Duration | Key design choices |
|---|---|---|---|
| `prompt-000.md` | **Bootstrap.** Initialize git repo, create directory skeleton, write README with methodology. No research. | ~1 min | Separated from research so the repo structure is clean before any content arrives. The full source-tier taxonomy (7 tiers) and confidence-rating system (4 levels) are written here, not in the research prompt, so they exist as immutable reference for all downstream work. |
| `prompt-001.md` | **Main research.** Spawn sub-agents, populate 11 case files, appendices, analysis, structured data. The heavy lift. | ~1-2 hours | Sub-agent orchestration (see below). Pre-registered hypotheses. Bounded search budgets. Copyright discipline. Commit-per-artifact strategy. |
| `prompt-002.md` | **PDF generation.** Produce print-ready PDFs from the markdown artifacts. | ~10-20 min | Checks for pandoc/weasyprint. Creates CSS/config. Generates main dossier PDF, 11 individual case PDFs, 3 diagram PDFs (one per layer), and a timeline PDF. |
| `prompt-003.md` | **Website integration.** Build the `/unpublished/missing-scientists` section of a personal website. | ~30-60 min | Reads the research repo (read-only). Vanilla TypeScript + CSS + D3. Interactive diagram with layer toggles. Interactive timeline. Feature branch workflow. |
| `prompt-004.md` | **Maintenance/update.** Run manually when news breaks. | Variable | Not part of the initial chain. Designed for re-runs: scoped research, artifact updates, version bumping. |

### The runner script

`run-all.sh` chains prompts 000-003 with `&&` — if any prompt exits non-zero, the chain halts. Output is streamed as JSON and pretty-printed via `jq` with color coding for thinking blocks, assistant text, tool calls, and tool results. The raw JSON stream is always captured for later analysis.

```bash
./run-all.sh 2>&1 | tee run-all.log
```

A `say "Research pipeline complete"` at the end provides an audible notification on macOS when the pipeline finishes — useful when running overnight.

## How prompt-001 works: sub-agent orchestration

Prompt 001 is the research engine. It was designed around **parallel sub-agent orchestration** — Claude Code's ability to spawn child agents via the Task tool. Here's how the work was distributed:

### Agent architecture

```
Lead Orchestrator (prompt-001 session)
  |
  |-- [parallel] Case Research Agents (11x, one per case)
  |     Each: 8-12 Tier 1 source searches, 5-10 Tier 2 corroborations
  |     Output: cases/{slug}.md + appendices/primary-sources/{slug}/
  |
  |-- [parallel] Primary Source Hunter (1x)
  |     Focus: Tier 1 documents across all cases
  |     Output: appendices/primary-sources/ (cross-case)
  |
  |-- [parallel] Foreign Coverage Agent (1x)
  |     Searched: Russia, China, Iran, Israel, UK, France, Germany, India, Japan
  |     Output: appendices/foreign-coverage/{country}.md
  |
  |-- [parallel] Named Expert Commentary Agent (1x)
  |     Located: 10 on-the-record experts (Swecker, Coulthart, Kaku, etc.)
  |     Output: appendices/named-expert-commentary/{name}.md
  |
  |-- [sequential, after cases complete] Cross-Case Analysis Agent (1x)
  |     Output: analysis/connection-analysis.md, hypotheses.md, foreign-intel-layer.md
  |
  |-- [sequential, after analysis complete] Diagram & Timeline Agent (1x)
  |     Output: data/diagram-data.json, data/timeline-data.json
  |
  Lead writes dossier abstract + executive summary LAST
```

### Why this structure?

- **Case agents run in parallel** because they're independent — researching Chavez doesn't depend on researching Loureiro. This is where most of the wall-clock time savings come from.
- **Primary source hunter runs separately** because its job is different from the case agents'. Case agents write narratives; the source hunter collects raw evidence. They populate different parts of the same directories.
- **Cross-case analysis runs after cases** because it needs to read finalized case files to identify connections. Running it earlier would mean analyzing incomplete data.
- **Diagram/timeline runs after analysis** because it needs to know what connections and events exist before encoding them as structured JSON.
- **The dossier summary is written last** so it reflects what was actually produced, not what was planned.

### What each agent was told

Every sub-agent received embedded copies of:
- The full safety rules (no contact, no sudo, no push, working directory only)
- The source-tier taxonomy and confidence-rating system
- Copyright discipline rules (paraphrase, max 15 words per quote, one quote per source)
- The refuse-to-invent rule (if you can't source it, leave a gap)
- The pre-registered hypothesis list (read-only reference)
- A bounded search budget
- The required output format for their artifacts

This redundancy was intentional. Sub-agents don't inherit the parent's full context — they need explicit instructions.

## How the prompts were built

### Design philosophy

The prompts were written with several principles:

1. **Specify outcomes, not mouse-clicks.** The prompts describe what the artifacts should contain and what standards they must meet, not step-by-step tool invocations. The agent decides how to search, what to fetch, and how to organize its work.

2. **Build in honest failure modes.** Every prompt includes instructions for what to do when sources can't be found, when pages return 403, when claims can't be confirmed. The `logs/known-unknowns.md` register and `logs/contradictions.md` tracker exist because the prompts demand them — they're not afterthoughts.

3. **Pre-register hypotheses.** The nine hypotheses (H1-H9) were written into the prompt before any research was done. This prevents the analysis from pattern-hunting post hoc. The analysis evaluates evidence for and against each hypothesis rather than building a narrative.

4. **Enforce source discipline structurally.** The 7-tier source taxonomy isn't a suggestion — every factual claim in every case file must carry a tier label and a confidence rating. This makes it mechanically impossible to write unsourced assertions without visibly breaking the format.

5. **Design for interruption.** The idempotency requirement (check for existing files before redoing work) and the incremental commit strategy (one commit per case file) mean that a crashed session loses at most one artifact's worth of work.

6. **Allow prompt self-modification.** Each prompt can alter downstream prompts for correctness (not style). This was used once: prompt-003 modified prompt-004 to clarify that website updates require `npm run build`, not re-running prompt-003.

### Iteration on prompt design

The prompts were not written in isolation. Key decisions made during drafting:

- **The source-tier taxonomy started at 3 tiers and expanded to 7.** The initial draft had Primary/Secondary/Tertiary. During drafting, it became clear that finer distinctions were needed — anonymous-source reporting (Tier 5) behaves very differently from named-expert commentary (Tier 4), and foreign state-affiliated press (Tier 7) needs its own category with editorial orientation noted.

- **The hypothesis list was expanded from 5 to 9.** H6 (UAP adjacency), H7 (internal U.S. program protection), H8 (independent events misgrouped), and H9 (exotic hypotheses) were added during drafting to ensure the analysis couldn't ignore frameworks that were circulating publicly, even uncomfortable ones.

- **Copyright discipline was added after the first draft.** The initial version didn't limit quotation. A revision added the 15-word-per-quote, one-quote-per-source rule and the paraphrase-by-default requirement.

- **The foreign coverage agent was split out from the case agents.** Initially, foreign coverage was part of each case agent's job. It was separated because (a) it requires a different search strategy (outlet-specific queries rather than case-specific queries) and (b) the geopolitical framing analysis works better when one agent reads all foreign coverage together.

## The run: what actually happened

### Timeline

All times are Central (UTC-5). The pipeline ran on the evening of April 20, 2026.

**Phase 1: Bootstrap (prompt 000)**
- `21:47` — Committed: `chore: bootstrap research repository structure` (27 files, 1,362 insertions)
- Created full directory skeleton, README with methodology, all prompt files, schemas, runner script
- Duration: ~2 minutes

**Phase 2: Research (prompt 001) — the big one**
- `21:53` — First research commit: `framework: add pre-registered hypotheses` (expanded H1-H9, updated JSON schemas)
- `21:54-21:56` — Case files and appendices arrive in rapid succession as parallel sub-agents complete:
  - `21:54:32` — Chavez case + primary sources
  - `21:54:34` — Casias case + primary sources
  - `21:54:35` — Hicks case (no T1 sources found beyond obituary)
  - `21:54:35` — Grillmair case
  - `21:54:46` — Reza case + first expert commentary (Swecker, Coulthart)
  - `21:55:08` — Maiwald + Thomas cases + CSIS expert
  - `21:56:01` — Garcia case + UK coverage + DOE Secretary commentary
  - `21:56:09` — Loureiro case
  - `21:56:48` — Eskridge case
  - `21:56:59` — McCasland case (the longest — 255 lines, most complex career/UAP angle)
- `21:57-21:59` — Log updates, remaining primary sources, government-wide sources, research log entries
- `22:07` — Cross-case analysis agent completes: connection-analysis.md, hypotheses.md, foreign-intel-layer.md (586 insertions)
- `22:09` — Dossier written last (abstract + executive summary), as designed
- **Then the rate limit hit.**

**The rate limit incident**

After commit `4d2d916` (dossier complete), the session hit an Anthropic usage-quota rate limit. The agent had been running for about 22 minutes and produced 31 commits. The `&&` chain in `run-all.sh` broke, so prompts 002 and 003 never ran.

Critically, the agent had *written* but not *committed* four files at the moment it was interrupted:
- `data/diagram-data.json` (831 lines, fully populated)
- `data/timeline-data.json` (436 lines, fully populated)
- `logs/contradictions.md` (expanded from 20-line skeleton to 101 lines)
- `logs/known-unknowns.md` (expanded from 45-line skeleton to 156 lines)

These files sat in the working tree as uncommitted changes.

**Phase 2.5: Recovery**

Two recovery prompts were written to handle this:

1. **`prompt-resume.md`** — A general-purpose "finish the pipeline from wherever it is" prompt. Would have surveyed state, reconciled uncommitted work, then run prompts 002 and 003 in sequence. This was written first but not used directly.

2. **`prompt-reconcile.md`** — A more surgical prompt focused only on reconciling the interrupted prompt-001 state. This is what was actually run. It:
   - Surveyed the repo state (31 committed, 4 uncommitted files)
   - Confirmed all uncommitted files were complete and valid
   - Committed them as `prompt-001: finalize artifacts interrupted by rate limit`
   - Ran a thorough completeness audit (the full audit report is at `logs/audit-report.md`)
   - Fixed audit gaps: created STATUS.md (never generated), updated CHANGELOG, fixed an H4 assessment discrepancy between dossier.md and hypotheses.md, added missing Hicks/Maiwald contradiction entries
   - Produced a formal verdict: `READY_FOR_PROMPT_002`

The reconcile prompt was intentionally detailed about its audit methodology — per-case structural checks, truncation scans, stub/placeholder detection, citation integrity, research log correlation, broken link detection, and gap severity classification (BLOCKER/SIGNIFICANT/MINOR). This was designed so the audit itself would be transparent and reproducible.

Recovery commits (`00:34-00:42`, April 21):
```
7c891e4 prompt-001: finalize artifacts interrupted by rate limit
525f3a2 prompt-001: fill audit gaps — STATUS.md, contradictions, H4 discrepancy
3cd9a2a prompt-001: reconcile summary and audit report
```

**Phase 3: PDF generation (prompt 002)**
- `00:44` — Untracked `run-all.log` removed from git
- `00:56` — `build: generate PDFs (dossier, cases, diagrams, timeline)`
  - Created `pdf-config/build-pdfs.py` (522 lines — a Python script for PDF generation)
  - Created `pdf-config/print.css` (271 lines — print-appropriate styling)
  - Created `pdf-config/metadata.yaml`
  - Generated: 1 main dossier PDF, 11 case PDFs, 3 diagram PDFs (tight/medium/corkboard layers), 1 timeline PDF
  - PDFs are in `pdf-output/` (gitignored — the markdown is the source of truth)

**Phase 4: Website (prompt 003)**
- Ran interactively (not via `run-all.sh`) in a separate session
- Built `/unpublished/missing-scientists` section in the mattnoth-dev website repo
- Created 20 pages: landing, 11 cases, 3 analysis, diagram, timeline, methodology, sources, transparency
- Used vanilla TypeScript + CSS + D3 (no frameworks, per explicit instruction)
- Interactive diagram with tight/medium/corkboard layer toggles
- Feature branch `feature/missing-scientists` merged to main locally
- Post-integration commit: `01:58` — `post phase 3 commit` (CLAUDE.md, TODO, prompt alterations, website notes)

**Phase 5: Manual iteration**
- `02:36` — `update TODO, dossier, and add glossary data` — manual follow-up adding TODO items from user review and a glossary JSON file
- This is where the project stood at the end of the first day

## Research methodology in practice

### What the agents actually searched

The research log (`logs/research-log.md`, 730+ lines) records every web search query, every page fetch attempt, every 403 error, every dead end. Some highlights:

- **Total web searches across all agents:** approximately 150+ distinct queries
- **Pages fetched:** approximately 100+ attempts, with a significant failure rate (~15-20% returned HTTP 403)
- **Most-researched case:** McCasland (19 searches) — justified by career complexity (AFRL, SAPOC, NRO, DeLonge/UAP angle)
- **Least-researched case:** Thomas (7 searches) — justified by weaker fit to the pattern
- **Highest source count:** Loureiro (7 primary source files) — the case with the most documentation (named suspect, confession video, court proceedings)
- **Most contentious sourcing:** Garcia — the entire KCNSC employment claim traces to a single anonymous source via the Daily Mail. The research log documents the full sourcing chain across 15 searches attempting to find independent confirmation.

### Source discipline outcomes

Final artifact counts:
- **11 case files** (95-255 lines each)
- **Appendix: 11 per-case primary-source directories** + 4 government-wide documents
- **Appendix: 5 foreign-coverage country files** (Russia, China, Iran, UK, India)
- **Appendix: 10 named-expert commentary files**
- **Logs: 16 within-case + 4 cross-case contradictions documented**
- **Logs: 18 case-specific + 7 cross-case known unknowns documented**

The agents found and documented meaningful coverage from Russia (RT, Pravda), China (Global Times), Iran (Tehran Times, Press TV), UK (LBC, IBTimes UK, UnHerd), and India (WION — the highest-volume foreign outlet, which contributed original reporting on the "Mondaloy connection" between Reza and McCasland). France, Germany, Japan, Israel (mainstream), Australia, and Qatar/Al Jazeera turned up no meaningful coverage — this absence is documented, not silently omitted.

### What the agents could not find

Key gaps documented in `logs/known-unknowns.md`:
- **Chavez:** Specific LANL role/title/division. No LANL institutional statement.
- **Casias:** No Tier 1 confirmation of the factory-reset phone claim (it's family-sourced).
- **Garcia:** No independent confirmation of KCNSC employment. The biggest single sourcing gap.
- **Hicks & Maiwald:** Cause of death not disclosed for either. "No autopsy" claims lack traceable T1 sourcing.
- **Reza:** JPL title only partially verified. Cell phone forensic results not released. Find-a-Grave anomaly unexplained.
- **McCasland:** BCSO press release PDF returned 403. No direct access to court filings.
- **Eskridge:** No official police/coroner report publicly available.
- **Base-rate analysis:** The null hypothesis (H1) cannot be rigorously evaluated without comparing the observed cluster rate against expected rates for the defense/aerospace workforce. This requires workforce demographic data that isn't freely available.

### Hypothesis evaluation results

The analysis evaluated all 9 pre-registered hypotheses. Summary of assessments:

| Hypothesis | Assessment |
|---|---|
| H1 — Coincidence/base rate | Indeterminate (can't evaluate without actuarial data) |
| H2 — Geographic clustering (NM) | Partially supported |
| H3 — Institutional clustering (JPL) | Partially supported |
| H4 — Foreign intelligence targeting | Weak support |
| H5 — Propulsion/materials specialization | Partially supported |
| H6 — UAP/disclosure adjacency | Weak support |
| H7 — Internal U.S. program protection | Not supported |
| H8 — Independent events misgrouped | Partially supported (strongest for Grillmair, Loureiro) |
| H9 — Exotic hypotheses | Not supported |

No hypothesis was declared the "winner." The analysis explicitly states this is an evidence evaluation, not a conclusion.

## Key decisions and their rationale

### Decisions made during prompt design

1. **Include all 11 cases from the White House list, even weak fits.** Thomas (pharma, not defense) and Eskridge (2022, ruled suicide) are included with explicit "weaker fit" rationale rather than excluded. Rationale: excluding cases that don't fit a narrative is itself a form of bias. Better to include with clear explanation of why the fit is weak.

2. **Pre-register hypotheses before research.** This prevents post-hoc pattern hunting. The hypothesis list includes uncomfortable possibilities (H7: U.S. government targeting its own scientists; H9: exotic/UAP involvement) specifically because excluding them would be a form of editorial bias.

3. **No country pre-excluded or pre-implicated.** The foreign intelligence hypothesis (H4) evaluates Russia, China, Iran, Israel, UK, and the United States itself on evidence alone. This was a deliberate choice stated in the methodology.

4. **No contact policy.** Zero outreach to any person, family, agency, or journalist. All sourcing from already-public material. This is both an ethical choice (this is research, not journalism) and a practical one (AI agents should not be contacting real people).

5. **Sensational framing explicitly avoided.** Words like "assassinations," "silenced," "targeted" appear only when quoting sources, never in the repository's own prose. This was specified in the methodology before any research began.

### Decisions made by the agents during execution

1. **The Loureiro case agent flagged it as the strongest candidate for reclassification** — named suspect, ballistics/DNA/surveillance evidence, video confession, apparent personal motive. The agent made this assessment independently based on the evidence.

2. **The Garcia case agent traced the KCNSC employment claim through 6 outlets** and documented that every single one traces back to a single anonymous Daily Mail source. This sourcing chain analysis was the agent's own initiative, not explicitly requested in the prompt.

3. **The foreign coverage agent found that WION (India) produced the highest volume of coverage** among foreign outlets and contributed original reporting (the "Mondaloy connection"). This was unexpected — India was not expected to be the highest-engagement country.

4. **The expert commentary agent assessed Steven Greer as "low credibility"** and documented why (promotes UAP-related conspiracy theories without evidence, significant financial interests). This was the agent applying the prompt's credential-evaluation requirement.

5. **The cross-case analysis agent found expert opinion roughly evenly split** between espionage-concerned (Swecker, Coulthart, Kaku) and skeptical (Rodgers/CSIS, Roecker/NTI, Coffindaffer), with government officials (Patel, Wright) taking no-conclusions positions. The analysis presents this division rather than picking a side.

## Technical details

### Tools and infrastructure

- **Claude Code CLI** — Anthropic's CLI agent tool. All prompts run via `claude -p --output-format=stream-json --dangerously-skip-permissions`
- **Git** — Local only. All commits local. Human operator pushes.
- **Python 3** — Used by prompt-002 for PDF generation (`pdf-config/build-pdfs.py`)
- **D3.js** — Used by prompt-003 for interactive diagram and timeline
- **markdown-it** — Used by prompt-003 for markdown-to-HTML rendering
- **No databases, no APIs, no cloud services** — The git repo is the entire state

### Commit statistics

- **36 total commits** (as of end of first day)
- **31 commits from prompt-001** (the research phase)
- **3 commits from the reconciliation session**
- **1 commit from prompt-002** (PDF generation)
- **1 commit from the post-phase-3 cleanup**
- **~7,500 lines of research content** across case files, analysis, appendices, and logs
- **~1,500 lines of structured data** (diagram and timeline JSON)
- **~800 lines of PDF infrastructure** (build script + CSS)

### File counts

- 11 case files in `cases/`
- 3 analysis files in `analysis/`
- ~45 primary source files across `appendices/primary-sources/`
- 5 foreign coverage files
- 10 named expert commentary files
- 4 government-wide primary source documents
- 2 JSON data files with 2 JSON Schema definitions
- 5 log/audit files

## What went well

1. **Parallel sub-agents worked.** 11 case research agents running simultaneously meant the research phase produced commits every few seconds during peak throughput. The total research phase took ~22 minutes for 11 detailed case files — far faster than sequential execution.

2. **The incremental commit strategy saved the interrupted run.** When the rate limit hit, 31 of ~34 planned commits were already done. Only 4 files needed recovery.

3. **Source discipline held.** The agents genuinely refused to invent sources. The known-unknowns register has 25 entries because the agents logged gaps rather than filling them with plausible-sounding assertions.

4. **The hypothesis framework prevented narrative drift.** By pre-registering H1-H9, the analysis stayed evaluative rather than becoming advocacy for any particular theory.

5. **The reconciliation audit was thorough.** The audit report checked every case file for truncation, stubs, citation integrity, and research log correlation. It caught the H4 assessment discrepancy between dossier.md and hypotheses.md that the original session missed.

## What could be improved

1. **The rate limit was predictable and should have been planned for.** A session spawning 15+ sub-agents doing web searches was always going to be token-intensive. Future runs should either use a higher-tier plan or break prompt-001 into sub-prompts (e.g., 001a for cases 1-6, 001b for cases 7-11, 001c for analysis).

2. **Non-English foreign coverage was never searched.** The foreign coverage agent only searched English-language editions. Coverage in Russian, Chinese, Farsi, etc. is a documented gap.

3. **The base-rate analysis gap undermines H1 evaluation.** Without knowing the expected rate of deaths and disappearances in the defense/aerospace workforce, the coincidence hypothesis can't be rigorously assessed. This is the most important analytical gap.

4. **Some minor formatting inconsistencies across case files.** Grillmair, Hicks, Maiwald, and Reza have structural differences from the other cases (missing section headers, inline tier tags in different locations). These are cosmetic, not substantive, but reduce the consistency that makes the repository navigable.

5. **The website needs more polish.** First review identified: broken source links, leftover .md references in rendered prose, timeline visualization quality, diagram node label truncation, and overall visual polish. These are tracked in TODO-research.md.

6. **The prompt-resume.md approach (run the whole remaining pipeline in one session) was written but not tested.** The more surgical prompt-reconcile.md was used instead. The resume prompt's approach of running prompts 002 and 003 from inside a reconciliation session might have context window issues.

## Reproducing this work

To rebuild from scratch:

```bash
cd /path/to/empty/directory
# Copy in the prompt files (prompt-000.md through prompt-004.md), run-all.sh, RUNBOOK.md
chmod +x run-all.sh
./run-all.sh 2>&1 | tee run-all.log
```

To update when new information surfaces:

```bash
claude --dangerously-skip-permissions "$(cat prompt-004.md)"
```

To regenerate PDFs after research updates:

```bash
claude --dangerously-skip-permissions "$(cat prompt-002.md)"
```

To update the website after research updates:

```bash
cd /path/to/website && npm run build
```

## Open questions for the project itself

- **Automated updates:** Can prompt-004 be scheduled on a cron to automatically check for new developments and update the research? This is noted in the TODO but not yet implemented.
- **Open-sourcing:** If published, the prompt files themselves become the methodology documentation. The git history becomes the audit trail. The known-unknowns register becomes the disclosure of limitations. This transparency-by-design was intentional from the start.
- **Reusability:** The prompt architecture (bootstrap -> research with parallel sub-agents -> render -> serve -> maintain) could work for any structured investigation. The source-tier taxonomy and hypothesis framework are domain-specific but the pattern is general.

---

*Last updated: 2026-04-21*
*Total project elapsed time: ~5 hours from first commit to end of first day*
*Total commits: 36*
*Total research content: ~7,500 lines across 75+ files*
