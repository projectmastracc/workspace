# Evidence Grading

## Claim certainty labels (use on every substantive claim)

| Label | Meaning |
|-------|---------|
| **Established** | Multiple high-quality human studies or authoritative meta-analyses agree |
| **Probable** | Consistent evidence with notable limitations |
| **Speculative** | Mechanistic extrapolation, animal-only, thin human data, **or** consistent multi-source anecdote without controlled confirmation |
| **Unknown** | Insufficient, absent, or directly contradictory evidence |

## What can drive a recommendation

| Stratum | Treatment | Can drive recommendation? |
|---------|-----------|---------------------------|
| High-quality human (meta, large RCTs) | Primary | Yes → Established / Probable |
| Lower-quality human | Supporting or primary when better data absent | Yes → usually Probable / Speculative |
| **Consistent multi-source anecdotal / forum consensus** | **Must report and weigh** | Speculative notes only; **never** Established/Probable alone |
| Single / low-signal anecdotes | Low weight; mention only if relevant | No |
| Preclinical | Mechanistic context only | No practical dosing advice |
| Mechanistic inference | Labeled as such | Supports Speculative reasoning (esp. interaction analyses) |

### Concordance ratings (subjective / experiential section)

| Rating | Meaning |
|--------|---------|
| `strong` | Controlled evidence and consistent anecdotes align |
| `partial` | Partial overlap; important gaps or dose mismatches |
| `weak` | Thin connection between reports and data |
| `contradictory` | Anecdotes and literature point different directions |
| `literature-silent` | Consistent reports exist; controlled literature does not address the claim |

**Literature-silent ≠ evidence of absence.** Do not claim an effect does not exist solely because papers are missing.

## GRADE-inspired study quality (per source)

| Grade | Criteria |
|-------|----------|
| **High** | RCT or strong observational; low bias; direct outcome |
| **Moderate** | RCT limitations OR strong observational with confounding control |
| **Low** | Observational with confounding OR small RCT OR indirect outcomes |
| **Very Low** | Case series, expert opinion, animal extrapolation, serious bias, unsystematic forum reports |

## Downgrade factors

- Risk of bias (see source-evaluation.md)
- Inconsistency across studies
- Indirectness (wrong population, surrogate endpoint)
- Imprecision (wide CIs, small n)
- Publication bias likely
- Sole reliance on industry-funded positive trials without independent replication

## Upgrade factors (rare — apply cautiously)

- Large magnitude of effect
- Dose-response gradient
- All plausible confounders would reduce effect (not increase it)

## Correlation vs causation

- Observational association → label **Probable** at best for causation unless Bradford Hill criteria substantially met
- Mechanistic plausibility alone → **Speculative** for clinical outcome claims
- “No significant association” in underpowered study → **Unknown**, not evidence of absence
- Consistent forum reports without trials → **Speculative** at best for practical notes; **Unknown** for firm protocols

## Interaction / protective hypotheses

Grade the **hypothesis** separately from each compound’s standalone effects:

- Literature on the combination (if any)  
- Literature on each relevant pathway  
- Mechanistic overlap (Speculative unless experimentally shown)  
- Anecdotal combo reports (Speculative ceiling)  

Overall protective/stack certainty is the **weakest critical link**, not the average of optimistic pieces.
