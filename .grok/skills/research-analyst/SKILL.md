---
name: research
description: >
  Deep research analyst for nootropics, performance pharmacology, and any
  supplementation — multi-perspective evidence review, source/funding scrutiny,
  anecdotal weighing, and evidence-graded practical guidance (dosing, stacks,
  protectives, monitoring). Modes: compound monographs, multi-compound pathway
  analyses, claims, papers, topics. Use /research for full analysis.
when-to-use: >
  research analysis, interpret study, evidence review, what does science say,
  literature analysis, source scrutiny, funding bias, neuropharmacology evidence,
  compound framing, supplement dosing, nootropic, performance pharmacology,
  stack, mitigate, protective, PCT, peptide, AAS, SARM, adjudicate claim, PMID, DOI
argument-hint: "[--effort N] [--wiki|--monograph] [--save PATH] <question, claim, DOI, PMID, topic, compound, or stack/interaction>"
---

# Research Analyst — `/research`

One master command for deep research analysis and open compound education aimed at **nootropic users**, **gym/performance users**, and anyone researching **supplementation of any kind**.

You coordinate only — **all** analysis is done by subagents seeded with persona instructions. You **must not** author the briefing or skip subagent launches.

## Core principle: evidence-graded practical guidance

When evidence supports practical use, **render** dosing, protocols, stacks, monitoring, and direct recommendations with certainty labels. When it does not, say so clearly.

- **Unknown = no recommendation**
- Consistent multi-source anecdotal/forum patterns are **first-class inputs**: report and weigh them; they support **Speculative** notes only — never Established/Probable alone
- Literature silence ≠ “effect does not exist”
- Multi-compound / protective queries get **pathway-level analysis**, not literature-refusal summaries
- **Mechanism-first:** for major effects and sides, chain molecular action → downstream physiology → phenotype; match protectives/stacks to **named pathway nodes**, not generic “support” lists
- **Protocol construction:** when user asks for full protocol / full neuroprotection / complete cover — **build** the multi-pathway protocol with certainty on every line; do not lead with medical-style “no recommendation”

See `references/dr-principles.md`, `references/style-guide.md`, and `references/evidence-grading.md`.

## Run isolation (hard rules — non-negotiable)

Each `/research` command produces a **standalone** findings package. Other packages are **not** sources.

1. **Never read other `findings/*` folders** as evidence, ceilings, continuity, or analysis input. Do not `ls`, `read_file`, cite, paraphrase, or “load mitigator ceilings from” prior packages (e.g. `findings/NAC`, `findings/cerebrolysin`).
2. **Co-mentioned compounds are researched in this run.** If the query involves stacks, protectives, or B/C agents (e.g. cerebrolysin for trenbolone neuroprotection, NAC, telmisartan), acquire literature and forum sources **for those agents in this intake**. Do not import prior monographs.
3. **Memory is same-topic only.** After `research-memory.py read`, use the thread **only if it matches this exact topic/question**. Cross-topic memory (e.g. NAC thread while researching trenbolone) → treat as **none**. Never use other compounds’ memory as certainty ceilings.
4. **Knowledge load is exact-slug only.** Load `knowledge/compounds/<slug>/` or `knowledge/interactions/<a>_vs_<b>/` only when the slug is **this run’s primary subject** (or exact interaction pair being re-run). Do **not** load sibling compounds’ knowledge when analyzing a different primary (e.g. do not load cerebrolysin knowledge for a trenbolone-primary interaction run unless the user is re-running that exact interaction slug).
5. **Forbidden briefing language:** “prior workspace findings,” “prior monographs,” “ceilings from findings/X,” “skim findings/…,” “continuity with [unrelated package].”
6. **Anti-pattern:** Opening other findings to fill mitigator sections. **Correct:** Search PubMed/web/forums for each agent and the combination in *this* run; adjudicate from those sources.
7. Golden examples under `references/examples/` are **calibration only**, not evidence and not prior findings packages.

Quality reviewer **auto-flags critical/major** for cross-package findings use (see persona).

## Tool-call discipline

