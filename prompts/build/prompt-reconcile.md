# Reconcile Interrupted Prompt-001 Work

## Non-interactive execution (read first)

This prompt runs via `claude --dangerously-skip-permissions` in print mode. There is no stdin. Any question you emit will not be answered and the process will exit. Make decisions autonomously per the spec. If genuinely ambiguous and uncovered by the spec, use best judgment, log in `logs/research-log.md`, and proceed. The only reason to exit non-zero is a hard-safety-rule violation you cannot avoid.

## Context

The pipeline `run-all.sh` was previously executed in `/Users/mnoth/source/research-missing-scientists/`. `prompt-000` completed and committed cleanly. `prompt-001` ran to near-completion — committing 31 commits across case dossiers, analysis files, appendices, and the top-level `dossier.md` — then hit an Anthropic usage-quota rate limit mid-flight. Because the `&&` chain in `run-all.sh` broke, `prompt-002` (PDF generation) and `prompt-003` (website integration) never ran.

When this prompt starts, the working tree may contain uncommitted modifications to files like `data/diagram-data.json`, `data/timeline-data.json`, `logs/contradictions.md`, `logs/known-unknowns.md`, and/or `run-all.log`. These are the partial final artifacts from `prompt-001` that never got committed before the limit hit.

## Your job

Reconcile the interrupted `prompt-001` state so the repo is clean and coherent before prompt-002 runs in a later session. Do not run prompt-002 or prompt-003 in this session. Do not re-do research — the research is already committed.

### Step 1 — Survey state

Operate entirely within `/Users/mnoth/source/research-missing-scientists/`. From that directory:

1. Run `git status` and `git log --oneline` to confirm what has already been committed.
2. List the working tree top level, then recurse one level into `analysis/`, `appendices/`, `cases/`, `data/`, `logs/`, `pdf-output/`.
3. Confirm which of these exist and are non-trivial: `cases/*.md` for all 11 subjects (casias, chavez, eskridge, garcia, grillmair, hicks, loureiro, maiwald, mccasland, reza, thomas), `dossier.md`, `analysis/connection-analysis.md`, `analysis/foreign-intel-layer.md`, `analysis/hypotheses.md`, `data/diagram-data.json`, `data/timeline-data.json`.
4. Append a survey summary to `logs/research-log.md` under a new heading `## Reconcile survey (YYYY-MM-DD)` capturing what you found.

### Step 2 — Reconcile uncommitted work

For every uncommitted modified or untracked file in the working tree:

1. Read the file and compare it to what `prompt-001.md` specifies should be produced.
2. If the file matches or improves upon the spec, keep it.
3. If the file is clearly incomplete, truncated mid-sentence, or inconsistent with the spec, decide whether to complete it yourself from the committed case files and dossier, or to revert it. Prefer completing over reverting — the research is done, you are only finishing the artifact. Do not perform fresh web research in this session.
4. `run-all.log` is a transcript file, not a pipeline artifact. Leave it untracked. If it is not already covered by `.gitignore`, add a single-line entry for it.

Commit all finalized files in one commit with the message `prompt-001: finalize artifacts interrupted by rate limit`. If you had to complete truncated files, include a short `logs/research-log.md` note describing each completion, and commit that log update as part of the same commit.

### Step 3 — Thorough research completeness audit

The goal of this step is to verify that `prompt-001` actually *completed its research work*, not merely that files exist on disk. Rate-limit interruptions can produce files that look populated at a glance but are truncated, stubbed, or missing sections. Be rigorous.

You will produce a structured audit report at `logs/audit-report.md`. Overwrite this file if it already exists. Use clear markdown headings and a per-case status table.

#### Step 3a — Derive the completeness spec

Read `prompt-001.md` end-to-end. Extract and write to `logs/audit-checklist.md` (create or overwrite):

1. The exact list of required sections in each `cases/<case>.md` file (headings, required subsections).
2. Required sections in `dossier.md` (abstract, executive summary, case index, hypothesis summary, cross-references, etc. — whatever the spec says).
3. Required contents of `analysis/connection-analysis.md`, `analysis/foreign-intel-layer.md`, `analysis/hypotheses.md`.
4. Required schema, fields, and coverage in `data/diagram-data.json` and `data/timeline-data.json`. Note any schema file present in `data/schema/`.
5. Required appendix coverage: per-case primary sources, plus any `appendices/foreign-coverage/` and `appendices/named-expert-commentary/` requirements.
6. Any minimum evidence thresholds the spec sets (e.g., "at least N primary sources per case", "at least one foreign-language source where applicable").

