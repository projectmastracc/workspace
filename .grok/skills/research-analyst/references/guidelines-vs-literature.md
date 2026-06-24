# Guidelines vs Literature

Compare mainstream guidance to published evidence. Authority is not evidence.

## Sources to check

| Body | Examples | Where to find |
|------|----------|---------------|
| US | APA, FDA labels, CDC, NIH | apa.org, fda.gov, cdc.gov |
| UK | NICE | nice.org.uk |
| International | WHO | who.int |

Always note **year** and **jurisdiction** — guidelines differ by country and revision cycle.

## Alignment labels

| Label | Meaning |
|-------|---------|
| **Supports** | High-quality literature consistent with guideline recommendation |
| **Partial** | Literature supports some but not all claims; or weaker evidence tier than guideline implies |
| **Contradicts** | Best available evidence points opposite direction or refutes key claim |
| **No evidence** | Guideline rests on consensus, tradition, or extrapolation without direct data |

## Mismatch severity

| Severity | When to use |
|----------|-------------|
| **Minor** | Wording stronger than evidence; directionally correct |
| **Material** | Recommendation exceeds evidence grade; important population excluded from data |
| **Fundamental** | Core claim contradicted by meta-analyses or large RCTs |

## Common reasons for mismatch

- Outdated panel (evidence base moved; guideline not revised)
- Expert consensus without RCT support (Grade Low/Very Low underneath)
- Regulatory or liability framing (precaution beyond data)
- Industry-funded panel or COI on guideline authors
- Population mismatch (pediatric guideline from adult data, etc.)
- Surrogate endpoints promoted to clinical certainty

## Reporting template

```markdown
| Guideline | Recommends | Literature | Alignment | Severity | Notes |
|-----------|------------|------------|-----------|----------|-------|
| APA 20XX | ... | Meta-analysis Y (**Probable**) | Partial | Material | Panel predates key RCTs |
```

## Worked example (pattern)

**Guideline:** Hypothetical College recommends intervention A as first-line for condition X.

**Literature:** Two meta-analyses show small effect vs placebo; one large RCT null; industry funding on majority of positive trials.

**Verdict:** Guideline **Partially** supported at best (**Probable** for small benefit in subset). Calling A "first-line" **materially exceeds** evidence if null RCT is high quality. Note funding asymmetry and guideline revision date.