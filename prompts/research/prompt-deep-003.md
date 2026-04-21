# Prompt Deep-003 — Foreign-Language & International Source Expansion

## Non-interactive execution (read first)

This prompt runs via `claude -p --output-format=stream-json` — print mode. There is no stdin. Make decisions autonomously per the spec. Log ambiguities in `logs/research-log.md` and proceed.

You are Claude Code operating in `/Users/mnoth/source/research-missing-scientists/`. The initial research (prompt-001) searched for foreign coverage but only in English. This prompt expands into non-English sources — the TODO-research.md explicitly flags this as a significant gap. The goal is to find how state-affiliated and independent foreign media covered these events in their own languages, which may reveal different framing, different facts emphasized, or original reporting not available in English.

## Hard Safety Rules

- Working directory: `/Users/mnoth/source/research-missing-scientists/`. Do not touch anything outside it.
- No sudo. No system-wide installs.
- No git push. No auth to any service.
- No contacting anyone. Research uses already-public material only.
- Copyright discipline: paraphrase, ≤15 words per quote, one quote per source max. Translate before paraphrasing.
- If unsure, stop and log the uncertainty.

## Alignment (read `prompts/research/README.md` § "Alignment rules" before starting)

This prompt updates `appendices/foreign-coverage/` files. It may update `cases/{slug}.md` foreign coverage sections. It does NOT touch analysis files, data files, or dossier.md.

No country is pre-excluded or pre-implicated. Coverage is documented neutrally with outlet orientation noted.

## Context

Read `appendices/foreign-coverage/` to see what exists. Prior research found English-language coverage from:
- Russia (TASS, RT — English editions)
- China (SCMP, Xinhua — English editions)
- Iran (Press TV — English edition)
- India (WION, NDTV — English)
- UK (BBC, Daily Mail, The Guardian — English)

The gap: native-language editions of these outlets, plus outlets that publish primarily in their native language and were not searched at all.

## Sub-agent orchestration

Spawn regional sub-agents in parallel. Each agent searches in the target language(s) using native-language search queries.

### Agent 1: Russian-Language Sources

```
Search Russian-language media for coverage of the missing/dead U.S. scientists cluster.

Search terms (in Russian — construct appropriate queries):
- "пропавшие американские учёные" (missing American scientists)
- "учёные Лос-Аламос" (Los Alamos scientists)
- "смерть учёных США" (death of U.S. scientists)
- Individual names transliterated into Cyrillic
- "ФБР расследование учёные" (FBI investigation scientists)

Target outlets:
- TASS (tass.ru) — state news agency
- RIA Novosti (ria.ru) — state-owned
- Kommersant (kommersant.ru) — business/independent-leaning
- Novaya Gazeta (novayagazeta.ru) — independent/opposition (if accessible)
- Izvestia, Rossiyskaya Gazeta — state
- Telegram channels of major Russian journalists (public posts only)
- Military-focused outlets: Военное обозрение, Звезда

For each source found:
- Note outlet name, orientation (state/independent/opposition), URL, date
- Translate and paraphrase the key claims (do not reproduce full articles)
- Flag any facts or framing NOT present in English-language coverage
- Note whether coverage attributes events to foreign intelligence, coincidence, or other explanations

Update `appendices/foreign-coverage/russia.md` (add to existing file).
Log searches in `logs/research-log.md`.
Commit: `research-deep-003: russian-language sources`
```

### Agent 2: Chinese-Language Sources

```
Search Chinese-language media for coverage.

Search terms (in Chinese):
- "美国科学家失踪" (American scientists missing)
- "洛斯阿拉莫斯 科学家" (Los Alamos scientists)
- "美国国防科学家 死亡" (U.S. defense scientists death)
- "FBI 调查 科学家" (FBI investigation scientists)
- Individual names in Chinese transliteration

Target outlets:
- Xinhua (xinhuanet.com) — state
- People's Daily (people.com.cn) — CCP organ
- Global Times (huanqiu.com Chinese edition) — state, hawkish
- Caixin (caixin.com) — financial/independent-leaning
- Guancha (guancha.cn) — nationalist commentary
- Weibo and Zhihu trending discussions (public only)
- CCTV transcripts

Same documentation approach as Agent 1.
Update `appendices/foreign-coverage/china.md`.
Log searches in `logs/research-log.md`.
Commit: `research-deep-003: chinese-language sources`
```

