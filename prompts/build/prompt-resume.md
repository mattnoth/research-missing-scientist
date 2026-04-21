# Resume Pipeline After Rate Limit

## Non-interactive execution (read first)

This prompt runs via `claude -p --output-format=stream-json` (or `claude --dangerously-skip-permissions`). There is no stdin. Any question you emit will not be answered and the process will exit. Make decisions autonomously per the spec. If genuinely ambiguous and uncovered by the spec, use best judgment, log in `logs/research-log.md`, and proceed. The only reason to exit non-zero is a hard-safety-rule violation you cannot avoid.

## Context

The pipeline `run-all.sh` was previously executed. `prompt-000` completed and committed cleanly. `prompt-001` ran to near-completion — committing 31 commits across case dossiers, analysis files, appendices, and the top-level `dossier.md` — then hit an Anthropic usage-quota rate limit mid-flight. Because the `&&` chain in `run-all.sh` broke, `prompt-002` (PDF generation) and `prompt-003` (website integration) never ran.

When this prompt starts, the working tree may contain uncommitted modifications to files like `data/diagram-data.json`, `data/timeline-data.json`, `logs/contradictions.md`, `logs/known-unknowns.md`, and/or `run-all.log`. These are the partial final artifacts from `prompt-001` that never got committed before the limit hit.

## Your job

Finish the pipeline from wherever it actually is. Be idempotent. Do not wipe prior work.

### Step 1 — Survey state

Operate entirely within `/Users/mnoth/source/research-missing-scientists/`. From that directory:

1. Run `git status` and `git log --oneline` to confirm what has already been committed.
2. List the working tree (`ls -la`, then recurse one level for `analysis/`, `appendices/`, `cases/`, `data/`, `logs/`, `pdf-output/`).
3. Confirm which of these exist and are non-trivial: `cases/*.md` (all 11 subjects: casias, chavez, eskridge, garcia, grillmair, hicks, loureiro, maiwald, mccasland, reza, thomas), `dossier.md`, `analysis/connection-analysis.md`, `analysis/foreign-intel-layer.md`, `analysis/hypotheses.md`, `data/diagram-data.json`, `data/timeline-data.json`.
4. Record this survey at the bottom of `logs/research-log.md` under a new heading `## Resume survey (YYYY-MM-DD)` so the decision trail is preserved.

### Step 2 — Reconcile uncommitted prompt-001 work

For every uncommitted modified or untracked file in the working tree:

1. Read the file and compare it to what `prompt-001.md` specifies should be produced.
2. If the file matches or improves upon the spec, **keep it** — stage and commit under the message `prompt-001: finalize artifacts interrupted by rate limit` (one commit for all prompt-001 finalization files together).
3. If the file is clearly incomplete, truncated mid-sentence, or inconsistent with the spec, note the defect in `logs/research-log.md` and decide whether to (a) complete it yourself from the committed case files / dossier, or (b) revert it. Prefer completing over reverting — the research work is already done; you are just finishing the artifact.
4. `run-all.log` is a transcript file, not a pipeline artifact. Leave it untracked and unchanged, or add it to `.gitignore` if it is not already ignored.

### Step 3 — Audit prompt-001 completeness

Before moving on, confirm all prompt-001 deliverables exist and are coherent:

- All 11 case files in `cases/` are present, each with the sections required by `prompt-001.md`.
- `dossier.md` is complete with abstract, executive summary, case index, and cross-references.
- `analysis/` contains `connection-analysis.md`, `foreign-intel-layer.md`, `hypotheses.md` and they reference evidence in `cases/` and `appendices/`.
- `data/diagram-data.json` and `data/timeline-data.json` validate against any schema in `data/schema/` (if present) and cover all 11 cases.
- `logs/contradictions.md` and `logs/known-unknowns.md` are populated.
- `appendices/primary-sources/` contains a subdirectory per case with the sources referenced in that case's dossier entry.

If anything in this list is missing or materially incomplete, either produce it yourself (you already have the committed case files and analysis to work from — do not re-research) or, if the gap is unfillable without fresh research, document it clearly in `logs/known-unknowns.md` and `logs/research-log.md` and proceed. Commit any fill-ins as `prompt-001: fill audit gaps — <brief description>`.

### Step 4 — Run prompt-002 (PDF generation)

Read `prompt-002.md` from this directory and execute its full spec. Commit its outputs per that prompt's own instructions. If prompt-002 detects that its outputs already exist and are current, it should no-op — that is fine. Otherwise, generate the PDFs under `pdf-output/` as specified.

### Step 5 — Run prompt-003 (website integration)

Read `prompt-003.md` from this directory and execute its full spec. This likely touches `/Users/mnoth/source/mattnoth-dev/` per the `run-all.sh` next-steps message — respect the boundary it defines (local merge into main, do not push). If prompt-003 writes outside the research repo, follow its own rules about scope; do not expand those rules.

### Step 6 — Final report

At the end, append a concise summary to `logs/research-log.md` under `## Resume summary (YYYY-MM-DD)` covering:

- What was uncommitted at start and how you handled each file.
- Which audit gaps you found and filled (if any).
- Whether prompt-002 and prompt-003 ran to completion.
- Any remaining known issues to flag for Matt.

Then print to stdout a short status block with the same information so it shows up in `run-all.log` equivalents.

## Hard safety rules

- Do not `git reset --hard`, `git clean -fd`, or otherwise destroy existing work.
- Do not force-push anything.
- Do not delete the `.git` directory or re-initialize the repo.
- Do not attempt to contact any real person involved in the underlying research subjects by any means.
- Do not escalate with `sudo` or install new system-level software. Python packages via `pip install --user` or `uv` in a local venv are acceptable only if `prompt-002` or `prompt-003` explicitly require them.
- Do not write outside `/Users/mnoth/source/research-missing-scientists/` except where `prompt-003` explicitly scopes work into `/Users/mnoth/source/mattnoth-dev/` per its own spec.

Proceed.
