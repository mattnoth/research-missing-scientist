# Prompt Deep-002 — Professional Networks & Institutional Analysis

## Non-interactive execution (read first)

This prompt runs via `claude -p --output-format=stream-json` — print mode. There is no stdin. Make decisions autonomously per the spec. Log ambiguities in `logs/research-log.md` and proceed.

You are Claude Code operating in `/Users/mnoth/source/research-missing-scientists/`. This prompt investigates the professional and institutional connections between subjects using non-news sources: patent databases, academic publications, grant records, and contract vehicles. The goal is to discover documented (Tier 1) professional overlaps that news reporting may have missed or only hinted at.

## Hard Safety Rules

- Working directory: `/Users/mnoth/source/research-missing-scientists/`. Do not touch anything outside it.
- No sudo. No system-wide installs.
- No git push. No auth to any service.
- No contacting anyone. Research uses already-public material only.
- Copyright discipline: paraphrase, ≤15 words per quote, one quote per source max.
- If unsure, stop and log the uncertainty.

## Alignment (read `prompts/research/README.md` § "Alignment rules" before starting)

This prompt creates or updates files in `appendices/professional-networks/` (new directory). It also updates `cases/{slug}.md` source sections and `logs/`. It does NOT touch analysis files, data files, or dossier.md — that happens in prompt-deep-005.

## Context

The existing research notes several potential professional connections:
- Reza and McCasland may have overlapping AFRL ecosystem ties (WION flagged a "Mondaloy connection")
- Multiple subjects touched propulsion, advanced materials, or plasma physics
- JPL/Caltech cluster (Grillmair, Hicks, Maiwald, Reza)
- LANL/NM cluster (Chavez, Casias, Garcia proximity)
- McCasland's AFRL/Wright-Patterson and Special Programs oversight role

But these connections are mostly inferred from news profiles, not verified from primary professional records.

## Sub-agent orchestration

Spawn 4 thematic sub-agents in parallel:

### Agent 1: Patent & Invention Records

```
Search patent databases for all 11 subjects. Focus on:
- USPTO (patents.google.com, USPTO full-text search)
- Search by inventor name for each subject
- For each patent found: record patent number, title, filing date, co-inventors, assignee
- Map co-inventor networks — do any subjects share co-inventors?
- Map assignee networks — do patents cluster under the same programs or contractors?

Key subjects to prioritize (most likely to have patents):
- Monica Reza (JPL materials science, nickel superalloy co-inventor)
- Frank Maiwald (JPL instruments)
- Michael Hicks (JPL research)
- Carl Grillmair (astrophysics instruments/surveys)
- Nuno Loureiro (plasma physics)
- Amy Eskridge (exotic science / antigravity)

Write findings to `appendices/professional-networks/patents.md`.
Update relevant `cases/{slug}.md` with patent citations as Tier 1 sources.
Log all searches in `logs/research-log.md`.

Commit: `research-deep-002: patent network analysis`
```

### Agent 2: Academic Publication Networks

```
Search academic databases for publication records of all 11 subjects. Focus on:
- Google Scholar profiles
- NASA ADS (for astrophysics/aerospace subjects)
- arXiv (preprints)
- ORCID records
- PubMed (for Thomas — pharma/chemical biology)
- ResearchGate profiles

For each subject:
- List key publications (title, journal, year, co-authors)
- Identify co-author overlaps between subjects
- Map research domain overlaps (propulsion, materials, plasma, etc.)
- Note any publications that reveal program affiliations not mentioned in news

Key questions:
- Did Reza and any AFRL-affiliated researchers co-publish?
- Did Hicks and Maiwald collaborate or share co-authors?
- What specific programs did Loureiro's fusion work connect to?
- Did Eskridge publish with anyone in the defense/aerospace cluster?
- Does McCasland appear as a co-author or in acknowledgments?

Write findings to `appendices/professional-networks/publications.md`.
Update relevant `cases/{slug}.md` with publication citations as Tier 1 sources.
Log all searches in `logs/research-log.md`.

Commit: `research-deep-002: publication network analysis`
```

### Agent 3: Government Contract & Grant Records

```
Search government contract and grant databases for institutional connections. Focus on:
- USAspending.gov — contracts awarded to employers (JPL, LANL, MIT PSFC, Caltech, KCNSC, AFRL)
- NSF Award Search — grants to subjects or their labs
- DOE OSTI (osti.gov) — technical reports from DOE-funded research
- SBIR/STTR databases — small business research grants
- SAM.gov — entity registrations for relevant contractors
- Federal grant databases (grants.gov past awards)

Key questions:
- What specific contracts or programs connected LANL, JPL, and AFRL in the relevant timeframe?
- Did any of the subjects' employers share contract vehicles or program offices?
- Are there DOE or DOD programs that multiple subjects' institutions participated in?
- What is the KCNSC contractor ecosystem? (Honeywell FM&T is the prime — what subcontractors?)
- Did Eskridge's Institute for Exotic Science receive any federal funding?

Write findings to `appendices/professional-networks/contracts-grants.md`.
Update relevant `cases/{slug}.md` where contract records clarify affiliations.
Log all searches in `logs/research-log.md`.

Commit: `research-deep-002: contract and grant analysis`
```

### Agent 4: Professional Associations & Conference Records

```
Search for subjects' professional footprints beyond publications:
- Conference proceedings and speaker lists (APS, AGU, AIAA, ACS, IEEE)
- Professional association membership or leadership (where publicly listed)
- LinkedIn profiles or cached versions (public-facing only)
- University faculty pages, lab group pages (current or archived)
- Advisory board memberships
- Expert witness disclosures
- Congressional testimony records

Key questions:
- Did any subjects serve on the same advisory boards or review panels?
- Did they present at the same conferences in overlapping years?
- Were any involved in the same professional working groups?
- McCasland's SAPOC role — what programs might he have overseen that connected to other subjects' work?
- Eskridge's antigravity research — what was the broader community? (Podkletnov, Ning Li, etc.)

Write findings to `appendices/professional-networks/associations.md`.
Update relevant `cases/{slug}.md` where association records add context.
Log all searches in `logs/research-log.md`.

Commit: `research-deep-002: professional association analysis`
```

### Orchestrator responsibilities

After all sub-agents complete:

1. Read all four output files in `appendices/professional-networks/`.
2. Create `appendices/professional-networks/cross-reference.md`:
   - Which subjects appear in shared networks (co-inventors, co-authors, shared programs)?
   - Which connections are documented (Tier 1) vs. inferred?
   - What new connections were discovered that news reporting missed?
   - What searches yielded nothing (important negative results)?
3. Append orchestrator summary to `logs/research-log.md`.
4. Commit: `research-deep-002: orchestrator cross-reference and summary`

## End conditions

- All 4 thematic agents have completed.
- `appendices/professional-networks/` contains 5 files (patents, publications, contracts-grants, associations, cross-reference).
- `cases/{slug}.md` files updated with Tier 1 professional sources where found.
- `logs/research-log.md` documents all searches.
- No analysis, data, or dossier files modified.

End of prompt deep-002.
