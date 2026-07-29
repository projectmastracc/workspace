# Methodological Appraisal — Cerebrolysin Human Evidence
**Role:** Methodologist | **RESEARCH_ID:** b150373f  
**Scope:** Stroke (AIS), TBI, Alzheimer’s disease (AD), vascular dementia (VaD)  
**Standards applied:** `source-evaluation.md`, `evidence-grading.md`  
**Question form:** Does human trial evidence support authors’ efficacy/safety claims for Cerebrolysin, and at what certainty for long-term function?

---

## 1. PICO Frameworks (by indication)

### 1.1 Acute ischemic stroke (AIS)
| Element | Definition used in pivotal evidence |
|--------|--------------------------------------|
| **P** | Adults with imaging-confirmed AIS; baseline NIHSS typically mild–moderate (trial medians ~7–14); often MCA/ICA territory; initiation windows 3–72 h (most ≤12–24 h) |
| **I** | Cerebrolysin IV 30–50 mL/day × 10–21 days (most common 30 mL × 10 d), as add-on to SOC (ASA ± rt-PA ± rehab) |
| **C** | Placebo (0.9% saline) + same SOC |
| **O (primary in MAs)** | Early neurological deficit: NIHSS change day 21/30 (**surrogate / intermediate**) |
| **O (clinically decisive)** | Day-90 mRS (ordinal or dichotomized 0–1 / 0–2); mortality; SAEs; hemorrhagic transformation |
| **O (often missing)** | ≥6-month function, QoL, cognition, participation, cost-utility |

### 1.2 Traumatic brain injury (TBI)
| Element | Definition |
|--------|------------|
| **P** | Moderate–severe TBI (admission GCS ~10; CAPTAIN II mean GCS 10.4, BPRS ~2.6) |
| **I** | Cerebrolysin 50 mL then cyclic regimens (CAPTAIN series) |
| **C** | Placebo + usual care |
| **O** | Multidimensional ensemble of functional + neuropsychological scales at days 10/30/90 (Wei–Lachin MW); HADS; safety |

### 1.3 Alzheimer’s disease (AD)
| Element | Definition |
|--------|------------|
| **P** | Mild–moderate AD |
| **I** | Cerebrolysin IV (typically 30 mL/day courses; cyclic) |
| **C** | Placebo |
| **O** | Cognition (ADAS-cog / SMD), global clinical change (CIBIC+/CGI), combined “global benefit”; safety to ~6 months |

### 1.4 Vascular dementia (VaD)
| Element | Definition |
|--------|------------|
| **P** | Elderly mild–moderate VaD |
| **I** | Cerebrolysin IV courses of variable duration |
| **C** | Placebo |
| **O** | MMSE, ADAS-cog+, global response rates; AEs |

---

## 2. Design Appraisal — Key Studies / Meta-Analyses

### 2.1 Bornstein et al. 2018 — 9-RCT stroke MA (Wei–Lachin)
- **Citation:** Bornstein NM, et al. *Neurol Sci.* 2018;39:629–640. PMID: 29248999; DOI: 10.1007/s10072-017-3214-0; PMC5884916.
- **Design:** Mixed IPD (5 trials) + aggregate data (4) meta-analysis; PRISMA-aligned methods; nonparametric Mann–Whitney (MW) effect size; Wei–Lachin / MERT pooling pre-specified under blinded conditions for CARS-2 SAP.
- **Included:** MRI-1/2, Qaragozli, **CASTA**, CERE-LYSE-I, CARS-1, CARS-2, Amiri-Nikpour, Xue; N=1879 for primary NIHSS day 21/30.
- **Primary result claimed:** MW 0.60 for NIHSS day 21/30 (P<0.0001); NNT 7.7 for clinically relevant NIHSS change; day-90 mRS in NIHSS>12 subgroup MW 0.61 (N=314, P=0.0118).
- **Design strengths:** Largest early ensemble then available; IPD majority; full-scale ordinal analysis preferred over arbitrary dichotomization; leave-one-out robustness; sensitivity fixed/random models.
- **Design weaknesses (critical):**
  1. **Industry-tied authorship network** — Vester/Rahlfs (IDV biometry long associated with EVER analyses), Muresanu, Guekht, Bornstein (CASTA steering), Heiss; manufacturer assisted source identification. Trust downgrade trigger (source-evaluation.md: industry funding without independent replication).
  2. **Endpoint hierarchy inversion:** Primary analytic focus is **early NIHSS** (day 21/30), not day-90 disability — the regulatory/clinically preferred stroke outcome. Day-90 mRS restricted to post-hoc–style moderate–severe subset (N=314 from 3 trials with n≥10 in NIHSS>12).
  3. **Not prospectively registered as a review** (authors state objective was to verify CARS MA).
  4. Heterogeneous baseline severity (NIHSS medians 7–14) → floor effects in mild strokes; authors acknowledge CASTA as “negative outlier” on funnel plot.
  5. LOCF imputation; some OC-only aggregate studies.