If `prompt-001.md` is ambiguous on any of these, record your interpretation explicitly in the checklist so the audit is reproducible.

#### Step 3b — Per-case audit

For each of the 11 cases (casias, chavez, eskridge, garcia, grillmair, hicks, loureiro, maiwald, mccasland, reza, thomas):

1. **Read the full case file.** Not just the headings — the body. Confirm every required section from the checklist is present and populated with substantive content, not placeholder text.
2. **Truncation scan.** Flag any of: file ends mid-sentence; final paragraph has no terminal punctuation; unclosed markdown code block, table, or list; abrupt topic shift with no closing sentence; body length dramatically shorter than sibling cases with comparable scope.
3. **Stub / placeholder scan.** Flag any of: `TODO`, `FIXME`, `XXX`, `[placeholder]`, `[to be filled]`, `[pending]`, `research pending`, `TBD`, bare `...` at end of paragraph, empty section under a heading, single-sentence sections where the spec expects a paragraph or more.
4. **Citation integrity.** Every specific factual claim (dates, names, locations, quoted statements, agency findings) should trace to a source. Scan for citation patterns (links, footnotes, `[source: ...]`, inline URLs). Verify referenced sources exist in `appendices/primary-sources/<case>/`. Flag unsupported claims.
5. **Primary source coverage.** `ls appendices/primary-sources/<case>/` — count files. Compare to the spec's minimum threshold (from the checklist). Flag cases under threshold.
6. **Research log trace.** `grep -i "<case name>" logs/research-log.md`. Confirm there is an entry documenting searches performed, pages fetched, key findings, and files written. A case with no research-log entry is suspect even if `cases/<case>.md` looks populated — flag it for manual review.

Record per-case findings in `logs/audit-report.md` as a table with columns: case, required-sections-present, missing-sections, truncation-flag, stub-flag, source-count, research-log-entry, verdict (one of: COMPLETE, MINOR-GAPS, MAJOR-GAPS, INCOMPLETE).

#### Step 3c — Top-level artifact audit

