# Prompt Deep-004 — Historical Precedent & Base-Rate Analysis

## Non-interactive execution (read first)

This prompt runs via `claude -p --output-format=stream-json` — print mode. There is no stdin. Make decisions autonomously per the spec. Log ambiguities in `logs/research-log.md` and proceed.

You are Claude Code operating in `/Users/mnoth/source/research-missing-scientists/`. This prompt addresses two critical analytical gaps: (1) historical precedent for state-actor targeting of scientists, and (2) base-rate statistical context for evaluating whether the observed cluster is anomalous. These are the most important inputs for evaluating hypotheses H1 (coincidence) and H4 (foreign intelligence).

## Hard Safety Rules

- Working directory: `/Users/mnoth/source/research-missing-scientists/`. Do not touch anything outside it.
- No sudo. No system-wide installs.
- No git push. No auth to any service.
- No contacting anyone. Research uses already-public material only.
- Copyright discipline: paraphrase, ≤15 words per quote, one quote per source max.
- If unsure, stop and log the uncertainty.

## Alignment (read `prompts/research/README.md` § "Alignment rules" before starting)

This prompt creates files in `appendices/historical-precedent/` and `appendices/base-rate-analysis/` (new directories). It does NOT touch case files, analysis files, data files, or dossier.md. The integration prompt (deep-005) will weave these findings into the analysis.

## Sub-agent orchestration

Spawn 3 thematic sub-agents in parallel:

### Agent 1: Historical Precedent — Foreign Targeting of Scientists

```
Research documented historical cases of foreign intelligence services targeting scientists and defense personnel. Focus on cases with declassified or publicly documented evidence.

Categories to research:

1. **Cold War era (documented)**:
   - Soviet intelligence operations targeting U.S. nuclear scientists (beyond the well-known spy cases)
   - CIA operations targeting Soviet/Chinese scientists
   - Scientist defections and their circumstances
   - Mysterious deaths of scientists attributed to intelligence operations (e.g., Frank Olson, Gerald Bull)

2. **Post-Cold War (1990s–2010s)**:
   - Iran's nuclear scientist assassinations (2010–2020) — Mohsen Fakhrizadeh and predecessors
   - Iraqi scientist deaths post-2003 invasion
   - North Korean scientist defection attempts
   - Chinese intelligence recruitment of U.S. researchers (documented DOJ cases)

3. **Contemporary (2015–present)**:
   - DOJ "China Initiative" prosecutions — what patterns of targeting were documented?
   - Russian intelligence operations targeting Western defense researchers
   - Documented SVR/GRU/MSS operations against defense-adjacent targets
   - Any documented Mossad operations against scientists in this period

4. **Methodology patterns**:
   - How do intelligence services historically target scientists? (recruitment vs. elimination vs. intimidation)
   - What makes a scientist a target? (clearance level, specific knowledge domains, access to programs)
   - Historical evidence on whether targeting looks like what we see in these 11 cases

For each historical case:
- Source: academic papers, declassified documents, court records, credible investigative journalism (books, longform)
- Tier: most will be Tier 1 (court docs, declassified) or Tier 2 (investigative books/journalism)
- Relevance: how does this precedent inform evaluation of the current cluster?

Write to `appendices/historical-precedent/foreign-targeting.md`.
Log all searches in `logs/research-log.md`.
Commit: `research-deep-004: historical precedent — foreign targeting`
```

### Agent 2: Historical Precedent — Domestic Incidents

