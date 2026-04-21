# Research Log

Chronological record of searches performed, sources consulted, and decisions made. Also serves as the append-only session ledger per [.claude/commands/end-session.md](../.claude/commands/end-session.md).

## 2026-04-21 — Harness-integration conformance check (read-only)

**What happened:**
- Executed `drafts/prompt-harness-integration.md` Phases 1–3 (discovery, gap analysis, install plan).
- Harness classified as **Mature, conforming** — all three required artifacts present, adapter table matches, no conflicts.
- No filesystem changes made; `APPROVED` gate not reached because nothing needed doing.

## 2026-04-21 — Agent harness install (tailored)

**What happened:**
- Committed [INSTALL-PROMPT.md](../INSTALL-PROMPT.md) and [AGENT-HARNESS.md](../AGENT-HARNESS.md) — generic, portable agent-harness tooling.
- Installed a **tailored** harness variant in this repo instead of running the generic install. Rationale: this repo's knowledge already has a domain-native taxonomy (`cases/`, `analysis/`, `appendices/`, `logs/`); the generic layer model (`knowledge/`, `workflows/`, `extractions/`) would force renames without adding value.
- Created [NAVIGATION.md](../NAVIGATION.md) — intent-keyed routing table covering dossier, research content, methodology, open threads, agent operation.
- Created [.claude/commands/end-session.md](../.claude/commands/end-session.md) — session-close ritual with 8 steps: research-content capture, integrity artifacts (contradictions, known-unknowns, dossier sync), tier consistency, navigation, actionables reconciliation, mandatory research-log append, status/changelog, final report.
- Edited [CLAUDE.md](../CLAUDE.md) — added a "Session structure" section pointing at NAVIGATION.md, `/end-session`, and AGENT-HARNESS.md.
- Existing artifacts preserved and integrated: `logs/research-log.md` is the session ledger (this entry is the first dogfood), `TODO-research.md` is the actionables file.

**Key decisions:**
- No `progress.md` created — `logs/research-log.md` already plays that role.
- No `knowledge/`, `workflows/`, `extractions/` directories created — current structure is sufficient.
- Rotation threshold intentionally deferred: research-log is structured by prompt-run, not per-session entries. Split to `logs/research-log-prompt-NNN.md` when a run section grows unwieldy.
- INSTALL-PROMPT.md is kept in-repo (untracked → tracked) for future reuse, not because we ran the generic install here.

## 2026-04-20 — Bootstrap (prompt 000)

- Initialized repository structure.
- No research performed in this prompt; plumbing only.

## 2026-04-20 — Prompt 001 research begins

### Orchestration approach
- **Lead orchestrator** reads the full prompt, spawns sub-agents, enforces source discipline, merges outputs.
- **Case-research agents** — one per case, 11 total, run in parallel. Each writes `cases/{slug}.md` and populates `appendices/primary-sources/{slug}/`.
- **Primary-source hunter** — separate agent, runs in parallel with case agents, focuses exclusively on Tier 1 documents.
- **Foreign-coverage agent** — searches foreign press, runs in parallel.
- **Named-expert-commentary agent** — locates on-the-record expert statements, runs in parallel.
- **Cross-case analysis agent** — runs after case files are complete.
- **Diagram-and-timeline agent** — runs after analysis is complete.
- Orchestrator writes dossier abstract and executive summary **last**.

### Cases included (initial list from prompt)
1. Anthony "Tony" Chavez — LANL, missing May 2025
2. Melissa Casias — LANL, missing June 2025
3. Monica Jacinto Reza — NASA JPL, missing June 2025
4. Steven Garcia — govt contractor (disputed), missing Aug 2025
5. William Neil McCasland — retired USAF Maj Gen, missing Feb 2026
6. Carl Grillmair — Caltech/IPAC, shot Feb 2026 (suspect arrested)
7. Nuno Loureiro — MIT PSFC, shot Dec 2025 (suspect linked)
8. Michael David Hicks — JPL, died July 2023
9. Frank Maiwald — JPL, died July 2024
10. Jason Thomas — Novartis, missing Dec 2025 / found Mar 2026 (weaker fit)
11. Amy Eskridge — exotic science researcher, died June 2022 (weaker fit)

### Decisions
- All 11 cases from the prompt are included initially. Inclusion rationale will be documented per case.
- Additional cases may be added if discovered during research. Exclusions documented here.

### Chavez case research

**Date:** 2026-04-20
**Researcher:** Sub-agent (Claude)

#### Searches performed
1. WebSearch: "Anthony Chavez Los Alamos missing 2025" -- 10 results, strong coverage
2. WebSearch: "Tony Chavez LANL missing New Mexico" -- 10 results, overlapping with #1
3. WebSearch: ""Anthony Chavez" "Los Alamos" missing" -- 10 results, overlapping
4. WebSearch: "Anthony Chavez Los Alamos police department missing person update 2025" -- 10 results
5. WebSearch: ""Anthony Chavez" LANL retired role job title Los Alamos National Laboratory" -- 10 results, no job title found
6. WebSearch: "Los Alamos National Laboratory statement Anthony Chavez missing employee" -- 10 results, no LANL-specific statement found
7. WebSearch: "Anthony Chavez Los Alamos Silver Alert Pueblo Canyon search cadaver dogs" -- 10 results

#### Pages fetched
1. NM DPS missing person record (T1) -- successful, key details extracted
2. Los Alamos Reporter LAPD notice (T1 via T3) -- successful
3. Los Alamos Reporter social media concern article (T3) -- successful, Carl Buckland friend details
4. CBS News broader pattern article (T4) -- successful but minimal Chavez-specific detail
5. KOB.com article (T3) -- content truncated, limited value
6. Boomtown Los Alamos article (T3) -- paywalled, only metadata extracted
7. michaelrcronin.com article (T5) -- successful but limited new detail
8. LA Daily Post LAPD search update (T3) -- successful, Deputy Chief Rodriguez quote
9. losalamosnm.gov county page (T1) -- returned HTTP 403
10. NewsNation article (T4) -- returned HTTP 403

#### Key findings
- **Tier 1 sources identified:** NM DPS missing person database entry; LAPD official statements (via local media and county website). County website returned 403.
- **No LANL institutional statement found.** Only the broader NNSA acknowledgment applies.
- **No Silver Alert found** despite Chavez being 78 years old.
- **Specific LANL role unknown.** No source identifies job title, division, or clearance status. This is a significant gap for inclusion assessment.
- **Case number:** #2025-0254 (from Los Alamos Reporter)
- **DOB confirmed:** January 7, 1947 (NM DPS)