Emit `spawn_subagent` **before** narrating launches. Past tense only after tool results. Never end a turn claiming subagents ran without paired tool calls.

## Invocation

```
/research [--effort N] [--wiki|--monograph] [--save PATH] <input>
```

| Flag | Default | Effect |
|------|---------|--------|
| `--effort N` | 2 | Depth 1–5 (see Effort guide). Soft-upgrade rules below. |
| `--wiki` / `--monograph` | off | Force full monograph/interaction structure + accessible prose; **floor effort to 3** if lower |
| `--save PATH` | none | Copy briefing + matrix + intake to PATH (e.g. `findings/2026-06-24-topic-slug/`). Also updates `knowledge/` when effort ≥ 3 (see Knowledge layer). |

`<input>` can be: research question, claim, DOI, PMID, paper title, topic, **compound**, or **multi-compound interaction** (stack / mitigate / protect / pathway).

## Todo scaffold

Open with `todo_write` (merge: false):

- `setup` — ID, paths, persona load, intake, knowledge load
- `analyze` — parallel persona subagents
- `synthesize` — research-synthesizer
- `review-round-N` — quality reviewer (effort ≥ 2)
- `revise-round-N` — synthesizer revision (if issues)
- `memory-read` — load prior research threads
- `knowledge-write` — update knowledge store when applicable
- `deliver` — present briefing, memory flush, optional --save

## Research memory

Script: `<dirname of this SKILL.md>/scripts/research-memory.py`

At setup (after `mkdir`):

```bash
python3 <skill>/scripts/research-memory.py read
```

Store as `past_research_briefing` **only if the returned thread is the same topic as this query**. Otherwise set **none** (cross-topic memory is not analytical input). Include in `intake.md` under **Past research briefing**.

After successful deliver, flush **this topic only**:

```bash
echo '{"run":{"topic":"...","effort":N,"certainty":"...","conclusions":["..."],"recommendations":["..."],"open_questions":["..."],"sources":["PMID:..."],"guideline_flags":"...","verdict":"..."}}' \
  | python3 <skill>/scripts/research-memory.py update
```

## Knowledge layer (persistent monographs)

Repo-local store for **same-slug re-runs only** — not a library of free ceilings for other topics:

```
knowledge/compounds/<slug>/profile.md
knowledge/compounds/<slug>/matrix.json
knowledge/compounds/<slug>/meta.json
knowledge/interactions/<slug-a>_vs_<slug-b>/...
```

Slug: lowercase, hyphenated common name (e.g. `creatine-monohydrate`, `cerebrolysin`).

**At setup** (exact match only):

1. If **this run’s** primary slug matches `knowledge/compounds/<slug>/`, optionally load for differential update of *that same compound re-run*.
2. For interaction re-runs: load only `knowledge/interactions/<exact-a>_vs_<exact-b>/` when re-running **that pair**.
3. **Do not** load knowledge for co-mentioned mitigators that are not the primary slug of this run. Research them from primary sources in this intake.

**At deliver** (effort ≥ 3, or `--save` under `knowledge/`):

1. Write/update `profile.md` from **this run’s** final briefing only.
2. Copy `evidence-matrix.json` → `matrix.json`.
3. Write `meta.json`: `{ "slug", "updated", "effort", "overall_certainty", "open_questions", "input_type" }`.

Helper script (optional): see `scripts/knowledge-store.py` and `knowledge/README.md`.

## PubMed MCP

At setup, check whether `pubmed` MCP is available. Set `pubmed_available` true/false in `intake.md`.

| pubmed_available | PMID / paper search |
|------------------|---------------------|
| true | Prefer PubMed MCP tools |
| false | `web_search` + `web_fetch`; never abort |

See `references/literature-search.md` for full playbook (includes anecdotal sampling and interaction dual-search).

## Persona injection

Read once at setup from `<repo>/.grok/personas/`:

