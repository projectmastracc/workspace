# Research Analyst — Project Plan

**Status:** Phase 1 + Phase 2–3 complete (2026-06-24)  
**Scope:** `/research` only — unrelated skills live outside this project.

---

## Vision

One master command for deep evidence analysis: sources, funding, methods, inference, guidelines vs literature — **DNR** (no personal medical advice).

---

## Implemented

### Phase 1
- Agent, 5 personas, `/research` skill, 6 core references, DNR + guidelines policy

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

---

## Architecture

```
/research → intake (+ memory + MCP) → parallel personas → synthesizer → quality gate → deliver + memory flush
```

---

## Verification checklist

- [ ] Two runs same topic — second references memory
- [ ] Health topic effort 3 — Guidelines vs Literature section
- [ ] Guideline/literature mismatch — called out with severity
- [ ] PubMed MCP off — still completes
- [ ] `--save findings/test` — artifacts on disk
- [ ] Quality reviewer blocks DNR violations

---

## Deferred

- `--export docx`
- `biostatistician` persona at effort 4+
- Automated smoke-test script

---

## Commands

```
/research <topic>
/research --effort 4 --save findings/my-topic <claim or DOI>
```