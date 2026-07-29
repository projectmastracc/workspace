# Compound Taxonomy — Class Routing

Use this taxonomy to classify intake and route to the correct lens checklist.  
Audience seed: **nootropics**, **gym/performance**, and **general supplementation**.

This taxonomy also seeds the persistent knowledge index (`knowledge/compounds/`, `knowledge/interactions/`).

## Classification tree

```
compound
├── neuropharmacology
│   ├── psychotropic (SSRI, SNRI, atypical antipsychotic, mood stabilizer)
│   ├── nootropic (racetam, ampakine, cholinergic, stimulant-adjacent)
│   ├── botanical_nootropic (bacopa, ginkgo, lion’s mane, etc.)
│   ├── CNS peptide (cerebrolysin, semax, selank, dihexa-class interest, etc.)
│   ├── cholinergic_support (alpha-GPC, citicoline, huperzine)
│   └── neuromodulator (ketamine, esketamine, psilocybin, etc.)
├── performance
│   ├── anabolic_androgenic (testosterone, nandrolone, trenbolone, etc.)
│   ├── selective_androgen (SARM: Ostarine, LGD, RAD, YK-11, etc.)
│   ├── peptide_hormone (GH, IGF-1, GHRP/GHRH, insulin-related)
│   ├── healing_peptide (BPC-157, TB-500, etc.)
│   ├── ancillary (AI, SERM, HCG, cabergoline, etc.)
│   ├── pct_recovery (tamoxifen, clomid, enclomiphene, etc.)
│   ├── cardiovascular_protective (telmisartan, nebivolol, citrus bergamot interest, etc.)
│   └── metabolic_support (metformin/berberine interest, insulin sensitizers — label carefully)
└── nutrition
    ├── vitamin_mineral
    ├── amino_acid (creatine, beta-alanine, citrulline, etc.)
    ├── botanical_adaptogen (ashwagandha, rhodiola, etc.)
    ├── ergogenic (caffeine, nitrates, etc.)
    ├── antioxidant_thiol (NAC, glutathione precursors)
    └── probiotic_prebiotic
```

## Intake classifier signals

| Signal | Likely class / type |
|--------|---------------------|
| Drug name (generic/brand) | neuropharmacology or performance |
| "Cycle", "stack", "PCT", "blast" | performance; if two agents + mitigate/protect → **interaction** |
| "Supplement", "dose per day", "timing" | nutrition |
| Peptide sequence or "-morelin" / "-lysin" peptide names | performance peptide or CNS peptide |
| "Nootropic", "cognitive", receptor name | neuropharmacology |
| "Mitigate", "protect", "against the effects of", "A + B" | **input_type=interaction** (see SKILL.md) |

## Multi-class compounds

| Compound | Primary lens | Secondary lens |
|----------|--------------|----------------|
| Creatine | nutrition | performance |
| Caffeine | nutrition | neuropharmacology |
| Modafinil | neuropharmacology | performance |
| Ashwagandha | nutrition | neuropharmacology (anxiolytic) |
| BPC-157 | performance | nutrition (gut) |
| NAC | nutrition | neuropharmacology / performance (mucolytic, redox) |
| Bacopa | neuropharmacology | nutrition (botanical) |
| Telmisartan | performance (protective) | neuropharmacology (off-target interest) |

When multi-class: apply both lens checklists; synthesize Practical Guidance per use case.

## Interaction index intent

Known protective / stack pairs may be stored under `knowledge/interactions/<a>_vs_<b>/` after high-effort runs. Taxonomy classes help label each side (e.g. AAS problem + CNS peptide mitigator; AAS problem + ARB protective).

## Unknown / ambiguous input

If compound identity is unclear:
1. Ask for clarification in intake (orchestrator) OR
2. Frame as topic search and list candidate compounds with taxonomy tags