```
Research documented historical cases of unusual deaths or disappearances of U.S. defense/intelligence personnel where the cause remained unclear or contested.

Categories to research:

1. **Marconi scientists deaths (1980s UK)**:
   - 25+ defense electronics scientists died under unusual circumstances in 1980s Britain
   - What was ultimately determined? Government investigations, academic analysis
   - How does that cluster compare to the current one in scale, timeline, and professional domain?

2. **U.S. microbiologists deaths (2001–2005)**:
   - Cluster of microbiologist deaths following anthrax attacks
   - How many, what were the circumstances, what investigations occurred?
   - Academic or investigative analysis of whether cluster was anomalous

3. **Other documented clusters**:
   - Any other documented clusters of defense-adjacent professional deaths
   - What was the outcome of investigations?
   - Were any confirmed as targeted vs. coincidence?

4. **Insider threat and program protection**:
   - Documented cases where U.S. government actions harmed or silenced its own personnel to protect classified programs
   - Whistleblower retaliation cases in defense/intelligence (documented, not alleged)
   - Relevant for evaluating H7 (internal program protection)

5. **SAP/Special Access Program history**:
   - McCasland's role as SAPOC executive secretary — what is publicly known about SAPOC?
   - Historical incidents involving SAP security (leaks, investigations, personnel actions)
   - Congressional oversight of SAPs — what has been publicly documented?

Write to `appendices/historical-precedent/domestic-incidents.md`.
Log all searches in `logs/research-log.md`.
Commit: `research-deep-004: historical precedent — domestic incidents`
```

### Agent 3: Base-Rate & Statistical Context

```
Research the statistical context needed to evaluate whether 11 events in ~4 years is anomalous for the U.S. defense/aerospace research workforce.

Data to find:

1. **Workforce demographics**:
   - Total size of U.S. defense/aerospace cleared workforce (ODNI annual reports, DCSA data)
   - DOE Q/L clearance holder counts (DOE reports)
   - LANL, JPL, MIT workforce sizes (annual reports, institutional data)
   - Total STEM workforce in defense-adjacent sectors

2. **Background mortality/disappearance rates**:
   - CDC WONDER data: death rates by occupation (if available) or by age/sex cohort matching the subjects
   - Missing persons statistics: NamUs, NCIC data on annual missing adults
   - National Vital Statistics System data relevant to age/sex cohorts
   - BLS Census of Fatal Occupational Injuries (CFOI) for relevant sectors

3. **Actuarial calculation**:
   - Given a population of ~30,000–150,000 (depending on how broadly "defense scientist" is defined), what is the expected number of deaths and disappearances in a 4-year window?
   - What is the expected number of homicides, accidents, disappearances per year in this demographic?
   - Is the observed cluster (11 events, some with apprehended suspects) statistically anomalous?
   - What assumptions drive the answer? Document sensitivity to population size and category definitions.

4. **Selection bias analysis**:
   - How many scientists/engineers at these institutions died of natural causes in the same period? (Obituary searches)
   - Is the grouping a function of media attention creating a category that didn't previously exist?
   - Are there professionals in non-defense sectors who went missing/died unusually in the same period that could just as easily be grouped?

5. **Prior academic analysis**:
   - Has anyone published statistical analysis of the current cluster or similar historical clusters?
   - Actuarial or epidemiological literature on occupational mortality in defense sectors

Write to `appendices/base-rate-analysis/statistical-context.md`.
Note: this is necessarily rough and bounded by available public data. Be explicit about what data was and wasn't available, and what assumptions drive any calculations. Ranges are better than false precision.

Log all searches in `logs/research-log.md`.
Commit: `research-deep-004: base-rate statistical context`
```

### Orchestrator responsibilities

After all sub-agents complete:

1. Read all output files.
2. Create `appendices/historical-precedent/summary.md`:
   - Key parallels to the current cluster
   - Key differences from the current cluster
   - What historical precedent suggests about plausibility of each hypothesis
3. Append orchestrator summary to `logs/research-log.md`.
4. Commit: `research-deep-004: orchestrator summary`

## End conditions

- All 3 thematic agents have completed.
- `appendices/historical-precedent/` contains: `foreign-targeting.md`, `domestic-incidents.md`, `summary.md`.
- `appendices/base-rate-analysis/` contains: `statistical-context.md`.
- `logs/research-log.md` documents all searches.
- No case files, analysis files, data files, or dossier modified.

End of prompt deep-004.
