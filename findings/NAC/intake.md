# Intake
- **RESEARCH_ID**: 16607efb
- **Effort**: 5
- **Input**: NAC - N-Acetyl Cysteine
- **Parsed question**: Comprehensive compound education on N-acetylcysteine (NAC / N-acetyl-L-cysteine): identity, mechanism, established medical uses, psychiatric/addiction/respiratory/fertility/COVID evidence, safety, dosing, guidelines vs literature, Practical Guidance across neuropharmacology + nutrition/supplement lenses.
- **Input type**: compound
- **Guidance requested**: true (compound input)
- **User context**: none
- **Compound class**: Multi-lens — **nutrition** (amino acid derivative / supplement) + **neuropharmacology** (glutamate/GSH, psychiatric adjunct) + medical drug (antidote, mucolytic)
- **Applicable lenses**: nutrition (primary for OTC use); neuropharmacology (primary for psychiatric/addiction); performance (secondary — antioxidant training claims)
- **PubMed MCP**: unavailable — web_search + web_fetch
- **Past research briefing**: Cerebrolysin and YK11 threads (unrelated). No NAC continuity.

## Search strategy
- Terms: N-acetylcysteine, NAC, acetaminophen overdose Rumack-Matthew, COPD mucolytic, OCD meta-analysis, schizophrenia Berk, cannabis cocaine addiction, PCOS fertility, COVID, contrast nephropathy, safety GI anaphylactoid, GSH glutamate cystine-glutamate antiporter, FDA dietary supplement status
- Effort 5: 8–15+ sources including guidelines, SRs/MAs, pivotal RCTs, independent critiques

## Sources acquired (pivotal list for analysts)

### Mechanism / overview
1. **Tenório et al. 2021** — *N-Acetylcysteine (NAC): Impacts on Human Health.* Antioxidants. DOI 10.3390/antiox10060967 (MDPI; high-cite review). GSH precursor, mucolytic disulfide breaking, redox, fertility notes, safety profile.
2. **Dodd et al. 2008** — *N-acetylcysteine for antioxidant therapy: pharmacology and clinical utility.* Expert Opin Biol Ther. DOI 10.1517/14728220802517901.
3. **Aldini et al. 2018** — NAC antioxidant and disulfide-breaking mechanisms. Free Radic Res. DOI 10.1080/10715762.2018.1468564.
4. **Ezeriņa et al. 2018** — Fast-acting antioxidant via H2S/sulfane sulfur. Cell Chem Biol. PMID 29429900.

### Established medical uses
5. **Acetaminophen (paracetamol) overdose** — FDA-approved antidote; IV/oral protocols (Prescott/3-bag vs simplified); Rumack-Matthew nomogram standard of care. Label/clinical toxicology consensus — **Established**.
6. **Mucolytic / COPD** — Oral NAC long used; European/respiratory literature supports mucolytic benefit at adequate dose (often ≥1200 mg/day for exacerbations in some MAs); GOLD references mucolytics selectively.
7. **Contrast-induced nephropathy prevention** — Mixed/null in high-quality trials; many guidelines de-emphasize routine NAC for CIN.

### Psychiatry / addiction
8. **Deep et al. / psychiatric reviews** — Schizophrenia: negative symptoms / total scores improved as adjunct (Berk–Dean Australian program lineage) — promising MAs.
9. **OCD MAs** — Gadallah 2020; Eghdami 2024 (PMC11456833); Oliver 2015 SR OCRD; Carollo 2024 promise paper; **critical independent note**: Advanced Interventions UK review — adult effect may be small/fragile; first-trial positive bias.
10. **Deepmala et al. 2015** — *Clinical trials of N-acetylcysteine in psychiatry and neurology: a systematic review.* Neurosci Biobehav Rev (often cited umbrella).
11. **Addiction** — Cannabis (Gray et al. adolescent trial positive; adult mixed), cocaine craving, nicotine — mixed; reviews 2018–2024.
12. **Trichotillomania / skin-picking / autism irritability** — Small RCTs, mixed.

### Other domains
13. **PCOS / male fertility** — Meta-analyses of ovulation/sperm parameters (Tenório summary).
14. **COVID-19** — Mechanistic rationale + observational/adjuvant data; RCTs mixed; not standard SOC antiviral. Izquierdo-Alonso 2022 review.
15. **Performance / exercise** — Antioxidant may blunt training adaptations at high chronic doses (**Speculative**/contested) — flag for performance lens.

### Guidelines / regulatory
16. **FDA** — Drug for APAP OD; oral NAC also sold as dietary supplement (historical FDA enforcement around 2020–2022 “not dietary supplement” letter controversy; currently widely sold as supplement).
17. **Clinical toxicology guidelines** — NAC for APAP toxicity (e.g., ACMT/EAPCCT-aligned practice).
18. **NICE/GOLD/respiratory** — Mucolytics conditional; not universal.

## Key claims to adjudicate
| Claim | Expected direction |
|-------|-------------------|
| APAP OD antidote | **Established** |
| Mucolytic / COPD symptom benefit | **Probable** at adequate oral doses |
| Psychiatric adjunct (SCZ negative sx) | **Probable** modest |
| OCD adjunct | **Speculative** mixed/fragile adult data (post-Sarris 2022/AIS) |
| Addiction universal cure | **Unknown** / substance-specific mixed |
| General longevity antioxidant | **Unknown** / oversold |
| High-dose IV for everything | Misapplication of OD protocol |
| Safe OTC 600–2400 mg | **Probable** tolerability with GI AEs |

## Full-text gaps
- Some PMC reCAPTCHA / MDPI access denied in orchestrator environment; subagents should re-fetch abstracts/full text.
- Do not invent trial N or effect sizes beyond acquired abstracts.

## Guidance requirements for compound-framer
- Separate **prescription medical uses** vs **supplement self-use**
- Dosing tables: APAP (protocol only under medical care), mucolytic 600–1200+ mg, psychiatric trials often 2000–3000 mg/day divided
- Harm reduction: GI AEs; IV anaphylactoid; asthma caution; nitroglycerin interaction; charcoal interference in OD context
- Stacks: glycine/glyNAC hype — label bro-science vs sparse RCTs
- FDA/supplement legal nuance without fearmongering
