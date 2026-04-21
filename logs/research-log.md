# Research Log

Chronological record of searches performed, sources consulted, and decisions made.

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
2. Los Alamos Reporter LAPD notice (T1 via T2) -- successful
3. Los Alamos Reporter social media concern article (T2) -- successful, Carl Buckland friend details
4. CBS News broader pattern article (T2) -- successful but minimal Chavez-specific detail
5. KOB.com article (T2) -- content truncated, limited value
6. Boomtown Los Alamos article (T2) -- paywalled, only metadata extracted
7. michaelrcronin.com article (T3) -- successful but limited new detail
8. LA Daily Post LAPD search update (T2) -- successful, Deputy Chief Rodriguez quote
9. losalamosnm.gov county page (T1) -- returned HTTP 403
10. NewsNation article (T2) -- returned HTTP 403

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
- **Factory-reset phone claim is FAMILY-SOURCED (niece Jazmin McMillen), NOT confirmed by NMSP publicly.** Tier 2 provenance, not Tier 1.
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
1. ABC7 Los Angeles -- charges and timeline (T2), successful
2. Caltech official memorial (T1) -- successful, comprehensive biographical data
3. FOX 11 Los Angeles -- suspect prior arrest details (T2), successful
4. Wikipedia -- Carl Grillmair biography (T3), successful, useful for cross-referencing
5. Pasadena Now -- prior arrest and release details (T2), successful
6. MyNewsLA -- initial LASD report details (T2), successful
7. MyNewsLA -- arraignment postponement (T2), successful
8. Yahoo News (LA Times syndication) -- December trespassing deep dive (T2), successful; most detailed source on Snyder's criminal history
9. CBS Los Angeles -- initial shooting report (T2), successful
10. Caltech student newspaper (The California Tech) -- colleague quotes (T2), successful
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
1. WebSearch: "Monica Jacinto Reza JPL missing 2025" -- 10 results, strong coverage across T2/T6 sources
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
1. Wikipedia - Monica Jacinto (T3) -- successful, comprehensive biography with reliability caveats noted on page
2. FOX 11 Los Angeles (T2) -- successful, LASD lead agency confirmed, federal probe details
3. Solve the Case / LASD listing (T1) -- successful, full physical description, case numbers, detective names
4. Google Patents US-20100266442-A1 (T1) -- successful, full patent details, inventors, composition, applications
5. Crescenta Valley Weekly / Vienna statement (T1 via T2) -- successful, key LASD quotes
6. The Sentinel Briefing "Green Burial" (T6) -- successful, Find a Grave anomaly, search evidence details
7. Yahoo News / Men's Journal (T2) -- successful, companion details, running claim, career details
8. The Sentinel Briefing "Phone Gap" (T6) -- successful, cell phone forensics claim, 911 call
9. Justia Patents (T1) -- returned 403
10. KTLA (T2) -- returned 403
11. NewsNation (T2) -- returned 403
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
5. Newsweek "List of dead or missing scientists" (T2) -- successful; "no record of an autopsy" claim; colleague Dr. Joe Masiero quote
6. Newsweek "Obituaries shed light" (T2) -- successful; described as "astronomer, artist and father"
7. Fox 11 LA (T2) -- successful; LA County connection, federal review confirmed
8. CBS News (T2) -- successful; skeptical perspectives from CSIS, NTI, former DOE official
9. Global Times (T7) -- successful; Chinese state media framing with conspiracy amplification

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
3. Newsweek "List of dead or missing scientists" (T2) -- successful; "no record of an autopsy" claim; principal investigator description
4. Newsweek "Obituaries shed light" (T2) -- successful; no new details beyond obituary
5. Fox 11 LA (T2) -- successful; LA County connection, federal review confirmed
6. CBS News (T2) -- successful; skeptical perspectives (same as Hicks research)
7. The Hill (T2) -- 403 Forbidden
8. Global Times (T7) -- successful (shared fetch with Hicks); Maiwald listed among 11 cases

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
