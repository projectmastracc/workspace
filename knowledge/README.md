# Knowledge layer — compound & interaction profiles

Persistent, repo-local monographs produced or updated by high-effort `/research` runs. Complements cross-session memory (`~/.grok/research-memory/`), which is workspace-hashed and not meant for shareable compound pages.

## Layout

```
knowledge/
  compounds/
    <slug>/
      profile.md      # Full or condensed briefing (wiki-ready markdown)
      matrix.json     # evidence-matrix.json snapshot
      meta.json       # slug, updated, effort, certainty, open_questions, input_type
  interactions/
    <slug-a>_vs_<slug-b>/
      profile.md
      matrix.json
      meta.json
```

## Slug rules

- Lowercase ASCII
- Hyphen-separated common name
- Prefer generic names: `creatine-monohydrate`, `bacopa-monnieri`, `cerebrolysin`, `trenbolone`
- Interaction: `cerebrolysin_vs_trenbolone` (alphabetize only if roles are symmetric; otherwise **problem_vs_mitigator** or keep A_vs_B as analyzed)

## When the skill reads

On setup for `compound` or `interaction` inputs, if a matching folder exists:

1. Load `profile.md` + `meta.json` into intake as **Prior knowledge profile**
2. Prefer differential update: refresh claims, open questions, and matrix fields rather than rewriting from zero when evidence is unchanged

## When the skill writes

- Effort ≥ 3, or
- `--save` path under `knowledge/`, or
- Explicit user request to update knowledge

Write `profile.md` from the final briefing, copy matrix, update `meta.json`:

```json
{
  "slug": "creatine-monohydrate",
  "updated": "2026-07-29",
  "effort": 3,
  "overall_certainty": "Established",
  "input_type": "compound",
  "open_questions": ["..."],
  "lenses": ["nutrition", "performance"]
}
```

## What belongs here

- High-quality monographs and interaction analyses you want to reuse
- Golden or production profiles after human review

## What does not

- Raw `/tmp` artifacts
- Speculative one-off effort-1 notes without review
- Unlabeled medical advice personalizations

## Taxonomy seed

Class routing for new compounds: `.grok/skills/research-analyst/references/compound-taxonomy.md`.
