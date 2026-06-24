# Research Analyst — Project Plan

**Status:** Phase 1–3 complete; Phase 4 + DR reversal complete (2026-06-24)  
**Scope:** `/research` only — unrelated skills live outside this project.

---

## Vision

One master command for deep evidence analysis and open compound education: sources, funding, methods, inference, guidelines vs literature — **DR** (actionable evidence-graded guidance).

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
- 3 golden examples in `references/examples/`
- Persona updates (inference-analyst, synthesizer, quality-reviewer)

### Phase 4 — Compound education + DR reversal
- [`dr-principles.md`](../skills/research-analyst/references/dr-principles.md) — Do Render doctrine (replaces DNR)
- [`open-research.md`](../skills/research-analyst/references/open-research.md)
- [`compound-lenses.md`](../skills/research-analyst/references/compound-lenses.md)
- [`compound-taxonomy.md`](../skills/research-analyst/references/compound-taxonomy.md)
- [`compound-profile-template.md`](../skills/research-analyst/references/compound-profile-template.md)
- [`compound-framer.toml`](../personas/compound-framer.toml)
- [`example-compound-creatine.md`](../skills/research-analyst/references/examples/example-compound-creatine.md)
- SKILL.md: compound intake classifier, compound-framer spawn at effort ≥ 2
- evidence-matrix schema: `recommendations[]`, `compound`, `bro_science_claims[]`

---

## Architecture

```
/research → intake (+ memory + MCP + classifier) → parallel personas (+ compound-framer) → synthesizer → quality gate → deliver + memory flush
```

---

## Verification checklist

- [ ] Two runs same topic — second references memory
- [ ] Compound query (e.g. creatine) — Practical Guidance section present
- [ ] Health topic effort 3 — Guidelines vs Literature section with DR recommendation
- [ ] Guideline/literature mismatch — called out with severity + recommend against
- [ ] PubMed MCP off — still completes
- [ ] `--save findings/test` — artifacts on disk
- [ ] Quality reviewer blocks Unknown-presented-as-Established; does not block evidence-graded dosing

---

## Deferred

- `--export docx`
- `biostatistician` persona at effort 4+
- Automated smoke-test script
- Golden example for performance compound (e.g. testosterone)

---

## Commands

```
/research creatine
/research --effort 4 --save findings/my-compound <compound or claim>
```