- **Conclusion alignment:** Authors claim “beneficial effect on early global neurological deficits” and “clinically relevant… functional outcome at day 90… in moderate to severe.” The early NIHSS claim is statistically supported within the chosen model (**Probable** for early NIHSS under industry-linked synthesis). The day-90 functional claim **outruns** the full ITT data — it is a severity-restricted secondary analysis, not a pre-registered universal day-90 win. **Speculative → Probable only in moderate–severe**, with industry COI caveat.

### 2.2 Patel et al. 2025 — 14-RCT stroke SR/MA (RoB 2 + GRADE)
- **Citation:** Patel PN, Mangal D, Patel K. *Cureus.* 2025;17(8):e91054. DOI: 10.7759/cureus.91054; PMID: 41018475.
- **Design:** PROSPERO-registered (CRD4201108156 noted); PRISMA 2020; RoB 2.0; GRADE; random-effects DerSimonian–Laird; N=2,884; 14 RCTs 2001–2025 including CASTA, CARS, CEREHETIS, Homberg ESCAS.
- **Funding/COI:** Authors declare **no financial support and no relationships** — independence upgrade vs Bornstein/Vester packages.
- **Primary result:** ΔNIHSS MD +1.39 (95% CI 0.53–2.25; P=0.020; **I²=62.5%**; only 6/14 trials contributed MD data, N=1,521). mRS 0–2 RR 1.31 (0.90–1.91; NS; I²=80.3%). SAE RR 1.08 NS; mortality RR 0.86 NS; hemorrhagic transformation RR 0.55 (0.32–0.92).
- **Authors’ GRADE (Table 8):** NIHSS moderate; mRS 0–2 moderate; SAE/mortality/HT high. **Internal inconsistency:** body text states mRS was rated **low** certainty (downgraded for inconsistency + imprecision); Table 8 lists moderate. Methodologist judgment: **mRS should be Low–Moderate at best** given I²=80%, CI crossing 1, and CASTA neutrality.
- **Design strengths:** Independent authors; contemporary trial set; explicit GRADE; stratification by follow-up ≤30 vs >30 d; transparent RoB traffic-light (12/14 low overall RoB per authors).
- **Design weaknesses:**
  1. **Cureus venue** — peer-reviewed but lower selectivity; rapid cycle (review began 08/08/2025, published 08/26/2025).
  2. NIHSS pooling uses only 6 trials with extractable MDs; remaining 8 not in primary continuous analysis → selective contribution.
  3. High heterogeneity for both NIHSS and mRS; >30-day NIHSS subgroup MD 0.97 (−1.61 to 3.56) **NS** and dominated by CASTA weight.
  4. GRADE “High” for SAE/mortality is optimistic relative to Cochrane Ziganshina 2023 (possible non-fatal SAE increase, moderate certainty).
  5. Dichotomized mRS 0–2 loses ordinal information (Bornstein correctly preferred full-scale ordinal).
- **Conclusion alignment:** Authors appropriately conclude moderate-certainty early NIHSS benefit and **inconclusive long-term functional independence** — better calibrated than Bornstein on day-90 claims. **Probable** for modest early NIHSS; **Unknown** for routine day-90 mRS benefit in unselected AIS; moderate–severe day-90 **Speculative**.

