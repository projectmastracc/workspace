# Research Analyst

Deep research analysis and open compound education for Grok — one command (`/research`), multi-perspective rigor, **DR** (actionable evidence-graded guidance), guidelines audited against literature.

**Plan:** [`.grok/plans/research-analyst.md`](.grok/plans/research-analyst.md)

## Quick start

1. Select **research-analyst** agent: `/config-agents`
2. Run analysis:

```
/research creatine
```

```
/research --effort 4 --save findings/trenbolone trenbolone
```

```
/research --effort 3 --save findings/ketamine-mechanism What does human evidence say about ketamine's mechanism in depression?
```

## Command

```
/research [--effort N] [--save PATH] <question | claim | DOI | PMID | topic | compound>
```

| Flag | Default | Purpose |
|------|---------|---------|
| `--effort` | 2 | Depth 1–5 |
| `--save` | — | Save briefing + matrix + intake (e.g. `findings/<date>-<slug>/`) |

## What you get

Parallel specialist analysis → integrated briefing + `evidence-matrix.json`:

- Source critic (funding, COI, trust)
- Methodologist (design, bias, stats, applied applicability)
- Inference analyst (truth mapping, evidence-graded recommendations)
- Compound framer (effort ≥ 2, compound inputs — three-lens framing + Practical Guidance)
- Quality reviewer (effort ≥ 2)

## DR — Do Render

Actionable, evidence-graded guidance across neuropharmacology, performance pharmacology, and nutrition/supplements. Guidelines credited when literature-backed; mismatches called out with recommendations against bunk guidance. **Unknown** = no recommendation.

## Project layout

```
.grok/
  agents/research-analyst.md
  config.toml                    # PubMed MCP
  personas/                      # 6 specialists (+ compound-framer)
  skills/research-analyst/
    SKILL.md
    scripts/research-memory.py   # cross-session threads
    references/
      dr-principles.md
      compound-lenses.md
      compound-profile-template.md
      ...
  plans/research-analyst.md
findings/                        # saved reports (gitignored)
AGENTS.md
```

## Cross-session memory

Prior `/research` runs on the same topic are loaded automatically via `research-memory.py` (~/.grok/research-memory/).

## PubMed MCP

Configured in `.grok/config.toml`. Falls back to web search if unavailable.