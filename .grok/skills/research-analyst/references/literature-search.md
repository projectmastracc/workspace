# Literature Search Playbook

## Step 1: Formulate PICO (or dual-PICO for interactions)

| Field | Question |
|-------|----------|
| **P** — Population | Who? species, age, condition severity, training status |
| **I** — Intervention/Exposure | Drug, dose, duration, mechanism |
| **C** — Comparator | Placebo, active control, none |
| **O** — Outcome | Primary clinical endpoint; not surrogate unless validated |

For `input_type=interaction`, write PICO for compound A, compound B, and the combination/mitigation hypothesis.

Write PICO in `intake.md` before searching.

## Step 2: Search hierarchy (stratified)

1. **Systematic reviews / meta-analyses** — start here for broad questions  
2. **RCTs** — intervention efficacy and causation  
3. **Observational** — when RCTs unethical or missing; flag confounding  
4. **Regulatory / labels** — FDA, EMA, product monographs when they exist  
5. **Mechanistic** — animal, in-vitro; label **Speculative** for clinical claims  
6. **Contradictory / failed trials** — actively search for null results and critiques (required effort ≥ 2)  
7. **High-signal anecdotal / forum patterns** — when the compound or effect has heavy community discourse; force a weighing step later  

## Step 3: Databases and tools

| Tool | Use |
|------|-----|
| PubMed MCP | PMID lookup, structured search when available |
| `web_search` | Reviews, landmark papers, guideline PDFs, forum consensus signals |
| `web_fetch` | DOI landing pages, open-access full text, key threads |

**PubMed query template:**
```
("intervention term"[Title/Abstract] OR "synonym"[Title/Abstract])
AND ("outcome term"[Title/Abstract])
AND (systematic review[pt] OR meta-analysis[pt] OR randomized controlled trial[pt])
```

Document exact query strings and **date range** in `intake.md`.

## Step 4: Interaction / stack / protective searches

When `input_type=interaction` (or stack/mitigate language):

1. Search compound A alone for the relevant harms or effects.  
2. Search compound B alone for protective or overlapping mechanisms.  
3. Search **combination terms**: “A AND B”, mitigate, protect, attenuate, stack, concurrent.  
4. Search pathway-level terms (e.g. “androgen receptor neurotoxicity”, “BDNF peptide”, “blood pressure testosterone ARB”).  
5. Sample high-signal anecdotal sources on the **combination** if community discussion exists.

Never stop at “no combo RCTs found” without pathway-level source work.

## Step 5: Anecdotal / forum sampling (when material)

Use when: sparse human data, strong community use (nootropics, peptides, AAS/SARMs, obscure stacks), or user asks about subjective effects.

| Source class | How to treat |
|--------------|--------------|
| Multi-thread, multi-year forum consensus (e.g. high-engagement Reddit, Longecity, Meso-Rx, relevant Discord digests) | Pattern-match; note consistency; **Speculative** ceiling |
| Examine.com community / similar secondary | Supporting context; verify against primary when possible |
| Single anecdote / marketing testimonials | Low weight; mention only if relevant |
| Influencer protocols without sources | Tag; do not treat as evidence |

**Rules:**

- Label all as non-peer-reviewed.  
- Prefer **patterns** (many independent reports with similar dose/effect) over vivid single stories.  
- Record in intake: which forums/topics sampled and that they are experiential.  
- Downstream: Subjective Profile must weigh these against controlled literature.

## Step 6: Inclusion rules

- Peer-reviewed preferred; preprints labeled and certainty downgraded  
- Retracted papers excluded from support (note if still cited in discourse)  
- Prefer last 15 years unless seminal/historical paper required  
- Include at least one **contradictory or null** source for contested topics (effort ≥ 2)  
- For performance compounds: include safety / endocrine / CV literature, not only efficacy claims  

## Step 7: Source count by effort

| Effort | Target |
|--------|--------|
| 1 | 2–4 pivotal |
| 2 | 4–8 incl. one review if exists; contradictory set if contested; anecdotal sample if discourse-heavy |
| 3+ | 8–15 incl. systematic reviews + primary studies + contradictory evidence; interaction dual-compound coverage |
| 4–5 | Extended set; multiple alternatives or deep pathway sources |

## Step 8: Full-text gaps

If paywalled: use abstract + methods from PubMed; state gap in intake. Never invent methods or results.

## Step 9: Record in intake.md

Always capture:

- Search strategy (terms, databases)  
- Date range  
- PubMed MCP available / unavailable  
- Whether anecdotal sources were sampled (and which)  
- For interaction: A terms, B terms, combo terms  
