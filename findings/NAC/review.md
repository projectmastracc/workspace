# Research Quality Review — 16607efb (N-Acetylcysteine)

**Role:** Research quality reviewer (DR, completeness, certainty, source integrity, schema)  
**Date:** 2026-07-29  
**Round:** 2 (re-review after revision)  
**Artifacts reviewed:** `briefing.md`, `evidence-matrix.json`, `compound.md`, `inference.md` (spot-check), prior Round 1 findings  
**Standards:** `dr-principles.md`, `guidelines-vs-literature.md`, `evidence-matrix-schema.json`, `compound-profile-template.md`  
**Effort:** 5  

---

## Verdict

### **APPROVE**

**Open critical:** 0  
**Open major:** 0  
**Open minor (non-blocking):** 2 residual notes  

Round 1 majors **M1–M3 are closed**. Auto-flags remain green. Package is gate-ready for DR delivery.

---

## Round 1 → Round 2 disposition

| ID | Issue | Round 2 status | Evidence of fix |
|----|--------|----------------|-----------------|
| **M1** | Adult OCD **Speculative–Probable** lag in compound/inference vs briefing **Speculative** | **CLOSED** | `compound.md` §4/§8/cards/summary: **Speculative** fragile adult signal; separate from SCZ Probable. `inference.md` C4 heading + scorecard **Speculative**; “time-window slices do not upgrade to Probable.” Briefing §14 “Resolved: Speculative.” Matrix C4/R4 **Speculative**. |
| **M2** | glyNAC soft “optional experiment / Speculative–Probable” | **CLOSED** | Compound §8.4 + card #5: **Speculative** biomarkers; **Unknown** healthspan/lifespan; **no recommendation** as anti-aging. Briefing §8.1 longevity row: **No recommendation** for outcome goals. Matrix R9/R10 unchanged in spirit, aligned. |
| **M3** | C14 mixed Probable under Established | **CLOSED** | Matrix split: **C14a** GSH+mucolytic **Established**; **C14b** system xc− **Probable**; **C14c** H₂S/sulfane **Speculative**. |
| m1 | Hybrid certainty labels | **Mostly closed** | No remaining Speculative–Probable in compound/briefing body (historical mention only in disagreements table). Residual: inference C6 “Probable–Speculative for live birth” (see m-R2-1). |
| m2 | overall_certainty oversimplification | **Closed enough** | `question` NOTE documents indication-dependent grades; headline Probable framed as adjunct synthesis, not global. |
| m4 | R5/R8 certainty on recommend-against | **CLOSED** | R5 **Established** (universal addiction framing not supported); R8 **Probable** (do not rely on NAC for CIN). |
| m6 | Longevity “optional experiment” phrasing | **CLOSED** | Briefing §8.1: **No recommendation** for outcome goals; experimental self-use outside evidence-graded advice. |
| m7 | Compound Source Integrity | **CLOSED** | Compound now has integrity table/blurb (OCD trust Low–Moderate for positive claims, etc.). |

---

## Auto-flag checklist (Round 2)

| Auto-flag | Status | Notes |
|-----------|--------|-------|
| Missing Practical Guidance | **PASS** | Briefing §8 + compound §8 complete |
| DIY APAP OD as home recommendation | **PASS** | Hospital-only; never DIY; educational protocols only |
| Unknown longevity recommended | **PASS** | Explicit no recommendation; glyNAC not anti-aging protocol |
| Missing Source Integrity | **PASS** | Briefing §11; compound integrity section; sources.md |
| Missing Guidelines vs Literature | **PASS** | §7 present; CIN material mismatch + recommend against |
| Invalid matrix / missing `recommendations[]` | **PASS** | R1–R18; claims intact; C14a/b/c valid |
| Certainty without labels | **PASS** | Discrete labels on claims/recs/DR cards |
| Bro-science as Established | **PASS** | Hangover/longevity/universal addiction/first-line OCD correctly contradicted/unknown/speculative |

---

## Critical findings (Round 2)

*None.*

---

## Major findings (Round 2)

*None open.*

### Spot-check confirmations

**OCD (M1):**  
- Briefing: **Speculative** (fragile); DR card #4 optional low-stakes only.  
- Compound: **Speculative**; “Do not group with SCZ as equally supported.”  
- Inference: C4 → **Speculative**; scorecard matches.  
- Matrix C4 + R4: **Speculative**; R4 states “Not a Probable recommendation.”

**glyNAC (M2):**  
- Compound card #5: recommend against proven anti-aging; no rec for outcomes.  
- Stacks: Speculative biomarkers only; experimental research label only.  
- Matrix R10: no recommendation for glyNAC as anti-aging.

**C14 (M3):**  
- C14a Established / C14b Probable / C14c Speculative — correct certainty packaging.

---

## Residual minor notes (non-blocking; optional polish)

### m-R2-1 — Inference C6 hybrid for live birth

**Where:** `inference.md` C6 heading: “**Probable–Speculative** for live birth.”

**Exact fix (optional):** “**Probable** for ovulatory/metabolic surrogates; **Speculative** for live-birth primacy.” Avoid hybrid token in the heading.

### m-R2-2 — Some matrix sources remain lineage/placeholder

**Where:** e.g. `S_NEILL_CRS`, `S_COCAINE_LINE`, `S_MICHAILIDIS_LINE`, `S_ZHOU_2024` may still lack full DOI/PMID.

**Exact fix (optional):** Attach primary DOI/PMID when re-fetching; does not change certainty grades or DR actions.

---

## DR / schema / integrity (Round 2 summary)

| Dimension | Assessment |
|-----------|------------|
| **DR actionable guidance** | Strong; Established/Probable rendered; Speculative labeled experimental; Unknown = no rec |
| **APAP boundary** | Compliant hospital-only |
| **GvL** | CIN material mismatch handled; psych non-first-line aligned |
| **Source integrity** | Berk–Dean, Zambon noise, AIS vs positive MAs, COVID overclaim all surfaced |
| **Schema** | Valid claims/recommendations/sources; C14 split resolves certainty inflation |
| **Package coherence** | Briefing ↔ compound ↔ inference ↔ matrix aligned on OCD/glyNAC/mechanisms |

---

## Final gate decision

| Gate | Result |
|------|--------|
| Critical blockers | **0** |
| Major blockers | **0** |
| Round 1 M1–M3 | **All closed** |
| **Verdict** | **approve** |

Optional minors m-R2-1/m-R2-2 may be cleaned in a polish pass; they do not reopen the gate.

---

*End of Round 2 review — RESEARCH_ID 16607efb*
