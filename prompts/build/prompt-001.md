# Prompt 001 — Research and Core Artifacts

## Non-interactive execution (read first)

This prompt runs via `claude -p --output-format=stream-json` — print mode. There is no stdin. Any question you emit will not be answered and the process will exit. Make decisions autonomously per the spec. If genuinely ambiguous and uncovered by the spec, use best judgment, log in `logs/research-log.md`, and proceed. The only reason to exit non-zero is a hard-safety-rule violation you cannot avoid.

You are Claude Code operating in `/Users/mnoth/source/research-missing-scientists/` (already initialized as a git repo by prompt 000). This is the main research prompt. Your task is to produce the research artifacts as markdown files and structured data, with rigorous source discipline, honest record-keeping, and explicit neutrality. No rendering — PDFs come in prompt 002, website in prompt 003.

This prompt is long on purpose. Read all of it before starting.

## Hard Safety Rules (unchanged from prompt 000)

- **Working directory is `/Users/mnoth/source/research-missing-scientists/`.** Do not touch anything outside it.
- **Do not install anything system-wide. No `sudo`.** If a reputable tool is genuinely needed, ask first. For this prompt you almost certainly don't need to install anything.
- **Do not push to any git remote. Do not authenticate to any service.**
- **Do not attempt to contact anyone.** Ever. No emails, no forms, no messages. Research uses already-public material only.
- **No `curl` to arbitrary endpoints.** Use only the provided web search and web fetch tools.
- **If unsure, stop and ask.**

## Downstream prompt alteration

If, in the course of completing this prompt, you identify issues with `prompt-002.md`, `prompt-003.md`, or `prompt-004.md` that would prevent them from executing correctly — missing context, incorrect assumptions about artifacts or state this prompt produces, conflicts with structural decisions you've made — you may alter them. Document every alteration in `logs/prompt-alterations.md` with: prompt filename, what was changed, why, and the date. Do not alter prompts for stylistic preference; only for correctness.

## Context: the investigation

Starting in mid-April 2026, the Trump White House (via Press Secretary Karoline Leavitt) and the FBI confirmed a "holistic review" of a cluster of approximately 11 U.S. scientists and officials — tied to nuclear, aerospace, military, or advanced research — who have died or disappeared under unusual circumstances since 2022, with most concentrated in 2025–2026. The House Oversight Committee (Chairman James Comer, Rep. Eric Burlison) has also opened its own investigation. Media speculation ranges from coincidence to foreign intelligence targeting to internal cover-ups. Two cases (Grillmair, Loureiro) have named apprehended suspects with apparent non-conspiracy explanations; others (Chavez, Casias, Garcia, McCasland, Reza) remain genuinely unexplained.

Cases commonly named in public coverage (not an authoritative list — this repository defines its own inclusion criteria, see methodology in README):

- **Anthony "Tony" Chavez** — retired Los Alamos National Laboratory employee. Missing since May 4, 2025, Los Alamos, NM.
- **Melissa Casias** — administrative employee with security clearance at LANL. Missing since June 26, 2025, Taos County, NM. Both personal and work phones factory-reset.
- **Monica Jacinto Reza** — Director of Materials Processing at NASA JPL; co-inventor of a nickel superalloy for rocket engines. Missing since June 22, 2025, Angeles National Forest, CA.
- **Steven Garcia** — government contractor reportedly at Kansas City National Security Campus. Missing since August 28, 2025, Albuquerque, NM. (Employer claim traces to a single anonymous source — flag this.)
- **William Neil McCasland** — retired U.S. Air Force Major General, former commander of AFRL at Wright-Patterson and Phillips Research Site at Kirtland AFB, former director of Special Programs at OUSD(AT&L) and executive secretary of the Special Access Program Oversight Committee. Missing since February 27, 2026, Albuquerque, NM.
- **Carl Grillmair** — Caltech/IPAC astrophysicist. Shot at his home, February 16, 2026, Llano, CA. Suspect arrested; charged with murder, carjacking, burglary.
- **Nuno Loureiro** — Director of MIT Plasma Science and Fusion Center. Shot at his home, December 15, 2025, Brookline, MA; died December 16. Suspect (former classmate from Portugal) linked to a separate Brown University shooting; died by suicide.
- **Michael David Hicks** — JPL research scientist (DART, NEAT, Dawn). Died July 30, 2023, Los Angeles.
- **Frank Maiwald** — JPL principal researcher (SBG-VSWIR, AMR). Died July 4, 2024, Los Angeles. Cause of death reportedly not publicly disclosed.
- **Jason Thomas** — Novartis associate director of chemical biology (cancer). Missing from Wakefield, MA December 12, 2025; found in Lake Quannapowitt March 17, 2026. Weaker fit — pharma, not aerospace/nuclear — include with clear inclusion rationale.
- **Amy Eskridge** — co-founder Institute for Exotic Science, antigravity researcher. Died June 11, 2022, Huntsville, AL. Ruled self-inflicted gunshot. Her father is a retired NASA engineer. Weaker fit — older, ruled suicide — include with clear inclusion rationale.

