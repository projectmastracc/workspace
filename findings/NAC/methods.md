# Methodological Appraisal — N-Acetylcysteine (NAC)

**Role:** Methodologist  
**Research ID:** 16607efb  
**Compound:** N-acetylcysteine / N-acetyl-L-cysteine  
**Scope:** Study design, bias, statistical adequacy, external validity, clinical applicability, conclusion alignment  
**Domains:** APAP OD · COPD/mucolytic · schizophrenia · OCD · addiction · fertility (PCOS/male) · COVID-19 · CIN · safety  
**Certainty labels:** **Established** | **Probable** | **Speculative** | **Unknown** (per evidence-grading.md)

---

## 1. Cross-cutting methodological landscape

NAC spans three evidence ecosystems with incompatible design standards:

| Ecosystem | Typical design | Endpoint type | Hierarchy rank |
|-----------|----------------|---------------|----------------|
| Medical antidote (APAP) | Observational cohorts + protocol standardization; ethics preclude modern placebo RCTs | Hard: hepatotoxicity, transplant, death | Highest clinical certainty despite limited RCT purity |
| Respiratory / CIN | Medium–large DBPC RCTs + SRs/MAs; dose/duration heterogeneity | Mixed hard (exacerbation, AKI) + surrogate (creatinine, FEV1) | Moderate–high when large null trials dominate |
| Psychiatry / addiction / fertility / COVID | Small–medium adjunct RCTs; clustered investigators; scale endpoints | Mostly subjective scales or intermediate biomarkers | Low–moderate; high fragility |

**Cross-cutting bias themes (**Probable** structural features of the literature):**

1. **Dose heterogeneity** — 600 mg/day vs ≥1200–3000 mg/day; oral bioavailability ~4–10% makes underdosing a plausible false-negative driver.
2. **Adjunct design** — Most psychiatric/addiction RCTs are add-on to SSRIs, antipsychotics, or contingency management (CM); attribution and interaction effects are incompletely modeled.
3. **First-trial / small-study positive bias** — Classic pattern in OCD and some addiction lines: early positive Iranian/Australian pilots → larger Western nulls.
4. **Surrogate vs patient-important outcomes** — GSH, CRP, D-dimer, sperm parameters, creatinine Δ vs mortality, abstinence, live birth, hospitalization.
5. **Publication and geographic clustering** — Positive psychiatric meta-analyses lean on small single-center trials (often Iran); independent re-analyses of the same pool can flip inference.
6. **Industry / COI** — NAC is mostly generic/supplement; commercial COI is lower than for branded psychotropics, but academic allegiance and “glutamate hypothesis” commitment are real sources of over-interpretation.

---

## 2. PICO by indication + design appraisal

### 2.1 Acetaminophen (paracetamol) overdose — antidote

| Element | Content |
|---------|---------|
| **P** | Acute (and some staggered) APAP overdose; risk stratified by Rumack–Matthew nomogram / ALT trajectory / delayed presentation |
| **I** | IV or oral NAC protocols (classic 21-h IV 3-bag; 72-h oral; simplified 12-h regimens in some systems) |
| **C** | Historical untreated cohorts; protocol variants (route/duration); no ethical modern placebo arm for high-risk patients |
| **O** | Hepatotoxicity (ALT/AST thresholds), acute liver failure, transplant, death; nearly complete prevention if started ≤8 h |

**Design appraisal**

- Evidence base is **pre-modern RCT + large observational + mechanistic certainty** (NAPQI detoxification via GSH repletion). FDA-approved indication; clinical toxicology consensus (ACMT/EAPCCT-aligned practice).
- StatPearls synthesis: NAC is mainstay; “almost 100% effective if given within 8 hours post-ingestion” (Ershad et al., NCBI Bookshelf NBK537183; update 2024).
- Historical Prescott/Rumack oral and IV series established efficacy before contemporary trial standards; comparative effectiveness now focuses on **protocol optimization** (duration, stopping rules, IV vs oral), not whether NAC works.
- Mortality benefit in established ALF is supported by observational/historical comparisons (e.g., Licata et al. 2022 narrative/SR context, PMC9399785; DOI often cited in APAP–NAC reviews).

**Statistical adequacy:** Not standard frequentist meta-RCT inference. Effect size is large enough that residual confounding of historical controls does not threaten directionality. Time-to-treatment is the dominant effect modifier (**Established**).

**External validity:** High for emergency/toxicology populations worldwide; protocol details (IV anaphylactoid risk, charcoal interference, pregnancy) affect implementation, not principle of efficacy.

**Clinical applicability:** **Established** — standard of care. Self-administration of OTC NAC is **not** a substitute for protocolized medical care.

