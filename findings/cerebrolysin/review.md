# Research Quality Review — Cerebrolysin (b150373f)

**Reviewer role:** Research quality gate (DR, completeness, certainty, source integrity, schema)  
**Date:** 2026-07-29  

---

## Round 2 (re-review after synthesizer revision)

**Artifacts re-read:** `briefing.md`, `evidence-matrix.json`, prior Round 1 issues in this file.  
**Verdict: approve**

| Gate | Round 1 | Round 2 |
|------|---------|---------|
| Critical | 0 | **0 open** |
| Major | 3 | **0 open** |
| Minor | 9 | **0–1 cosmetic residual** (non-blocking) |

---

## Major issue closure (M1–M3)

| ID | Round 1 issue | Round 2 verification | Status |
|----|---------------|----------------------|--------|
| **M1** | C3 Speculative in matrix vs Probable in narrative | Matrix C3 = **Speculative** (grade Low); funding_notes state FINAL ADJUDICATION Option A. Briefing §4.1 row “**C3 final**” = **Speculative**. §10 disagreements integrate to Speculative only. Early NIHSS separately Probable. | **Closed** |
| **M2** | R1 “especially moderate–severe” as Probable day-90 | R1 statement: Probable attaches to **early NIHSS** adjunct only; explicitly “Unselected day-90 mRS … Unknown; moderate–severe day-90 enrichment is Speculative … must not drive a Probable day-90 protocol claim.” `inference_note` ties R1 Probable to C1, not C3. No “especially moderate–severe” protocol language. | **Closed** |
| **M3** | Regimen map / summary over-sold severity | §9.7 #1: early recovery **Probable**; unselected day-90 **Unknown**; moderate–severe enrichment **Speculative** (counseling only). §11 summary aligned. §9.2 dosing table labels C3 Speculative. Guidelines §7 mismatch summary aligned. | **Closed** |

**Consistency spot-check:** No remaining “especially moderate,” “preferably moderate,” “Unknown–Speculative,” or “Speculative–Probable” primary hybrids in `briefing.md` for C3. Hybrid-style phrasing reduced to primary label + parenthetical (“bordering Speculative” for AD durability only — acceptable).

---

## Minor issue closure (m1–m9)

| ID | Issue | Round 2 | Status |
|----|-------|---------|--------|
| m1 | Hybrid certainty primary labels | C2/C3 use single primary labels; residual “bordering Speculative” is secondary gloss | **Closed** |
| m2 | Missing C4, C12–C14 in matrix | C4, C12, C13, C14 present with supporting/contradicting | **Closed** |
| m3 | Jarosz / CEREHETIS / Staszewski not in matrix sources | S16 Jarosz; S17/S18 reperfusion sources wired to C4/C5 | **Closed** |
| m4 | AHA PMID inconsistency | S8 + briefing refs + §7 table use **PMID 30869305**; note documents 31390963 secondary cite | **Closed** |
| m5 | C15 Unknown/High false-claim form | C15 inverted true fact; certainty **Established**, grade High | **Closed** |
| m6 | R5 category `contraindication` | R5 category **general** | **Closed** |
| m7 | R5 wording as hard forbid | R5: “No recommendation … evidence absent (Unknown)” | **Closed** |
| m8 | Template section order | Optional; Source Integrity §8 retained (DR-positive) | **Closed (waived)** |
| m9 | CAPTAIN I under-represented | S19 Poon; C5 contradicting notes CAPTAIN I ITT miss; R2 source_ids include S19 | **Closed** |

---

## Residual minor / cosmetic (non-blocking)

1. **Inference.md not re-synced in this re-read** — Round 1 noted inference C3 as Probable; briefing §10 now records prior inference and **final Option A Speculative**. If `inference.md` still shows C3 Probable as current (not historical), optional clean-up for archive hygiene only — **does not block approve** if matrix + briefing are source of truth for delivery.
2. **C13 Probable for combo vs donepezil** remains thin (limited industry-linked RCTs); already grade Low + COI notes — acceptable, not a new major.

---

## Auto-flag checklist (Round 2)

| Criterion | Result |
|-----------|--------|
| Practical Guidance | Pass (§9) |
| Unknown dose as Established | Pass |
| Parenteral harm reduction | Pass |
| Source Integrity / EVER | Pass (§8) |
| Guidelines vs Literature (AHA/Cochrane) | Pass (§7) |
| Matrix `recommendations[]` | Pass (R1–R11) |
| Invented citations | No new flags |
| Bro-science as Established | Pass |
| Certainty calibration (C3/R1) | **Pass** |

---

## Schema / DR snapshot

- Required matrix fields present; C3/R1 certainty enums valid.
- DR: Unknown → no recommendation (prevention); Probable early-NIHSS adjunct with explicit day-90 ceilings; EVER dual-cite retained.
- Harm reduction: DIY against, label CIs, monitoring intact.

---

## Summary judgment

**Approve.** All three Round 1 majors (C3 sync, R1 early-NIHSS-only Probable, regimen map alignment) are fixed in both `evidence-matrix.json` and `briefing.md`. Minors m1–m9 closed or waived. Optional residual: archive-sync `inference.md` if still stale on C3.

---

## Round 1 archive (superseded)

> Prior verdict: **needs revision** (0 critical · 3 major · 9 minor).  
> Blockers were C3 cross-artifact contradiction, R1 over-weighting Speculative severity as Probable, and Practical Guidance outrunning matrix.  
> Full Round 1 detail preserved conceptually above as closed rows; do not re-open without new evidence.

*End of review (Round 2 approve).*
