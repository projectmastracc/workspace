# Research Analyst — Project Plan

**Status:** Phase 5 complete (Sci-Wiki depth + interaction mode + anecdotal first-class) — 2026-07-29  
**Scope:** `/research` only — unrelated skills live outside this project.  
**Depth spec:** [`docs/improvement-plan-sciwiki-depth.md`](../../docs/improvement-plan-sciwiki-depth.md)

---

## Vision

One master command for deep evidence analysis and open compound education for **nootropic users**, **gym/performance users**, and **any supplementation** research: sources, funding, methods, inference, guidelines vs literature, anecdotal weighing, and multi-compound pathway analyses — with **evidence-graded practical guidance**.

---

## Implemented

### Phase 1
- Agent, 5 personas, `/research` skill, 6 core references, guidelines policy

### Phase 2 — Infrastructure
- [`research-memory.py`](../skills/research-analyst/scripts/research-memory.py) — cross-session threads
- [`.grok/config.toml`](../config.toml) — PubMed MCP
- `findings/` + `.gitignore` — saved report storage
- SKILL.md hooks for memory, MCP, `--save`

### Phase 3 — Depth
- [`guidelines-vs-literature.md`](../skills/research-analyst/references/guidelines-vs-literature.md)
- [`literature-search.md`](../skills/research-analyst/references/literature-search.md)
- Golden examples in `references/examples/`
- Persona updates (inference-analyst, synthesizer, quality-reviewer)

### Phase 4 — Compound education + guidance doctrine
- [`dr-principles.md`](../skills/research-analyst/references/dr-principles.md) — evidence-graded practical guidance
- [`open-research.md`](../skills/research-analyst/references/open-research.md)
- [`compound-lenses.md`](../skills/research-analyst/references/compound-lenses.md)
- [`compound-taxonomy.md`](../skills/research-analyst/references/compound-taxonomy.md)
- [`compound-profile-template.md`](../skills/research-analyst/references/compound-profile-template.md)
- [`compound-framer.toml`](../personas/compound-framer.toml)
- SKILL.md: compound intake classifier, compound-framer spawn at effort ≥ 2
- evidence-matrix schema: `recommendations[]`, `compound`, `bro_science_claims[]`

### Phase 5 — Sci-Wiki depth (this phase)
- Softened “DR” branding → user-facing **evidence-graded practical guidance**
- 15-section compound monograph template + Executive Card
- [`interaction-profile-template.md`](../skills/research-analyst/references/interaction-profile-template.md) + `input_type=interaction`
- First-class anecdotal weighing (literature-silent ≠ non-existence)
- [`style-guide.md`](../skills/research-analyst/references/style-guide.md)
- Schema: `anecdotal_patterns`, `pathway_overlap`, `protective_hypothesis`, `executive_verdict`, `monitoring_protocol`, …
- Expanded personas (framer, inference, reviewer, synthesizer, source-critic, methodologist)
- Golden examples: creatine (updated), mixed nootropic, lit-silent anecdote, interaction protective, AAS harm-reduction
- [`evaluation-checklist.md`](../skills/research-analyst/references/evaluation-checklist.md)
- `knowledge/compounds/` + `knowledge/interactions/` persistent profiles
- LICENSE (MIT), README audience positioning, `--wiki`/`--monograph` flag

---

## Architecture

```
/research → intake (+ memory + knowledge + MCP + classifier)
         → parallel personas (+ compound-framer for compound/interaction)
         → synthesizer (monograph | interaction | general)
         → quality gate (structure + anecdotal + pathway)
         → deliver + memory flush + knowledge write (effort ≥ 3)
```

---

## Verification checklist

- [x] Compound template = 15 sections + Executive Card + anecdotal rules
- [x] Interaction template + classifier + quality-reviewer pathway gate
- [x] Anecdotal first-class rules in principles, grading, personas
- [x] Schema fields for anecdotal_patterns / pathway_overlap / monitoring
- [x] Golden examples for lit-silent anecdote + protective interaction
- [x] Knowledge layer directories + README + SKILL hooks
- [x] LICENSE + README + AGENTS language refresh
- [ ] Runtime smoke: `/research creatine` (effort 2) produces Executive Card + Practical Guidance
- [ ] Runtime smoke: literature-silent anecdotal claim run shows weighing, not adamant denial
- [ ] Runtime smoke: multi-compound protective query produces pathway maps
- [ ] Two runs same topic — second references memory
- [ ] PubMed MCP off — still completes
- [ ] `--save findings/test` — artifacts on disk
- [ ] Quality reviewer blocks Unknown-as-Established and interaction refusal

---

## Deferred

- `--export html|docx` pipeline
- `biostatistician` persona at effort 4+
- Automated live `/research` CI (PubMed-dependent)
- Re-running all historical `findings/*` under new templates

---

## Commands

```
/research creatine
/research --effort 3 --wiki bacopa
/research --effort 4 --save findings/my-compound <compound or claim>
/research --effort 3 "evaluation of A as a preventative against effects of B"
```