Use your judgment to add cases that fit the pattern and were missed, or exclude cases that don't fit on examination. Document every inclusion and exclusion decision in `logs/research-log.md`.

## Source discipline (critical — review README methodology before starting)

The README methodology section (written by prompt 000) defines the full tier system. Summary:

- **Tier 1** — Primary sources (LE releases, court docs, WH transcripts on .gov, institutional statements, Congressional records, direct family statements)
- **Tier 2** — Secondary reporting (mainstream and local news)
- **Tier 3** — Tertiary / aggregator
- **Tier 4** — Named expert commentary (on-the-record statements from identifiable experts)
- **Tier 5** — Secondary reporting relying on anonymous sources
- **Tier 6** — Independent commentary, Substack, YouTube, TikTok, podcasts
- **Tier 7** — Foreign state-affiliated press

Every factual claim additionally carries a confidence rating: **Confirmed**, **Reported**, **Alleged**, or **Speculated**. Tier is provenance. Rating is weight. They are independent.

**Copyright discipline:** Paraphrase, do not reproduce. Never quote more than ~15 words from a single source. Maximum one short quote per source. Summaries in your own words. This is both legal practice and good research practice — mechanical reproduction of source language is less useful than genuine synthesis.

**Refuse to invent:** If a fact cannot be sourced, say so. Leave gaps. Log them in `logs/known-unknowns.md`. Do not fill with plausible-sounding assertions.

## Pre-registered hypotheses

Before any pattern analysis, these hypotheses are registered. The research evaluates evidence for and against each, rather than pattern-hunting post hoc. You may add hypotheses to this list but may not remove or weaken any without explicit justification in `analysis/hypotheses.md`.