#### Contradictions identified
- Height/weight discrepancy between NM DPS (5'7", 145 lbs) and LAPD notice (5'6", 135 lbs)
- Race listed as "Unknown/Other" in NM DPS vs. "White male" in LAPD notice
- Last seen date: NM DPS says 05/08 (report date), local media says May 4 (actual last sighting)
- NM DPS case entry date of 01/13/2023 is anomalous

#### Gaps remaining
- Specific LANL role/title/division
- Security clearance status
- Whether Silver Alert was issued
- Surveillance footage findings
- Medical history
- Who reported him missing
- Federal review status specific to this case
- Explanation for NM DPS 2023 case entry date

#### Files written
- `cases/chavez.md` -- full case file
- `appendices/primary-sources/chavez/nm-dps-missing-person-record.md`
- `appendices/primary-sources/chavez/lapd-missing-person-notices.md`

### Casias case research

**Date:** 2026-04-20
**Researcher:** Sub-agent (Claude)

#### Searches performed
1. WebSearch: "Melissa Casias LANL missing 2025" -- 10 results, strong coverage
2. WebSearch: "Melissa Casias Taos County missing" -- 10 results, overlapping with #1
3. WebSearch: "Melissa Casias Los Alamos missing person" -- 10 results, additional national outlets
4. WebSearch: "Melissa Casias phones factory reset wiped LANL" -- 10 results, confirmed family-sourced claim
5. WebSearch: "New Mexico State Police Melissa Casias press release missing endangered" -- found NamUs listing MP150628
6. WebSearch: "site:nmsp.dps.nm.gov OR site:namus.nij.ojp.gov Melissa Casias" -- confirmed NamUs entry
7. WebSearch: "Melissa Casias niece Jazmin McMillen phones wiped" -- traced phone-reset claim to McMillen

#### Pages fetched
1. ABQ Journal (Aug 26, 2025) -- most detailed single source; full timeline, phone detail, blue truck lead
2. Santa Fe New Mexican (early July 2025) -- strong early reporting; phone detail, family quotes
3. Taos News (July 9, July 23, Sept 3, 2025) -- local coverage, paywalled/JS-rendered (partial extraction only)
4. CBS News (2026) -- national aggregation; McMillen quote on clearance level
5. KOB (nuclear ties article) -- partial extraction only
6. NBC Dateline -- 403 error
7. NamUs MP150628 -- JS-rendered, confirmed via metadata only
8. KRQE -- 403 error
9. KOB (family one month) -- JS-rendered, minimal extraction

#### Key findings
- **Factory-reset phone claim is FAMILY-SOURCED (niece Jazmin McMillen), NOT confirmed by NMSP publicly.** Tier 3 provenance (via local media), not Tier 1.
- McMillen told CBS: "Melissa was an administrative assistant and did not have high-level clearance" -- pushes back on high-clearance framing.
- McMillen also told CBS she has not "seen any evidence linking her to any of the other cases."
- NMSP spokesperson Wilson Silver confirmed "no updates" in August 2025; notably restrained public posture.
- No standalone NMSP press release was found online.
- No LANL or DOE statement was found.
- Taos News reported "family divided" on July 9 -- details not fully accessible.
- Mark Casias (husband) repeatedly noted as "unavailable for comment."
- NamUs case MP150628 confirmed.

#### Contradictions identified
- Clearance level: task brief says "security clearance"; niece says "did not have high-level clearance" (not necessarily contradictory -- admin staff typically hold Q clearance for facility access)
- "Forgot badge" narrative vs. husband's account of her going to another LANL location
- Family division reported but not elaborated

#### Gaps remaining
- No Tier 1 confirmation of phone factory reset
- Taos News articles largely inaccessible (JS-rendered or paywalled)
- No LANL or DOE public statement located
- No information on investigation progress after September 2025
- Family division details unclear
- Foreign coverage not searched
- Surveillance footage details (alone? distressed? others visible?)
- Backpack contents unknown
- Post office errand purpose unknown

#### Files written
- `cases/casias.md` -- full case file
- `appendices/primary-sources/casias/namus-mp150628.md`
- `appendices/primary-sources/casias/nmsp-statements.md`

### Grillmair case research

**Date:** 2026-04-20
**Researcher:** Sub-agent (Claude)

#### Searches performed
1. WebSearch: "Carl Grillmair Caltech shot 2026" -- 10 results, strong coverage across major outlets
2. WebSearch: "Carl Grillmair IPAC astrophysicist killed" -- 10 results, overlapping; found Caltech memorial, Wikipedia, Newsweek congressional article
3. WebSearch: "Grillmair Llano California murder" -- 10 results, strong local and national coverage
4. WebSearch: "Freddy Snyder arraignment Lancaster Grillmair murder 2026" -- 10 results; confirmed postponement to April 29
5. WebSearch: ""Carl Grillmair" LA County Board honors resolution" -- 10 results; found Supervisor Barger adjournment
6. WebSearch: ""Freddy Snyder" Llano criminal history trespassing Grillmair property" -- 10 results; found LA Times deep dive via Yahoo syndication
7. WebSearch: ""Carl Grillmair" "Los Angeles Times" Llano porch desert compound" -- 10 results
8. WebSearch: "Grillmair LASD press release homicide Llano February 2026" -- 10 results; no direct LASD .gov URL found

#### Pages fetched
1. ABC7 Los Angeles -- charges and timeline (T3), successful
2. Caltech official memorial (T1) -- successful, comprehensive biographical data
3. FOX 11 Los Angeles -- suspect prior arrest details (T3), successful
4. Wikipedia -- Carl Grillmair biography (T5), successful, useful for cross-referencing
5. Pasadena Now -- prior arrest and release details (T3), successful
6. MyNewsLA -- initial LASD report details (T3), successful
7. MyNewsLA -- arraignment postponement (T3), successful
8. Yahoo News (LA Times syndication) -- December trespassing deep dive (T3), successful; most detailed source on Snyder's criminal history
9. CBS Los Angeles -- initial shooting report (T3), successful
10. Caltech student newspaper (The California Tech) -- colleague quotes (T3), successful
11. KTLA -- 403 error
12. LA Mag -- 403 error

#### Key findings
- **Named suspect Freddy Snyder, 29, charged with murder, carjacking, and burglary.** Strong criminal case.
- **Pattern of escalating criminal behavior by Snyder:** trespassing with loaded rifle (Dec 20) -> attempted jail escape (Dec 21) -> released on OR (Dec 23) -> neighbor burglary (Dec 28) -> weapons charges dismissed (Feb 5) -> fatal shooting (Feb 16) -> carjacked own mother (Feb 16).
- **System failure:** Felony weapons charges dismissed less than two weeks before the murder, reportedly due to lack of prior record.
- **No known motive disclosed.** Detectives say they found no prior connection between the men beyond the December trespassing.
- **Grillmair's work was entirely unclassified civilian research:** exoplanets, stellar streams, near-Earth object surveying. No known security clearances.
- **Caltech memorial (T1) provided comprehensive career details.** 147 publications, NASA medal, nearly 30 years at IPAC.
- **LA County Board of Supervisors honored Grillmair on March 3, 2026 (T1).**
- **No direct LASD press release found on lasd.org.** All LE-sourced facts come through media relay.

#### Contradictions identified
- Date of death: Feb 16 (consensus/most sources) vs. Feb 17 or Feb 21 in some outlets
- Bail amount: $2M (CBS) vs. $3.175M (Fox 11, MyNewsLA, Pasadena Now)
- 911 caller identity not disclosed

#### Gaps remaining
- No motive publicly disclosed
- No direct LASD press release located (only media relays of LE information)
- Arraignment outcome unknown (scheduled for April 29, 2026)
- Snyder's mental health status and whether evaluation ordered
- Identity of 911 caller
- Whether firearm used in shooting forensically matches the rifle from December
- No court filings directly accessed (no public docket link found)
- LA Times deep investigation was accessible only through Yahoo syndication

#### Assessment
This case has the strongest non-conspiracy explanation of any in the cluster. A local man with an escalating pattern of criminal behavior, who had previously trespassed on Grillmair's property while armed, returned and killed him. The primary systemic question is why the justice system failed to hold Snyder after the December arrest. This case supports hypothesis H8 (independent events misgrouped) most strongly. It does not support H4, H5, or H7.

#### Files written
- `cases/grillmair.md` -- full case file
- `appendices/primary-sources/grillmair/caltech-memorial.md`
- `appendices/primary-sources/grillmair/la-county-bos-adjournment.md`
- `appendices/primary-sources/grillmair/lasd-initial-report.md`

### Reza case research

**Date:** 2026-04-20
**Researcher:** Sub-agent (Claude)

#### Searches performed
1. WebSearch: "Monica Jacinto Reza JPL missing 2025" -- 10 results, strong coverage across T3/T4/T7 sources
2. WebSearch: "Monica Reza NASA JPL Angeles National Forest missing" -- 10 results, overlapping; House Oversight and Newsweek results
3. WebSearch: "Monica Reza nickel superalloy inventor patent JPL" -- 10 results; patent records confirmed via Google Patents and Justia
4. WebSearch: ""Monica Jacinto" OR "Monica Reza" LASD sheriff missing person statement 2025" -- 10 results; KTLA, Crescenta Valley Weekly, Websleuths
5. WebSearch: ""Monica Jacinto" patent US20100266442 "burn-resistant" nickel alloy" -- 10 results; patent details confirmed
6. WebSearch: ""Monica Reza" OR "Monica Jacinto" "Find a Grave" death declared 2025" -- 10 results; Sentinel Briefing investigation
7. WebSearch: ""Monica Jacinto" JPL "materials processing" director Aerojet Rocketdyne career" -- 10 results; LinkedIn profile located (not fetched), career timeline
8. WebSearch: ""Monica Reza" cell phone forensic data Angeles National Forest search evidence 2025" -- 10 results; Sentinel phone gap article
9. WebSearch: "House Oversight Committee missing scientists investigation Monica Reza 2026" -- 10 results; Comer/Burlison press release, Fortune, Newsweek
10. WebSearch: "NASA JPL statement Monica Reza missing scientist 2025 2026" -- 10 results; no JPL-specific statement found
11. WebSearch: ""Monica Reza" 911 call screaming woman Mount Waterman June 2025" -- 10 results; Sentinel and Websleuths

#### Pages fetched
1. Wikipedia - Monica Jacinto (T5) -- successful, comprehensive biography with reliability caveats noted on page
2. FOX 11 Los Angeles (T3) -- successful, LASD lead agency confirmed, federal probe details
3. Solve the Case / LASD listing (T1) -- successful, full physical description, case numbers, detective names
4. Google Patents US-20100266442-A1 (T1) -- successful, full patent details, inventors, composition, applications
5. Crescenta Valley Weekly / Vienna statement (T1 via T3) -- successful, key LASD quotes
6. The Sentinel Briefing "Green Burial" (T7) -- successful, Find a Grave anomaly, search evidence details
7. Yahoo News / Men's Journal (T4) -- successful, companion details, running claim, career details
8. The Sentinel Briefing "Phone Gap" (T7) -- successful, cell phone forensics claim, 911 call
9. Justia Patents (T1) -- returned 403
10. KTLA (T3) -- returned 403
11. NewsNation (T4) -- returned 403
12. House Oversight press release (T1) -- returned 403

#### Key findings
- **Patent claims CONFIRMED.** Three US patent applications (2003, 2004, 2010) for "Burn-resistant and high tensile strength metal alloys" list Monica A. Jacinto and Dallis Ann Hardwick as co-inventors. Alloy known commercially as Mondaloy. Used in AR1 engine components. Patent assigned to individuals, not corporate entity.
- **JPL title partially verified.** LASD listing on Solve the Case states "Director of the Materials Processing Group at NASA JPL" (T1). No JPL directory or NASA statement independently confirms. Wikipedia repeats title with reliability caveats.
- **Prior career at Aerojet Rocketdyne confirmed** (37+ years, Technical Fellow rank). Also worked at Boeing (2004, Associate Technical Fellow).
- **LASD is lead agency.** Case NIC: M668487735. Classified as "at-risk missing person." Assigned to Homicide Bureau Missing Persons Unit.
- **Find a Grave anomaly documented.** Memorial created June 26, 2025, listing death date June 22, 2025, with "green burial" -- while search was still active. Memorial removed ~March 27, 2026, after media reporting.
- **Cell phone forensic data was obtained but not publicly released** (per since-removed Montrose SAR Facebook post).
- **911 call same morning** from Mt. Waterman area reported woman screaming. Not publicly connected to or excluded from case.
- **No NASA/JPL institutional statement found** specifically about Reza.
- **No family public statements found** beyond privacy request conveyed through LASD.
- **Federal investigation confirmed** via House Oversight Committee (Comer/Burlison) and White House.

#### Contradictions identified
1. Find a Grave memorial with death date and "green burial" created while search active; no death certificate or remains located
2. Cell phone data obtained but never released; SAR post about it removed
3. Minor title discrepancies across sources (Director of Materials Processing vs. Director of Materials Processing Group vs. Fellow at Rocketdyne -- likely sequential roles)

#### Gaps remaining
- No JPL organizational confirmation of title
- No NASA/JPL public statement about Reza
- Hiking companions not publicly identified
- Cell phone forensic results unknown
- Find a Grave creator "lillian" not identified
- Security clearance level unspecified
- No family public statements beyond privacy request
- Connection to McCasland (also missing) alleged but unconfirmed
- Dallis Hardwick (co-inventor, d. 2015) death circumstances not examined
- House Oversight press release content not accessible (403)

#### Files written
- `cases/reza.md` -- full case file
- `appendices/primary-sources/reza/lasd-missing-person-listing.md`
- `appendices/primary-sources/reza/lasd-vienna-statement-2025-07-03.md`
- `appendices/primary-sources/reza/patent-us20100266442a1.md`

### Hicks case research

**Date:** 2026-04-20
**Researcher:** Sub-agent (Claude)

#### Searches performed
1. WebSearch: "Michael David Hicks JPL died 2023" -- 10 results, strong coverage (DPS memorial, LPL memorial, Newsweek, oversight.house.gov)
2. WebSearch: "Michael Hicks JPL DART Dawn scientist obituary" -- 10 results, overlapping; found LPL news article, multiple 2026 pattern articles
3. WebSearch: "Michael Hicks JPL cause of death autopsy Los Angeles coroner" -- 10 results, mostly Michael Jackson results; no coroner-specific Hicks data
4. WebSearch: ""Michael Hicks" JPL Sunland California death 2023 family" -- 10 results; found Forest Lawn obituary
5. WebSearch: ""Michael Hicks" asteroid NEAT DART publications JPL" -- 10 results; no direct publication list, confirmed 80+ papers
6. WebSearch: "Comer Burlison missing scientists JPL Hicks Maiwald investigation" -- 10 results; confirmed Congressional inquiry
7. WebSearch: "White House FBI investigation dead missing scientists NASA JPL 2026" -- 10 results; confirmed federal review
8. WebSearch: "missing dead NASA scientists Global Times Russia China coverage Hicks Maiwald" -- 10 results; found Global Times article

#### Pages fetched
1. AAS DPS obituary (T1) -- 403 Forbidden; confirmed via search snippets
2. U of Arizona LPL memorial (T1) -- successful; PhD 1997, JPL 1998-2022, 80+ papers, missions listed
3. U of Arizona LPL news (T1) -- successful; dissertation title confirmed
4. Forest Lawn obituary (T1) -- successful; full biographical and family details, memorial service, al-anon donation request
5. Newsweek "List of dead or missing scientists" (T4) -- successful; "no record of an autopsy" claim; colleague Dr. Joe Masiero quote
6. Newsweek "Obituaries shed light" (T4) -- successful; described as "astronomer, artist and father"
7. Fox 11 LA (T3) -- successful; LA County connection, federal review confirmed
8. CBS News (T4) -- successful; skeptical perspectives from CSIS, NTI, former DOE official
9. Global Times (T8) -- successful; Chinese state media framing with conspiracy amplification

#### Key findings
- **Cause of death not disclosed in any source.** Not in obituary, not in professional memorials, not in media reporting.
- **No autopsy record found** per Newsweek reporting; not confirmed by LA County Medical Examiner on record.
- **Left JPL in 2022, died 2023.** One-year gap unexplained. Possible retirement, layoff (JPL had budget cuts), health, or other reasons.
- **Obituary requests donations to al-anon.org** -- Al-Anon is a support organization for families of people with alcohol use disorders. This may provide biographical context.
- **No NASA/JPL institutional statement found** regarding his death.
- **Colleague Dr. Joe Masiero on record** with mentoring characterization.
- **CBS News review found no links between any of the deaths** in the broader pattern.

#### Contradictions identified
- Employment end (2022) vs. death (2023) gap unexplained
- "No autopsy record found" may reflect incomplete records search rather than confirmed no autopsy
- Pattern claims by Congress/media vs. skepticism from security analysts

#### Gaps remaining
- Cause of death
- Whether autopsy was conducted (no on-record statement from LACME)
- Reason for leaving JPL in 2022
- Security clearance level (planetary science work may not require high clearances)
- Federal agency response to Comer/Burlison inquiry
- Full publication list

#### Files written
- `cases/hicks.md` -- full case file
- `appendices/primary-sources/hicks/source-index.md`

### Maiwald case research

**Date:** 2026-04-20
**Researcher:** Sub-agent (Claude)

#### Searches performed
1. WebSearch: "Frank Maiwald JPL died 2024" -- 10 results, strong coverage (Legacy.com obituary, MSN, Newsweek, The Hill)
2. WebSearch: "Frank Maiwald JPL researcher obituary" -- 10 results, overlapping; confirmed Legacy.com as sole obituary source
3. WebSearch: "Frank Maiwald JPL cause of death autopsy Los Angeles" -- 10 results; X/social media claim of no autopsy; LiveNOW from FOX coverage
4. WebSearch: "Frank Maiwald SBG-VSWIR instrument JPL publications research" -- 10 results; found IEEE, SPIE publications, Google Scholar profile
5. WebSearch: "Frank Maiwald JPL HIFI Herschel space observatory publications" -- 10 results; found ResearchGate, JPL repository, 3,400+ citations
6. WebSearch: ""Frank Maiwald" OR "Michael Hicks" JPL scientist security clearance classified" -- 10 results; no specific clearance info found

#### Pages fetched
1. Legacy.com obituary (T1) -- successful; full biographical and family details, JPL projects listed, no cause of death
2. Google Scholar profile (T1) -- partially successful; rendered as code, confirmed PhD Applied Physics
3. Newsweek "List of dead or missing scientists" (T4) -- successful; "no record of an autopsy" claim; principal investigator description
4. Newsweek "Obituaries shed light" (T4) -- successful; no new details beyond obituary
5. Fox 11 LA (T3) -- successful; LA County connection, federal review confirmed
6. CBS News (T4) -- successful; skeptical perspectives (same as Hicks research)
7. The Hill (T4) -- 403 Forbidden
8. Global Times (T8) -- successful (shared fetch with Hicks); Maiwald listed among 11 cases

#### Key findings
- **Cause of death not disclosed in any source.** Obituary simply states he "passed away."
- **No autopsy reportedly performed** per multiple media outlets; original basis for claim unclear (possibly records search).
- **NASA never commented publicly on Maiwald's death.** Only public record is Legacy.com obituary.
- **Active researcher at time of death:** Co-authored SPIE paper published May 2024, died July 4, 2024.
- **JPL Principal designation** -- an honor for "outstanding individual contributions," distinct from PI role.
- **June 2023 astrobiology breakthrough claim** -- media report he led research relevant to detecting life on icy moons ~13 months before death. Specific publication not identified.
- **German-born** -- immigration/citizenship status and clearance eligibility implications unreported.
- **3,400+ citations** across career; research spanned THz technology, microwave radiometry, and imaging spectrometry.
- **CBS News review found no links** between any of the deaths.

#### Contradictions identified
- "Principal researcher" vs. "principal investigator" conflated in media; JPL "Principal" is a specific honor
- "No autopsy performed" -- source of claim unclear; not confirmed on-record by LACME
- Employment start date approximate (~1999 from media; obituary does not specify)
- Pattern claims vs. security analyst skepticism

#### Gaps remaining
- Cause of death
- Whether autopsy was conducted (no on-record LACME statement)
- Security clearance level
- Specific June 2023 astrobiology publication
- NASA/JPL internal communications about his death
- Immigration/citizenship status
- Federal agency response to Comer/Burlison inquiry

#### Files written
- `cases/maiwald.md` -- full case file
- `appendices/primary-sources/maiwald/source-index.md`

### Garcia case research

**Date:** 2026-04-20
**Researcher:** Sub-agent (Claude)

#### Searches performed
1. WebSearch: "Steven Garcia Albuquerque missing 2025" -- 10 results; NM DPS record, Newsweek, CBS, Fox, KOB 4, NewsNation, Cybernews, BroBible, aggregators
2. WebSearch: "Steven Garcia Kansas City National Security Campus" -- 10 results; NewsNation (Lauren Conlin), Newsweek, British Brief, Cybernews
3. WebSearch: "Steven Garcia missing scientist government contractor" -- 10 results; CBS, Newsweek, NewsNation, Fox, Daily Wire
4. WebSearch: "Steven Garcia Albuquerque missing August 2025 APD police report property custodian" -- 10 results; no APD press release found
5. WebSearch: ""Steven Garcia" "Daily Mail" Kansas City National Security Campus missing Albuquerque" -- confirmed Daily Mail as origin of KCNSC claim via anonymous source
6. WebSearch: "Steven Garcia Albuquerque Silver Alert APD missing person 2025" -- no Silver Alert found; NM DPS record confirmed
7. WebSearch: "Steven Garcia Albuquerque police department missing person endangered August 28" -- no APD press release found
8. WebSearch: "dailymail.co.uk Steven Garcia Kansas City National Security Campus missing" -- Daily Mail article confirmed as origin but not directly fetchable
9. WebSearch: "Kansas City National Security Campus statement Steven Garcia missing employee" -- no KCNSC statement; NNSA general statement located
10. WebSearch: ""Steven Garcia" "Cattail Court" Albuquerque missing" -- address detail confirmed from anonymous source
11. WebSearch: "Lauren Conlin Steven Garcia NewsNation investigation reporter" -- Conlin covers case, appears to relay anonymous-source claims
12. WebSearch: ""Steven Garcia" found body update 2026 Albuquerque" -- no resolution; still missing
13. WebSearch: "site:krqe.com OR site:koat.com OR site:kob.com Steven Garcia" -- KOB 4 found; no KRQE/KOAT coverage
14. WebSearch: "Honeywell Kansas City National Security Campus statement missing scientists employees" -- NNSA general statement found
15. WebSearch: "Lauren Conlin Daily Mail Steven Garcia KCNSC nuclear exclusive reporter" -- confirmed DailyMail.com as origin outlet

#### Pages fetched
1. NM DPS Missing Persons record M101688 (T1) -- successful; key biographical data extracted
2. Newsweek "Missing government security man compared to Neil McCasland case" (T4) -- successful; noted Newsweek did not independently verify KCNSC employment
3. CBS News cluster overview (T4) -- successful; used "reportedly" for KCNSC claim
4. LiveNOW from FOX overview (T4) -- successful; cited "Fox News" for KCNSC claim
5. British Brief article (T5) -- successful; explicitly attributed KCNSC claim to anonymous source via Daily Mail
6. Newsweek FBI investigation overview (T4) -- successful; Garcia listed with no sourcing detail
7. Daily Wire article (T5) -- successful; cited Economic Times India, not independent
8. NewsNation Lauren Conlin segment (T4) -- returned 403
9. Cybernews article (T5) -- returned 403
10. Colorado Springs Gazette (T4) -- returned 403
11. BroBible article (T5) -- JS-heavy, no article body rendered

#### Key findings: KCNSC employment sourcing chain
**The entire KCNSC employment claim traces to a single anonymous source speaking to DailyMail.com (~April 12, 2026).** No outlet has published independent confirmation:
- **Daily Mail:** Original outlet; anonymous source described Garcia as property custodian at KCNSC with top clearance
- **Newsweek:** Explicitly stated it "has not independently verified his employment details"; reached out to KCNSC (no response documented)
- **CBS News:** Used "reportedly" without attribution
- **Fox News Digital:** Appears to have repeated the claim; LiveNOW from FOX cited Fox News as source
- **NewsNation:** Reporter Lauren Conlin discussed Garcia on air, appears to relay the anonymous source's characterizations
- **British Brief:** Explicitly cited "anonymous source revealed to the Daily Mail"
- **Daily Wire:** Cited Economic Times India
- **KCNSC/Honeywell FM&T:** No public statement confirming or denying
- **NNSA:** General statement acknowledging awareness of reports; did not name Garcia

#### Contradictions identified
1. APD "danger to himself" warning vs. anonymous source's "very stable person" characterization
2. Employment claim from anonymous source vs. complete absence of official confirmation

#### Gaps remaining
- Was Garcia actually employed at KCNSC? No official confirmation exists
- APD basis for "danger to himself" warning
- Identity and credibility of the anonymous source
- No APD press release or Silver Alert located
- No family statements found
- No FBI/federal review status specific to Garcia
- Investigation updates since August 2025
- No NamUs entry found

#### Files written
- `cases/garcia.md` -- full case file
- `appendices/primary-sources/garcia/nm-dps-missing-persons.md`
- `appendices/primary-sources/garcia/nnsa-statement.md`

### Loureiro case research

**Date:** 2026-04-20
**Researcher:** Sub-agent (Claude)

#### Searches performed
1. "Nuno Loureiro MIT shot 2025 Brookline" -- 10 results
2. "Nuno Loureiro MIT Plasma Science Fusion Center director" -- 10 results
3. "Brookline shooting December 2025 Brown University connection" -- 10 results
4. "Claudio Valente video confession storage unit motive Brown MIT shooting" -- 10 results
5. "Nuno Loureiro MIT fusion research defense Department of Energy SPARC" -- 10 results
6. "Norfolk County DA Brookline police Nuno Loureiro murder investigation" -- 10 results
7. "MIT Plasma Science Fusion Center Department of Defense DARPA funding contracts" -- 10 results
8. "Claudio Valente Instituto Superior Tecnico grudge Loureiro classmate motive 2026" -- 10 results
9. "Claudio Valente Brown University PhD dropout Portugal top student career failure resentment" -- 10 results
10. "Nuno Loureiro wife family Brookline apartment shot foyer 9 Gibbs Street" -- 10 results

#### Pages fetched (10 successful, 3 failed)
MIT obituary, Wikipedia Brown shooting, WBUR timeline, ABC News grudge article, NextBigFuture fusion work, Boston 25 confession transcript, Wikipedia Loureiro, MIT Statement, CBS Boston police reports. Failed: Brookline.News (429), NBC News (403), Boston Globe (paywall).

#### Key findings
- Named suspect with ballistics, DNA, fingerprints, surveillance, rental car records, and video confession
- Motive: academic resentment/grudge (law enforcement sources); Valente did not explicitly state motive
- Brown was primary target (planned ~3 years); Loureiro murder was personal secondary attack
- No evidence of defense/national security motive
- Strongest candidate for reclassification from the pattern

#### Files written
- `cases/loureiro.md`
- `appendices/primary-sources/loureiro/mit-obituary.md`
- `appendices/primary-sources/loureiro/mit-statement-20251219.md`
- `appendices/primary-sources/loureiro/doj-confession-transcript-summary.md`
- `appendices/primary-sources/loureiro/brown-shooting-wikipedia-summary.md`

### Foreign coverage research

**Date:** 2026-04-20
**Researcher:** Sub-agent (Claude)

#### Search strategy
Searched for coverage in Russia, China, Iran, Israel, UK, France, Germany, India, Japan, Australia, and Qatar. Used outlet-specific searches (RT, TASS, Xinhua, Global Times, Press TV, Tehran Times, BBC, Guardian, Le Monde, Der Spiegel, WION, NHK, Haaretz, SCMP, Al Jazeera, Daily Mail, LBC, IBTimes UK, UnHerd, Sky News, Telegraph, Times of India, NDTV, ABC Australia, Sydney Morning Herald, Jerusalem Post, Times of Israel, Japan Times). Searched in English.

#### Countries with confirmed coverage (files written)

1. **Russia** -- RT (2 articles), Pravda UK (1 commentary). State-affiliated. Sensationalist framing; implicit U.S.-dysfunction narrative. See `appendices/foreign-coverage/russia.md`.
2. **China** -- Global Times (1 article). State-affiliated. UFO conspiracy angle foregrounded; omitted China-as-suspect framing from U.S. lawmakers. See `appendices/foreign-coverage/china.md`.
3. **Iran** -- Tehran Times (1 op-ed), Press TV (1 article). State-affiliated. Tehran Times advanced unique "knowledge sequestration" theory. See `appendices/foreign-coverage/iran.md`.
4. **United Kingdom** -- LBC (1), IBTimes UK (1), UnHerd (1). Independent outlets. Widest editorial range: LBC sensationalist, UnHerd skeptical. See `appendices/foreign-coverage/united-kingdom.md`.
5. **India** -- WION (5+ articles/videos), Northeast Live TV (1). Independent. Highest volume of any foreign outlet. Original Mondaloy angle. See `appendices/foreign-coverage/india.md`.

#### Countries with no meaningful coverage found
France, Germany, Japan, Israel (mainstream), Australia, Qatar/Al Jazeera.

#### Files written
- `appendices/foreign-coverage/russia.md`
- `appendices/foreign-coverage/china.md`
- `appendices/foreign-coverage/iran.md`
- `appendices/foreign-coverage/united-kingdom.md`
- `appendices/foreign-coverage/india.md`

### Named expert commentary research

**Date:** 2026-04-20
**Researcher:** Named-expert-commentary sub-agent (Claude)

Searched for on-the-record statements from identifiable experts on the missing/dead U.S. defense scientists cluster. Created 10 individual profile files in `appendices/named-expert-commentary/`.

#### Experts documented (10 total)

**High credibility / Direct expertise:**
1. Chris Swecker (former FBI Asst. Director) -- Espionage hypothesis, conditional framing. File: `chris-swecker.md`
2. Joseph Rodgers (CSIS, Deputy Dir. Nuclear Issues) -- Skeptical of pattern. File: `joseph-rodgers-csis.md`
3. Scott Roecker (NTI, VP Nuclear Materials Security) -- Skeptical; scale argument. File: `scott-roecker-nti.md`
4. Jennifer Coffindaffer (retired FBI agent) -- Rejected conspiracy framing. File: `jennifer-coffindaffer.md`

**Official government (direct authority):**
5. Kash Patel (FBI Director) -- Confirmed investigation, no conclusions yet. File: `kash-patel.md`
6. Chris Wright (Energy Secretary) -- Confirmed DOE review, nothing alarming yet. File: `chris-wright-doe.md`

**Adjacent expertise / Media:**
7. Ross Coulthart (journalist, NewsNation) -- "Grave national security crisis." File: `ross-coulthart.md`
8. Michio Kaku (physicist, CCNY) -- "Cause for national concern." File: `michio-kaku.md`
9. Luis Elizondo (former AATIP director) -- Restrained; deferred to law enforcement. File: `luis-elizondo.md`

**Low credibility:**
10. Steven Greer (Disclosure Project founder) -- UAP criminal-org narrative. File: `steven-greer.md`

#### Key finding: Expert opinion is divided
- Espionage-concerned: Swecker, Coulthart, Kaku
- Skeptical: Rodgers (CSIS), Roecker (NTI), Coffindaffer
- Official no-conclusions: Patel, Wright
- UAP-narrative: Coulthart, Greer; Elizondo restrained

#### Files written
- `appendices/named-expert-commentary/ross-coulthart.md`
- `appendices/named-expert-commentary/chris-swecker.md`
- `appendices/named-expert-commentary/michio-kaku.md`
- `appendices/named-expert-commentary/joseph-rodgers-csis.md`
- `appendices/named-expert-commentary/scott-roecker-nti.md`
- `appendices/named-expert-commentary/jennifer-coffindaffer.md`
- `appendices/named-expert-commentary/luis-elizondo.md`
- `appendices/named-expert-commentary/steven-greer.md`
- `appendices/named-expert-commentary/kash-patel.md`
- `appendices/named-expert-commentary/chris-wright-doe.md`

### Thomas case research

**Date:** 2026-04-20
**Researcher:** Sub-agent (Claude)

#### Searches performed
1. WebSearch: "Jason Thomas Novartis missing Wakefield Massachusetts 2025" -- 10 results
2. WebSearch: "Jason Thomas Lake Quannapowitt body found March 2026 cause of death" -- 10 results
3. WebSearch: "Jason Thomas Novartis chemical biology cancer research background education" -- 10 results
4. WebSearch: ""Jason Thomas" Wakefield wife "Kristen Bartoli" missing December 2025" -- 10 results
5. WebSearch: "Jason Thomas Novartis obituary funeral Burlington Massachusetts 2026" -- 10 results
6. WebSearch: ""Jason Thomas" Wakefield medical examiner cause manner death 2026" -- 10 results
7. WebSearch: ""Jason Thomas" Wakefield police chief Skory search canine drone December 2025" -- 10 results

#### Pages fetched
1. Wakefield town website / DA Marian Ryan statement (T1) -- successful
2. Legacy.com obituary (T1) -- successful
3. Boston 25 News wife interview (T3) -- successful
4. NBC Dateline (T4) -- 403 Forbidden
5. Middlesex DA press release (T1) -- 403 Forbidden
6. Boston.com March 17 (T3) -- partial extraction

#### Key findings
- DA Marian Ryan: no foul play suspected (T1)
- Cause/manner of death not yet publicly released by Chief Medical Examiner
- Both parents died within ~90 minutes of each other, November 2025
- Left home without phone/wallet; last seen near railroad tracks
- Body found March 17, 2026 in Lake Quannapowitt after ice melted
- No connection to defense/aerospace/classified work; Novartis pharma cancer research
- Weakest fit in repository

#### Contradictions
- Age 45 vs 46 (birthday between disappearance and obituary)

#### Gaps
- Official cause/manner of death
- Whether lake was searched in December
- Mental health context

#### Files written
- `cases/thomas.md`
- `appendices/primary-sources/thomas/sources.md`

### Eskridge case research

**Date:** 2026-04-20
**Researcher:** Sub-agent (Claude)

#### Searches performed
1. WebSearch: "Amy Eskridge Institute Exotic Science died 2022 Huntsville" -- 10 results
2. WebSearch: "Amy Eskridge Huntsville Alabama death ruled suicide gunshot 2022" -- 10 results
3. WebSearch: "Amy Eskridge "Richard Eskridge" NASA engineer father HoloChron" -- 10 results
4. WebSearch: "Amy Eskridge obituary Huntsville Alabama 2022" -- 10 results
5. WebSearch: "Amy Eskridge father Richard "nothing suspicious" death daughter statement" -- 10 results
6. WebSearch: "Amy Eskridge "Franc Milburn" investigation Congress report antigravity" -- 10 results
7. WebSearch: "Amy Eskridge 2020 interview Jeremy Rys threats directed energy weapon burns" -- 10 results
8. WebSearch: "Amy Eskridge Huntsville police department investigation 2022 coroner report Madison County" -- 10 results

#### Pages fetched
1. Newsweek "Who is Amy Eskridge?" (T4) -- successful
2. The Arab Tribune obituary (T1) -- successful
3. Fox News "11th scientist death" (T4) -- successful
4. Yahoo News / Fox News syndication (T4) -- successful
5. IBTimes UK father's statement (T4) -- rendering failure
6. NewsNation father interview (T4) -- 403 Forbidden

#### Key findings
- Death confirmed June 11, 2022, age 34, Huntsville, AL (T1 obituary)
- Reported as self-inflicted gunshot wound; no police/coroner report publicly released
- Father Richard Eskridge dismissed conspiracy theories: "nothing suspicious" (T4)
- Father is retired NASA MSFC engineer (plasma physics, fusion); co-founded organizations with Amy
- 2020 interview: threat claims, DEW claims, harassment -- all self-reported, unverified
- Franc Milburn claims not suicide; reportedly submitted to Congress 2023 (no record found)
- Shellenberger testified "murdered by private aerospace company" (no evidence documented)
- No peer-reviewed antigravity experimental publications found
- 2022 death predates 2025-2026 cluster by three years

#### Contradictions
1. Father says "nothing suspicious" vs Milburn/Shellenberger allege murder
2. Suicide ruling widespread in media but no official documentation located
3. Threat claims specific but entirely self-reported

#### Gaps
- Official police/coroner report
- Whether police reports were filed about threats
- Milburn investigation details
- Congressional submission documentation
- Shellenberger testimony evidence basis
- Circumstances of gunshot

#### Files written
- `cases/eskridge.md`
- `appendices/primary-sources/eskridge/sources.md`

### McCasland case research

**Date:** 2026-04-20
**Researcher:** Sub-agent (Claude)

#### Searches performed
19 web searches conducted covering: disappearance details, military career (AFRL, SAPOC, NRO, GPS, Office of Special Projects), post-retirement career (ATA/BlueHalo, Riverside Research), DeLonge/UAP connection (WikiLeaks emails, wife's statements, congressional interest), search efforts (BCSO, FBI), 911 call details, and political affiliations.

#### Pages fetched (successful)
10 pages successfully fetched: Wikipedia biography (T5), Newsweek (3 articles, T4), ABC News (T4), Fox News (T4), CBS News (T4), WikiLeaks emailid/3099 (T1), ABQ Journal (T3), Newsweek "Who is McCasland" (T4). 8 pages returned 403 or failed rendering, including the BCSO press release PDF (T1) and House Oversight press release (T1).

#### Key findings
- Military career comprehensively documented: 34-year USAF career spanning classified satellite reconnaissance, GPS, AFRL command, NRO, SAPOC executive secretary.
- Disappeared Feb 27, 2026 between 11:10 AM and 12:04 PM. Left phone/glasses/wearables. Took boots/wallet/.38 revolver/backpack.
- Wife's 911 call: "I have some indication that he must have planned not to be found." Also relayed statement about not wanting to live with deteriorating brain/body.
- Mental fog confirmed but not dementia per wife and BCSO.
- DeLonge/UAP: WikiLeaks email documents DeLonge's claims; wife confirms brief unpaid consulting for fiction; denies Roswell knowledge. McCasland silent.
- BCSO: no evidence of foul play, no classified-work connection, no link to other cases.
- Still missing as of April 20, 2026. No sightings. USAF sweatshirt found 1.25 mi east, unconfirmed as his.

#### Assessment
Highest-profile case in cluster. Current evidence more consistent with voluntary departure driven by medical/psychological distress than foul play. Supports H1/H8, H2, tangentially H6 (weaker than publicly perceived). Does not currently support H4 or H7.

#### Files written
- `cases/mccasland.md`
- `appendices/primary-sources/mccasland/wikileaks-podesta-email-3099.md`
- `appendices/primary-sources/mccasland/bcso-press-release-2026-03-12.md`
- `appendices/primary-sources/mccasland/house-oversight-press-release.md`
- `appendices/primary-sources/mccasland/riverside-research-appointment.md`

## Reconcile survey (2026-04-21)

### What was committed (31 commits, a0ab7ef through 4d2d916)
- All 11 case files: `cases/{casias,chavez,eskridge,garcia,grillmair,hicks,loureiro,maiwald,mccasland,reza,thomas}.md`
- `dossier.md` (112 lines, with abstract, executive summary, case index)
- `analysis/connection-analysis.md` (166 lines)
- `analysis/foreign-intel-layer.md` (169 lines)
- `analysis/hypotheses.md` (308 lines)
- `appendices/primary-sources/` — 11 per-case subdirectories, plus 4 government-wide documents
- `appendices/foreign-coverage/` — 5 country files (china, india, iran, russia, united-kingdom)
- `appendices/named-expert-commentary/` — 10 expert files
- `logs/research-log.md` — fully populated research log
- Skeleton versions of `data/diagram-data.json` (5 lines), `data/timeline-data.json` (4 lines), `logs/contradictions.md` (20 lines), `logs/known-unknowns.md` (45 lines)
- `data/schema/diagram-schema.json`, `data/schema/timeline-schema.json`

### Uncommitted modified files (rate-limit artifacts)
- `data/diagram-data.json` — 831 lines, fully populated with 11 person nodes, 10 institution nodes, 6 location nodes, 6 program nodes, 44 edges, 3 layer definitions. Valid JSON.
- `data/timeline-data.json` — 436 lines, fully populated with 29 case events, 14 context events. Valid JSON.
- `logs/contradictions.md` — 101 lines, expanded from 20-line skeleton; 12 within-case + 4 cross-case contradictions documented.
- `logs/known-unknowns.md` — 156 lines, expanded from 45-line skeleton; 16 case-specific + 7 cross-case analytical gaps.
- `run-all.log` — 58 new lines of pipeline transcript (not a research artifact).

### Untracked files
- `prompt-reconcile.md` — reconciliation prompt (operational, not a pipeline artifact)
- `prompt-resume.md` — resume prompt (operational, not a pipeline artifact)
- `reconcile.log` — reconciliation log (operational)

### Missing artifacts
- `STATUS.md` — required by prompt-001 spec as a final deliverable. Never created.

### Directory health
- `pdf-output/` — empty (expected; prompt-002 produces PDFs)
- No empty directories under `appendices/primary-sources/` — all 11 cases have files
- `.gitignore` does not cover `run-all.log` or `reconcile.log`

### Assessment
All four uncommitted modified files are complete, well-formed, and consistent with the spec. None are truncated. The rate limit hit after these files were written but before they could be committed. They should be committed as-is.

## Reconcile summary (2026-04-21)

### Uncommitted files at start and how each was handled
- `data/diagram-data.json` — Complete, 831 lines. Committed as-is (7c891e4).
- `data/timeline-data.json` — Complete, 436 lines. Committed as-is (7c891e4).
- `logs/contradictions.md` — Complete, 101 lines. Committed as-is (7c891e4). Later updated to add missing Hicks/Maiwald entries (525f3a2).
- `logs/known-unknowns.md` — Complete, 156 lines. Committed as-is (7c891e4).
- `run-all.log` — Pipeline transcript. Added to .gitignore; left untracked (7c891e4).
- `prompt-reconcile.md` — Operational prompt file. Left untracked.
- `prompt-resume.md` — Operational prompt file. Left untracked.
- `reconcile.log` — Operational log. Added to .gitignore; left untracked.

### Audit gaps fixed
- Created `STATUS.md` (required by spec, never generated due to rate limit).
- Updated `CHANGELOG.md` with prompt-001 completion and reconcile entries.
- Fixed H4 assessment discrepancy: dossier.md table now matches hypotheses.md ("Weak support").
- Added 4 missing contradiction entries for Hicks and Maiwald to `logs/contradictions.md`.

### Deferred gaps (NEEDS_RESEARCH)
- Non-English foreign coverage not searched (documented in known-unknowns.md).
- Base-rate actuarial analysis not performed (documented in known-unknowns.md).

### Full audit
See `logs/audit-report.md` for the complete per-case and top-level artifact audit.

READY_FOR_PROMPT_002

## 2026-04-21 — Tier migration inventory (prompt-retag-tiers)

### Scope
Migrating all source tier references from the old 7-tier system to the new 8-tier system per `prompts/build/prompt-retag-tiers.md`.

### Files already migrated (new-system tags confirmed)
- `cases/casias.md` — T1, T3 tags ✓
- `cases/chavez.md` — T1, T3, T4, T5, T8 tags ✓
- `cases/eskridge.md` — T1, T4, T5 tags ✓
- `cases/garcia.md` — T1, T3, T6 tags ✓
- `cases/hicks.md` — T1, T3, T4 tags ✓
- `cases/maiwald.md` — T1, T3, T4 tags ✓
- `cases/reza.md` — T1, T3, T4, T5, T7 tags ✓
- `cases/thomas.md` — T1, T3, T4, T7 tags ✓
- `analysis/connection-analysis.md` — T1, T3, T4 tags ✓
- `analysis/hypotheses.md` — T3, T6 tags ✓
- `appendices/foreign-coverage/china.md` — Tier 3 for SCMP ✓ (geographic proximity to HK/China story)
- `appendices/primary-sources/*` — all T1 ✓

### Files needing migration

**`cases/grillmair.md`** — ~40 old T2 tags. All sources are local LA media (ABC7, Fox 11 LA, CBS LA, MyNewsLA, Pasadena Now, LA Times/Yahoo, Caltech student paper). All T2 → T3.

**`cases/mccasland.md`** — ~35 old T2 tags. Mix of national outlets (CNN, ABC News, Fox News, Newsweek, NewsNation → T4), local (ABQ Journal → T3), and aggregator (Wikipedia → T5).

**`cases/loureiro.md`** — ~20 old T2 tags. Mix of local (CBS Boston, WBUR, Boston 25 → T3), national (NBC News, PBS, ABC News → T4), and aggregator (Wikipedia, NextBigFuture → T5). Also: Max Planck condolence statement reclassified T2 → T1 (institutional primary source); CNN Portugal → T3 (geographic proximity to Portuguese story).

**`logs/research-log.md`** — ~60 old tags across all tiers:
- Old T7 (Global Times, 2 occurrences) → T8
- Old T6 (Sentinel Briefing, 2 occurrences) → T7
- Old T3 (Wikipedia, aggregators, ~6 occurrences) → T5
- Old T2 (~50 occurrences) → T3 or T4 per outlet

**`logs/contradictions.md`** — 10 remaining old T2 tags (lines 75, 85, 90, 95, 104, 105, 109, 110, 114, 119). All are national outlets (Newsweek, Fox News, CBS News, NewsNation) → T4.

**`logs/audit-checklist.md`** — 2 old-system references in example/description text.

### Ambiguities logged

1. **Max Planck Institute condolence statement (loureiro.md line 159):** Tagged old T2 (media) but is actually an institutional statement → reclassified as T1. Not a media outlet.
2. **CNN Portugal (loureiro.md line 158):** Portuguese outlet covering a case involving two Portuguese nationals. Geographic/cultural proximity to the story → classified as T3 (beat reporting), not T4.
3. **NextBigFuture (loureiro.md line 92):** Tech blog/aggregator, not original reporting → classified as T5 (aggregator), not T4.
4. **British Brief (research-log.md line 413):** Small UK news/commentary site → classified as T5 (aggregator/tertiary), not T4. Lacks the reporting capacity of listed T4 international outlets.
5. **Colorado Springs Gazette (research-log.md line 418):** Covers military beat broadly but has no geographic proximity to the Garcia case (Albuquerque) → classified as T4.
6. **Daily Wire (research-log.md line 415):** Cited Economic Times India, not independent reporting → classified as T5 (aggregator/tertiary).

## 2026-04-21 — Tier migration complete (prompt-retag-tiers)

### Summary

Migration from 7-tier to 8-tier source classification system complete.

**Tags updated by new tier:**
| New Tier | Count (approx.) | Migration path |
|----------|-----------------|----------------|
| T1 | 0 changed | Unchanged (1 reclassification: Max Planck condolence → T1) |
| T3 (local/beat) | ~45 | From old T2: local NM outlets, local LA outlets, local Boston outlets, CNN Portugal |
| T4 (national) | ~65 | From old T2: Newsweek, CBS News, CNN, ABC News, Fox News, NBC News, NewsNation, The Hill, Fortune, PBS, IBTimes UK, Daily Mail |
| T5 (aggregator) | ~10 | From old T3: Wikipedia, BroBible, Cybernews, michaelrcronin.com; from old T2: NextBigFuture, British Brief, Daily Wire |
| T7 (independent) | 2 | From old T6: Sentinel Briefing (2 articles) |
| T8 (foreign state) | 2 | From old T7: Global Times (2 entries) |

**Files modified (22 total):**
- `cases/grillmair.md`, `cases/mccasland.md`, `cases/loureiro.md`
- `analysis/foreign-intel-layer.md`
- `logs/research-log.md`, `logs/contradictions.md`, `logs/audit-checklist.md`, `logs/audit-report.md`
- `appendices/primary-sources/eskridge/sources.md`, `appendices/primary-sources/thomas/sources.md`
- `appendices/primary-sources/garcia/nnsa-statement.md`, `appendices/primary-sources/casias/nmsp-statements.md`
- `appendices/primary-sources/grillmair/lasd-initial-report.md`
- `appendices/primary-sources/loureiro/brown-shooting-wikipedia-summary.md`
- `appendices/primary-sources/mccasland/bcso-press-release-2026-03-12.md`, `appendices/primary-sources/mccasland/house-oversight-press-release.md`
- `TODO-research.md` (marked migration tasks complete)
- 8 case files already migrated in prior pass (casias, chavez, eskridge, garcia, hicks, maiwald, reza, thomas)

**Files NOT modified (per exclusion list):**
- `README.md`, `CLAUDE.md`, `prompts/research/README.md`, `prompts/build/prompt-retag-tiers.md`

**Prompt specification files left unchanged:**
- `prompts/build/prompt-000.md`, `prompts/build/prompt-001.md`, `prompts/research/prompt-deep-*.md` — These define the OLD tier system as originally written. Updating them would rewrite historical specifications. They describe the system under which prompt-001 research was conducted.

**Quality checks passed:**
- No file in `cases/`, `analysis/`, `appendices/`, or `logs/` contains old-system `(T2)` tags
- `(T2)` grep returns only the excluded migration prompt file
- No news outlet is tagged T2 — T2 is reserved for named expert commentary
- Total tier references approximately equal before and after (tags remapped, not added or removed)