### 2.3 CASTA (Heiss et al. 2012) — pivotal large RCT
- **Citation:** Heiss WD, et al. *Stroke.* 2012;43:630–636. PMID: 22282884; DOI: 10.1161/STROKEAHA.111.628537.
- **Design:** Multicenter Asia double-blind RCT; N=1,070 (529 Cerebrolysin / 541 placebo); 30 mL × 10 d within 12 h + ASA; primary = **combined global directional test** of mRS + BI + NIHSS at **day 90** (Wei–Lachin-style).
- **Result:** **Neutral** overall (global MW ≈ 0.50; no group difference). Median baseline NIHSS only 9 (mild); mortality ~5.4%. Post-hoc NIHSS>12 subgroup: NIHSS OR 1.27 (CI lower 0.97), mRS OR 1.27 (CI lower 0.90); mortality 10.5% vs 20.2% (HR ~1.97 lower bound >1).
- **Appraisal:** Highest external-validity individual stroke trial. Primary endpoint **pre-specified and missed**. Mild severity reduced assay sensitivity (floor effects) — **Established** observation. Subgroup signals are hypothesis-generating only (**Speculative** for confirmatory claims). Industry sponsorship typical for program; still the best single negative-overall RCT.

### 2.4 CARS / CARS-2 (Muresanu 2016; Guekht 2015/2017 package)
- **Citation:** Muresanu DF, et al. *Stroke.* 2016;47:151–159. PMID: 26564102; DOI: 10.1161/STROKEAHA.115.009416. Guekht A, et al. *Neurol Sci.* 2017 (CARS MA).
- **Design:** Multicenter DB RCT; primary **ARAT day 90** (upper-limb motor) with concurrent rehab; 30 mL × 21 d, start 24–72 h; N=208 CARS-1.
- **Result:** CARS-1 ARAT MW 0.71 (large; P<0.0001); multivariate 12-scale MW 0.62. CARS-2 milder baseline; combined MA positive early motor/NIHSS.
- **Appraisal:** Pre-specified primary motor endpoint hit in CARS-1 — stronger design than pure NIHSS-surrogate trials. **Industry-linked** investigators (Muresanu core EVER collaborator). CARS-2 attenuated severity/effects → combined package still positive but severity-dependent. Supports early motor recovery claim in selected moderate patients with structured rehab (**Probable** for ARAT in that niche; not equivalent to unselected day-90 mRS).

### 2.5 CAPTAIN II (Muresanu 2020) + Vester CAPTAIN prospective MA (2021)
- **Citations:**  
  - Muresanu DF, et al. *Neurol Sci.* 2020. PMID: 31897941.  
  - Vester JC, et al. *Neurol Sci.* 2021;42:4531–4541. PMID: 33620612; DOI: 10.1007/s10072-020-04974-6.
- **Design CAPTAIN II:** Phase IIIb/IV **single-center**, prospective, DB, placebo-controlled; N=142 enrolled / 139 analyzed; primary = **multidimensional ensemble of 13 outcome scales** at day 90 (Wei–Lachin MW).
- **Result:** MW_combined 0.59 (95% CI 0.52–0.66; P=0.0119) day 90; “small-to-medium.” CAPTAIN I (Asia-Pacific, n=46): ITT primary missed (P<0.1); PP significant. Prospective MA N=185: day 30 and 90 MW 0.60, significant.
- **Critical flags:**
  1. **Single-center CAPTAIN II** — major external-validity and operational-bias risk (center-specific rehab quality, rater culture, selection).
  2. **Endpoint multiplicity by design:** 13-scale ensemble increases sensitivity but complicates interpretation; stand-alone significance on subset of scales; multiplicity control via multivariate directional test is statistically coherent but clinically opaque (which domain drives care decisions?).
  3. **Same biometric/industry network** (Vester, Muresanu) as stroke MAs.
  4. Small absolute N for moderate–severe TBI claims; CAPTAIN I ITT failure undercuts robustness.
- **Conclusion alignment:** Authors claim confirmation of “beneficial effects… overall outcome after moderate to severe TBI.” Observed: positive multidimensional MW in single-center phase III/IV + small multi-site pilot. **Does not establish** multi-center, independently replicated day-90 functional benefit. Grade: **Speculative–Probable** (signal present; single-center + industry + multiplicity limit).