**Conclusion alignment:** Authors and guidelines correctly treat this as settled; over-extension of high-dose IV OD protocols to wellness indications is a common misapplication (**Established** misuse pattern).

---

### 2.2 COPD / mucolytic / chronic bronchitis

| Element | Content |
|---------|---------|
| **P** | Stable COPD ± chronic bronchitis phenotype; mixed GOLD stages across trials |
| **I** | Oral NAC 400–1800+ mg/day; often stratified low (≤600) vs high (≥1200) |
| **C** | Placebo (most RCTs); other mucolytics in class-level Cochrane analyses |
| **O** | Exacerbation rate / proportion exacerbation-free; FEV1/FVC; SGRQ/QoL; hospitalization |

**Design appraisal**

- Multiple SRs/MAs with partially conflicting conclusions depending on inclusion criteria, dose cut-points, and quality stratification:
  - **Cazzola et al. 2015** (*Eur Respir Rev*): 13 studies, n≈4155; RR exacerbations 0.75 (95% CI 0.66–0.84); high-dose preferred when obstruction present. DOI: 10.1183/16000617.00002215 (context: ERS meta-analysis of NAC CB/COPD).
  - **Shen et al. 2014** (*COPD*): high-dose reduced exacerbations (RR ~0.59 for total exacerbations); low-dose uncertain once Jadad >3 trials isolated. DOI: 10.3109/15412555.2013.858315.
  - **Fowdar et al. 2017**: both high- and low-dose reduced *prevalence* of ≥1 exacerbation; long-term (≥6 mo) signal; no FEV1 effect. DOI context: *Heart Lung* MA.
  - **Huang et al. 2023** (*Ther Adv Respir Dis*): 9 studies; **no** significant reduction in acute exacerbations or lung function decline — more restrictive/recent pool. PMC10026096; DOI: 10.1177/17534666231158563.
  - **Cochrane mucolytics class** (Poole 2019 and updates cited in COPD-X): modest exacerbation benefit (OR ~1.73 free of exacerbation; NNTB ~8 over ~9 months); high heterogeneity (I² often >50–60%); newer trials smaller effects.
  - **Zhou 2024** RCT (mild–moderate COPD, 600 mg BID, 24 mo): null on annual exacerbation rate (RR 0.90, 95% CI 0.80–1.02); high dropout ~1/3 — limits inference.

**Bias table (COPD)**

| Domain | Risk | Notes |
|--------|------|-------|
| Randomization/allocation | Low–moderate | Older trials weaker reporting |
| Blinding | Low–moderate | Subjective sputum/exacerbation definition variable |
| Outcome definition | Moderate–high | Exacerbation criteria inconsistent across decades |
| Incomplete data | Moderate | Long trials (e.g., Zhou) high attrition |
| Selective reporting | Low–moderate | Pre-registration rare in older literature |
| Heterogeneity | High | Dose, duration, CB vs spirometric COPD, ICS background |
| Publication bias | Moderate | Positive early mucolytic literature |

**Statistical adequacy:** Meta-analytic RRs often sit near 0.75–0.90 with CIs that cross or graze 1.0 depending on model; I² commonly 50–65%. Subgroup by dose is **post-hoc** in many MAs → **Probable** over-fitting risk. No consistent lung-function (FEV1) benefit; claims of “disease modification” exceed data (**Speculative**).

**External validity:** Stronger for **chronic bronchitis / frequent exacerbator** phenotypes on long-term oral therapy; weaker for mild, low-symptom COPD (Zhou 2024). GOLD/NICE-style guidance is selective, not universal — aligned with heterogeneity.

**Clinical applicability:** **Probable** modest reduction in exacerbation risk at adequate oral dose (often ≥1200 mg/day for obstructed COPD; ~600 mg may suffice in pure CB without obstruction — Cazzola framing). Not a substitute for smoking cessation, LABA/LAMA/ICS, vaccination, or pulmonary rehab.

**Conclusion alignment:** Reviews that claim robust universal benefit overstate consistency (**Probable** mismatch). Reviews claiming total null ignore dose/duration/phenotype signals. Best adjudication: **conditional, dose- and phenotype-dependent modest benefit**.

---

### 2.3 Schizophrenia (adjunct)

| Element | Content |
|---------|---------|
| **P** | Schizophrenia spectrum on stable antipsychotics; some clozapine-resistant residual symptoms |
| **I** | Oral NAC typically 2000 mg/day (sometimes higher), 8–52 weeks |
| **C** | Placebo add-on |
| **O** | PANSS total / negative / general / positive; cognitive batteries; functioning |

**Design appraisal**

