# Research: Deaths and Disappearances of U.S. Defense and Advanced-Research Scientists

An evidence-based investigation into a cluster of deaths and disappearances of U.S. scientists and researchers tied to defense, aerospace, nuclear, and advanced-research programs.

## Methodology

### Source tiers
Every source cited in this repository is categorized by tier. Tiers are not a
fixed list of three — finer distinctions are used where the evidence warrants.

- **Tier 1 — Primary sources.** Law enforcement press releases and case
  bulletins (LAPD, BCSO, NMSP, LA County Sheriff, Taos County); court filings
  and charging documents; White House press-briefing transcripts on .gov or
  equivalent archival sources; official statements from DOE/NNSA/FBI/Air Force
  on .gov domains; Congressional records; institutional statements and
  obituaries published directly by the employer (Caltech, MIT PSFC, NASA JPL,
  LANL, KCNSC, AFRL); direct statements from family members (Facebook posts
  from verified family accounts, family-run search pages, on-camera press
  conferences) — primary for the family's own statements, not for facts about
  the investigation itself.

- **Tier 2 — Secondary reporting.** Mainstream news (CNN, CBS, ABC, NBC,
  Reuters, AP, Washington Post, NYT); local news (Albuquerque Journal, Taos
  News, Los Alamos Reporter, KRQE, KOB, CBS LA, Boston Globe); specialty
  trade press. Network "Dateline" and "what we know" roundups are Tier 2,
  not primary, even when they quote primary sources.

- **Tier 3 — Tertiary / aggregator.** Wikipedia; news roundups citing other
  news outlets without original reporting; "here's what we know so far"
  compilations.

- **Tier 4 — Named expert commentary.** On-the-record statements from
  identifiable subject-matter experts (e.g., former FBI officials, CSIS /
  NTI / think tank analysts, UAP-disclosure advocates with documented
  professional backgrounds). Evaluated individually on the expert's
  credentials and the relevance of their claim.

- **Tier 5 — Secondary reporting relying on anonymous sources.** Claims that
  appear in Tier 2 outlets but trace to a single anonymous source and are
  then repeated across other outlets. The Daily Mail's KCNSC employment
  claim for Steven Garcia is the canonical example.

- **Tier 6 — Independent commentary, Substack, YouTube, TikTok, podcasts,
  social media.** Useful for finding leads and seeing what claims are in
  circulation. Not used as evidence for factual claims.

- **Tier 7 — Foreign state-affiliated press.** Included when geopolitically
  relevant. Country of origin and known editorial orientation noted. Not
  dismissed for being foreign; not elevated for being foreign.

### Confidence ratings
Separate from source tier, every factual claim in this repository carries
one of the following labels:

- **Confirmed** — Multiple independent primary sources, or a single primary
  source making a self-evidencing statement (e.g., a sheriff's press
  release stating the sheriff issued an alert).
- **Reported** — Appears in credible secondary reporting, often with named
  sources, but not directly confirmable via primary documentation.
- **Alleged** — Claim made by a specific identifiable source but not
  independently confirmed.
- **Speculated** — Inference, theory, or pattern-matching not directly
  asserted by any source.

The **tier** tells you provenance. The **rating** tells you weight. These
are independent. A Tier 1 source can make a "may have been a danger to
himself" statement that rates only "Reported." A Tier 2 article can cite
a rock-solid court filing that rates "Confirmed."

### Inclusion criteria for cases
Cases are included based on this repository's own criteria, not based on
any external list (including the White House review list):

- Employment in or documented association with U.S. defense, aerospace,
  nuclear, or advanced-research programs
- Death or disappearance between 2022 and the present
- At least one of: unexplained circumstances; unresolved investigation;
  primary-source law-enforcement or institutional involvement

Cases that fit the pattern are included regardless of whether they appear
on any public list. Cases on public lists that do not fit the pattern are
still included, with a clear "inclusion rationale" explaining the weaker
fit (e.g., Amy Eskridge, Jason Thomas).

### Neutrality and bias handling
- No country or political entity is pre-excluded or pre-implicated.
  Hypotheses involving any state actor (including allies such as Israel
  and the United Kingdom, adversaries such as Russia, China, and Iran,
  and the United States itself) are evaluated on evidence alone.
- Sensational framing ("assassinations," "silenced," "targeted") is
  avoided in this repository's own prose. Such framing from sources is
  quoted and attributed, not adopted.
- White House, FBI, and other U.S. government statements are Tier 1 as
  documents (they are primary evidence of what was officially said) but
  the factual claims inside them are evaluated on the same standard as
  any other source.
- Exotic hypotheses (foreign intelligence targeting, UAP/UFO-related
  theories, other speculative frameworks) are evaluated as hypotheses:
  what evidence would support them, what evidence contradicts them, and
  what is the base rate. Not dismissed a priori; not endorsed without
  evidence.

### No contact policy
No attempts are made to contact any individual, family member, agency,
employer, or journalist in connection with this research. All sourcing
uses already-public material only.

## How to read this repository

- **`dossier.md`** — The top-level synthesized document covering all cases and analysis.
- **`cases/`** — One markdown file per case with structured facts, sources, and confidence ratings.
- **`appendices/`** — Supporting material: primary-source excerpts, named expert commentary, and foreign coverage with provenance.
- **`analysis/`** — Cross-case connection analysis, pre-registered hypotheses, and dedicated analysis layers.
- **`data/`** — Structured JSON specs for diagrams and timelines, with schemas.
- **`logs/`** — Research log, contradiction tracker, and known-unknowns register.

PDFs are generated separately (prompt 002) into `pdf-output/` and are gitignored. The website rendering is handled separately (prompt 003).