### Agent 3: Persian-Language Sources

```
Search Persian/Farsi-language Iranian media.

Search terms (in Farsi):
- "دانشمندان آمریکایی گمشده" (missing American scientists)
- "مرگ دانشمندان هسته‌ای آمریکا" (death of American nuclear scientists)
- Names transliterated to Farsi script

Target outlets:
- IRNA (irna.ir) — state
- Fars News (farsnews.ir) — IRGC-affiliated
- Tasnim (tasnimnews.com) — IRGC-affiliated
- Press TV Farsi edition
- Reformist outlets if accessible (Shargh, Etemad)

Iran has particular relevance given: (a) its own history of scientist assassinations, (b) nuclear program competition, (c) potential framing as U.S. hypocrisy. Look for any "turnabout" framing.

Update `appendices/foreign-coverage/iran.md`.
Log searches in `logs/research-log.md`.
Commit: `research-deep-003: persian-language sources`
```

### Agent 4: European Languages (German, French, Hebrew)

```
Search European-language media.

German:
- Der Spiegel, FAZ, Süddeutsche Zeitung, Bild, Tagesschau
- Search: "vermisste US-Wissenschaftler", "tote Forscher USA", "Los Alamos Wissenschaftler"

French:
- Le Monde, Le Figaro, France 24, Libération
- Search: "scientifiques américains disparus", "morts scientifiques défense USA"

Hebrew:
- Haaretz, Ynet, Jerusalem Post (Hebrew edition), Maariv
- Search: "מדענים אמריקאים נעדרים" (missing American scientists)
- Israel has particular relevance given intelligence capability and defense-tech cooperation

For each: note outlet, orientation, URL, date. Translate and paraphrase.
Flag framing differences from U.S./English coverage.

Update or create: `appendices/foreign-coverage/germany.md`, `appendices/foreign-coverage/france.md`, `appendices/foreign-coverage/israel.md`.
Log searches in `logs/research-log.md`.
Commit: `research-deep-003: european-language sources`
```

### Agent 5: Additional Languages (Japanese, Hindi, Arabic, Korean)

```
Search additional language media where coverage may exist.

Japanese:
- NHK, Asahi Shimbun, Yomiuri, Nikkei
- Search: "米国科学者 行方不明" (U.S. scientists missing)
- Japan has relevance: defense tech cooperation, JAXA-NASA links

Hindi:
- NDTV Hindi, Aaj Tak, Dainik Jagran, Navbharat Times
- Search: "अमेरिकी वैज्ञानिक लापता" (American scientists missing)
- WION covered this prominently in English; check Hindi-language depth

Arabic (Gulf + Levant):
- Al Jazeera Arabic, Al Arabiya, Asharq Al-Awsat
- Search: "علماء أمريكيون مفقودون" (American scientists missing)

Korean:
- Chosun Ilbo, JoongAng, Hankyoreh, KBS
- Search: "미국 과학자 실종" (U.S. scientist missing)
- South Korea relevance: defense tech cooperation, nuclear deterrence interest

Same documentation approach.
Create files in `appendices/foreign-coverage/` for each country with coverage.
Log searches in `logs/research-log.md`.
Commit: `research-deep-003: additional-language sources`
```

### Orchestrator responsibilities

After all sub-agents complete:

1. Read all updated/created files in `appendices/foreign-coverage/`.
2. Append to each relevant `cases/{slug}.md` → Foreign Coverage section with new sources.
3. Write summary in `logs/research-log.md`:
   - Countries and languages searched
   - Total new sources found per country
   - Key framing differences discovered
   - Notable absences (countries where expected coverage doesn't exist)
4. If any foreign source contains a factual claim not present in any English source, flag it prominently.
5. Commit: `research-deep-003: orchestrator summary and case file updates`

## End conditions

- All 5 regional agents have completed.
- `appendices/foreign-coverage/` files updated or created for all target countries.
- `cases/{slug}.md` foreign coverage sections updated.
- `logs/research-log.md` documents all language searches.
- No analysis, data, or dossier files modified.

End of prompt deep-003.