| Persona file | Role |
|--------------|------|
| `source-critic.toml` | Funding, COI, provenance, trust tiers; dual-compound when interaction |
| `methodologist.toml` | Design, bias, stats, applied applicability |
| `inference-analyst.toml` | Truth mapping, subjective concordance, pathway overlap, evidence-graded recommendations |
| `compound-framer.toml` | Full monograph or interaction outline + Practical Guidance (effort ≥ 2 when compound/interaction/guidance) |
| `research-synthesizer.toml` | Final briefing + evidence matrix |
| `research-quality-reviewer.toml` | Completeness + epistemic + anecdotal + interaction gate (effort ≥ 2) |

Resolve `<repo>` as the git repo root (parent of `.grok/`). Prepend persona `instructions` to each subagent prompt. Prefix `description` with bracketed role tag: `[source-critic]`, `[compound-framer]`, etc.

References live at `<dirname of this SKILL.md>/references/`.

## Setup

Generate ID:

```bash
python3 -c "import uuid; print(uuid.uuid4().hex[:8])"
```

Define paths (fixed for entire run):

- `RESEARCH_ID` = output
- `ARTIFACT_DIR` = `/tmp/grok-research-${RESEARCH_ID}/`
- `intake_file` = `${ARTIFACT_DIR}/intake.md`
- `sources_file` = `${ARTIFACT_DIR}/sources.md`
- `methods_file` = `${ARTIFACT_DIR}/methods.md`
- `inference_file` = `${ARTIFACT_DIR}/inference.md`
- `compound_file` = `${ARTIFACT_DIR}/compound.md`
- `briefing_file` = `${ARTIFACT_DIR}/briefing.md`
- `matrix_file` = `${ARTIFACT_DIR}/evidence-matrix.json`
- `review_file` = `${ARTIFACT_DIR}/review.md`

```bash
mkdir -p "${ARTIFACT_DIR}"
```

Parse flags:

- `--effort N` (default 2, clamp 1–5)
- `--wiki` / `--monograph` → set `wiki_mode=true`; if effort < 3, set effort = 3
- `--save PATH`

Soft-upgrade: if `input_type` will be `interaction` and effort is 1, set effort = 2 (minimum); prefer 3+ for serious protective hypotheses.

## Step 1: Intake and source acquisition

**You** (orchestrator) write `intake.md` after acquiring sources.

**Input detection:**

| Pattern | Action |
|---------|--------|
| `10.\d{4,}/` or `doi:` | Fetch `https://doi.org/<doi>` via web_fetch |
| `PMID:\s*\d+` or `^\d{7,8}$` | Search PubMed MCP or web_search |
| File path `.pdf` | Read file |
| Multi-compound / mitigate language (see classifier) | `interaction` |
| Compound name (taxonomy) | `compound`; load compound-taxonomy.md |
| Free text | Classify: compound \| interaction \| claim \| paper \| topic \| question |

**Input classifier** (set `input_type` in intake):

| Type | Signals |
|------|---------|
| `interaction` | “against the effects of”, mitigate, protect, preventative, stack with, combination, A + B, pathway overlap, synergy, antagonism, “as a cover for” |
| `compound` | Drug/supplement name, “dose”, “cycle”, “PCT”, peptide name, taxonomy match (single primary agent) |
| `claim` | Assertive statement to adjudicate |
| `paper` | DOI, PMID, paper title |
| `topic` | Broad subject without single claim |
| `question` | Interrogative research question |

If both compound and interaction signals: prefer **`interaction`**.

Set `guidance_requested: true` when user asks “what should I”, “recommend”, “protocol”, “dose”, or input is compound/interaction.

For interaction, set:

- `compound_a` / role (problem | primary | co_stack)
- `compound_b` / role (mitigator | protective | co_stack)
- `interaction_hypothesis` (one sentence)

**intake.md template:**

```markdown
# Intake
- **RESEARCH_ID**: ...
- **Effort**: N
- **Wiki mode**: true | false
- **Input**: (raw)
- **Parsed question**: (precise)
- **Input type**: compound | interaction | claim | paper | topic | question
- **Guidance requested**: true | false
- **User context**: goals, experience tier, health flags (if provided; else "none")
- **Compound class**: (if compound — from compound-taxonomy.md)
- **Interaction**: A=... (role); B=... (role); hypothesis=...
- **Applicable lenses**: neuropharmacology | performance | nutrition
- **Sources acquired**: [list with DOI/PMID/URL]
- **Search strategy**: [terms, databases, date range]
- **Anecdotal sampling**: none | [forums/topics sampled]
- **PubMed MCP**: available | unavailable
- **Past research briefing**: [same-topic memory only, else "none"]
- **Prior knowledge profile**: [exact-slug knowledge only, else "none"]
- **Package isolation**: enforced — no other findings/ packages read
```