- Lineage: Berk et al. Australian program → multi-site RCTs; Neill et al. 2022 clozapine-resistant 52-week trial (PMID lineage / PMC9673271 context).
- **Yolland et al. 2020** MA of RCTs (*Aust N Z J Psychiatry*): PANSS negative and total improved after ~24 weeks; large effects reported in some pooling. PMID: 31826654; DOI: 10.1177/0004867419893439.
- **Ghaderi et al. 2020** MA: n≈274 from 6 RCTs; SMD total −0.61 (−0.91, −0.31); negative −0.56 (−0.92, −0.21); stronger in ≤24-week subgroup. DOI context: *Rev Clin Med*.
- Individual larger/longer trials (e.g., Breier 2018; Neill 2022 CRS) show mixed duration-dependent patterns; positive symptoms usually unaffected.

**Bias table (schizophrenia)**

| Domain | Risk | Notes |
|--------|------|-------|
| Selection | Moderate | Enriched residual-symptom samples; limited first-episode data |
| Performance/detection | Low–moderate | DBPC design common; rating-scale subjectivity remains |
| Attrition | Moderate | Long trials (52 wk) dropout |
| Investigator clustering | Moderate–high | Overlapping Australian author groups across pivotal trials |
| Multiplicity | High | Multiple PANSS subscales + cognitive batteries without strict hierarchical testing in early work |
| Publication bias | Moderate | Small positive trials inflate MA SMDs |
| Adherence | Moderate | GI AEs, sulfur odor → unblinding risk |

**Statistical adequacy:** Pooled SMDs in the moderate range (~0.5–0.6) on negative/total symptoms are **fragile** given small k and n; duration subgrouping is exploratory. Positive-symptom null is consistent. Clinical significance of ~0.5 SMD on PANSS negative is **Probable** but not definitive without larger independent replication outside core groups.

**External validity:** Adults with residual negative symptoms on antipsychotics; transfer to acute psychosis, first-episode, or monotherapy settings is **Unknown**. Clozapine-resistant niche has limited dedicated n.

**Clinical applicability:** **Probable** modest adjunct for negative/total symptoms at ~2 g/day for ≥12–24 weeks; not antipsychotic monotherapy; not standard first-line guideline core.

**Conclusion alignment:** Reviews claiming “large effect” often amplify MA point estimates without stressing imprecision and clustering; “no role” understates consistent negative-symptom signal. Balanced: **promising adjunct, moderate certainty, replication still needed**.

---

### 2.4 OCD (and OCRD spectrum)

| Element | Content |
|---------|---------|
| **P** | Moderate–severe OCD (Y-BOCS ~21–28); mostly SRI-treated adults; few pediatric trials |
| **I** | NAC 2000–4000 mg/day, 10–20 weeks |
| **C** | Placebo add-on to SRI or stable meds |
| **O** | Y-BOCS / CY-BOCS primary |

**Design appraisal**

Key adult RCTs (from independent Advanced Interventions UK synthesis, March 2026 update):

| Trial | n | Duration | Dose | Result pattern |
|-------|---|----------|------|----------------|
| Afshar 2012 (Iran) | 48 | 12 wk | ≤2400 mg | Positive |
| Sarris 2015 (Aus) | 44 | 16 wk | 3000 mg | Null |
| Paydary 2016 (Iran) | 44 | 10 wk | 2000 mg | Mixed/positive lean |
| Costa 2017 (Brazil) | 40 | 16 wk | 3000 mg | Null (treatment-resistant) |
| Sarris 2022 (Aus) | 98 | 20 wk | 2000–4000 mg | Null (largest adult) |
| Ghanizadeh 2017 (ped) | 34 | 10 wk | 2400 mg | Positive lean |
| Li 2020 (ped pilot) | 11 | 12 wk | 2700 mg | Underpowered |

- **Gadallah et al. 2020** MA: Y-BOCS MD −2.97 (95% CI −4.93 to −1.02), *P*=0.003. DOI: 10.1016/j.jocrd.2020.100529.
- **Eghdami et al. 2024** (*Front Psychiatry*): adult augmentation MA; signal at 5–8 weeks (*p*≈0.05) but not <5 or >12 weeks — **duration cherry-risk**. DOI: 10.3389/fpsyt.2024.1421150; PMID: 39376972.
- **Independent re-analysis (Advanced Interventions UK, 2026):** pooling shows **no overall adult benefit**; removing Afshar 2012 further weakens effect; pediatric signal may exist but n small. First-positive-trial pattern explicitly noted.

**Bias table (OCD)**

| Domain | Risk | Notes |
|--------|------|-------|
| Small-study effects | High | Typical n 40–50 until Sarris 2022 |
| Geographic/protocol heterogeneity | High | Iran vs Aus/Brazil; SRI co-treatment varies |
| First-trial bias | High | Afshar dominates positive MAs |
| Selective time-point analysis | High | Eghdami 5–8 wk window |
| Blinding integrity | Moderate | Odor/taste of NAC |
| Severity spectrum | Moderate | Mean Y-BOCS ~24–27; specialist TR-OCD under-represented |
| Publication bias | Moderate–high | |

