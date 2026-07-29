# Research Analyst

Maximum-depth compound and **protection-stack** research for Grok — one command, **one document**.

Built for:

- **Nootropic users**
- **Gym / performance users** (including AAS/SARM/peptide contexts)
- **Anyone researching supplementation**

## What you get

A single comprehensive `briefing.md` that includes:

1. **Full pathway map** — known **and** hypothesized  
2. **Clinical evidence** — evaluated across study tiers  
3. **Forum / anecdotal evidence** — patterns weighed against clinical  
4. **Sides with real mechanisms** — not just a list  
5. **Counters per pathway node** — e.g. if a compound wrecks sleep via thermal + arousal + inhibitory-tone (+ hypothesized wake-drive) pathways, each node gets specific countermeasures  
6. **Assembled stack** when you ask for protection / mitigation  

No effort levels. Always full depth. Intermediate persona files stay internal — you see one document.

## Quick start

```
/research trenbolone
```

```
/research full neuroprotective stack against trenbolone sides — every pathway and counter
```

```
/research --save findings/bacopa bacopa monnieri
```

## Command

```
/research [--save PATH] <compound | protection stack | claim | pathway question>
```

## Design principles

| Principle | Meaning |
|-----------|---------|
| Mechanism first | Phenotype → pathways → counters |
| Both evidence worlds | Clinical + forums |
| Stack engineering | Per-side counters, not “avoid only” |
| One file | `briefing.md` is the product |
| Isolation | Each findings package is standalone |

## Layout

```
.grok/skills/research-analyst/   # skill + templates
.grok/personas/                  # internal specialists
findings/<slug>/briefing.md      # saved outputs (one doc)
knowledge/                       # optional same-slug cache
AGENTS.md
```

## License

MIT — see [LICENSE](LICENSE).