### 2.6 Gauthier et al. 2015 — AD meta-analysis
- **Citation:** Gauthier S, et al. *Dement Geriatr Cogn Disord.* 2015;39:332–347. PMID: 25832905; DOI: 10.1159/000377672.
- **Design:** 6 RCTs Cerebrolysin vs placebo, mild–moderate AD; cognition SMD, global clinical change OR, combined “global benefit” MW; safety.
- **Results:** Cognition SMD −0.40 at 4 weeks (P=0.0031); at 6 months SMD −0.37 **NS** (CI −0.90 to 0.16). Global clinical change OR 3.32 (4 wk) and 4.98 (6 mo). Global benefit MW 0.57 both time points. Safety ≈ placebo.
- **Appraisal:** Small–moderate short-term cognitive/global effects; **6-month cognition CI crosses null**. Trials generally small, older, often Eastern Europe/Asia, IV cyclic dosing not US-standard-of-care. Author network includes Vester; manufacturer-adjacent program history. Not FDA-approved; no large modern confirmatory AD RCT with biomarker staging.  
  **Conclusion alignment:** “Overall beneficial effect and favorable benefit-risk” — overstates durability. Short-term CGI/cognition **Probable** (with COI caveats); sustained 6-month cognitive benefit **Unknown/Speculative**; disease modification **Unknown**.

### 2.7 Cochrane VaD — Chen et al. 2013
- **Citation:** Chen N, et al. *Cochrane Database Syst Rev.* 2013;(1):CD008900. DOI: 10.1002/14651858.CD008900.pub2. PMID: 23440834.
- **Design:** Independent Cochrane SR; 6 RCTs, N=597 VaD.
- **Results:** MMSE WMD +1.10 (0.37–1.82); ADAS-cog+ WMD −4.01 (−5.36 to −2.66); global response RR 2.71 (1.83–4.00); non-serious AEs RR 0.97 NS.
- **Authors’ conclusion (key):** Positive effects possible, **but insufficient evidence to recommend as routine treatment** — limited trials, variable treatment duration, short follow-up.
- **Appraisal:** Highest independence for VaD. Effect sizes small (MMSE ~1 point). Methodologically cautious conclusion is correctly calibrated. **Probable** small short-term cognitive/global benefit; **not Established** for routine use; long-term function **Unknown**.

### 2.8 Independent negative/cautious poles
- **Ziganshina et al. Cochrane AIS 2020/2023** (CD007026): Focused on death/SAE; moderate-certainty **no mortality benefit**; possible **increase in non-fatal SAE** (RR ~2.39 in some analyses). Does not pool full ordinal NIHSS/mRS the way Bornstein does — different PICO emphasis. Independence high; outcome selection (death-first) reduces power for recovery claims but correctly flags safety uncertainty vs industry MAs.
- **AHA/ASA 2019 AIS guidelines** (Powers et al., PMID 30869305): Cerebrolysin **not** standard endorsed therapy in US — literature vs guideline mismatch is real; methodologist does not defer to authority alone, but notes absence from high-income guideline algorithms reflects CASTA neutrality + regulatory status.
- **AlzDiscovery Cognitive Vitality (2016):** Independent-ish synthesis; AD metas positive with quality caveats; VaD small effect; **prevention Unknown**; generally safe short-term.

### 2.9 Safety MA — Strilciuc et al. 2021
- **Citation:** Strilciuc S, et al. *Pharmaceuticals.* 2021;14:1297. DOI: 10.3390/ph14121297.
- **Design:** 12 RCTs, N=2,202; SAE/mortality NS vs placebo; trend SAE reduction at 50 mL high dose.
- **Appraisal:** Consistent with Patel SAE RR~1.0. Authorship/network still Cerebrolysin-program adjacent. Discordance with Ziganshina non-fatal SAE signal unresolved without IPD re-analysis of SAE classification. Safety ≈ placebo for death/overall SAE is **Probable**; high-dose SAE reduction **Speculative**.

---

## 3. Bias Summary Table

