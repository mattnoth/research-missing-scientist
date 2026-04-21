# Prompt Deep-005 — Integration, Comparison & Gap Audit

## Non-interactive execution (read first)

This prompt runs via `claude -p --output-format=stream-json` — print mode. There is no stdin. Make decisions autonomously per the spec. Log ambiguities in `logs/research-log.md` and proceed.

You are Claude Code operating in `/Users/mnoth/source/research-missing-scientists/`. This is the final prompt in the deep-research series. It runs AFTER prompts deep-001 through deep-004 have completed. Its job is to integrate findings from the deep dives into the core analysis, update data files, and produce an honest audit of what improved and what gaps remain.

## Hard Safety Rules

- Working directory: `/Users/mnoth/source/research-missing-scientists/`. Do not touch anything outside it.
- No sudo. No system-wide installs.
- No git push. No auth to any service.
- No contacting anyone. Research uses already-public material only.
- Copyright discipline: paraphrase, ≤15 words per quote, one quote per source max.
- If unsure, stop and log the uncertainty.

## Alignment (read `prompts/research/README.md` § "Alignment rules" before starting)

This is the only research prompt that modifies analysis files, data files, and the dossier. All changes must be traceable to specific findings from deep-001 through deep-004.

## Pre-flight checks

Before doing any work, verify the deep research prompts have run:

1. Check `logs/research-log.md` for entries from deep-001, deep-002, deep-003, deep-004.
2. Check for expected output directories:
   - `appendices/primary-sources/` (should have been updated by deep-001)
   - `appendices/professional-networks/` (created by deep-002)
   - `appendices/foreign-coverage/` (updated by deep-003)
   - `appendices/historical-precedent/` and `appendices/base-rate-analysis/` (created by deep-004)
3. If any are missing, log which prompts haven't run yet and proceed with what's available. Do not fabricate findings for prompts that haven't run.

## Phase 1: Source quality audit

Spawn a sub-agent for this:

```
Read every `cases/{slug}.md` file (all 11). For each case, count:
- Total sources by tier (T1, T2, T3, T4, T5, T6, T7)
- Total sources overall
- Confidence rating distribution (Confirmed, Reported, Alleged, Speculated claims)

Produce `logs/source-audit.md` with:
- Per-case source tier breakdown (table)
- Cross-case comparison
- Before vs. after comparison: compare current counts against the baseline (~70% T2) to measure improvement
- Remaining gaps: which cases are still under-sourced at Tier 1?
- Source quality score per case (ratio of T1+T4 to T2+T3+T5+T6+T7)

Commit: `research-deep-005: source quality audit`
```

## Phase 2: Analysis integration

After the audit completes, run these sub-agents in parallel:

### Agent A: Update connection analysis

