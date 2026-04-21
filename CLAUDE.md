# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

This is a structured research repository investigating deaths and disappearances of U.S. defense and advanced-research scientists. It is **not a software project** — it is a living-artifact research dossier maintained through a pipeline of Claude Code prompts. All content is markdown and JSON; there is no application code to build or test.

## Repository structure

- `dossier.md` — Top-level synthesized document (start here)
- `cases/` — One file per case (11 total), each following a standard schema with status, dates, affiliation, narrative, source tiers, contradictions, and open questions
- `analysis/` — Cross-case connection analysis, pre-registered hypotheses (H1-H9), foreign-intelligence layer
- `appendices/` — Primary-source excerpts, foreign coverage, named expert commentary
- `data/` — JSON specs for diagrams and timelines with JSON Schema 2020-12 definitions
- `logs/` — Research log, contradiction tracker, known-unknowns register, audit artifacts
- `STATUS.md` — Post-run summary with flags for review
- `CHANGELOG.md` — Version history
- `RUNBOOK.md` — Detailed operational instructions

## Critical rules

- **No contact policy**: Never attempt to contact any individual, family, agency, employer, or journalist. All sourcing uses already-public material only.
- **Git push allowed**: Agents may push to origin when instructed.
- **No sudo**: Never.
- **Source tiering**: Every source is categorized Tier 1-8 (see README.md for definitions). Every factual claim carries a confidence rating: Confirmed, Reported, Alleged, or Speculated. The quote provenance rule applies: claims found only in national mainstream reporting (Tier 4) or lower must be traced to a higher-tier origin when possible.
- **Neutrality**: No country or entity is pre-excluded or pre-implicated. Sensational framing is avoided in repository prose (quoted and attributed when from sources).
- **Idempotency**: Research prompts are designed to be re-runnable — check for existing case files before redoing work.
