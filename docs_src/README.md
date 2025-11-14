# Generative AI glossary

![CI](https://github.com/Danielskry/gen-ai-glossary/actions/workflows/ci.yml/badge.svg)
![Docs](https://github.com/Danielskry/gen-ai-glossary/actions/workflows/docs.yml/badge.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)
![Glossary terms](https://img.shields.io/badge/dynamic/json?color=blue&label=Glossary%20terms&query=length&url=https://raw.githubusercontent.com/Danielskry/gen-ai-glossary/main/data/terms.json)

**A shared glossary to keep generative AI terminology clear, consistent, and discoverable 🤖** 

**Live docs:** https://danielskry.github.io/gen-ai-glossary/

This repository is a living glossary for concepts in generative AI, agentic AI, orchestration, retrieval, and context engineering. The field shifts quickly, so terminology and aliases change often. This project tracks established meanings, alternate names, and sources in one place. 

This glossary is community maintained. Terms update as research and usage evolve.

## Explore the glossary
- [Agent concepts](glossary/GLOSSARY_AGENTS.md)
- [Context engineering](glossary/GLOSSARY_CONTEXT_ENGINEERING.md)
- [Guardrails and evaluation](glossary/GLOSSARY_GUARDRAILS.md)
- [Memory systems](glossary/GLOSSARY_MEMORY.md)
- [Orchestration & tool use](glossary/GLOSSARY_ORCHESTRATION.md)
- [Retrieval & RAG patterns](glossary/GLOSSARY_RETRIEVAL.md)

## Why this project matters
- **Clear definitions.** Concepts evolve fast and communities often use multiple names. This glossary helps keep meaning stable and discoverable.
- **Good sources only.** Every entry references documentation or research that can be traced and verified.
- **Single data source.** `data/terms.json` drives everything: definitions, aliases, categories, Markdown, navigation, and the docs site.
- **Built for contributors.** Validation and CI ensure that edits stay consistent and up to date as the glossary grows.

## Structure of the repository
| Path                      | Description                                                            |
| ------------------------- | ---------------------------------------------------------------------- |
| `data/terms.json`         | The authoritative list of terms, aliases, categories, and sources.     |
| `data/terms.schema.json`  | JSON schema that enforces formatting and field rules.                  |
| `scripts/glossary.py`     | Utility script for validation and automatic docs generation.           |
| `scripts/publish_docs.py` | Builds the MkDocs site into `docs/` (plus `.nojekyll`) for GitHub Pages. |
| `docs_src/glossary/`      | Generated term cards for the documentation site. Do not edit manually. |
| `mkdocs.yml`              | MkDocs Material configuration, including navigation and styling.       |
| `.github/workflows/*.yml` | CI pipelines for validation and automated GitHub Pages deployment.     |


## Quick start
1. `pip install -r requirements.txt`
2. Make your edits in `data/terms.json` (add terms, aliases, or better sources).
3. `python scripts/glossary.py validate` – schema, duplicates, and generated headings.
4. `python scripts/glossary.py generate` – refresh Markdown + nav.
5. `mkdocs serve` – preview at http://127.0.0.1:8000/
6. `python scripts/publish_docs.py` – rebuilds the MkDocs site into `docs/` for GitHub Pages.

Prefer a dry run first? `python scripts/glossary.py generate --dry-run`

## How to help improve the glossary
1. Add or modify entries in `data/terms.json`, including aliases and reliable references.
2. Re-run the Quick start commands (`python scripts/glossary.py validate`, `python scripts/glossary.py generate`, and `python scripts/publish_docs.py`) so Markdown and `docs/` reflect your edits.
3. Review the Git diff and commit the JSON, generated Markdown, and refreshed `docs/` site.
4. Open a pull request with a brief note on the motivation or source quality.

The CI checks ensure that generated files match the source of truth, so builds stay consistent.

**Example term entry:**
```json
{
    "term": "Agent",
    "definition": "AI agents are autonomous software systems that use artificial intelligence to perform tasks, make decisions, and interact with their environment on behalf of a user or another system. They apply reasoning, planning, and memory, and can adapt over time to pursue goals more effectively.",
    "category": "agents",
    "aliases": ["AI agent", "autonomous agent", "agentic AI", "intelligent agent"],
    "sources": [
      "https://cloud.google.com/discover/what-are-ai-agents",
      "https://www.ibm.com/think/topics/ai-agents",
      "https://github.com/resources/articles/what-are-ai-agents"
    ]
  },
```

## Contribute

Contributions are welcome. If you notice a term that is missing, unclear, or evolving in the field, feel free to propose updates. Discussion first is encouraged, but not required. Please see `CONTRUBTIONS.md` for more.