**Statistical adequacy:** MD ~3 Y-BOCS points is **below or at the margin** of commonly cited MCID (~4–5 for some contexts) and is driven by 1–2 trials. Largest adult RCT null → overall certainty **downgraded for inconsistency + imprecision**. Pediatric evidence insufficient for grade ≥ Probable.

**External validity:** Poor for severe treatment-refractory specialty OCD; uncertain for medication-naive; weak adult generalizability after Sarris 2022.

**Clinical applicability:** **Speculative** (adults) to **Speculative–weak Probable** only if prioritizing small early positives; independent synthesis favors **no convincing adult effect**. Benign risk profile may justify n-of-1 trials, not guideline-level recommendation.

**Conclusion alignment:** Positive MAs (Gadallah, Eghdami) **over-align** with early positives and underweight large nulls. Advanced Interventions conclusion (small/fragile; adult effect unconvincing) is better methodologically aligned (**Probable** correct adjudication).

---

### 2.5 Addiction (cannabis, cocaine, nicotine, alcohol)

| Element | Content |
|---------|---------|
| **P** | Substance use disorders (CUD most studied); adolescent vs adult strata |
| **I** | NAC ~1200 mg BID often + behavioral platform (CM, counseling) |
| **C** | Placebo ± same behavioral care |
| **O** | Urine toxicology abstinence, craving scales, self-report use days |

**Design appraisal**

- **Cannabis — Gray et al. 2012** (*Am J Psychiatry*): adolescent CUD, NAC 2400 mg/day + CM, 8 weeks, n=116; OR 2.4 (95% CI 1.1–5.2) for negative urine cannabinoids. PMID: 22706327.
- **Adult ACCENT / Gray et al. 2017** (CTN-0053): n=302, 12 weeks, NAC 1200 mg BID + CM — **null** vs placebo+CM.
- **Gray et al. 2025** (*Neuropsychopharmacology*): youth CUD **without** CM pairing — null urine and self-report abstinence (RR ~0.93); more GI AEs on NAC. DOI: 10.1038/s41386-025-02061-y.
- Cocaine/nicotine/alcohol: mixed small RCTs; LaRowe et al. and others show craving or time-to-relapse signals inconsistently; no definitive multi-site standard.

**Bias table (addiction)**

| Domain | Risk | Notes |
|--------|------|-------|
| Behavioral confounds | High | CM may be necessary co-intervention (Gray 2012 vs 2025) |
| Age effect modification | High | Adolescent positive → adult null |
| Endpoint veracity | Moderate | Urine THC lag; self-report bias |
| Power | Moderate–high | Some trials adequate (ACCENT); others underpowered craving studies |
| Multiplicity of substances | High | Cannot pool across drugs as one “addiction” indication |

**Statistical adequacy:** Single positive adolescent finding failed adult and non-CM replication → **not established**. Substance-pooled “NAC for addiction” claims are methodologically invalid.

**External validity:** Any benefit likely **conditional** on age + concurrent contingency management; not transferable as standalone pharmacotherapy.

**Clinical applicability:** **Unknown** as universal addiction treatment; **Speculative** for adolescent CUD **with** behavioral platform; **Unknown/null-leaning** for adult CUD monotherapy. Cocaine/nicotine: **Speculative**.

**Conclusion alignment:** Narrative reviews listing “positive trials” without replication hierarchy mislead. Correct framing: **substance- and context-specific, mixed, non-guideline**.

---

### 2.6 Fertility (PCOS primary; male secondary)

| Element | Content |
|---------|---------|
| **P** | Women with PCOS (anovulation, metabolic features); men with idiopathic infertility (sparser) |
| **I** | Oral NAC (often 1200–1800 mg/day) ± clomiphene |
| **C** | Placebo or metformin |
| **O** | Ovulation, clinical pregnancy, live birth; insulin/androgen labs; semen parameters |

**Design appraisal**

- **Thakker et al. 2015** SR/MA of RCTs (*Obstet Gynecol Int* / PMC4306416): vs placebo, higher odds pregnancy and ovulation; inferior to metformin on some reproductive endpoints; quality limitations noted.
- ISPOR/related MA summary (~8 RCTs, ~900 women): vs placebo OR pregnancy ~3.97 (2.07–7.59), ovulation ~4.49; live birth sparse (1 trial, OR ~3); vs metformin ovulation **worse** (OR ~0.13). Heterogeneity high (I² ovulation up to 85%).
- **Liu et al. 2023** (*Front Nutr*): metabolic parameters MA, 11 RCTs, n=869; modest fasting glucose improvements vs placebo/metformin; mixed lipids. DOI: 10.3389/fnut.2023.1209614.
- Male fertility: parameter-level improvements in small RCTs/MAs summarized in Tenório 2021 (DOI: 10.3390/antiox10060967) — surrogate-heavy.