```
Read:
- `analysis/connection-analysis.md` (current version)
- `appendices/professional-networks/cross-reference.md` (from deep-002, if exists)
- All `appendices/professional-networks/*.md` files

Update `analysis/connection-analysis.md`:
- Add any newly documented connections to the Tight layer (patent co-inventorship, co-authorship, shared contracts — these are Tier 1 connections)
- Add any newly inferred connections to the Medium layer
- Do NOT remove existing connections — only add or upgrade confidence levels
- For each new connection, cite the source (appendix file and specific record)

Log changes in `logs/research-log.md`.
Commit: `research-deep-005: connection analysis update`
```

### Agent B: Update hypothesis evaluations

```
Read:
- `analysis/hypotheses.md` (current version)
- `appendices/historical-precedent/summary.md` (from deep-004, if exists)
- `appendices/base-rate-analysis/statistical-context.md` (from deep-004, if exists)
- `appendices/professional-networks/cross-reference.md` (from deep-002, if exists)
- Updated foreign coverage files (from deep-003)

Update `analysis/hypotheses.md`:
- H1 (Coincidence): integrate base-rate findings. Does the statistical context change the assessment?
- H4 (Foreign intelligence): integrate historical precedent. Does precedent analysis strengthen or weaken?
- H5 (Propulsion/materials specialization): integrate patent/publication networks. Are domain overlaps documented or inferred?
- H6 (UAP adjacency): integrate any new McCasland/Eskridge findings from professional records.
- H7 (Internal program protection): integrate SAP/SAPOC historical findings.
- All others: update if new evidence applies.

For each hypothesis update:
- State what new evidence was added
- State whether the assessment changed and why
- Preserve the existing evidence — add to it, do not replace

Log changes in `logs/research-log.md`.
Commit: `research-deep-005: hypothesis evaluation update`
```

### Agent C: Update foreign intelligence layer

```
Read:
- `analysis/foreign-intel-layer.md` (current version)
- All `appendices/foreign-coverage/*.md` files (especially newly added non-English sources from deep-003)
- `appendices/historical-precedent/foreign-targeting.md` (from deep-004, if exists)

Update `analysis/foreign-intel-layer.md`:
- Add historical precedent section referencing deep-004 findings
- Integrate any new foreign-media framing or claims from deep-003
- Note which foreign outlets covered the story and how — especially divergences from U.S. framing
- Maintain neutrality: no country pre-excluded or pre-implicated

Log changes in `logs/research-log.md`.
Commit: `research-deep-005: foreign intel layer update`
```

## Phase 3: Data file updates (sequential, after Phase 2)

After analysis updates are complete:

### Update diagram data

```
Read `data/diagram-data.json` and its schema.
Read the updated `analysis/connection-analysis.md`.

Add any new nodes or edges discovered by deep-002 (professional networks):
- New co-inventor links → edges with type "co-inventor", layer "tight"
- New co-author links → edges with type "co-author", layer "tight"
- New shared-program links → edges with type "program", layer appropriate to evidence level
- New institutional links → edges as appropriate

Validate against `data/schema/diagram-schema.json`.
Commit: `research-deep-005: diagram data update`
```

### Update timeline data

```
Read `data/timeline-data.json` and its schema.
Read `logs/research-log.md` for any newly discovered dates or events.

Add any new events discovered during deep research:
- Newly dated institutional statements
- Court filing dates (Grillmair, Loureiro)
- Patent filing dates relevant to case connections
- Historical precedent dates (as context events, clearly labeled)

Validate against schema.
Commit: `research-deep-005: timeline data update`
```

## Phase 4: Dossier update (last)

After all analysis and data updates:

```
Read the current `dossier.md`.
Read the updated analysis files.
Read `logs/source-audit.md`.

Update `dossier.md`:
- Rewrite the abstract ONLY if findings changed materially (new confirmed connections, hypothesis assessments shifted, major new sources)
- Rewrite the executive summary ONLY if warranted by same criteria
- Update the methodology reference to note the deep-research expansion
- Update the open questions section based on current `logs/known-unknowns.md`

If changes were minor (no hypothesis shifts, no major new connections), note in the dossier that a deep-source expansion was performed and reference the source audit for details. Do NOT inflate the significance of marginal improvements.

Commit: `research-deep-005: dossier update`
```

## Phase 5: Final reporting

1. Update `STATUS.md` with:
   - Deep research completion status (which prompts ran)
   - Source quality improvement metrics (from audit)
   - Key findings from deep research
   - Remaining gaps
   - Whether PDFs and website need regeneration (they do if dossier or data changed)

2. Update `CHANGELOG.md`:
   - Version bump (minor if analysis changed, patch if only sources improved)
   - Date and scope of deep research

3. Append final summary to `logs/research-log.md`.

4. Commit: `research-deep-005: status and changelog update`

## End conditions

- Source quality audit completed and written to `logs/source-audit.md`.
- Analysis files updated with deep-research findings.
- Data files updated and validated.
- Dossier updated (or noted as unchanged with reason).
- STATUS.md and CHANGELOG.md updated.
- All changes committed with scoped messages.
- Research log has complete record of integration work.

End of prompt deep-005.