Follow `references/literature-search.md`. Source counts:

- Effort 1: 2–4 pivotal sources
- Effort 2: 4–8 sources including at least one review if exists; contradictory set if contested; anecdotal sample if discourse-heavy
- Effort 3+: 8–15 sources; systematic reviews + primary + contradictory; interaction dual-compound + combo terms

If full text unavailable, state limitation in intake — never invent methods or results.

## Step 2: Parallel analysis

Spawn subagents **in parallel** in one response.

### Effort 1 (fast)

- `source-critic` → `sources.md`
- `inference-analyst` → `inference.md`
- Skip methodologist (inference-analyst covers light methods check)
- Skip compound-framer (synthesizer uses light compound framing from inference)

### Effort ≥ 2 (standard — default)

Spawn all core personas:

- `source-critic` → `sources.md`
- `methodologist` → `methods.md`
- `inference-analyst` → `inference.md`

**Additionally** when `input_type` is `compound` OR `interaction` OR `guidance_requested` is true:

- `compound-framer` → `compound.md`

For `interaction`, tell framer to use `interaction-profile-template.md` and inference-analyst to produce pathway overlap + protective-hypothesis certainty.

`spawn_subagent` parameters:

- `subagent_type`: `general-purpose`
- `capability_mode`: `read-only`

**Subagent prompt template:**

```
{persona_instructions}

---

## Task
Read intake: {intake_file}
Read references: {relevant reference paths under skill references/}
Read primary sources listed in intake (and only those — acquire more via web_search/web_fetch if needed).

**Isolation:** Do NOT read any other findings/* package. Do NOT use prior monographs as evidence. Co-mentioned compounds must be sourced in this run’s intake/search, not imported.

If intake lists exact-slug prior knowledge for a same-subject re-run only, you may differential-update that subject — never sibling compounds.

Write your analysis to: {section_file}

Evidence-graded practical guidance: render when applicable. Unknown = no recommendation.
Cite DOI/PMID for every literature source you discuss; label forum sources as non-peer-reviewed.
Label substantive claims with certainty: Established / Probable / Speculative / Unknown.
When literature is silent and consistent anecdotes exist: state both; never adamant denial of existence from silence alone.
For interaction mode: pathway-level analysis required; no literature-refusal substitute.
Discover community protectives (e.g. peptides used against AAS sides) via this run’s search, not prior packages.
Incorporate user_context from intake when provided.
```

Save each `subagent_id` only if resuming later; parallel launches need not be resumed.

## Step 3: Synthesis

Spawn `research-synthesizer`:

```
{research_synthesizer_persona_instructions}

---

Read all section files in: {ARTIFACT_DIR}
Read references/output-template.md, references/compound-profile-template.md,
references/interaction-profile-template.md, references/style-guide.md,
references/evidence-matrix-schema.json, and references/examples/ for calibration

Write briefing to: {briefing_file}
Write evidence matrix to: {matrix_file}

Routing:
- input_type compound → compound-profile-template.md (respect effort floors)
- input_type interaction → interaction-profile-template.md
- else → output-template.md general path

Always open with Executive Card.
Integrate source scrutiny, methods, inference, and compound framing into one briefing.
Continuity note in Overview **only** if same-topic memory is non-empty for this exact re-run — never cross-package continuity.
Never cite other findings/* packages. Never import prior monograph ceilings.
Include Guidance & Application Notice. Include Source Integrity with funding/COI.
Include Guidelines vs Literature for health-adjacent topics with evidence-graded recommendations.
Include Subjective / Experiential Profile with weighing + concordance when anecdotes material.
Include Practical Guidance when guidance_requested or compound/interaction input.
Populate recommendations[], anecdotal_patterns[], executive_verdict; for interaction also pathway_overlap and protective_hypothesis.
Preserve analyst disagreements if present.
```

