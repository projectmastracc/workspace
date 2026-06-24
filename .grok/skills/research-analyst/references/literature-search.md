# Literature Search Playbook

## Step 1: Formulate PICO

| Field | Question |
|-------|----------|
| **P** — Population | Who? species, age, condition severity |
| **I** — Intervention/Exposure | Drug, dose, duration, mechanism |
| **C** — Comparator | Placebo, active control, none |
| **O** — Outcome | Primary clinical endpoint; not surrogate unless validated |

Write PICO in `intake.md` before searching.

## Step 2: Search hierarchy

1. **Systematic reviews / meta-analyses** — start here for broad questions
2. **RCTs** — for intervention efficacy and causation
3. **Observational** — when RCTs unethical or missing; flag confounding
4. **Mechanistic** — animal, in-vitro; label **Speculative** for clinical claims
5. **Contradictory set** — actively search for null results and critiques

## Step 3: Databases and tools

| Tool | Use |
|------|-----|
| PubMed MCP | PMID lookup, structured search when available |
| `web_search` | Find reviews, landmark papers, guideline PDFs |
| `web_fetch` | DOI landing pages, open-access full text |

**PubMed query template:**
```
("intervention term"[Title/Abstract] OR "synonym"[Title/Abstract])
AND ("outcome term"[Title/Abstract])
AND (systematic review[pt] OR meta-analysis[pt] OR randomized controlled trial[pt])
```

Document exact query strings in `intake.md`.

## Step 4: Inclusion rules

- Peer-reviewed preferred; preprints labeled and certainty downgraded
- Retracted papers excluded from support (note if still cited in discourse)
- Prefer last 15 years unless seminal/historical paper required
- Include at least one **contradictory or null** source for contested topics (effort ≥ 2)

## Step 5: Source count by effort

| Effort | Target |
|--------|--------|
| 1 | 2–4 pivotal |
| 2 | 4–8 incl. one review if exists |
| 3+ | 8–15 incl. systematic reviews + contradictory evidence |

## Step 6: Full-text gaps

If paywalled: use abstract + methods from PubMed; state gap in intake. Never invent methods or results.