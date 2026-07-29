# Evaluation Checklist — Sci-Wiki Depth

Use this to verify golden examples, saved findings, and high-effort briefings. Quality reviewer is the runtime gate; this is the structural/epistemic regression checklist.

---

## A. Structural checks

| # | Check | Compound | Interaction | General |
|---|--------|----------|-------------|---------|
| A1 | Executive Card present at top | required | required | required |
| A2 | Clean ATX headings matching template | required | required | required |
| A3 | All effort-required sections present | per effort floor | per effort floor | core sections |
| A4 | Tables used for dosing / comparisons / pathway points where relevant | preferred | required for §4 | preferred |
| A5 | Guidance & Application Notice + References | required | required | required |
| A6 | `evidence-matrix.json` valid vs schema (when produced) | required effort ≥ 2 | required | when guidance rendered |

### Compound section set (effort ≥ 3)

Bottom-line, Chemistry, Mechanism, PK, Human Evidence, Preclinical, Subjective Profile, Practical Guidance, Safety, Interactions, History, Comparative, Open Questions, Evidence Matrix/Sources, FAQ.

### Interaction section set (effort ≥ 3)

Executive verdict, Pathway A, Pathway B, Interaction points, Controlled literature, Anecdotal patterns, Weighing, Practical + monitoring, Risks/unknowns, Open questions.

---

## B. Epistemic & anecdotal checks

| # | Check | Pass criteria |
|---|--------|---------------|
| B1 | Certainty labels | Every practical recommendation has inline **Established** / **Probable** / **Speculative** / **Unknown** |
| B2 | Unknown rule | No firm protocol under **Unknown** |
| B3 | Subjective weighing | Subjective Profile (or interaction §6–7) has explicit weighing sentence + concordance rating |
| B4 | Literature-silent posture | If anecdotes consistent and lit limited: **both** stated; no adamant “does not exist” solely from missing papers |
| B5 | Anecdote ceiling | Pure anecdote never labeled Established or Probable as guidance basis |
| B6 | Interaction depth | Interaction queries include pathway-level analysis — not literature-refusal only |
| B7 | Source trail | Key claims cite sources; trust tiers on pivotal sources |
| B8 | Safety | Safety/monitoring present for non-trivial risk (AAS, SARM, peptide, high-dose neuro) |
| B9 | Preclinical dosing | No dosing advice from preclinical alone |
| B10 | Guidelines | Health-adjacent topics address guidelines vs literature when mainstream guidance exists |

### Forbidden phrase heuristics (flag for human review)

- “does not exist” / “no effect whatsoever” without controlled negative evidence  
- “literature does not support combining — avoid both” as the only analysis  
- “may/might/could” as the sole substitute for an Unknown label  
- “Established” attached to pure forum consensus  

---

## C. Utility checks

| # | Check |
|---|--------|
| C1 | Reader can extract usable practical notes (or clear insufficient-evidence) from Executive Card + Practical Guidance alone |
| C2 | Reader can see how forum reports relate to controlled evidence without reading the entire document |
| C3 | Multi-compound questions show mechanistic interaction reasoning |
| C4 | Open questions are concrete (study types / endpoints), not vague “more research needed” only |
| C5 | Audience fit: language usable by nootropic / gym / supplement researchers without jargon walls |

---

## D. Matrix field checks (effort ≥ 2)

| Field | When required |
|-------|----------------|
| `executive_verdict` | Always preferred |
| `recommendations[]` | When Practical Guidance rendered |
| `anecdotal_patterns[]` | When subjective/forum content material |
| `subjective_concordance` | When anecdotal_patterns non-empty |
| `pathway_overlap` / `protective_hypothesis` | `input_type=interaction` |
| `monitoring_protocol` | Performance / high-risk compounds |
| `comparative_alternatives` | Effort ≥ 3 when alternatives discussed |
| `bro_science_claims[]` | Optional legacy; OK alongside anecdotal_patterns |

---

## E. Golden example map

| Example file | Must pass |
|--------------|-----------|
| `example-compound-creatine.md` | A, B1–2, C1, high-evidence Practical Guidance |
| `example-nootropic-mixed-evidence.md` | B3–5, mixed certainty |
| `example-literature-silent-anecdote.md` | **B4** critical |
| `example-interaction-protective.md` | **B6**, interaction section set |
| `example-performance-aas-harm-reduction.md` | B8, monitoring |

---

## Quick pass/fail

**PASS** if all applicable A checks + B1–B8 + C1–C2 hold for the query type and effort.  
**FAIL** if any of B2, B4, B5, B6, B8 violated on a high-effort compound/interaction briefing.
