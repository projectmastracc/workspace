# Research Briefing Output Template

Every `briefing.md` must open with an **Executive Card**, then follow the template for the input type.

| Input type | Template |
|------------|----------|
| `compound` | `compound-profile-template.md` (15-section monograph) |
| `interaction` | `interaction-profile-template.md` (pathway / protective / stack) |
| `claim` / `paper` / `topic` / `question` | This file (general research briefing) |

Style: `style-guide.md`. Principles: `dr-principles.md`.

---

## Executive Card (always first — all input types)

| Field | Content |
|-------|---------|
| **Subject** | Compound, claim, paper, topic, or interaction hypothesis |
| **Overall certainty** | Established / Probable / Speculative / Unknown |
| **Verdict** | One sentence |
| **Key practical note** | Actionable highlight or “insufficient evidence for recommendation” |
| **Top caveats** | 1–3 bullets (safety, funding, gaps) |

---

## General research briefing (non-compound, non-interaction)

### 1. Bottom-line / Overview

≤200 words. What does the evidence support? Actionable bottom line when guidance was requested.

### 2. Question Under Analysis

Precise statement of the claim, topic, or paper being analyzed.

### 3. What Research Truly Says

Plain-language synthesis bounded by data. Certainty labels on each bullet.

### 4. Source Integrity

Funding, COI, peer-review status, trust tiers for pivotal sources. Table format encouraged.

### 5. Methods & Evidence Quality

Design appraisal, bias table, statistical adequacy, external validity.

### 6. Competing Interpretations

Steelmanned cases for and against (contested topics). Equal rigor both sides.

### 7. Guidelines vs Literature

(When health-adjacent or guideline-relevant.) Guideline | recommendation | literature alignment | mismatch explanation | recommendation if mismatch.

### 8. Subjective / Experiential Patterns

(When forums or user reports are material to the question.) Patterns + weighing + concordance. Literature silence ≠ “does not exist.”

### 9. Inference Limits

What cannot be concluded. Correlation/causation gaps. Animal→human leaps.

### 10. Analyst Disagreements

(If any) Where personas diverged.

### 11. Practical Guidance

(When user requested guidance.) Evidence-graded dosing, timing, stacks, monitoring, harm reduction. **Unknown** = state what cannot be recommended.

### 12. What Would Change This Conclusion

Specific evidence that would upgrade or downgrade certainty.

### 13. FAQ / Common Claims

(When useful.) Short adjudicated answers with certainty labels.

### 14. Guidance & Application Notice

Evidence-graded synthesis; user assumes responsibility; **Unknown** = no recommendation; consult qualified professionals for individual medical decisions.

### 15. References

DOI/PMID/URL for all cited sources. Label forum/anecdotal sources.

---

## Synthesizer routing rules

1. Always write the Executive Card first.  
2. If `input_type=compound` → full `compound-profile-template.md` (respect effort floors).  
3. If `input_type=interaction` → full `interaction-profile-template.md`.  
4. Else → general template above.  
5. Populate `evidence-matrix.json` per schema, including `anecdotal_patterns`, `executive_verdict`, and interaction fields when applicable.  
6. Never recommend on Unknown. Never omit subjective weighing when anecdotes are material.  
