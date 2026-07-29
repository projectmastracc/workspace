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

### 2. Pathway map of Compound A (mechanism → phenotype)

The problem compound or primary agent. **Do not stop at a side-effect list.** For each major adverse domain (sleep, mood, structure, CV, etc.), chain:

1. **Molecular / receptor action** (what the drug does)  
2. **Downstream physiology** (what systems change)  
3. **Observable phenotype** (what the user experiences)  
4. **Certainty** on each link  

Required for side-effect-heavy queries (e.g. “why tren ruins sleep”):

| Phenotype | Upstream mechanism(s) | Downstream cascade | Intervention nodes (what could theoretically act here) | Certainty |
|-----------|----------------------|--------------------|--------------------------------------------------------|-----------|
| e.g. insomnia / night sweats | … | … | … | … |

Include organ systems, time course, dose-dependence. Label pure speculation.

### 3. Pathway map of Compound B (or each mitigator)

For **each** candidate mitigator / protective:

1. Its own MoA (molecular → downstream)  
2. **Which nodes on A’s map it hits** (must map explicitly — not “generally neuroprotective”)  
3. Dose/route relevance if known  
4. Certainty that the node match is real vs hand-wavy  

### 4. Points of potential interaction / protection

**Node-matched** interaction surface — every row must name the shared pathway node:

| Phenotype of A | Node on A’s cascade | B agent | How B hits that node | Direction | Certainty |
|----------------|---------------------|---------|----------------------|-----------|-----------|
| … | … | … | … | protect / synergize / antagonize / unclear | … |

Reject vague rows like “brain health / protect / Speculative” without a mechanism.

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

### 8. Practical implications + full protocol (when requested)

**If the user asked for full neuroprotection / full protocol / complete cover:** this section is the main deliverable. Lead with it in spirit — do **not** open with “no protocol exists.”

#### 8.1 Full mechanism-mapped protocol (required for “full protection” queries)

Build a complete protocol:

1. **Pathway inventory** — every material node from §2  
2. **Per-node mitigations** — agents/actions that hit that node  
3. **Phased schedule** — pre-exposure · on-exposure · acute side management · exit / recovery  
4. **Doses / ranges** when literature, labels, or consistent community practice exist — each with certainty  
5. **Monitoring + stop criteria**  
6. **Joint-cover caveat** in one line: complete prevention is not proven (**Speculative**/**Unknown** as guarantee) — still ship the protocol  

| Phase | Pathway node | Phenotype addressed | Agent / action | Dose / practice | Certainty |
|-------|--------------|---------------------|----------------|-----------------|-----------|
| … | … | … | … | … | … |

#### 8.2 Phenotype → mechanism → tool (always)

| User problem | Mechanism targeted | Tool / strategy | Certainty | Notes |
|--------------|-------------------|-----------------|-----------|-------|
| … | … | … | … | … |

#### 8.3 Monitoring & stop criteria

Labs, symptoms, hard stops.

#### 8.4 What is experimental vs load-bearing

Separate core levers (**Probable**/**Established**) from experimental lines (**Speculative**).

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
- **Package isolation:** Mitigators (including community protectives such as peptides used against AAS sides) must be evidenced from **this run’s** literature and forum sampling. Do not import prior monographs or other `findings/*` packages.
