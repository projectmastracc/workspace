# Contributing

This repo is the **Research Analyst** Grok skill: multi-agent evidence analysis for nootropics, performance pharmacology, and general supplementation.

## Where to edit

| Change | Location |
|--------|----------|
| Orchestration / flags / classifier | `.grok/skills/research-analyst/SKILL.md` |
| Personas | `.grok/personas/*.toml` |
| Templates & principles | `.grok/skills/research-analyst/references/` |
| Golden examples | `references/examples/` |
| Persistent monographs | `knowledge/compounds/`, `knowledge/interactions/` |
| Project rules | `AGENTS.md` |
| Depth roadmap | `docs/improvement-plan-sciwiki-depth.md` |

## Adding a golden example

1. Create `references/examples/example-<name>.md` following `style-guide.md` and the relevant template.
2. Include an Executive Card and explicit certainty labels.
3. If testing anecdotal rules: include weighing sentence + concordance rating.
4. If testing interaction mode: dual pathway maps + interaction points table.
5. Register it in `references/evaluation-checklist.md` section E.
6. Run through the evaluation checklist mentally (or via review) before merging.

## Updating knowledge profiles

Prefer high-effort (`--effort 3+`) runs with human skim:

```
/research --effort 3 --wiki --save knowledge/compounds/<slug> <compound>
```

Or copy from `findings/` after review. Keep `meta.json` in sync (see `knowledge/README.md`).

## Product bar

- One max-depth `briefing.md` per run (not multi-file dumps)  
- Full pathways: known + hypothesized  
- Clinical + forum both complete  
- Sides: mechanism → node → counters  
- Protection stacks: build them; do not lead with refusal  
- Package isolation: each findings slug standalone

See `references/dr-principles.md` and `references/evaluation-checklist.md`.

## License

Contributions are under the MIT License (see `LICENSE`).
