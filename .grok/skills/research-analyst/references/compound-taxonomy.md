# Compound Taxonomy — Class Routing

Use this taxonomy to classify intake and route to the correct lens checklist.

## Classification tree

```
compound
├── neuropharmacology
│   ├── psychotropic (SSRI, SNRI, atypical antipsychotic, mood stabilizer)
│   ├── nootropic (racetam, cholinergic, stimulant-adjacent)
│   ├── CNS peptide (semax, selank, etc.)
│   └── neuromodulator (ketamine, psilocybin, etc.)
├── performance
│   ├── anabolic_androgenic (testosterone, nandrolone, trenbolone, etc.)
│   ├── selective_androgen (SARM)
│   ├── peptide_hormone (GH, IGF-1, GHRP, etc.)
│   ├── ancillary (AI, SERM, HCG, etc.)
│   └── pct_recovery (tamoxifen, clomid, enclomiphene, etc.)
└── nutrition
    ├── vitamin_mineral
    ├── amino_acid (creatine, beta-alanine, etc.)
    ├── botanical_adaptogen (ashwagandha, rhodiola, etc.)
    ├── ergogenic (caffeine, citrulline, etc.)
    └── probiotic_prebiotic
```

## Intake classifier signals

| Signal | Likely class |
|--------|--------------|
| Drug name (generic/brand) | neuropharmacology or performance |
| "Cycle", "stack", "PCT", "blast" | performance |
| "Supplement", "dose per day", "timing" | nutrition |
| Peptide sequence or "-morelin" suffix | performance (peptide_hormone) |
| "Nootropic", "cognitive", receptor name | neuropharmacology |

## Multi-class compounds

| Compound | Primary lens | Secondary lens |
|----------|--------------|----------------|
| Creatine | nutrition | performance |
| Caffeine | nutrition | neuropharmacology |
| Modafinil | neuropharmacology | performance |
| Ashwagandha | nutrition | neuropharmacology (anxiolytic) |
| BPC-157 | performance | nutrition (gut) |

When multi-class: apply both lens checklists; synthesize Practical Guidance per use case.

## Unknown / ambiguous input

If compound identity is unclear:
1. Ask for clarification in intake (orchestrator) OR
2. Frame as topic search and list candidate compounds with taxonomy tags