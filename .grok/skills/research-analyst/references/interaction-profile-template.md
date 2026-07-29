# Interaction / Pathway / Protective Analysis Template

Use this template for `briefing.md` when `input_type` is **interaction** — multi-compound queries about stacking, mitigation, protection, synergy, or antagonism.

Examples of triggers:

- “evaluation of cerebrolysin as a preventative against trenbolone negative effects”
- “does telmisartan mitigate BP/lipid effects of high-dose testosterone”
- “mechanistic overlap and stacking rationale for A + B”

**Do not** answer with a blanket “literature does not support combining them” or “avoid both.” Deliver pathway-level analysis. Literature silence is not disproof of a mechanistically plausible protective effect — label it **Speculative** / **Unknown** as appropriate.

Audience: nootropic users, gym/performance users, and anyone researching stacks or protectives.

---

## Effort floors

| Effort | Depth |
|--------|-------|
| **1** | Not recommended for interaction queries — soft-upgrade to ≥ 2 |
| **2** | Executive Card + sections 1, 4–9 condensed; matrix |
| **3+** | Full 10-section structure + dual pathway maps + explicit weighing |
| **4–5** | Full structure + extended literature + deeper mechanism maps |

`--wiki` / `--monograph` floors effort to **3** if lower was requested.

---

## Executive Card (always first)

| Field | Content |
|-------|---------|
| **Hypothesis** | e.g. “B mitigates A’s X effects” or “A + B stack for Y” |
| **Compounds** | A (problem / primary) and B (mitigator / co-stack) — roles labeled |
| **Overall certainty** | For the protective / stacking hypothesis |
| **Verdict** | One sentence on whether the hypothesis is supported, plausible, or unsupported |
| **Key practical note** | What (if anything) evidence-graded practice allows |
| **Top risks / unknowns** | 1–3 bullets |

---

## Required sections (order)

### 1. Executive verdict

Structured verdict on the proposed protective / stacking hypothesis with overall certainty label. Separate:

- What is **established** in literature  
- What is **mechanistically plausible**  
- What is **anecdotal only**  
- What remains **unknown**

### 2. Pathway map of Compound A

The problem compound or primary agent (e.g. trenbolone negative effects). Cover:

- Primary mechanisms of harm or intended effect  
- Organ systems / pathways involved  
- Time course and dose-dependence if known  
- Certainty labels on each pathway claim  

### 3. Pathway map of Compound B

The candidate mitigator or co-stack agent. Same structure: mechanisms, systems, dose relevance, certainty.

### 4. Points of potential interaction / protection

Explicit interaction surface:

| Point | System / pathway | Direction (protect / synergize / antagonize / unclear) | Certainty |
|-------|------------------|--------------------------------------------------------|-----------|
| … | … | … | … |

Include receptor-level, downstream signaling, metabolic, and organ-system points. Mark pure speculation clearly.

### 5. What controlled literature actually says

About the **combination** if studied, and about each relevant pathway independently. Stratify by design quality. State absences explicitly (“no human RCTs of A+B for outcome X”).

### 6. What consistent anecdotal / forum patterns report

About the combination or about B mitigating A’s side effects. Pattern-match multi-source reports; note consistency and common dose contexts. Label non-peer-reviewed.

### 7. Weighing

Concordance between literature, mechanism, and anecdote:

| Domain | Summary | Concordance |
|--------|---------|-------------|
| Controlled literature | … | … |
| Mechanism | … | … |
| Anecdote / forum | … | … |

**Rules:**

- Literature silence ≠ disproof of a mechanistically plausible effect.  
- Consistent anecdotes support **Speculative** notes only.  
- Never elevate pure mechanism + anecdote to Established/Probable.

### 8. Practical implications + monitoring

Evidence-graded guidance **only** where certainty supports it:

- Whether to consider the stack / protective strategy at all  
- Dosing context if any recommendation is warranted  
- Monitoring (labs, symptoms, stop criteria)  
- Harm reduction  

**Unknown = no recommendation.** Prefer “insufficient evidence for a protocol; if already using A, monitoring priorities are …” over inventing protectives.

### 9. Key risks and unknowns

Real risks of A, B, and the combination. Absolute contraindications. Long-term gaps. Do not soft-pedal AAS / SARM / peptide / high-dose neuro risks.

### 10. Open questions

2–5 concrete studies or data types that would most improve certainty on the hypothesis.

---

## Closing (always)

### Guidance & Application Notice

Evidence-graded synthesis; multi-compound strategies often sit at Speculative/Unknown; user assumes responsibility; **Unknown** = no recommendation; consult qualified professionals for individual medical decisions — especially for controlled substances and high-risk classes.

### References

DOI/PMID/URL for literature; clearly labeled forum/anecdotal sources.

---

## Orchestration notes (for synthesizer / framer)

- Compound-framer owns this outline for `input_type=interaction`.  
- Inference-analyst produces pathway overlap + protective-hypothesis certainty for the matrix.  
- Quality reviewer **rejects** pure literature-refusal summaries that skip pathway analysis.  
- Populate `pathway_overlap`, `protective_hypothesis`, and `anecdotal_patterns` in `evidence-matrix.json`.
