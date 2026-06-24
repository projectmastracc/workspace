# Research Analyst

Deep research analysis for Grok — one command (`/research`), multi-perspective rigor, DNR (no personal medical advice), guidelines audited against literature.

**Plan:** [`.grok/plans/research-analyst.md`](.grok/plans/research-analyst.md)

## Quick start

1. Select **research-analyst** agent: `/config-agents`
2. Run analysis:

```
/research What does human evidence say about ketamine's mechanism in depression?
```

```
/research --effort 3 --save findings/ketamine-mechanism SSRIs and adolescent suicide risk
```

## Command

```
/research [--effort N] [--save PATH] <question | claim | DOI | PMID | topic>
```

| Flag | Default | Purpose |
|------|---------|---------|
| `--effort` | 2 | Depth 1–5 |
| `--save` | — | Save briefing + matrix + intake (e.g. `findings/<date>-<slug>/`) |

## What you get

Parallel specialist analysis → integrated briefing + `evidence-matrix.json`:

- Source critic (funding, COI, trust)
- Methodologist (design, bias, stats)
- Inference analyst (truth mapping, guidelines vs literature)
- Quality reviewer (effort ≥ 2)

## DNR

Reports what research says — not personal medical advice. Guidelines credited when literature-backed; mismatches called out.

## Project layout

```
.grok/
  agents/research-analyst.md
  config.toml                    # PubMed MCP
  personas/                      # 5 specialists
  skills/research-analyst/
    SKILL.md
    scripts/research-memory.py   # cross-session threads
    references/
  plans/research-analyst.md
findings/                        # saved reports (gitignored)
AGENTS.md
```

## Cross-session memory

Prior `/research` runs on the same topic are loaded automatically via `research-memory.py` (~/.grok/research-memory/).

## PubMed MCP

Configured in `.grok/config.toml`. Falls back to web search if unavailable.