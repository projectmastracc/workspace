# Research Analyst

Deep research analysis and open compound education for Grok — one command (`/research`), multi-perspective rigor, and **evidence-graded practical guidance**.

Built as a research tool for:

- **Nootropic users** (racetams, botanicals, peptides, neuromodulators, stacks)
- **Gym / performance users** (ergogenics, AAS/SARMs, PCT, protectives, monitoring)
- **Anyone interested in supplementation** (vitamins, minerals, amino acids, adaptogens, and beyond)

**Plan:** [`.grok/plans/research-analyst.md`](.grok/plans/research-analyst.md)  
**Depth roadmap (Phase 5):** [`docs/improvement-plan-sciwiki-depth.md`](docs/improvement-plan-sciwiki-depth.md)

## Quick start

1. Select **research-analyst** agent: `/config-agents`
2. Run analysis:

```
/research creatine
```

```
/research --effort 3 --wiki bacopa monnieri
```

```
/research --effort 3 --save findings/cerebrolysin-skin "cerebrolysin skin quality and anti-ageing appearance claims"
```

```
/research --effort 3 "evaluation of cerebrolysin as a preventative measure against the negative effects of trenbolone"
```

```
/research --effort 4 --save findings/telmisartan-testosterone does telmisartan meaningfully mitigate blood-pressure and lipid effects of high-dose testosterone?
```

## Command

```
/research [--effort N] [--wiki|--monograph] [--save PATH] <question | claim | DOI | PMID | topic | compound | stack/interaction>
```

| Flag | Default | Purpose |
|------|---------|---------|
| `--effort` | 2 | Depth 1–5 (1=fast, 2=standard, 3=full monograph/interaction, 4–5=max rigor) |
| `--wiki` / `--monograph` | off | Force full structure + accessible prose; floors effort to 3 |
| `--save` | — | Save briefing + matrix + intake (e.g. `findings/<date>-<slug>/`) |

## What you get

Parallel specialist analysis → integrated briefing + `evidence-matrix.json`:

- **Executive Card** — verdict, certainty, practical note, caveats at a glance
- Source critic (funding, COI, trust — including forum source labeling)
- Methodologist (design, bias, stats, applied applicability)
- Inference analyst (truth mapping, subjective concordance, pathway overlap)
- Compound framer (effort ≥ 2 — full monograph or multi-compound pathway analysis)
- Quality reviewer (effort ≥ 2 — structure, certainty, anecdotal weighing, interaction depth)

### Analysis modes

| Mode | When | Output shape |
|------|------|--------------|
| **Compound monograph** | Single compound / dosing / profile | Up to 15 Sci-Wiki-style sections including Subjective Profile |
| **Interaction / pathway** | Stack, mitigate, protect, A vs B effects | Dual pathway maps, interaction points, weighing, monitoring |
| **General research** | Claim, paper, topic, question | Executive Card + structured research briefing |

### Evidence rules (short)

- Certainty labels on every substantive claim and recommendation: **Established** / **Probable** / **Speculative** / **Unknown**
- **Unknown = no recommendation**
- Consistent multi-source anecdotal patterns are **reported and weighed** (Speculative ceiling only)
- Literature silence ≠ “effect does not exist”
- Interaction queries get pathway analysis, not blanket refusal

## Project layout

```
.grok/
  agents/research-analyst.md
  config.toml                    # PubMed MCP
  personas/                      # specialists
  skills/research-analyst/
    SKILL.md
    scripts/research-memory.py
    references/                  # templates, principles, golden examples
  plans/research-analyst.md
docs/                            # improvement plan and design notes
knowledge/                       # persistent compound/interaction profiles
  compounds/
  interactions/
findings/                        # saved reports (often gitignored)
AGENTS.md
LICENSE
```

## Knowledge layer

High-effort runs can write or update:

```
knowledge/compounds/<slug>/profile.md
knowledge/compounds/<slug>/matrix.json
knowledge/compounds/<slug>/meta.json
```

Subsequent runs load prior profiles for differential updates. See [`knowledge/README.md`](knowledge/README.md).

## Cross-session memory

Prior `/research` runs on the same topic are loaded automatically via `research-memory.py` (`~/.grok/research-memory/`).

## PubMed MCP

Configured in `.grok/config.toml`. Falls back to web search if unavailable.

## Golden examples

Calibration targets under `.grok/skills/research-analyst/references/examples/`:

- Creatine — high-evidence performance/nutrition
- Bacopa-style mixed nootropic — anecdotal weighing
- Literature-silent + strong anecdote (cerebrolysin skin-style)
- Interaction/protective (cerebrolysin vs trenbolone-style)
- AAS harm-reduction depth

Structural evaluation: `references/evaluation-checklist.md`.

## License

MIT — see [LICENSE](LICENSE).
