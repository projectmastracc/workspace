# Research Quality Review — e62f5f0a (YK11)

**Reviewer role:** Research quality gate (DR compliance, completeness, certainty calibration, source integrity, schema validity)  
**Artifacts reviewed:** `briefing.md`, `evidence-matrix.json`, section files under `/tmp/grok-research-e62f5f0a/`, DR principles, guidelines-vs-literature, evidence-matrix schema, compound-profile template  
**Verdict: PASS** (no critical or major blockers; optional minor nits only)

---

## Critical issues (must fix)

**None.**

- **DR / Unknown dosing:** Community ranges (5–15 mg/day, 4–8 weeks) appear only as bro-science / **Unknown**, with explicit **do not recommend a dose** (Exec Summary; §16.1; R4; bottom line). No Unknown-certainty protocol presented as actionable.
- **Myostatin grading:** Correctly framed as **AR-dependent Fst induction** (indirect pathway), not direct MSTN/ActRII antagonist (C7 **Unknown**/unsupported; C8 **Probable** cells only; §6.2; Competing Interpretations A; R1–R2).
- **No invented human trials:** Zero RCTs/PK/efficacy stated consistently; human performance **Unknown**.
- **Schema / matrix:** Valid structure with required top-level fields, non-empty `claims[]`, `sources[]`, `recommendations[]` (R1–R12), and `bro_science_claims[]` with allowed verdicts.

---

## Major issues

**None.**

Checks that would have been major if failed:

| Check | Result |
|-------|--------|
| Practical Guidance present (compound) | **Pass** — full §16 (dosing/timing/stacks/monitoring/harm reduction/not recommended/action tags) |
| Guidelines vs Literature present | **Pass** — §12 table (WADA, Health Canada, FDA, no CPG, PED marketing) with alignment + DR action |
| Source Integrity with funding/COI | **Pass** — §9 table + bias narrative (single-lab capture; MEXT/NRF; declared no COI where known) |
| Certainty labels on substantive claims | **Pass** — tables and narrative consistently tagged |
| Harm reduction for performance compound | **Pass** — bloodwork, stop criteria, HPG/PCT caveats, sport ban, source adulteration |
| Guidance & Application notice | **Pass** — §20 |

---

## Minor issues (optional polish; not required for PASS)

1. **Formatting glitch in Compound Context Summary (§17):**  
   `**No evidence-based human dose can be recommended (**Unknown**)**.`  
   Nested bold/parentheses render awkwardly. Prefer:  
   `No evidence-based human dose can be recommended (**Unknown**).`

2. **Orphan pipeline cite:** §5 item 3 mentions “Kanno 2022 cited in pipeline” but that paper is not in §21 References or matrix `sources[]`. Either drop the clause or add a full citation if used.

3. **Bro-science stack row certainty inconsistency (nit):** §15 table says stacks verdict “**Unknown** / potential antagonism” while matrix `bro_science_claims` uses verdict `"speculative"` and C14 is **Speculative** clinically / **Probable** in vitro. Align wording to **Speculative** (clinical stack benefit) + **Probable** (mechanistic N/C risk) to match R9/C14.

4. **Incomplete funding/COI on secondary sources (already disclosed, still a polish target):** Matrix S5 (Park), S7 (Dahleh 2023), S8 (Wang), S11 funding “not restated” — acceptable with explicit incompleteness flags; if a revision pass touches sources, fill DOI for Piper (S12) and Park funding/COI if available.

5. **Monitoring schedule certainty:** §16.4 intervals (~2–4 weeks) are class-inferred harm reduction (**Probable** prudence). Already framed as exposure contingency, not efficacy protocol — optional one-line reminder that intervals are **not** YK11-validated.

6. **FDA row in §12** is thinner than WADA/Health Canada (no year-specific advisory). Fine for alignment; optional: mirror one concrete FDA SARM product action URL already in References #12.

7. **Matrix vs briefing coverage:** S12 (Piper metabolism) is in matrix/sources but lightly used in briefing (PK table only). Optional: one sentence that metabolites support doping control, not therapeutic PK.

---

## What is good

- **DR discipline exemplary:** Recommend-against language for direct-MSTN and “safer gene-selective” marketing; **Unknown = no dose**; harm reduction without endorsement banner.
- **Mechanism adjudication is the right steelman + cut:** Fst as endogenous MSTN/activin antagonist acknowledged; primary identity still AR partial agonist / gene-selective candidate; Lee 2021 title treated as framing compression.
- **Gene ≠ tissue selectivity** held at every layer (Exec, claims C3/C4, Competing B, R3).
- **Source integrity** names single-lab concentration, n=3/multiplicity issues, abstract-only limits, and commercial free-rider hype — matches epistemic standards.
- **Guidelines vs literature** correctly supports regulatory non-authorization/ban; **fundamental** mismatch for forum protocols.
- **Evidence matrix** maps cleanly to briefing claims; recommendations cover dosing, timing, stack, monitoring, harm_reduction, contraindication, general; bro_science verdicts use allowed enums.
- **Compound template coverage:** Identity → lenses → MoA → effects → risks → bro-science → guidelines → practical guidance → summary → notice → references — complete.
- **No overclaim of human data** anywhere in the acquisition narrative.

---

## Required revision instructions for synthesizer

**None required for gate pass.**

Optional (if synthesizer already open for a polish pass):

- Fix §17 nested-markdown on Unknown dose sentence.
- Remove or fully cite “Kanno 2022” pipeline mention.
- Align §15 stack-row certainty language with C14/R9 (**Speculative** clinical / **Probable** in vitro N/C).
- (Optional) Complete Piper DOI and secondary COI/funding fields in matrix.

---

## Checklist summary

| Criterion | Status |
|-----------|--------|
| 1. DR: no Unknown dose as actionable | **Pass** |
| 2. Myostatin = indirect Fst, not direct inhibitor | **Pass** |
| 3. Source Integrity with funding/COI | **Pass** |
| 4. Practical Guidance present | **Pass** |
| 5. Guidelines vs Literature present | **Pass** |
| 6. Matrix valid JSON + recommendations[] + bro_science_claims[] | **Pass** |
| 7. Certainty labels on substantive claims | **Pass** |
| 8. No invented human trials | **Pass** |

**Gate decision:** **PASS with only optional nits.** Ship-ready for DR-compliant compound briefing on YK11 MoA / AR selectivity / myostatin claims.