| Source | Design tier | Industry / investigator COI | RoB (appraisal) | Selective endpoint / multiplicity | Publication / selection bias risk | Independence |
|--------|-------------|----------------------------|-----------------|-----------------------------------|-----------------------------------|--------------|
| Bornstein 2018 MA | SR/MA (IPD+agg) | **High** (EVER-linked authors, IDV biometry, manufacturer source help) | Mixed; some unclear conduct data | Primary = early NIHSS not day-90 mRS; severity-restricted day-90 | Moderate (CASTA outlier noted; positive early literature) | Low |
| Patel 2025 MA | SR/MA | **None declared** | Authors: 12/14 low RoB; 2 some concerns | Dichotomized mRS; only 6 trials in ΔNIHSS MD | Low–moderate (funnel minor asymmetry) | High (relative) |
| CASTA 2012 | Large multi-center RCT | Industry-sponsored program | Low (DB multi-center) | Primary day-90 global **missed**; post-hoc severe subgroup | N/A (negative overall) | Moderate |
| CARS 2016 | Multi-center RCT | High (Muresanu/EVER network) | Low reported | Pre-spec ARAT hit — good | Positive package | Low–mod |
| CAPTAIN II 2020 | **Single-center** RCT | High (same network) | Unclear center effects | **13-scale ensemble** multiplicity | Positive; small CAPTAIN I ITT miss | Low |
| Vester 2021 CAPTAIN MA | Prospective MA of series | High | Dependent on CAPTAIN quality | Multidimensional primary | Series controlled by same group | Low |
| Gauthier 2015 AD MA | SR/MA 6 RCTs | Network-linked (Vester co-author) | Variable small older RCTs | Combined global benefit | Positive short-term literature | Low–mod |
| Chen 2013 Cochrane VaD | Independent Cochrane | None | Limited by primary trial quality | Fair | Low | **High** |
| Ziganshina Cochrane AIS | Independent Cochrane | None | Focus death/SAE | Death-first PICO | Low | **High** |
| Strilciuc 2021 safety | SR/MA | Program-adjacent | Fair | SAE definition heterogeneity | Moderate | Low–mod |
| Product monographs | Labeling / marketing | Industry primary | N/A | Efficacy claims not evidence | High | None |

**Trust downgrade triggers activated:** industry funding without independent multi-center replication (stroke moderate–severe mRS; TBI CAPTAIN); single-lab/single-center novelty (CAPTAIN II); surrogate early NIHSS without consistent day-90 validation; post-hoc severity subgroups (CASTA); multidimensional ensembles with opaque clinical translation.

**Trust upgrade triggers:** CASTA pre-registered primary (negative); Patel independent GRADE; Cochrane independence; some dose–severity gradients (more severe → larger early effects — biologic coherence, not proof).

---

## 4. Statistical Adequacy

| Domain | Assessment | Certainty on methods claim |
|--------|------------|----------------------------|
| Early NIHSS pooling (Bornstein MW 0.60; Patel MD +1.39) | Nonparametric MW appropriate for ordinal NIHSS; Wei–Lachin MERT valid for stochastic ordering. Patel continuous MD limited to 6 trials with high I² (62%). Effect modest (~1.4 NIHSS points). | **Probable** statistical signal for early NIHSS under random-effects / MERT |
| Day-90 mRS unselected | Patel RR 1.31 NS, I²=80%; CASTA neutral primary; Bornstein positive only in NIHSS>12 subset N=314 | **Does not support** universal day-90 functional claim — **Established** discordance early vs late |
| Dichotomization vs ordinal | Dichotomized mRS 0–2 loses power and depends on cut-point; Bornstein full-scale ordinal preferable when available | Method preference: ordinal > dichotomized (**Established** methodologic principle) |
| CAPTAIN multidimensional Wei–Lachin | Multivariate directional test controls family-wise structure better than 13 separate tests; still hard to map to a single clinical decision threshold; CAPTAIN I ITT miss | Coherent stats, fragile external validity |
| Multiplicity (stroke MAs) | Multiple time points (21/30/90), scales (NIHSS/mRS/BI/ARAT), severity strata without closed testing in most packages | Inflates type I risk for secondary claims — **Probable** over-claim risk |
| Heterogeneity | High for day-90 function (I²~80%); lower for early NIHSS in severe strata | Severity is effect modifier — **Probable** |
| Safety (death/SAE) | Patel/Strilciuc NS; Ziganshina signals non-fatal SAE increase in subset | Discordant — treat SAE increase as **Unresolved** |
| Power | CASTA powered for mild population → failed assay sensitivity; CAPTAIN N~140 single-center underpowered for rare AEs and generalizable function | Limits firm negatives and firm positives |

---

## 5. External Validity