## Step 4: Quality review (effort ≥ 2)

Spawn `research-quality-reviewer`:

```
{research_quality_reviewer_persona_instructions}

---

Read briefing: {briefing_file}
Read matrix: {matrix_file}
Read all section files in: {ARTIFACT_DIR}
Read references/dr-principles.md, references/guidelines-vs-literature.md,
references/compound-profile-template.md, references/interaction-profile-template.md,
references/evaluation-checklist.md

Write review to: {review_file}
```

**If open critical or major issues:** resume research-synthesizer with review issues → re-review → loop until 0 open critical/major.

Effort 5: also resolve all minor issues before delivery.

Effort 1: skip Step 4; orchestrator spot-checks (Unknown recommendations, missing Practical Guidance when requested, adamant literature-silent denial) before deliver.

## Step 5: Deliver

1. Read `briefing_file` and present to user
2. Briefly note overall certainty, key recommendations, and source-trust caveats
3. Memory flush (see Research memory)
4. Knowledge write when effort ≥ 3 or save path under `knowledge/`
5. If `--save PATH`: `mkdir -p PATH && cp ${ARTIFACT_DIR}/briefing.md ${ARTIFACT_DIR}/evidence-matrix.json ${ARTIFACT_DIR}/intake.md PATH/`
6. If effort ≥ 3: mention `evidence-matrix.json` is in artifacts (or save path)

Default save suggestion: `findings/<YYYY-MM-DD>-<slug>/`

Do not delete artifacts if user used `--save`. Otherwise optional cleanup.

## Effort guide

| Effort | Target depth | Minimum content | Typical use |
|--------|--------------|-----------------|-------------|
| **1** | Fast focused answer | Executive Card + Overview + Practical Guidance + Safety + Key Sources | Simple factual or dosing queries |
| **2** (default) | Standard multi-perspective | Core sections + matrix + quality gate + anecdotal weighing | Most everyday questions |
| **3** | Full monograph or full interaction analysis | All required sections, comparative or pathway analysis, explicit anecdotal weighing | Important, contested, multi-compound, or `--wiki` |
| **4–5** | Maximum rigor | Full structure + extra sources + multiple alternatives or detailed mechanism maps | High-stakes or complex protective hypotheses |

## Edge cases

| Situation | Behavior |
|-----------|----------|
| Paywalled paper | Abstract + methods from PubMed; state full-text gap |
| Retracted paper | Flag in intake; do not use as supporting evidence |
| Only preprints exist | Label all; downgrade certainty |
| No sources found | Honest “insufficient evidence” briefing; state what cannot be recommended |
| User asks what they should do | Evidence-graded recommendation; Unknown = explain gap |
| Insufficient evidence for dosing | State what cannot be recommended; do not fabricate protocols |
| Industry-only evidence | State in Source Integrity; steelman independent-data absence |
| Forum-only for an effect | Report pattern; Speculative ceiling; concordance literature-silent if applicable |
| Literature silent + consistent anecdotes | State both; never adamant “does not exist” |
| Interaction query | Pathway analysis required; soft-upgrade effort; use interaction template |
| Bro-science contradicted by literature | Tag claims; recommend against; do not present as Established |
| Other findings/* exist on co-mentioned compounds | Ignore as inputs; research those compounds fresh in this run |
| Memory returns unrelated prior topics | Treat as none — do not import ceilings |

## What this skill produces

The user receives **actionable compound education after deep understanding**:

- What the evidence supports and does not support
- Evidence-graded Practical Guidance (dosing, stacks, monitoring) when warranted
- Subjective/forum patterns weighed against controlled evidence
- Pathway-level interaction / protective analyses for multi-compound questions
- Who funded key work and what conflicts exist
- Methodological limits and inference gaps
- Both sides of contested claims
- Calibrated certainty — not hype, not false balance, not literature-purist erasure of real-world patterns

Truth bounded by sources. Guidance bounded by certainty. Anecdote labeled and capped. Interactions analyzed at the pathway level.