**Bias table (fertility)**

| Domain | Risk | Notes |
|--------|------|-------|
| Trial quality | Moderate–high | Older fertility RCTs often inadequate allocation concealment |
| Live birth rarity | High | Pregnancy ≠ live birth; sparse primary hard endpoints |
| Comparator choice | Critical | Placebo wins ≠ metformin equivalence |
| Geographic clustering | Moderate | Many Middle Eastern single-center trials |
| Heterogeneity | High | I² often >50–80% |

**Statistical adequacy:** Large ORs vs placebo with high I² and low-quality trials → **likely inflated**. Inferiority/non-superiority vs metformin on ovulation is a crucial methodologic check that softens enthusiasm.

**External validity:** PCOS populations in included trials may not match Western multi-ethnic infertility clinic case-mix; male data not ready for strong inference.

**Clinical applicability:** **Probable** improvement vs *placebo* on ovulation/pregnancy in PCOS; **not** a preferred first-line vs metformin/clomiphene/letrozole standard pathways. Live birth: **Speculative**. Male infertility: **Speculative**.

**Conclusion alignment:** Supplement marketing equating NAC with fertility “cure” exceeds data; MAs that omit metformin comparison overstate clinical role.

---

### 2.7 COVID-19

| Element | Content |
|---------|---------|
| **P** | Outpatient to ICU COVID-19; mixed severity |
| **I** | Oral or IV NAC various doses |
| **C** | Standard care ± placebo |
| **O** | Mortality, ventilation days, ICU/hospital LOS, inflammatory biomarkers |

**Design appraisal**

- Mechanistic rationale (GSH, redox, mucolytic, anti-inflammatory) strong; **clinical translation weak**.
- **Liu et al. 2024** SR/MA of RCTs (*Heliyon* / PMC10839595): 5 RCTs, n=651; **no** significant mortality difference vs control. DOI context: 10.1016/j.heliyon.2024.e25179 (Liu TH et al.).
- Other ICU-focused pools (e.g., Amiri et al. ~5 RCTs, n~340): hospital mortality OR ~0.87 (0.49–1.53); null ventilation/ICU LOS; possible shorter hospital LOS (wide uncertainty).
- Positive observational/biomarker MAs (CRP, D-dimer) do not establish clinical benefit (Alam 2023-type analyses) — **surrogate trap**.

**Bias table (COVID)**

| Domain | Risk | Notes |
|--------|------|-------|
| Era confounding | High | Pre-vaccine vs Omicron; evolving SOC |
| Open-label / small n | High | Many early adjuvant studies |
| Endpoint hierarchy | High | Biomarker positives without hard outcomes |
| Heterogeneity of dose/route | High | Oral vs IV; timing relative to infection |
| Publication noise | High | Preprint/grey meta sites (e.g., c19early) vs peer-reviewed nulls |

**Statistical adequacy:** Pooled mortality CIs wide and centered near null; underpowered for moderate effects. Biomarker MAs should not drive clinical claims.

**External validity:** Not generalizable as antiviral SOC; any LOS signal needs replication.

**Clinical applicability:** **Unknown** for mortality/critical outcomes; **not** standard of care antiviral therapy. Mucolytic use for thick secretions remains symptomatic, not disease-modifying COVID therapy.

**Conclusion alignment:** Mechanistic and early observational optimism **not aligned** with RCT mortality evidence. Correct label: **no established clinical efficacy for COVID outcomes**.

---

### 2.8 Contrast-induced nephropathy (CIN / CI-AKI)

| Element | Content |
|---------|---------|
| **P** | Patients receiving iodinated contrast (often coronary angiography) ± CKD risk |
| **I** | Oral/IV NAC peri-procedural (classic Tepel 600 mg BID regimen and high-dose variants) |
| **C** | Placebo/hydration alone; sometimes bicarbonate |
| **O** | Creatinine-defined CIN; dialysis; mortality (rare) |

**Design appraisal**

