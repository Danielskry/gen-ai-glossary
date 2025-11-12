## Contributing

Thanks for helping improve the Generative AI Glossary!

### Ways to contribute
- Add or refine terms in `data/terms.json`
- Improve definitions and add good sources
- Review PRs and suggest structure improvements

### Getting started
1. Fork and clone the repository.
2. Ensure Python 3.10+ (3.12 recommended) and install tooling: `pip install -r requirements.txt`
3. Validate terms + generated files: `python scripts/glossary.py validate`
4. Regenerate Markdown and refresh the MkDocs nav block: `python scripts/glossary.py generate`

### Schema
- See `data/terms.schema.json` for the expected shape of each term.
- The validator checks duplicates, headings, and schema (if `jsonschema` is installed, it is part of `requirements.txt`).

### Pull requests
- One focused change per PR
- Include before/after context if definitions change materially
- Ensure CI passes (validator + regeneration check)
