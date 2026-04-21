# Status — Prompt 001 Completion

## What was produced

### Case files (11)
All 11 case files in `cases/` are complete: casias, chavez, eskridge, garcia, grillmair, hicks, loureiro, maiwald, mccasland, reza, thomas. Each follows the standard schema with status, key dates, affiliation, inclusion rationale, narrative, source tiers, contradictions, and open questions.

### Analysis (3 files)
- `analysis/connection-analysis.md` — Three-layer (tight/medium/corkboard) cross-case analysis with confidence ratings.
- `analysis/hypotheses.md` — All 9 pre-registered hypotheses (H1–H9) evaluated with evidence for/against and assessment.
- `analysis/foreign-intel-layer.md` — Dedicated foreign-intelligence hypothesis evaluation with historical precedent, country-specific assessments, and named expert commentary.

### Dossier
`dossier.md` — Complete with abstract (278 words), executive summary (971 words), methodology reference, case index, connection analysis summary, hypothesis evaluation summary table, and open questions.

### Appendices
- `appendices/primary-sources/` — 11 per-case directories with Tier 1 source excerpts, plus 4 government-wide documents (DOE/NNSA, FBI, White House, House Oversight).
- `appendices/foreign-coverage/` — 5 country files (China, India, Iran, Russia, UK).
- `appendices/named-expert-commentary/` — 10 expert profiles with on-the-record statements and relevance assessments.

### Data
- `data/diagram-data.json` — 11 person nodes, 10 institution nodes, 7 location nodes, 6 program nodes, 44 edges, 3 layer definitions. Valid JSON.
- `data/timeline-data.json` — 29 case events, 14 context events. Valid JSON.
- `data/schema/diagram-schema.json` and `data/schema/timeline-schema.json` — JSON Schema 2020-12 definitions.

### Logs
- `logs/research-log.md` — Chronological record of all searches, findings, decisions, and dead ends.
- `logs/contradictions.md` — 16 within-case + 4 cross-case contradictions with resolution status.
- `logs/known-unknowns.md` — 18 case-specific + 7 cross-case analytical gaps.
- `logs/prompt-alterations.md` — Record of any downstream prompt changes.

## What was skipped and why

- **Non-English foreign coverage** — Searched English-language editions only. Non-English coverage in Russian, Chinese, Farsi, etc. is documented as a known unknown.
- **BBC coverage** — No BBC articles found. Absence is noted but may reflect editorial caution rather than non-coverage.
- **Several Tier 1 sources returned HTTP 403** — BCSO press release PDF, House Oversight press release page, some media outlets. Documented in research log.
- **Daily Mail articles** — Cited by many outlets as the origin of the Garcia KCNSC claim, but no Daily Mail article appeared directly in search results. Documented as a known unknown.

## Flags for review before running prompt 002

1. **H4 assessment wording** — The dossier summary table and hypotheses.md now both say "Weak support" for the foreign-intelligence hypothesis. Verify this aligns with the tone you want.
2. **Garcia KCNSC employment** — The entire employment claim rests on a single anonymous source via the Daily Mail. This is the most important unresolved factual question. If new information emerges, the case file and analysis files may need updating.
3. **Reza Find a Grave anomaly** — Genuinely unexplained. The memorial was created and later removed. No explanation has been published.
4. **Hicks and Maiwald causes of death** — Both remain undisclosed. The "no autopsy" claims lack traceable T1 sourcing.
5. **FBI investigation and House Oversight findings** — Both pending as of April 20, 2026. Results could change the analysis substantially.

## Timing

Prompt 001 ran on 2026-04-20 and produced 31 commits before hitting an Anthropic usage-quota rate limit. A reconcile session on 2026-04-21 committed the remaining artifacts (diagram-data, timeline-data, contradictions, known-unknowns) and performed a full completeness audit.