| Population / setting | Fit to trial evidence | Gaps |
|---------------------|----------------------|------|
| Mild AIS (NIHSS <8–10) | CASTA-like; floor effects; little room for drug benefit | Early NIHSS MAs overstate applicability to mild stroke |
| Moderate–severe AIS (NIHSS >12) | Best signal strata in Bornstein/CASTA post-hoc/CARS | Still no large independent multi-center confirmatory mRS-primary RCT in severe-only population |
| Post-thrombolysis / thrombectomy adjunct | CERE-LYSE-I, CEREHETIS, small MT cohorts (e.g., Staszewski 2025, ElBassiouny 2025) | Small / pilot; not guideline-changing |
| Moderate–severe TBI | CAPTAIN series only substantial modern package | **Single-center dominant**; Eastern European/Asia-Pacific centers; rehab co-intervention heterogeneous |
| Mild–moderate AD | Gauthier 6-RCT pool | Older trials; no modern amyloid/tau-staged cohorts; IV logistics limit US applicability |
| VaD | Cochrane 6 RCTs N=597 | Small effects; short FU; variable VaD diagnostic criteria |
| US / high-income guideline settings | Not FDA-approved; not AHA/ASA standard | Access, porcine origin, infusion logistics constrain |
| Dementia prevention / healthy cognitive enhancement | **No robust RCTs** | **Unknown** — do not extrapolate |

Geographic concentration (Eastern Europe, Russia, China, Iran, Asia) and investigator networks reduce generalizability to North American/Western European multi-ethnic stroke systems with high reperfusion rates.

---

## 6. Clinical Applicability

| Claim users may hear | Methodological support | Applicability grade |
|---------------------|------------------------|---------------------|
| “Improves early neurological recovery after AIS” | Bornstein + Patel; modest ΔNIHSS; industry + independent MAs align on direction | **Probable** for early NIHSS in moderate AIS with IV 30–50 mL × 10–21 d |
| “Improves day-90 functional independence (mRS)” | CASTA neutral overall; Patel mRS 0–2 NS; Bornstein only NIHSS>12 subset | **Unknown** unselected; **Speculative** moderate–severe only (final C3 adjudication) |
| “Safe as placebo” | Large safety MAs ≈ placebo death/SAE; Ziganshina non-fatal SAE concern | **Probable** overall tolerability; residual SAE classification uncertainty |
| “Works for moderate–severe TBI” | CAPTAIN multidimensional positive | **Speculative–Probable** — single-center + industry + ensemble endpoint |
| “Effective for mild–moderate AD” | Gauthier short-term CGI/cognition | **Probable** short-term global/cognitive change; **not** established disease modifier |
| “Effective for VaD” | Cochrane small benefit | **Probable** small short-term effect; **insufficient for routine recommendation** (authors correctly state) |
| “Prevents cognitive decline” | No prevention RCTs | **Unknown** |
| “Should be standard of care in AIS” | Conflicts with CASTA primary miss + AHA non-endorsement + mixed day-90 data | **Not supported** as universal standard |

**Harm-reduction applicability notes (methods → practice):** porcine-origin product (allergy, cultural/religious); epilepsy and severe renal impairment contraindications per label; IV infusion setting required; not oral research-chemical substitute. Monitoring should track seizure, infusion reactions, renal status.

---

## 7. Conclusion Alignment — Where Authors Outrun Data

| Source | Claim tone | Data boundary | Overreach? |
|--------|-----------|---------------|------------|
| Bornstein 2018 | Early NIHSS benefit + day-90 mRS benefit in moderate–severe | Day-90 based on N=314 severity subset, not full ensemble | **Yes** if read as general day-90 proof; **acceptable** if carefully limited to early NIHSS + severe subgroup hypothesis |
| Patel 2025 | Moderate-certainty early NIHSS; functional independence inconclusive | Aligns with pooled NS mRS | **Well calibrated** (minor GRADE table vs text inconsistency on mRS level) |
| CASTA authors | Neutral primary; favorable trend in severe | Correct | **No** overreach on primary |
| CAPTAIN / Vester | Confirms efficacy after moderate–severe TBI; “new horizon” | Single-center + multidimensional primary + small CAPTAIN I ITT fail | **Yes** — language exceeds multi-center confirmatory standard |
| Gauthier 2015 | Overall beneficial effect; clinicians should consider | 6-month cognition NS; small older RCTs | **Partial** — short-term yes; durable disease-modifying framing no |
| Cochrane VaD | Positive signals but insufficient for routine use | Matches small effects + short FU | **Exemplary calibration** |
| Ziganshina Cochrane | No mortality benefit; possible non-fatal SAE increase | Death/SAE-focused; does not refute early NIHSS recovery claims | Correct within PICO; sometimes over-read as “no clinical benefit of any kind” |
| Manufacturer materials | Broad efficacy across stroke/TBI/dementia | Selective citation of positive MAs | Marketing-adjacent — not efficacy proof |