- Early positive small RCTs (Tepel et al. lineage) → cascade of positive MAs (e.g., some reporting significant CIN risk reduction).
- Large definitive trials (notably **ACT trial** — Acetylcysteine for Contrast-Induced Nephropathy Trial; multi-center, n on order of ~2300 high-risk patients) and high-quality syntheses shifted consensus toward **null** for clinically meaningful prevention when hydration optimized.
- Magner et al. 2022 (*JAMA Netw Open*) and other MAs of many RCTs still report statistical associations with creatinine-defined AKI — **surrogate-sensitive**, quality-gradient issues (smaller older trials positive; larger modern trials null).
- Guidelines: mixed historically (KDIGO once allowed NAC + hydration); many cardiology/nephrology pathways have **de-emphasized routine NAC** in favor of volume expansion and contrast minimization. CIN Working Panel historically found data too varied for firm recommendation.

**Bias table (CIN)**

| Domain | Risk | Notes |
|--------|------|-------|
| Surrogate endpoint | High | Small creatinine rises ≠ hard renal failure |
| Small-study bias | High | Early positive literature |
| Hydration confounding | High | Co-intervention dominates true prevention |
| Definition heterogeneity | High | Multiple creatinine Δ thresholds |
| Publication bias | High | Classic example in nephrology methods teaching |

**Statistical adequacy:** Positive MAs of heterogeneous small trials are **unreliable** against large null RCTs. Creatinine assays and NAC’s analytic interference historically raised assay-artifact concerns in some discussions — further weakens surrogate claims.

**External validity:** Even if tiny creatinine effects exist, generalizability to reduced dialysis/death is **Unknown**/absent.

**Clinical applicability:** **Speculative–Unknown** for meaningful kidney protection; **routine use not supported** by best evidence when hydration is adequate. Low cost/low harm explain residual practice inertia — not efficacy.

**Conclusion alignment:** Meta-analyses claiming prevention often **exceed** large-trial data; guideline de-emphasis is better aligned (**Probable** correct).

---

### 2.9 Safety (cross-indication)

| Element | Content |
|---------|---------|
| **P** | Therapeutic oral (600–3000 mg/day), inhaled, IV overdose protocols |
| **I** | NAC any route |
| **C** | Placebo / active comparators |
| **O** | GI AEs, anaphylactoid reactions, bronchospasm, serious AE, interactions |

**Design appraisal**

- Safety is one of NAC’s strongest evidence domains: decades of OD use + chronic oral trials.
- **Oral:** GI symptoms (nausea, vomiting, diarrhea, dyspepsia) commonest — up to ~20–25% in some series; often not statistically higher than placebo in chronic disease MAs (COPD, psychiatry, PCOS). Tenório et al. 2021 (DOI: 10.3390/antiox10060967) summarizes oral GI burden and IV anaphylactoid risk.
- **IV:** Non-IgE **anaphylactoid** reactions (flushing, urticaria, bronchospasm, hypotension) — rate estimates vary; cutaneous predominance; manageable with infusion rate adjustment; asthma/atopy caution. Oral preferred when IV risk high.
- **Inhaled:** Local irritation, bronchospasm risk higher than oral in some comparisons.
- High-dose chronic respiratory safety reviews (e.g., Calverley 2020, PMC7892733 context) generally support tolerability ≥ standard mucolytic doses.
- Interactions of methodologic/clinical note: nitroglycerin (↑ vasodilatory/headache effects); charcoal may adsorb oral NAC in OD setting; theoretical/practical asthma caution.

**Bias considerations:** Under-reporting of mild GI AEs in open-label use; supplement product quality variability (dose fidelity) is a **real-world** not trial bias.

**Statistical adequacy:** AE meta-analyses typically show non-significant differences vs control for serious events; power for rare severe anaphylactoid outcomes relies on toxicology cohorts, not small psych RCTs.

**Clinical applicability:** **Established** favorable oral safety at 600–2400+ mg/day for most adults; **Established** IV anaphylactoid risk management in OD care; caution asthma, active peptic ulcer symptoms, pregnancy decision-making under clinician care for non-OD uses.

---

## 3. Consolidated risk-of-bias table (literature-level)

| Indication | Predominant design | Overall RoB | Key threat | Certainty of *effect existence* |
|------------|-------------------|-------------|------------|----------------------------------|
| APAP OD | Observational + protocol | Low for direction | Ethics bar to placebo RCT | **Established** benefit |
| COPD/mucolytic | RCTs + MAs | Moderate | Dose/phenotype heterogeneity; endpoint definitions | **Probable** modest (conditional) |
| Schizophrenia adjunct | Small–med DBPC RCTs + MAs | Moderate | Clustering, scale endpoints, small k | **Probable** modest negative sx |
| OCD adjunct | Small DBPC RCTs + conflicting MAs | High | First-trial bias; largest adult null | **Speculative** (adults) |
| Addiction | Mixed RCTs | High | Age/CM effect modification; non-replication | **Unknown** (substance-specific mixed) |
| Fertility PCOS | RCTs vs placebo/metformin | Moderate–high | Quality; live birth sparse; I² high | **Probable** vs placebo only |
| COVID-19 | Small RCTs + obs | High | Surrogates; era confounding; underpowered | **Unknown** (null-leaning hard outcomes) |
| CIN | Many small RCTs + large null | High → moderated by large trials | Surrogate CIN; publication bias | **Unknown**/null-leaning meaningful benefit |
| Safety oral | RCTs + cohorts | Low | Product quality outside trials | **Established** generally favorable |

