## Summary

Describe what this PR changes and why.

## Branch naming
- [ ] Branch name follows glossary naming (`term/<new-term>`, `fix/<existing-term>`, `docs/<doc-update>`). 

Examples: `term/context-engineering`, `term/revise-agentic-ai`, `fix/typo-vector-db`, `docs/update-readme`.

## Contribution checklist
- [ ] PR focuses on a single, well-scoped change set
- [ ] Ran `python scripts/glossary.py validate`
- [ ] Ran `python scripts/glossary.py generate` and committed the generated files
- [ ] Ran `python scripts/publish_docs.py` so `docs/` reflects generated content
- [ ] Added/updated sources for any new or changed terms