1. **`dossier.md`.** Read fully. Confirm required sections per checklist. Verify the case index links to all 11 `cases/*.md` files. Verify cross-references into `analysis/` and `appendices/`. Truncation and stub scans as in 3b. Confirm every case summary in the dossier is consistent with the fuller content in `cases/<case>.md` (no contradictions, no claims in the dossier that aren't in the case file).
2. **`analysis/*.md`.** For each of `connection-analysis.md`, `foreign-intel-layer.md`, `hypotheses.md`: read fully, verify spec sections, verify that every hypothesis, connection, or claim cites specific case evidence by filename or case name, flag any unsupported claim. `hypotheses.md` in particular should enumerate hypotheses explicitly (H1, H2, …) and evaluate each against the evidence.
3. **`data/*.json`.** Validate JSON syntactically: run `python3 -c "import json; json.load(open('data/diagram-data.json'))"` and the same for `timeline-data.json`. If `data/schema/` contains schema files, validate against them (use `python3` with `jsonschema` if available; otherwise structural eyeball check against the schema files). Confirm all 11 cases appear in each data file. Flag missing or malformed entries.
4. **`logs/contradictions.md` and `logs/known-unknowns.md`.** Confirm populated with case-specific entries, not just scaffolding. Cross-check: every "known unknown" flagged in a case file should have a corresponding entry in `known-unknowns.md`; every contradiction noted in a case should appear in `contradictions.md`.
5. **`appendices/foreign-coverage/` and `appendices/named-expert-commentary/`.** If the checklist requires content here, verify it exists and is non-trivial. Empty or near-empty directories here are a significant gap.

#### Step 3d — Integrity and coherence checks

1. **Broken internal links.** For every markdown link of the form `[text](path)` in `dossier.md`, `analysis/*.md`, and `cases/*.md` where the path is relative and local, verify the target file exists. Collect and list any broken links in the audit report.
2. **Case-name consistency.** The 11 canonical names (casias, chavez, eskridge, garcia, grillmair, hicks, loureiro, maiwald, mccasland, reza, thomas) should be used consistently in filenames, dossier entries, analysis references, and data JSON keys. Flag any inconsistency (alternate spellings, mismatched IDs).
3. **Commit coverage.** `git log --oneline --all` — scan commit messages. You should see evidence of research commits for each case. If a case has no commit trace in the log, that is a red flag: the file may have been written but the underlying research may have been interrupted.
4. **Empty directory scan.** `find appendices -type d -empty`. Any empty subdirectory under `appendices/primary-sources/` means missing research for that case.

#### Step 3e — Gap handling

For every gap identified in 3b–3d:

1. **Classify severity.** Use one of:
   - `BLOCKER` — prompt-002 cannot meaningfully run (e.g., a case file is a stub, data JSON is malformed, dossier has no case index).
   - `SIGNIFICANT` — research is materially incomplete for a case or analysis section, but prompt-002 could still technically run.
   - `MINOR` — cosmetic or structural issue (broken link, inconsistent naming) not affecting research substance.

2. **Classify fixability from committed material.**
   - `FIXABLE_NO_RESEARCH` — can be resolved by editing existing files (fix broken links, restructure sections, pull a missing summary from the case body into the dossier, fix JSON syntax).
   - `NEEDS_RESEARCH` — resolving requires fresh web fetches or new analysis. In this session, do not do this.

3. **Act accordingly.**
   - For `FIXABLE_NO_RESEARCH` gaps: fix them. Commit each coherent batch of fixes with a message like `prompt-001: fill audit gap — <description>`.
   - For `NEEDS_RESEARCH` gaps: do not touch. Document the gap in `logs/known-unknowns.md` and in the audit report with severity, case, specific missing content, and what a future research session would need to find.

Do not perform fresh research under any circumstance in this session.

### Step 4 — Readiness verdict and final report

At the end of `logs/audit-report.md`, write an explicit verdict using exactly one of these tokens on its own line, then elaborate below it:

- `READY_FOR_PROMPT_002` — all 11 cases COMPLETE or at worst MINOR-GAPS; all top-level artifacts present and coherent; no BLOCKER gaps; data JSON valid; no empty appendix directories for cases. Safe to run prompt-002 in a fresh session.
- `READY_WITH_CAVEATS` — no blockers, but one or more SIGNIFICANT gaps are deferred as `NEEDS_RESEARCH`. Prompt-002 can run and produce a coherent deliverable, but the output will reflect the documented gaps. List each caveat.
- `NOT_READY` — at least one BLOCKER gap remains unresolved (e.g., a case file is a stub, data JSON is malformed and unfixable from committed material, dossier is missing major sections). Prompt-002 should not run until a fresh research session addresses the blockers. List each blocker with severity, fixability, and what's needed.

Below the verdict token, include:

- A per-case status table (case → verdict from 3b).
- A list of gaps filled during this session with commit SHAs.
- A list of deferred gaps classified as `NEEDS_RESEARCH`, each with a specific prescription for what a future session would need to find.
- Final `git log --oneline` output showing the new commits from this session.

Also append a shorter `## Reconcile summary (YYYY-MM-DD)` to `logs/research-log.md` that:

- Summarizes what was uncommitted at start and how you handled each file.
- Points to `logs/audit-report.md` for the full audit.
- Restates the verdict token on its own line.

Commit the final log and audit report together as `prompt-001: reconcile summary and audit report`.

Finally, print to stdout a short status block: the verdict token, the number of gaps filled, the number of gaps deferred, and the count of new commits made this session. This makes it scannable in the terminal output.

## Hard safety rules

- Do not `git reset --hard`, `git clean -fd`, or otherwise destroy existing work.
- Do not force-push anything. Do not push at all in this session.
- Do not delete the `.git` directory or re-initialize the repo.
- Do not perform fresh web research or contact any real person involved in the underlying subjects.
- Do not escalate with `sudo` or install new system-level software.
- Do not write outside `/Users/mnoth/source/research-missing-scientists/`.
- Do not run `prompt-002.md` or `prompt-003.md` in this session — reconcile only.

Proceed.