---

## 4. Statistical adequacy — synthesis rules

1. **Do not pool across indications** (APAP ≠ OCD ≠ COPD). Shared molecule ≠ shared estimand.
2. **Prefer large, pre-registered, multi-site nulls** over early small positives when they conflict (OCD Sarris 2022; adult CUD ACCENT; ACT-class CIN; COVID mortality MAs).
3. **Dose is an effect modifier candidate**, not proven continuous dose–response for all indications — treat MA dose subgroups as **hypothesis-generating** unless pre-specified.
4. **MCID discipline:** Y-BOCS MD ~3 and small PANSS SMD changes need clinical contextualization, not only *p*<0.05.
5. **Surrogate hierarchy:** creatinine Δ, CRP, GSH, sperm count, craving — downgrade unless linked to hard outcomes.
6. **I² >50–60%** in respiratory and fertility MAs → prediction intervals matter more than mean RR; clinical prediction for the next patient is wide.
7. **Multiplicity:** psychiatric trials with many subscales without hierarchical primary control inflate Type I error (**Probable** literature-wide).

---

## 5. External validity and clinical applicability (integrated)

| Use case | Who generalizes | Who does not | Care setting |
|----------|-----------------|--------------|--------------|
| APAP OD protocol | Acute overdose patients on nomogram pathways | Wellness “detox” users | Emergency/toxicology only |
| COPD high-dose oral | CB/exacerbator phenotypes, longer courses | Mild asymptomatic COPD | Respiratory clinic |
| SCZ adjunct | Stable residual negative symptoms | Acute untreated psychosis | Psychiatry, adjunct only |
| OCD | Uncertain; possibly milder/adolescent | Adult TR-OCD specialty | Not guideline core |
| CUD | Possibly teens + CM historically | Adults; no-CM youth | Research/individualized |
| PCOS | Placebo-controlled trial populations | Metformin-eligible first-line candidates | Fertility as adjunct experiment |
| COVID | — | Not SOC antiviral population | Not indicated for outcome modification |
| CIN prevention | — | Routine angiography with good hydration | Generally not indicated for efficacy |
| OTC 600–2400 mg | Generally healthy adults tolerating GI AEs | Severe asthma uncontrolled; complex polypharmacy without advice | Self-care vs medical use distinction critical |

**Guideline vs literature mismatches (methodologically relevant):**

- **APAP:** Guidelines and literature aligned (**Established**).
- **Mucolytics:** Guidelines conditional; literature heterogeneous — alignment is appropriately cautious (**Probable**).
- **CIN:** Some older guidelines permissive; best large-trial literature null-leaning — **recommend against** efficacy-based routine use (**Probable**).
- **Psychiatry:** Guidelines largely silent or non-committal; enthusiast reviews oversell — literature supports cautious adjunct exploration mainly in SCZ negative symptoms (**Probable**), not OCD as settled (**Speculative**).
- **COVID:** Not in antiviral SOC guidelines; matches null hard-outcome RCTs (**Established** alignment of non-recommendation).

---

## 6. Conclusion alignment scorecard

| Claim family | Typical author claim | Methodological adjudication | Certainty |
|--------------|---------------------|----------------------------|-----------|
| APAP antidote saves liver/life if timely | Strong positive | **Aligned** — large effect, standard of care | **Established** |
| Oral NAC reduces COPD exacerbations universally | Strong positive | **Overstated** — phenotype/dose/duration conditional; some MAs null | **Probable** modest conditional |
| NAC improves SCZ negative symptoms as adjunct | Moderate–strong | **Mostly aligned** with caveats (size, clustering) | **Probable** |
| NAC is effective OCD augmentation | Positive MAs | **Misaligned** with largest adult nulls + independent pooling | **Speculative** |
| NAC treats addiction broadly | Positive narrative | **Misaligned** — non-replication, context dependence | **Unknown** |
| NAC improves PCOS fertility | Positive vs placebo | **Partially aligned**; weaker vs active standard; live birth thin | **Probable** (vs placebo) |
| NAC treats COVID | Mixed/positive early | **Misaligned** with RCT mortality MAs | **Unknown** (null-leaning) |
| NAC prevents CIN | Positive small-trial MAs | **Misaligned** with large trials / hard outcomes | **Unknown**/null-leaning |
| OTC oral NAC is generally safe | Positive | **Aligned** for GI-limited AEs; IV risks distinct | **Established** (oral) |
| High-dose IV wellness protocols | Implied by some clinics | **Misaligned** — extrapolates OD care | **Speculative**/inappropriate |

