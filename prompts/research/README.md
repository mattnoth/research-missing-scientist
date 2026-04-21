# Research Prompts — Deep Source Expansion

## Purpose

These prompts extend the research beyond Tier 2 (news media) sources, which currently comprise ~70% of the evidence base. Each prompt is a self-contained session designed to run within Claude Code's usage limits, using sub-agent orchestration to maximize coverage while conserving context.

## Prompt inventory

| Prompt | Focus | Sub-agents | Depends on |
|--------|-------|------------|------------|
| `prompt-deep-001.md` | Public records & primary sources | 1 per case (11) | — |
| `prompt-deep-002.md` | Professional networks & institutional links | 4 thematic agents | — |
| `prompt-deep-003.md` | Foreign-language & international sources | 1 per language/region | — |
| `prompt-deep-004.md` | Historical precedent & base-rate analysis | 3 thematic agents | — |
| `prompt-deep-005.md` | Integration & gap audit | 1 orchestrator + comparators | 001–004 |

Prompts 001–004 are independent and can run in any order across sessions. Prompt 005 runs last and integrates findings.

## Execution

Each prompt runs via:
```bash
claude -p "$(cat prompts/research/prompt-deep-NNN.md)" --output-format=stream-json
```

Or interactively by pasting the prompt content.

## Running order

1. Run any combination of 001–004 (independent sessions, any order).
2. Run 005 after all deep-dive sessions complete.
3. Run `prompt-004.md` (top-level news update) at any time for breaking developments.

## Alignment rules (apply to ALL research prompts)

These rules prevent drift across multi-session, multi-prompt execution:

### 1. Source of truth
- `cases/{slug}.md` files are the canonical record for each case.
- `analysis/` files are the canonical synthesis.
- `logs/contradictions.md` and `logs/known-unknowns.md` are the canonical uncertainty registers.
- New findings update these files in place; they do not create parallel artifacts.

### 2. Schema adherence
- Case files follow the schema defined in `prompts/build/prompt-001.md` § "Artifact specifications → cases/{slug}.md".
- New sections may be added but existing required fields must not be removed or renamed.
- Source tier and confidence rating systems (Tier 1–7, Confirmed/Reported/Alleged/Speculated) are immutable.

### 3. No silent overwrites
- Before updating any existing content, read the current version first.
- When a new source contradicts an existing claim, add to `logs/contradictions.md` — do not silently replace the old claim.
- When resolving a known unknown, remove it from `logs/known-unknowns.md` with a dated note.

### 4. Commit discipline
- Commit incrementally with scoped messages: `research-deep: {description}`.
- Never squash or amend prior commits.
- No git push.

### 5. Research log
- Every sub-agent appends to `logs/research-log.md` with: date, prompt ID, what was searched, what was found, what failed.
- Dead ends are documented — they are findings, not failures.

### 6. Idempotency
- Check whether a source or finding already exists before adding it.
- Re-running a prompt should not produce duplicates.

### 7. No downstream side effects
- Research prompts do not touch `pdf-output/`, `data/diagram-data.json`, `data/timeline-data.json`, or website files.
- Data files are updated only by prompt-deep-005 (integration) or prompt-004 (news update).

### 8. Safety rules (inherited from all prompts)
- No contact with any person, family, agency, or journalist.
- No sudo. No system installs. No git push. No auth to services.
- All sourcing uses already-public material only.
- Copyright discipline: paraphrase, ≤15 words per quote, one quote per source max.
- Refuse-to-invent: if a fact cannot be sourced, leave the gap and log it.