- **H1 — Coincidence / base-rate null hypothesis.** The cluster is a function of selection bias, base rates of mortality and disappearance in a large professional population, and post-hoc grouping.
- **H2 — Geographic clustering (New Mexico).** The concentration of cases in NM reflects the concentration of nuclear and aerospace defense work in NM (LANL, Kirtland, Sandia, KCNSC-NM), not a targeted pattern.
- **H3 — Institutional clustering (JPL / Caltech).** The LA County cluster reflects JPL/Caltech's outsized role in civilian space research, not targeting.
- **H4 — Foreign intelligence targeting (any state actor).** One or more foreign state intelligence services targeting U.S. defense-adjacent scientists. Evaluate against historical precedent and specific case evidence. No country pre-excluded or pre-implicated.
- **H5 — Propulsion and advanced-materials specialization.** Cases cluster in specific research domains (rocket propulsion, advanced metallurgy, plasma physics, fusion) that have strategic value.
- **H6 — UAP/UFO disclosure-community adjacency.** Subjects have documented ties to UAP disclosure efforts (McCasland's consulting for DeLonge's advisory work; Eskridge's exotic physics; AFRL-Wright-Patterson lineage). Evaluate the documentary record.
- **H7 — Internal U.S. program protection.** Targeting by U.S. government or contractor elements to protect classified programs from disclosure. Evaluate against historical precedent and specific case evidence.
- **H8 — Independent, unrelated events misgrouped.** Each case has its own mundane or criminal explanation (Grillmair and Loureiro most cleanly fit this) and the cluster is a media artifact.
- **H9 — Exotic hypotheses.** UAP/non-human-intelligence involvement, interdimensional, and similar. Evaluated as hypotheses: what evidence would support, what evidence contradicts, what is the base rate. Not pre-dismissed; not endorsed without evidence.

The analysis does not need to pick a winner. It evaluates each hypothesis against the evidence and states what it finds.

## Sub-agent orchestration

Use Claude Code's Task tool to parallelize. Recommended structure — adjust as you see fit, but document what you chose in `logs/research-log.md`:

1. **Lead / orchestrator (you)** — reads this prompt, spawns sub-agents, enforces source discipline, merges outputs, writes the abstract and executive summary last.
2. **Case-research sub-agents (parallel, one per case)** — each one researches a single case. Writes `cases/{slug}.md` and contributes to `appendices/primary-sources/`. Bounded search budget: roughly 8–12 attempts at Tier 1 sources, 5–10 at Tier 2 corroborations, more only if the case has unusual depth or complexity. Reports undersourcing honestly — does not pad with tertiary junk.
3. **Primary-source hunter sub-agent (separate, runs in parallel with case agents)** — its only job is to locate and excerpt Tier 1 documents across all cases. Populates `appendices/primary-sources/`. Does not write prose. Collects evidence only.
4. **Foreign-coverage sub-agent** — searches foreign-press coverage in countries with geopolitical stakes in this story (Russia, China, Iran, Israel, UK, France, Germany, India, Japan, plus others if relevant). Translates excerpts where needed. Notes country of origin and known editorial orientation. No country pre-excluded or pre-implicated. Where outlets are paywalled, looks for syndicated reposts on aggregators; if none exists, notes the existence of the paywalled source in `logs/known-unknowns.md` and does not attempt to bypass the paywall.
5. **Named-expert-commentary sub-agent** — locates on-the-record statements from identifiable experts (Coulthart, Elizondo, Swecker, CSIS/NTI analysts, others). Evaluates each on credentials and relevance. Populates `appendices/named-expert-commentary/`.
6. **Cross-case analysis sub-agent (runs after case files are complete)** — reads all finalized case files and produces `analysis/connection-analysis.md` at three layers (Tight / Medium / Corkboard). Evaluates pre-registered hypotheses in `analysis/hypotheses.md`. Writes the dedicated foreign-intelligence analysis layer in `analysis/foreign-intel-layer.md`.
7. **Diagram-and-timeline sub-agent (runs after analysis is complete)** — produces `data/diagram-data.json` and `data/timeline-data.json` (and their JSON Schemas in `data/schema/`), consuming the finalized case files and analysis. Must produce data, not rendering — structured JSON that prompt 003 will consume.

Instructions each sub-agent must receive (the orchestrator embeds these):
- Full safety rules (copy from this prompt)
- Source-tier taxonomy and confidence-rating system (copy from README)
- Copyright discipline (paraphrase, ≤15 words per quote, one quote per source max)
- Refuse-to-invent rule
- The hypotheses list (read-only reference)
- Required output format (see "Artifact specifications" below)
- Bounded search budget
- Reporting format for dead ends (what to write in `logs/research-log.md`)

Sequencing:
- 2, 3, 4, 5 run in parallel (independent research streams).
- 6 runs after 2 completes (needs finalized case files).
- 7 runs after 6 completes (needs finalized analysis).
- Orchestrator writes the dossier's executive summary and abstract **last**, after everything else exists, so the summary reflects what was actually produced, not what was planned.

## Artifact specifications

### `README.md`
Expand the skeleton written by prompt 000. Include:
- Project description
- The full methodology section (already written by 000, preserve it)
- "How to read this repository" — navigation guide for humans
- Living-artifact note — how updates work, reference to prompt-004 for maintenance
- Source tier legend (short form)
- Confidence rating legend (short form)
- Repository structure explanation

### `dossier.md` (the main artifact)
Top-level synthesized document. Structure:
1. **Abstract** (200–400 words) — written last. Summarizes what the research found, emphasizing what is and is not known. Neutral register.
2. **Executive summary** (800–1500 words) — written last. Longer synthesis with the main findings, hypothesis evaluations, and open questions.
3. **Methodology reference** — short, points to README.
4. **Case index** — table of all cases with: name, status, date of incident, location, affiliation, inclusion rationale, link to `cases/{slug}.md`.
5. **Connection analysis summary** — short version, points to `analysis/connection-analysis.md` for full treatment.
6. **Hypothesis evaluation summary** — short version, points to `analysis/hypotheses.md`.
7. **Open questions and known unknowns** — points to `logs/known-unknowns.md`.

### `cases/{slug}.md` (one per case)
Consistent schema across all case files. Required fields:
- **Slug and title**
- **Status** (Missing / Deceased — circumstances / Deceased — suspect apprehended / etc.)
- **Key dates** (last seen, reported missing, body found, death date, etc.)
- **Location(s)**
- **Affiliation and role** (with confidence ratings per claim)
- **Inclusion rationale** (why this case is in the repository; strong / weak fit)
- **Narrative of known facts** (paragraph prose, every factual claim tagged with tier and confidence rating; copyright discipline applied throughout)
- **What is documented vs. what is reported vs. what is alleged vs. what is speculated** — clearly separated sections or inline labels
- **Primary sources** — links to Tier 1 documents with verbatim excerpts in `appendices/primary-sources/{slug}/`
- **Secondary sources** — links only
- **Named expert commentary** — if any, with link to full text in `appendices/named-expert-commentary/`
- **Foreign coverage** — if any, with link and origin/orientation note
- **Contradictions** — any source-to-source disagreements on facts, cross-referenced to `logs/contradictions.md`
- **Open questions** — what this case's research could not resolve

### `appendices/primary-sources/{slug}/` (per case)
Verbatim excerpts of Tier 1 documents. Each excerpt is its own markdown file with:
- Source URL and access date
- Publisher/author
- Document type (press release, court filing, Silver Alert, etc.)
- Full text (or the relevant excerpt) — respecting copyright on paraphrase-vs-quote rules; institutional press releases and court documents can be quoted more fully as they are typically public-record, but err on the side of excerpt + link
- Date of document

### `appendices/named-expert-commentary/`
One file per named expert. Each file:
- Expert name, credentials, relevant professional history
- On-the-record statements (with source link and date)
- Relevance assessment (does this person have direct knowledge, adjacent expertise, or public commentary only)
- Any documented conflicts of interest or professional positioning

### `appendices/foreign-coverage/`
One file per country with meaningful coverage. Each file:
- Country and outlet(s)
- Outlet orientation (state-affiliated, independent, opposition, etc.) — documented, not inferred
- Coverage summary with translated excerpts where relevant
- How the coverage differs from U.S. reporting, if at all

### `analysis/connection-analysis.md`
Three layers, clearly labeled:
- **Tight** — Only documented, verifiable overlaps (employment, funding, geography, timing). Each connection cited to a specific source.
- **Medium** — Research-domain adjacencies, institutional funding chains, pattern-of-life similarities. Marked as research-supported inference.
- **Corkboard** — Speculative threads in public discussion (UAP/disclosure-community, targeting theories, exotic hypotheses). Clearly marked as speculative and attributed to the speculators.

Every connection carries a confidence rating. The section makes explicit what is documented, what is inferred, and what is speculated.

### `analysis/hypotheses.md`
Each hypothesis (H1–H9 and any added) gets:
- Statement of the hypothesis
- Evidence that would support it
- Evidence that would contradict it
- What the research found (evidence for, evidence against)
- Current assessment (supported / partially supported / not supported / indeterminate — with reasoning)

### `analysis/foreign-intel-layer.md`
Dedicated layer for H4 (and any refinements). Covers:
- Historical precedent for state-actor targeting of defense scientists (general, not speculative about current cases)
- Specific case evidence, if any, for each relevant state actor
- Assessment by named experts (Swecker, etc.) with credential context
- Open questions
- Explicit neutrality: no country pre-excluded or pre-implicated; evaluated on evidence alone

### `data/diagram-data.json`
Structured spec for the connection diagram. Schema (written to `data/schema/diagram-schema.json`):
- **Nodes** — people, institutions, programs, events, locations. Each with: id, label, type, metadata (affiliations, dates, URLs).
- **Edges** — connections. Each with: source id, target id, edge type (employment / funding / research-domain / geography / speculative-UAP / speculative-intel / other), layer (tight / medium / corkboard), confidence rating, evidence pointer (which case file or appendix supports this edge), label.
- **Layer metadata** — what each layer contains and how it's rendered.

### `data/timeline-data.json`
Structured spec for the timeline. Schema:
- **Events** — each with: id, date, type (disappearance / death / investigation milestone / institutional statement / political event), subject (case slug), description, source pointer, confidence rating.
- **Context events** — non-case events that provide context (White House briefing, House Oversight announcement, etc.).

### `logs/research-log.md`
Chronological log. Every sub-agent appends. Entries include:
- What was searched
- What was found (or not)
- Dead ends with reason
- Decisions made (inclusions, exclusions, scope boundaries)

### `logs/contradictions.md`
Table or structured list. Every source-to-source factual disagreement with resolution status.

### `logs/known-unknowns.md`
What the research could not resolve, with specificity (e.g., "Could not locate BCSO press release for Feb 28, 2026; only secondary reporting available").

### `CHANGELOG.md`
Initial entry: `v0.1.0 — Initial research complete`. Dated.

## Commit strategy
Commit incrementally as artifacts are produced. Suggested cadence:
- One commit per completed case file
- One commit per appendix section
- One commit for analysis files
- One commit for data/schema
- Final commit for dossier (abstract + exec summary)

Commit messages: `scope: description` (e.g., `case: add Chavez dossier entry`, `appendix: add primary-source excerpts for Casias`).

## End conditions
The prompt is complete when:
- All case files exist and are internally consistent
- All appendix directories are populated (or documented as empty with reason)
- All analysis files are complete
- Both data JSON files validate against their schemas
- All logs are populated honestly
- `dossier.md` is complete with abstract and executive summary written last
- Git log shows incremental commits throughout
- A final `STATUS.md` file at the repo root summarizes: what was produced, what was skipped and why, how long it took, and any flags for the user to review before running prompt 002

Do not run prompt 002 or 003 from this prompt. Do not generate PDFs. Do not touch `mattnoth-dev/`.

End of prompt 001.
