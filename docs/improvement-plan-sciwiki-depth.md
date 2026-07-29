# Research Analyst — Improvement Plan for scientificsean.wiki–Level Analysis Depth

**projectmastracc / workspace**  
Generated 2026-07-29 · Revised same day with user feedback  
Status: **Implemented** — Phase 5 shipped 2026-07-29 (v1.1)

A detailed architectural and content roadmap to elevate the multi-agent research skill into a system capable of producing complete, layered, evidence-weighted compound monographs and multi-compound pathway analyses comparable in depth and utility to high-quality entries on scientificsean.wiki, while remaining useful for gym/forum/performance contexts that rely heavily on quality anecdotal evidence.

---

## Table of Contents

1. [Introduction & Strategic Framing](#1-introduction--strategic-framing)
2. [Clarify “DR” and the Role of Anecdotal Evidence](#2-clarify-dr-and-the-role-of-anecdotal-evidence)
3. [Multi-Compound & Pathway Interaction Analyses](#3-multi-compound--pathway-interaction-analyses)
4. [Redesign the Compound Profile Template](#4-redesign-the-compound-profile-template)
5. [Strengthen and Expand Personas](#5-strengthen-and-expand-personas)
6. [Output and Presentation Upgrades](#6-output-and-presentation-upgrades)
7. [Evidence Breadth and Labeling Discipline](#7-evidence-breadth-and-labeling-discipline)
8. [Persistent Knowledge Layer](#8-persistent-knowledge-layer)
9. [Effort Scaling and Golden Examples](#9-effort-scaling-and-golden-examples)
10. [Style and Epistemic Polish](#10-style-and-epistemic-polish)
11. [Repo-Level Improvements](#11-repo-level-improvements)
12. [Implementation Priority & Roadmap](#12-implementation-priority--roadmap)
13. [File-Level Change Checklist](#13-file-level-change-checklist)
14. [Verification Criteria for Sci-Wiki Depth](#14-verification-criteria-for-sci-wiki-depth)

---

## 1. Introduction & Strategic Framing

The Research Analyst skill already possesses a rare combination of strengths: parallel specialist personas, explicit certainty labels (Established / Probable / Speculative / Unknown), rigorous source/funding/methodology scrutiny, and a quality gate. These elements give it higher epistemic integrity than the large majority of public compound resources.

scientificsean.wiki (the Sci-Wiki) achieves a different but complementary excellence. Its compound pages are modular, multi-dimensional monographs. They routinely cover mechanism, history, safety, subjective profile (explicitly “weighing the evidence above”), practical use, research landscape, and sourcing. The writing is accessible without being dumbed down. The result feels like a living reference entry rather than a research report.

**Critical user feedback that must shape this plan:**

- The current “DR / Do Research / Do Render” framing is confusing in practice.
- Gymbro / forum / performance applications are a primary use case. Quality anecdotal evidence (especially consistent, multi-source forum patterns) must be given a real seat at the table — not dismissed just because controlled literature is silent or negative.
- Example failure mode: the system being adamant that cerebrolysin has no skin youth / anti-ageing effects when anecdotal reports and forum consensus clearly indicate benefits to an extent. The correct posture is “literature is largely silent or limited; consistent anecdotal reports exist and should be weighed with appropriate caution.”
- Users need the ability to run complex multi-compound queries such as:  
  `/research evaluation of cerebrolysin as a preventative measure against the negative effects of trenbolone`  
  and receive a pathway-level interaction analysis, not a blanket “literature says don’t use either.”

The goal of this plan is therefore threefold:

1. Keep (and clarify) the strong epistemic standards.
2. Give quality anecdotal / forum evidence proper, labeled weight.
3. Explicitly support multi-compound pathway, protective, and interaction analyses so the skill is useful for real performance and harm-reduction questions.

---

## 2. Clarify “DR” and the Role of Anecdotal Evidence

### 2.1 The Terminology Problem

“DR — Do Render” (and any “Do Research” phrasing) is currently opaque. Users and even the system itself can misread the intent. The underlying principle is sound: when the evidence supports practical guidance, render it with a certainty label; when it does not, say so clearly and do not invent protocols.

**Recommended change:**

- Keep the certainty labels (Established / Probable / Speculative / Unknown) — these are excellent.
- Soften or replace the “DR / Do Render” branding in user-facing language with clearer phrasing such as:
  - “Evidence-graded practical guidance”
  - “What the evidence supports (and what it does not)”
  - “Actionable synthesis with certainty labels”
- Internally the system can still use a short principle name if useful, but the user-facing output and skill description should speak in plain language.

Update `AGENTS.md`, the agent description, SKILL.md, and all persona instructions so that the first thing a reader sees is the clarity of the certainty system, not an opaque acronym.

### 2.2 Quality Anecdotal Evidence Must Be First-Class (with Caveats)

The system currently risks being overly literature-purist. In performance pharmacology, nootropics, peptides, and many gym contexts, controlled human data are often sparse, while consistent multi-source anecdotal patterns exist and are practically informative.

**New stance (to be written into DR principles, style guide, and personas):**

| Evidence type | How it is treated | Can it drive a recommendation? |
|---------------|-------------------|--------------------------------|
| High-quality human (meta, large RCTs) | Primary | Yes → Established / Probable |
| Lower-quality human | Supporting or primary when better data absent | Yes → usually Probable / Speculative |
| Consistent, multi-source anecdotal / forum consensus | **First-class input that must be reported and weighed** | Can support **Speculative** practical notes; never Established or Probable by itself |
| Single or low-signal anecdotes | Mentioned only if relevant; low weight | No |
| Preclinical only | Mechanistic context | No practical dosing recommendations |

**Key rules:**

- When literature is silent or limited on an effect that forums consistently report (e.g. cerebrolysin skin quality / anti-ageing appearance), the system **must**:
  1. State that controlled literature is limited or silent.
  2. Accurately summarize the anecdotal pattern (what is reported, by how many independent sources, consistency, dose ranges if mentioned).
  3. Weigh the two: “Literature does not confirm this; consistent anecdotal reports exist and are worth noting with appropriate caution.”
  4. Never be adamant that the effect “does not exist” solely because papers are absent.
- Anecdotal evidence is always labeled as such and carries an automatic “grain of salt” framing.
- The Subjective / Experiential Profile section (see template) is the primary home for this weighing.

This change makes the skill far more useful for the actual audience while remaining honest.

---

## 3. Multi-Compound & Pathway Interaction Analyses

### 3.1 The Required Capability

Users need to ask questions of the form:

```
/research evaluation of cerebrolysin as a preventative measure against the negative effects of trenbolone
/research does telmisartan meaningfully mitigate the blood-pressure and lipid effects of high-dose testosterone
/research mechanistic overlap and stacking rationale for compound A + compound B
```

The system must **not** default to “literature does not support combining them” or “avoid both.” It must:

1. Map the relevant pathways / mechanisms of each compound.
2. Identify points of potential interaction, protection, synergy, or antagonism (receptor, downstream signaling, organ-system, metabolic).
3. Separate what is established in literature from what is mechanistically plausible from what is purely speculative or anecdotal.
4. Deliver a structured evaluation of the proposed protective / stacking hypothesis with certainty labels.
5. Still surface real risks and unknowns clearly.

### 3.2 New Analysis Mode: Interaction / Protective / Pathway Evaluation

When the input classifier detects a multi-compound or “against the effects of / mitigate / protect / stack with” query, the orchestrator should:

- Treat it as a special input type: `interaction` or `pathway_evaluation`.
- Spawn (or instruct) personas to cover both compounds plus the interaction surface.
- Produce a dedicated output structure (see template additions below) rather than two independent monographs.

### 3.3 Required Output Sections for Interaction Queries

In addition to (or instead of) a full single-compound monograph, interaction analyses should contain:

1. **Executive verdict** on the proposed protective / stacking hypothesis (with overall certainty).
2. **Pathway map of Compound A** (the potential problem compound — e.g. trenbolone negative effects).
3. **Pathway map of Compound B** (the candidate mitigator — e.g. cerebrolysin).
4. **Points of potential interaction / protection** — mechanistic overlap, downstream consequences, organ systems involved.
5. **What controlled literature actually says** about the combination or about each relevant pathway.
6. **What consistent anecdotal / forum patterns report** about the combination or about B mitigating A’s side effects.
7. **Weighing** — concordance between literature, mechanism, and anecdote.
8. **Practical implications** (if any evidence-graded guidance is warranted) + monitoring.
9. **Key risks and unknowns**.
10. **Open questions** that would most improve certainty.

This structure forces the system to do real pathway-level reasoning instead of literature-lookup refusal.

---

## 4. Redesign the Compound Profile Template

This remains the highest-leverage single-compound change. Expanding the canonical profile forces every high-effort run to address the same dimensions that make Sci-Wiki pages feel comprehensive, while the new interaction mode (Section 3) handles multi-compound questions.

### 4.1 Recommended Canonical Section Set (Single Compound)

Update `references/compound-profile-template.md` and the compound-framer persona so that the final briefing must contain the following sections in order.

#### 1. Bottom-line / Overview
4–8 sentences. Overall certainty for the primary use case, key practical takeaway, critical safety or evidence caveats. Must be accurate and self-contained.

#### 2. Chemistry & Classification
Class, key structural features if relevant, solubility/stability notes, close analogs.

#### 3. Mechanism of Action
Receptor / enzyme / pathway detail. Distinguish established actions from downstream hypotheses. Connect molecular action to claimed physiological or subjective effects where possible.

#### 4. Pharmacokinetics
Absorption, half-life, metabolism, CNS penetration, food effects. Flag sparse human PK data.

#### 5. Human Evidence
Stratified by design quality. Effect sizes, populations, limitations. Explicitly state what the data do *not* show.

#### 6. Preclinical / Mechanistic Support
Always labeled with translation risk.

#### 7. Subjective / Experiential Profile (weighing the evidence)
**Critical section.** Synthesize consistent forum / user-report patterns, then explicitly weigh them against controlled evidence. Rate concordance (strong / partial / weak / contradictory / literature-silent).  
When literature is silent on an effect that anecdotes consistently report, state both facts clearly and do not claim the effect “does not exist.”

#### 8. Practical Guidance (evidence-graded)
Dosing, titration, timing, duration, stacks, monitoring — only where certainty supports it. Unknown = no recommendation. Harm-reduction framing for higher-risk classes.

#### 9. Safety, Side Effects, Contraindications & Monitoring
Frequency/severity estimates, absolute/relative contraindications, recommended monitoring, long-term data gaps.

#### 10. Interactions
PK and PD interactions, common stacks (beneficial and risky).

#### 11. History & Development
Discovery, key papers or failed programs, regulatory status, cultural/use history.

#### 12. Reputation & Comparative Context
Standing vs alternatives; adjudication of common marketing or forum claims.

#### 13. Open Questions & What Would Change the Picture
2–5 concrete studies or data types that would most improve certainty.

#### 14. Evidence Matrix + Key Sources
Structured matrix + highest-trust citations with trust tiers.

#### 15. FAQ / Common Claims
Short adjudicated answers, each with a certainty label.

### 4.2 Interaction / Pathway Template Additions

When the query is classified as multi-compound or protective/mitigation, use the structure defined in Section 3.3. The compound-framer (or a dedicated interaction persona) owns this outline.

### 4.3 Template File Changes

- Rewrite `references/compound-profile-template.md` with the full single-compound outline + explicit guidance on anecdotal weighing.
- Add `references/interaction-profile-template.md` (or a major section in the same file) for pathway/protective analyses.
- Update the evidence-matrix schema with fields for `subjective_concordance`, `anecdotal_patterns`, `comparative_alternatives`, and (for interaction mode) `pathway_overlap` / `protective_hypothesis_certainty`.

---

## 5. Strengthen and Expand Personas

### 5.1 Compound-Framer Enhancements

Update `.grok/personas/compound-framer.toml` to:

- Own the full 15-section outline and refuse to omit required sections at effort ≥ 3.
- Generate the Subjective / Experiential Profile with explicit weighing language and a concordance rating.
- When literature is silent on a consistently reported anecdotal effect, surface both sides and avoid adamant negation.
- Produce comparative tables when alternatives exist.
- Ensure Practical Guidance never exceeds the certainty of the underlying evidence.
- For interaction queries, switch to (or collaborate on) the pathway/protective structure.

### 5.2 New or Expanded Roles

**Subjective-Effects / Experiential Analyst** (new persona or major expansion of inference-analyst)  
- Collect and pattern-match consistent multi-source user-report themes.  
- Map each theme onto controlled evidence.  
- Output a structured concordance table.  
- Explicit instruction: never elevate pure anecdote to Established or Probable; never dismiss consistent multi-source patterns solely because literature is silent.

**Pathway / Interaction Analyst** (new or mode of existing personas at effort ≥ 3 for multi-compound queries)  
- Map mechanisms of both compounds.  
- Identify plausible points of protection, synergy, or antagonism.  
- Separate literature-supported interactions from mechanistically plausible from purely speculative.  
- Produce the interaction-specific output sections.

**Comparative Pharmacologist**  
- Position the target against 2–5 alternatives on efficacy, safety, evidence quality, and practical convenience.

**Safety & Toxicology Lens**  
- Mandatory for AAS / SARM / peptide / high-dose neuro classes at effort ≥ 2. Surfaces rare risks, monitoring, contraindications.

### 5.3 Quality Reviewer Updates

Expanded checklist that blocks delivery if:

- Required monograph (or interaction) sections are missing at the declared effort.
- Every practical recommendation lacks a certainty label.
- Subjective profile lacks an explicit weighing statement and concordance rating.
- Consistent anecdotal patterns on a literature-silent effect are simply ignored or adamantly denied.
- Unknown claims are presented as actionable guidance.
- Safety/monitoring section is absent for non-trivial risk compounds.
- Interaction queries lack pathway-level analysis and instead give only a literature-refusal summary.

---

## 6. Output and Presentation Upgrades

### 6.1 Briefing.md as Wiki-Ready Markdown

Clean ATX headings matching the template, short paragraphs, tables for dosing and comparisons, consistent certainty badges (**Established**, **Probable**, **Speculative**, **Unknown**). Prefer active voice and concrete numbers.

### 6.2 Dual Output: Executive Card + Full Analysis

Every briefing opens with a compact Executive Card (compound/class or interaction hypothesis, overall certainty, one-sentence verdict, key practical note, top sources / caveats). Full analysis follows.

### 6.3 Flags and Export Options

- `--wiki` / `--monograph` — force full structure and accessible prose.
- `--export md|html|json` — additional artifacts.
- `--save PATH` — copies Executive Card + full analysis + matrix.

### 6.4 Schema Extensions

Add to `evidence-matrix-schema.json`:

- `subjective_concordance`
- `anecdotal_patterns` (array of {theme, consistency, sources_note, concordance})
- `comparative_alternatives`
- `pathway_overlap` / `protective_hypothesis` (for interaction mode)
- `executive_verdict`
- `monitoring_protocol`

---

## 7. Evidence Breadth and Labeling Discipline

### 7.1 Mandatory Evidence Strata (updated)

| Stratum | Treatment | Can drive recommendation? |
|---------|-----------|---------------------------|
| High-quality human | Primary | Yes → Established / Probable |
| Lower-quality human | Supporting or primary when better data absent | Yes → usually Probable / Speculative |
| **Consistent multi-source anecdotal / forum consensus** | **Must be reported and weighed** | Supports Speculative notes only; never Established/Probable alone |
| Single / low-signal anecdotes | Low weight; mention only if relevant | No |
| Preclinical | Mechanistic context only | No practical dosing advice |
| Mechanistic inference | Labeled as such | Supports Speculative reasoning in interaction analyses |

### 7.2 Search Playbook Updates

Expand `references/literature-search.md`:

- Prefer systematic reviews and large RCTs as anchors.
- Actively seek failed trials and negative results.
- For compounds or effects with heavy forum discussion, deliberately sample high-signal anecdotal sources and force the weighing step.
- For interaction queries, search both individual compounds *and* combination / mitigation terms.
- Capture regulatory documents when they exist.
- Record search strategy and date range in `intake.md`.

### 7.3 Hard Rules (clarified)

- Unknown = no firm recommendation.
- Consistent anecdotal patterns on literature-silent effects are reported and weighed; they are never treated as proof, nor are they erased.
- Preclinical data alone never produce dosing advice.
- Guideline-vs-literature mismatches are surfaced with severity and a clear recommendation.
- Interaction / protective hypotheses are evaluated at the pathway level; blanket refusal is not an acceptable substitute for analysis.

---

## 8. Persistent Knowledge Layer

### 8.1 Compound Knowledge Store

Successful high-effort runs write or update:

```
knowledge/compounds/<slug>/profile.md
knowledge/compounds/<slug>/matrix.json
knowledge/compounds/<slug>/meta.json
```

Subsequent runs load the prior profile and perform differential updates.

### 8.2 Interaction Knowledge

Interaction analyses can be stored under:

```
knowledge/interactions/<slug-a>_vs_<slug-b>/...
```

or linked from both compound profiles.

### 8.3 Cross-Linking and Taxonomy

Maintain a lightweight index of compounds, classes, and known interactions. `compound-taxonomy.md` seeds this index.

### 8.4 Workspace Isolation

Continue workspace-id hashing. Knowledge stays local unless explicitly exported.

---

## 9. Effort Scaling and Golden Examples

### 9.1 Effort Tier Definitions (revised)

| Effort | Target Depth | Minimum Content | Typical Use |
|--------|--------------|-----------------|-------------|
| **1** | Fast focused answer | Overview + Practical Guidance + Safety + Key Sources | Simple factual or dosing queries |
| **2** (default) | Standard multi-perspective | Core sections + evidence matrix + quality gate + anecdotal weighing | Most everyday questions |
| **3** | Full monograph or full interaction analysis | All required sections, comparative or pathway analysis, explicit anecdotal weighing | Important, contested, or multi-compound questions |
| **4–5** | Maximum rigor + extended literature + deeper pathway work | Full structure + extra sources + multiple alternatives or detailed mechanism maps | High-stakes or complex protective hypotheses |

### 9.2 Golden Example Library

Commit high-effort examples that stress the new requirements:

- Creatine monohydrate — clean high-evidence performance compound.
- A mixed-evidence nootropic (racetam or Bacopa) — tests anecdotal weighing.
- Ketamine / esketamine for depression — guideline-vs-literature + safety.
- A widely used AAS or SARM — harm-reduction + endocrine monitoring.
- **Cerebrolysin skin / anti-ageing claims** — literature-silent + strong anecdotal pattern (explicit test of the new anecdotal rules).
- **Cerebrolysin as potential mitigator of trenbolone negative effects** (or similar) — full pathway / protective analysis (explicit test of multi-compound mode).

Each golden example includes `briefing.md`, `matrix.json`, and a short note on why it is a quality target.

---

## 10. Style and Epistemic Polish

### 10.1 Prose Guidelines (new `references/style-guide.md`)

- Short paragraphs (3–5 sentences).
- Active voice and concrete numbers.
- Certainty labels inline and consistent on every substantive claim and recommendation.
- Subjective sections always contain an explicit weighing sentence.
- When literature is silent and anecdotes are consistent: state both facts; do not claim the effect does not exist.
- Avoid academic stiffness and forum casualness; aim for precise, calm, educational tone.
- Never use “may / might / could” to disguise an Unknown.

### 10.2 Epistemic Non-Negotiables (reaffirmed and extended)

- Unknown = no firm recommendation.
- Every practical recommendation carries a certainty label and source trail.
- Consistent multi-source anecdotal patterns are reported and weighed; they never alone produce Established or Probable guidance.
- Guidelines are not immune.
- Preclinical data alone never produce dosing advice.
- Interaction hypotheses receive pathway-level analysis; literature silence is not treated as disproof of a mechanistically plausible protective effect.
- Funding, COI, and design limitations are surfaced for key claims.
- Steelmanning of opposing views is required for contested claims.

---

## 11. Repo-Level Improvements

- Add `LICENSE` (MIT recommended).
- GitHub description + topics.
- Visible `docs/` layout with this plan and golden examples.
- Short extension notes in `AGENTS.md` or `CONTRIBUTING.md`.
- Lightweight evaluation harness that checks structural completeness, presence of weighing language, and proper handling of literature-silent + anecdotal cases.

---

## 12. Implementation Priority & Roadmap

### Phase A — Immediate Depth + Anecdotal Fix (highest priority)

- Clarify / soften “DR” language across AGENTS.md, SKILL.md, and personas.
- Rewrite compound-profile-template.md with full 15-section outline **and** explicit anecdotal-weighing rules (including the “literature silent ≠ effect does not exist” posture).
- Update compound-framer and quality-reviewer for the new subjective rules.
- Add style-guide.md.
- Adjust output template for Executive Card + clean headings.

### Phase B — Multi-Compound / Pathway Mode

- Add input classifier support for interaction / protective / mitigation queries.
- Create interaction-profile-template.md (or section).
- Add or expand Pathway / Interaction Analyst instructions.
- Update quality reviewer to reject pure literature-refusal answers on interaction queries.
- Produce the cerebrolysin-vs-trenbolone-style golden example.

### Phase C — Evidence & Subjective Layer Hardening

- Expand literature-search.md for stratified + anecdotal-aware search.
- Schema fields for anecdotal_patterns and pathway_overlap.
- Additional golden examples that stress literature-silent + strong anecdote cases.

### Phase D — Knowledge Persistence + Packaging

- `knowledge/compounds/` and interaction storage.
- Differential update logic in SKILL.md.
- LICENSE, examples committed, evaluation checklist.

---

## 13. File-Level Change Checklist

| Action | Path | Purpose |
|--------|------|---------|
| **CREATE** | `docs/improvement-plan-sciwiki-depth.md` | This document (v1.1) |
| **CREATE** | `.grok/skills/.../references/style-guide.md` | Prose + anecdotal weighing rules |
| **REWRITE** | `.grok/skills/.../references/compound-profile-template.md` | 15-section outline + anecdotal rules |
| **CREATE** | `.grok/skills/.../references/interaction-profile-template.md` | Pathway / protective analysis structure |
| **EDIT** | `.grok/personas/compound-framer.toml` | Outline enforcement + anecdotal + interaction handling |
| **EDIT** | `.grok/personas/research-quality-reviewer.toml` | Expanded checklist (incl. anecdotal & interaction) |
| **EDIT** | `.grok/personas/inference-analyst.toml` | Subjective concordance + pathway duties |
| **EDIT** | `.grok/skills/.../references/literature-search.md` | Stratified + anecdotal-aware + interaction search |
| **EDIT** | `.grok/skills/.../references/evidence-matrix-schema.json` | New fields (anecdotal_patterns, pathway_overlap, etc.) |
| **EDIT** | `.grok/skills/.../references/output-template.md` | Executive Card + clean headings |
| **EDIT** | `.grok/skills/research-analyst/SKILL.md` | Effort definitions, interaction mode, knowledge hooks, clearer language |
| **EDIT** | `AGENTS.md` | Clarify DR language; reaffirm extended epistemic rules |
| **EDIT** | `.grok/skills/.../references/dr-principles.md` | Soften branding; add anecdotal-first-class rules |
| **CREATE** | `knowledge/compounds/.gitkeep` | Persistent profiles |
| **CREATE** | Golden examples (incl. cerebrolysin anecdotal + cerebrolysin/tren interaction) | Style & regression anchors |
| **CREATE** | `LICENSE` | MIT or chosen license |
| **EDIT** | `.grok/plans/research-analyst.md` | Mark Phase 5 and link here |

---

## 14. Verification Criteria for Sci-Wiki Depth

A run reaches the target when the following pass.

### Structural Checks

- All required sections present for the query type (single-compound monograph or interaction analysis).
- Executive Card at the top.
- Clean ATX headings.
- Tables for dosing / comparisons / pathway points where relevant.

### Epistemic & Anecdotal Checks

- Every practical recommendation has an inline certainty label.
- No firm recommendation under Unknown.
- Subjective Profile contains explicit weighing and concordance rating.
- When literature is silent/limited and consistent anecdotal patterns exist, **both** are stated; the system does not adamantly claim the effect does not exist.
- Interaction / protective queries receive pathway-level analysis, not a literature-refusal summary.
- Key claims cite sources with trust tiers.
- Safety/monitoring present for non-trivial risk.

### Utility Checks

- Reader can extract usable practical notes (or a clear “insufficient evidence for recommendation”) quickly.
- Reader can see how forum reports relate to controlled evidence without reading the entire document.
- Complex multi-compound questions produce mechanistic interaction reasoning.
- Saved artifacts support later differential updates.

---

This revision directly addresses the observed failure modes (over-adamant literature-purism on cerebrolysin-style claims, confusing DR framing, and lack of pathway-level multi-compound analysis). Phase A + Phase B together should make the skill substantially more useful for the gym/forum/performance audience while preserving the epistemic discipline that makes it trustworthy.

**Document version:** 1.1  
**Target skill:** Research Analyst (`/research`)  
**Alignment goal:** scientificsean.wiki monograph depth + honest handling of quality anecdotal evidence + multi-compound pathway evaluation capability.