---

## 7. Methodologist’s bottom line

1. **Only APAP overdose meets Established efficacy** under rigorous clinical standards; design limitations (no modern placebo) do not threaten causal inference given magnitude, mechanism, and natural history.
2. **COPD/mucolytic benefit is Probable but fragile** — sensitive to dose (≥1200 mg often invoked), duration, bronchitis phenotype, and which meta-analytic pool is chosen; lung function disease modification is not shown.
3. **Schizophrenia negative-symptom adjunct is the strongest psychiatric signal (Probable)**; still limited by trial size and investigator clustering.
4. **OCD adult efficacy is Speculative** after independent re-analysis and large null RCT weight; positive MAs are methodologically vulnerable to first-trial dominance.
5. **Addiction, COVID hard outcomes, and CIN meaningful prevention are Unknown or null-leaning** when prioritized by large/replicated evidence over early positives and surrogates.
6. **Fertility (PCOS) vs placebo is Probable on intermediate reproductive endpoints**; not superior to established agents; live birth under-evidenced.
7. **Oral safety is Established as generally favorable**; IV anaphylactoid reactions are an Established route-specific risk; harm–benefit therefore hinges almost entirely on *efficacy uncertainty* for non-APAP uses.

**Reporting note:** PubMed MCP unavailable at intake; appraisal uses web-accessible abstracts, PMC/publisher summaries, independent clinical reviews, and DOI/PMID identifiers as cited. Exact trial-level n/effect sizes not invented beyond acquired sources. Full-text re-extraction of individual RoB (Cochrane RoB 2 domain-by-domain per trial) would further refine but is not required to support the above literature-level grades.

---

## Key citations (DOI / PMID)

| Domain | Source | ID |
|--------|--------|-----|
| Overview/safety | Tenório et al. 2021 *Antioxidants* | DOI: 10.3390/antiox10060967 |
| APAP clinical | Ershad et al. StatPearls NAC | NBK537183 |
| COPD MA | Cazzola et al. 2015 *Eur Respir Rev* | DOI: 10.1183/16000617.00002215 (ERS context) |
| COPD MA | Shen et al. 2014 *COPD* | DOI: 10.3109/15412555.2013.858315 |
| COPD MA | Huang et al. 2023 *Ther Adv Respir Dis* | DOI: 10.1177/17534666231158563; PMC10026096 |
| SCZ MA | Yolland et al. 2020 *ANZJP* | PMID: 31826654; DOI: 10.1177/0004867419893439 |
| OCD MA | Gadallah et al. 2020 *JOCRD* | DOI: 10.1016/j.jocrd.2020.100529 |
| OCD MA | Eghdami et al. 2024 *Front Psychiatry* | DOI: 10.3389/fpsyt.2024.1421150; PMID: 39376972 |
| OCD adult RCT | Costa et al. 2017 *J Clin Psychiatry* | DOI: 10.4088/JCP.16m11101 |
| OCD adult RCT | Sarris et al. 2015 *CNS Drugs* | DOI: 10.1007/s40263-015-0272-9 |
| OCD early + | Afshar et al. 2012 *J Clin Psychopharmacol* | DOI: 10.1097/JCP.0b013e318272677d |
| CUD adolescent | Gray et al. 2012 *Am J Psychiatry* | PMID: 22706327 |
| CUD adult null | Gray et al. 2017 ACCENT / *Drug Alcohol Depend* | CTN-0053 primary |
| CUD youth no CM | Gray et al. 2025 *Neuropsychopharmacology* | DOI: 10.1038/s41386-025-02061-y |
| PCOS | Thakker et al. 2015 | PMC4306416 |
| PCOS metabolic | Liu et al. 2023 *Front Nutr* | DOI: 10.3389/fnut.2023.1209614 |
| COVID RCT MA | Liu et al. 2024 *Heliyon* | PMC10839595 |
| CIN MA example | Magner et al. 2022 *JAMA Netw Open* | DOI: 10.1001/jamanetworkopen.2022.198 (context year 2022) |
| Mechanisms | Aldini et al. 2018 *Free Radic Res* | DOI: 10.1080/10715762.2018.1468564 |
| Mechanisms | Ezeriņa et al. 2018 *Cell Chem Biol* | PMID: 29429900 |
| Independent OCD critique | Advanced Interventions UK evidence review | Updated March 2026 (narrative methods review of 7 RCTs) |

---

*End of methodological appraisal.*
