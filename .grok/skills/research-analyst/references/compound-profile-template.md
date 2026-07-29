# Compound Profile Output Template

Use this template for `briefing.md` when `input_type` is **compound** (or user requests compound framing).  
For multi-compound protective / stack / mitigate queries, use `interaction-profile-template.md` instead.

Every briefing opens with an **Executive Card**, then sections below. Certainty labels (**Established** / **Probable** / **Speculative** / **Unknown**) on every substantive claim and recommendation.

Audience: nootropic users, gym/performance users, and anyone researching supplementation of any kind.

---

## Effort floors (which sections are required)

| Effort | Required sections |
|--------|-------------------|
| **1** | Executive Card + Bottom-line + Practical Guidance + Safety + Key Sources |
| **2** (default) | Core set: 1–10, 13–14; Subjective Profile with weighing; matrix; quality gate |
| **3** | **All 15 sections** + comparative table when alternatives exist |
| **4–5** | All 15 + deeper source set + multiple alternatives + extended open questions |

Do not omit required sections at the declared effort.

---

## Executive Card (always first)

Compact block at the top of every briefing:

| Field | Content |
|-------|---------|
| **Compound / class** | Name + primary taxonomy class |
| **Overall certainty** | For the primary use case |
| **Verdict** | One sentence |
| **Key practical note** | Dose/protocol highlight or “insufficient evidence for recommendation” |
| **Top caveats** | Safety, evidence gaps, or sourcing risks (1–3 bullets) |

---

## Canonical sections (order)

### 1. Bottom-line / Overview

4–8 sentences. Overall certainty for the primary use case, key practical takeaway, critical safety or evidence caveats. Must be accurate and self-contained without reading further.

### 2. Chemistry & Classification

Class, key structural features if relevant, solubility/stability notes, close analogs. Regulatory status where known.

### 3. Mechanism of Action (mechanism → phenotype)

Receptor / enzyme / pathway detail. Distinguish **established** molecular actions from **downstream hypotheses**.

**Required chain for major effects and side effects:**

| Claimed effect / side effect | Molecular action | Downstream cascade | Clinical/subjective phenotype | Certainty |
|------------------------------|------------------|--------------------|-------------------------------|-----------|
| … | … | … | … | … |

Do **not** list sides without “why.” Connect MoA → physiology → what the user feels or measures.

### 4. Pharmacokinetics

Absorption, half-life, metabolism, CNS penetration, food effects. Flag sparse human PK data explicitly.

### 5. Human Evidence

Stratified by design quality (meta/RCT > observational > case series). Effect sizes, populations, limitations. Explicitly state what the data do **not** show.

### 6. Preclinical / Mechanistic Support

Always labeled with translation risk. Never produce practical dosing from preclinical data alone.

### 7. Subjective / Experiential Profile (weighing the evidence)

**Critical section.** Primary home for forum / user-report patterns.

Required content:

1. Consistent multi-source anecdotal themes (what is reported, consistency, dose ranges if mentioned).
2. Explicit **weighing** against controlled evidence.
3. **Concordance rating:** `strong` | `partial` | `weak` | `contradictory` | `literature-silent`.

**Hard rules:**

- When literature is silent or limited on an effect that forums consistently report: state both facts clearly.
- **Never** claim the effect “does not exist” solely because papers are absent.
- Anecdote alone never yields **Established** or **Probable** guidance — **Speculative** practical notes only, with grain-of-salt framing.
- Single or low-signal anecdotes: mention only if relevant; low weight.

Example weighing sentence:

> Controlled literature is largely silent on X. Consistent multi-source forum reports describe Y at doses Z (**Speculative**; concordance: literature-silent). Worth noting with caution; not a basis for firm protocol advice.

### 8. Practical Guidance (evidence-graded, mechanism-mapped)

Dosing, titration, timing, duration, stacks, monitoring — only where certainty supports it.

- **Unknown = no recommendation** — state what evidence is missing.
- Each bullet tagged **Established** / **Probable** / **Speculative** / **Unknown**.
- Harm-reduction framing mandatory for AAS, SARMs, peptides, high-dose neuro, and other non-trivial risk classes.
- Never let Practical Guidance exceed the certainty of the underlying evidence.
- **Mechanism map required:** for stacks, protectives, and side-effect management, state which MoA/downstream node is being targeted (e.g. “targets thermogenesis-driven night sweats,” not just “for sleep”).

Suggested structure:

| Goal / problem | Pathway node targeted | Protocol element | Certainty |
|----------------|----------------------|------------------|-----------|
| … | … | … | … |

Also: Dosing · Timing · Duration/cycling · Stacks · Monitoring · Not recommended when

### 9. Safety, Side Effects, Contraindications & Monitoring

Frequency/severity estimates where known, absolute/relative contraindications, recommended monitoring, long-term data gaps. Required for non-trivial risk compounds at effort ≥ 2.

### 10. Interactions

PK and PD interactions; common stacks (beneficial and risky). For deep stack/protective questions, prefer full interaction mode.

### 11. History & Development

Discovery, key papers or failed programs, regulatory status, cultural/use history. (Required effort ≥ 3.)

### 12. Reputation & Comparative Context

Standing vs 2–5 alternatives on efficacy, safety, evidence quality, and practical convenience. Table preferred. Adjudicate common marketing or forum claims. (Required effort ≥ 3 when alternatives exist.)

### 13. Open Questions & What Would Change the Picture

2–5 concrete studies or data types that would most improve certainty.

### 14. Evidence Matrix + Key Sources

Structured matrix summary + highest-trust citations with trust tiers. Align with `evidence-matrix.json`.

### 15. FAQ / Common Claims

Short adjudicated answers, each with a certainty label. Prefer a table: Claim | Verdict | Certainty | Note.

---

## Closing (always)

### Guidance & Application Notice

Evidence-graded synthesis of published research and labeled experiential patterns; user assumes responsibility; **Unknown** = no recommendation; consult qualified professionals for individual medical decisions.

### References

DOI/PMID/URL for all cited sources. Label non-peer-reviewed / forum sources clearly.

---

## Anecdotal evidence quick reference

| Evidence type | Treatment | Can drive recommendation? |
|---------------|-----------|---------------------------|
| High-quality human (meta, large RCTs) | Primary | Yes → Established / Probable |
| Lower-quality human | Supporting or primary when better data absent | Yes → usually Probable / Speculative |
| Consistent multi-source anecdotal / forum consensus | **Must report and weigh** | Speculative notes only; never Established/Probable alone |
| Single / low-signal anecdotes | Low weight | No |
| Preclinical only | Mechanistic context | No practical dosing |