---

## 8. GRADE-Style Summary for Long-Term Function (day ≥90 / sustained)

| Outcome | Certainty | Rationale |
|---------|-----------|-----------|
| Early neurological recovery (NIHSS ≤30 d) AIS | **Moderate** → label **Probable** | Multiple RCTs + 2 MAs; consistent direction; industry COI + heterogeneity downgrade |
| Day-90 mRS / functional independence AIS (unselected) | **Low / Very low** → **Unknown** | CASTA primary miss; Patel RR NS high I²; severity interaction unresolved without new large RCT |
| Day-90 mRS AIS moderate–severe only | **Low** → **Speculative** (final) | Subgroup/secondary analyses; needs dedicated confirmatory trial |
| Multidimensional day-90 outcome moderate–severe TBI | **Low** → **Speculative–Probable** | Positive CAPTAIN series; single-center + industry + ensemble endpoint |
| AD short-term (≤4–12 wk) global/cognition | **Moderate** → **Probable** | Consistent small–moderate effects in 6-RCT MA |
| AD sustained ≥6 mo cognition / disease modification | **Very low** → **Unknown** | 6-mo cognition CI crosses null; no modern biomarker trials |
| VaD short-term cognition/global | **Low–Moderate** → **Probable** small effect | Cochrane; insufficient for routine use |
| Prevention of cognitive decline | **None** → **Unknown** | No prevention RCTs |
| All-cause death AIS | **Moderate** no benefit → **Probable** null | Cochrane + Patel |
| SAE overall AIS | **Moderate** no increase (industry MAs) vs **Moderate** possible non-fatal increase (Cochrane) → **Unresolved / Probable** overall tolerability | Classification discordance |

---

## 9. Methodologist’s Bottom Line

1. **What the human evidence actually supports**  
   - Modest **early** neurological improvement after AIS (**Probable**).  
   - Small short-term cognitive/global gains in mild–moderate AD and VaD (**Probable**), insufficient for routine VaD recommendation per Cochrane.  
   - Safety broadly comparable to placebo for death and overall SAE rates (**Probable**), with residual Cochrane concern on non-fatal SAE.  
   - TBI: multidimensional signal in CAPTAIN (**Speculative–Probable** only).

2. **What it does not support**  
   - Universal day-90 functional independence benefit in unselected AIS (**Unknown**; CASTA neutral primary is decisive counterweight).  
   - Disease modification or dementia prevention (**Unknown**).  
   - Elevation to US guideline-standard therapy on current data.

3. **Structural evidence problems**  
   - Heavy **industry-tied MA and CAPTAIN authorship** (Bornstein, Muresanu, Vester packages).  
   - **Endpoint multiplicity** and early-NIHSS primacy vs day-90 mRS discordance.  
   - **Single-center CAPTAIN II** limits TBI generalizability.  
   - GRADE for long-term function remains **Low/Very low** until an independent, multi-center, mRS-primary (or GOSE-primary for TBI), adequately powered RCT in the severity band where signals concentrate is completed.

4. **Highest-value next evidence**  
   - Pre-registered, industry-independent, multi-center RCT: moderate–severe AIS (NIHSS >10–12), day-90 ordinal mRS primary, with reperfusion stratification.  
   - Multi-center TBI replication of CAPTAIN with a pre-specified single primary (e.g., GOSE or composite with limited multiplicity).  
   - Modern AD trial with biomarker confirmation and ≥12-month cognition/CDR-SB.

---

*Appraisal uses only published peer-reviewed and Cochrane sources cited above; no unpublished numbers invented. Certainty labels per evidence-grading.md.*
