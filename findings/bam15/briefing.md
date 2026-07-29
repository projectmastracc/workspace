# BAM15 — Full Compound Profile

**Slug:** `bam15`  
**Type:** Compound profile  
**Research ID:** 67f68056  
**Date:** 2026-07-29  

---

## 1. Executive Card

| Field | Content |
|-------|---------|
| **Compound** | BAM15 (BAM-15); N5,N6-bis(2-fluorophenyl)[1,2,5]oxadiazolo[3,4-b]pyrazine-5,6-diamine; furazano[3,4-b]pyrazine protonophore uncoupler |
| **Class** | Synthetic mitochondrial protonophore (structurally unrelated to DNP/FCCP) |
| **Primary use cases** | Experimental fat loss / energy-expenditure agonist; metabolic insulin sensitization; NAFLD/NASH research; “safer uncoupler vs DNP” narrative in RC communities |
| **Regulatory / human status** | **No published human clinical trials.** Preclinical only. Research-chemical market exists; not approved as a drug or dietary supplement |
| **Bottom line** | BAM15 is a selective mitochondrial protonophore that, in mice, raises oxygen consumption, burns fat, and improves multi-tissue insulin sensitivity **without** reducing food intake, lean mass, or core body temperature at effective doses. It is ~7× more potent than DNP on OCR in vitro and maintains a wide OCR plateau without plasma-membrane depolarization (unlike FCCP). Oral BA ~67%, t½ ~1.7 h (mouse) — short for ideal human once-daily oral use. All efficacy/safety claims above the molecular level are **rodent-only** unless labeled otherwise. Forum self-use is sparse, dose-guessy, and reports local heat / HR effects that mouse papers largely did not emphasize. |
| **Biggest upsides** | Fat-selective mass loss + EE↑ without appetite cut (**Probable** mouse; **Unknown** human); lean mass preservation (**Probable** mouse); broad OCR window vs DNP (**Established** in vitro); no plasma-membrane depol (**Established**); liver TG / IR improvement (**Probable** mouse); mild antioxidant signature (**Probable** mouse) |
| **Biggest downsides / sides** | Zero human PK/safety (**Established** gap); short half-life / formulation pain (**Established** mouse); high-dose lethargy (mouse, partly vehicle-confounded) (**Probable**); forum tachycardia / facial heat / rare visual blur (**Speculative** human); class-level overdose risk if dose runaway (**Speculative** but mechanistically real for any protonophore); cardiac biphasic STAT3 (low protect / high injure) in cardiomyocytes (**Probable** in vitro); RC purity unknown (**Speculative** product risk) |
| **Stack role** | Experimental EE lever for body-comp / metabolic research. **Do not** stack with other chemical uncouplers (DNP, high-dose niclosamide, etc.). Orthogonal to GLP-1 appetite pathways; additive EE logic with training/NEAT is mechanistic but unproven in combination. |

---

## 2. Chemistry, Classification, PK

### Structure and mechanism class

- **Chemotype:** Bis(2-fluoroaniline)-substituted oxadiazolo-pyrazine (furazanopyrazine).  
- **Mode:** Lipophilic weak-acid **protonophore** — shuttles H⁺ across the inner mitochondrial membrane (IMM), dissipating Δp (ΔΨm + ΔpH) independent of ATP synthase.  
- **Protonophoric moiety:** Aniline NH (SAR work treats this as the key acidic proton for shuttling).  
- **Not:** UCP activator, ANT-required uncoupler, or ETC electron donor. Respiration remains rotenone-/antimycin-sensitive; ANT block (CAT) does not abolish BAM15 OCR (**Established**, Kenwood 2014).

### Differentiation from classical tools

| Property | BAM15 | DNP | FCCP |
|----------|-------|-----|------|
| OCR potency (approx.) | EC50 ~1.4 µM (NMuLi) | ~10 µM | Similar potency to BAM15 at low end |
| OCR plateau width | Wide (µM–tens of µM) | Narrow; high dose → respiratory inhibition | Narrower; fails at higher doses in cells |
| Plasma membrane depol | **No** (voltage/current clamp) | Yes (classically off-target) | **Yes** (clear) |
| Cytotoxicity (cell models) | Lower than equipotent FCCP | Narrow therapeutic index historically | Higher than BAM15 |
| Core temp (mouse effective EE) | No rise up to solubility-limited ~200 mg/kg p.o. acute | Hyperthermia risk is the defining toxicity | Tool compound, not anti-obesity drug |

**Certainty:** Molecular differentiation **Established** (Kenwood 2014; Alexopoulos 2020 head-to-head).

### Pharmacokinetics (mouse only)

| Parameter | Value | Source / notes | Certainty |
|-----------|-------|----------------|-----------|
| Oral bioavailability | ~**67%** | Alexopoulos 2020 (AUC p.o. vs i.v.) | **Established** (mouse) |
| t½ plasma | ~**1.7 h** | 10 mg/kg p.o.; Cmax ~8.2 µM | **Established** (mouse) |
| Diet admixture exposure | Serum ~**5–10 µM** overnight; ~**3 h** half-life in diet PK context | Axelrod ~85 mg/kg/day from 0.1% w/w HFD | **Probable** |
| Tissue distribution | **Liver-primary**; gradual clearance ~4 h; also lipid-rich depots (WAT > many lean organs); **brain low** | Oral 50 mg/kg tissue time-course | **Established** (mouse) |
| Solubility | **Low aqueous**; high p.o. doses become suspension/paste | Limits max practical dose | **Established** |
| Human PK | **None published** | — | **Unknown** |

**Formulation implication:** Short t½ → split dosing or continuous dietary exposure in animals. Developers (Santos/Hoehn / Continuum Biosciences) have publicly stated BAM15’s half-life is suboptimal for ideal human oral once-daily and pursue longer-exposure analogs/related chemotypes.

### Routes (research practice)

- **Lab animals:** Oral gavage (methylcellulose suspensions), diet admixture 0.05–0.15% w/w, i.p. (AKI models 1–5 mg/kg).  
- **RC market:** Oral liquids and “research injectable” solutions appear; purity, solvent (DMSO/oils), and actual content are **unverified**. Injectables add sterile/pyrogen risk on top of compound risk (**Speculative** product quality).

---

## 3. Complete Pathway Map (Known + Hypothesized)

| ID | Target / pathway | Known vs hypothesized | Downstream | Phenotypes | Key evidence | Certainty |
|----|------------------|----------------------|------------|------------|--------------|-----------|
| **P1** | IMM protonophore; ΔΨm↓ | Known | Uncouples ETC from ATP synthase; OCR↑; ATP per O₂↓ | EE↑; heat generation capacity | Kenwood; Firsov bilayers/mito | **Established** |
| **P2** | Compensatory substrate oxidation | Known (rodent) | Fat oxidation↑; RER↓; hepatic palmitate oxidation↑ | Fat mass↓ without intake↓ | Alexopoulos CLAMS + ¹⁴C-palmitate | **Established** mouse |
| **P3** | Mild uncoupling → ROS↓ | Known (class) / shown in BAM15 liver | Electron dwell time↓; superoxide↓; GSH↑; 4-HNE↓; eicosanoids↓ | Antioxidant / anti-inflammatory lipid profile | Liver metabolomics Alexopoulos | **Probable** |
| **P4** | AMPK | Context-dependent | Glucose uptake, FAO, anti-lipogenic gene programs | IR improvement; less de novo lipogenesis | Cited in reviews; **not** always phosphorylated in chronic BAM15 liver (Alexopoulos: ATP and AMPK unchanged chronically) | **Probable** acute/local; **Speculative** as universal chronic driver |
| **P5** | PGC-1α / mito biogenesis | Hypothesized–partial | TFAM, OXPHOS genes, quality control | Better mito network in stressed muscle | Sepsis/sarcopenia literature axes | **Probable** some models |
| **P6** | Mitophagy (PINK1–ubiquitin) + fusion (Mfn2↑, fission proteins↓) | Known in sarcopenic obesity models | Clear damaged mito; network remodeling | Attenuates sarcopenic obesity phenotype | Dantas 2022 | **Probable** |
| **P7** | Hepatic lipid clearance | Known | TG/NEFA↓; histology Oil Red O clears | NAFLD improvement | Alexopoulos; db/db Chen | **Established** mouse |
| **P8** | Multi-tissue insulin sensitivity | Known | Clamp GIR↑; muscle 2-DG uptake↑; adipose NEFA suppression↑; hepatic glucose output intermediate | Glucose tolerance, lower insulin | Hyperinsulinemic-euglycemic clamp | **Established** mouse |
| **P9** | Glucagon / late gluconeogenesis enzymes (G6Pase, FBPase) | Known db/db context | Hepatic glucose output↓ | Glycemia↓ | Chen et al. 2023 | **Probable** |
| **P10** | SREBP / ChREBP / Fasn / Scd1 lipogenic program↓ | Known | Less adipogenesis/DNL signaling | Fat accretion↓ | Gene/protein work in obesity papers | **Probable** |
| **P11** | NLRP3 inflammasome via NFκB nuclear translocation↓ | Known (class of chemical uncouplers incl. BAM15) | IL-1β program↓ | Anti-inflammatory | Hu 2021 | **Probable** |
| **P12** | Macrophage M1→M2 (glycolysis constraint) | Known LPS/sepsis models | Cytokine skew anti-inflammatory | Sepsis adjunct phenotype | Dang 2021 | **Probable** |
| **P13** | mtDNA release / mtROS loop in septic AKI | Known | Neutrophil/tubule injury↓ | Survival / creatinine benefit mouse sepsis | Tsuji JCI 2023 | **Probable** |
| **P14** | STAT3 biphasic in cardiomyocytes | Known in vitro | Low uncoupling: mitoROS/JAK → Tyr705 STAT3 protect; high: blocks AMPK–Ser727 path → injury, ATP↓ | Cardioprotection vs cardiotoxicity by dose | Gao 2018 | **Probable** in vitro; human dose mapping **Unknown** |
| **P15** | No plasma-membrane protonophore effect | Known | Avoids FCCP-like cytotoxicity/electrophysiology | Wider safe OCR window in cells | Kenwood clamp data | **Established** |
| **P16** | Core temperature set-point | Known mouse at tested doses | Heat dissipated within thermoregulatory capacity | “Thermoneutral fat loss” marketing claim | Rectal probe to 200 mg/kg; thermal imaging studies | **Established** mouse; **Unknown** human |
| **P17** | Cancer OXPHOS vulnerability | Known models | ΔΨm collapse, ROS, caspase, proliferation↓ | Anti-tumor in breast/AML/melanoma models | Zunica 2021; others | **Speculative** for therapy |
| **P18** | C. elegans lifespan / neurodegeneration relief | Model organism | Mito respiration support | Longevity phenotype worm | Cho 2022 | **Speculative** human |
| **P19** | Autonomic / HR response to EE↑ | Hypothesized | Compensatory CO / sympathetic tone | Palpitations, facial flush (forum) | Sparse self-logs | **Speculative** |
| **P20** | Systemic ATP stress / perceived fatigue | Hypothesized | CNS or muscle energetic cost | Lethargy, “detachment” | High-dose mouse + forum | **Speculative** |
| **P21** | Local heat without core fever | Hypothesized | Peripheral thermogenesis / flush | Face/ear heat | Forum vs mouse core | **Speculative** |
| **P22** | Mild BUN↑ / amino acid oxidation | Observed mouse | Urea cycle intermediates↑ | Lab flag without creatinine rise | Alexopoulos biochem | **Probable** mouse; clinical meaning **Unknown** |
| **P23** | Limited CNS exposure | Known distribution | Low brain levels | Little direct psychoactivity expected | Tissue Kp | **Probable** |
| **P24** | Mitochondrial Ca²⁺ efflux / handling | Biophysics | Matrix Ca²⁺ dynamics | Unclear systemic phenotype | Firsov 2021 | **Speculative** for user-facing effects |

---

## 4. Clinical Evidence (Full Evaluation)

### Human evidence

| Tier | Finding | Certainty |
|------|---------|-----------|
| Systematic reviews / meta-analyses of BAM15 in humans | **None** | — |
| RCTs / open-label human trials | **None published** | **Established** gap |
| Observational / case series | **None peer-reviewed** | — |
| Regulatory | Not approved; highest phase listed publicly as **preclinical** for BAM-15 entity | **Established** |

**What clinical data do *not* show:** human fat-loss effect size, human therapeutic index, human hyperthermia risk curve, human cardiac safety, human drug–drug interactions, pregnancy safety, long-term mito adaptation, performance impact on athletes.

Related context (not BAM15): historical DNP human weight loss (~2–3 lb/week at ~3 mg/kg) proves the **class** can work in humans but with lethal hyperthermia risk — **not** transferable as safety proof for BAM15.

### Preclinical — cornerstone studies

#### Kenwood et al., *Mol Metab* 2014 (discovery)

- **Design:** Library screen → OCR, ROS filter, Seahorse, isolated mito, swelling (protonophore proof), ANT independence, whole-cell electrophysiology vs FCCP, MTT cytotoxicity, renal I/R (1–5 mg/kg i.p.).  
- **Results:** Equal potency to FCCP on OCR but **wider range**; **no plasma membrane depol**; less cytotoxic; AKI protection.  
- **Limits:** Tool-compound focus; not chronic obesity study.  
- **Certainty for mechanism claims:** **Established**.

#### Alexopoulos et al., *Nat Commun* 2020 (obesity reverse + PK + clamp)

- **Design:** Male C57BL/6J; WD 45% fat; BAM15 0.05–0.15% w/w diet; prevention (8 d) and reversal (4 wk WD then 5 wk ±0.1%); CLAMS; EchoMRI; i.p. GTT; full hyperinsulinemic-euglycemic clamp; liver metabolomics; toxicity panels; acute p.o. temp and VO₂.  
- **Effect sizes (directionally):**  
  - OCR: 50 mg/kg p.o. ~+30% first hour; 100 mg/kg ~+50%; 0.1% diet ~+15% dark-cycle VO₂; RER↓.  
  - Fat: 0.1–0.15% fully prevents WD fat gain; reversal ~15% lower BW almost all fat; lean mass stable; intake unchanged.  
  - Clamp: GIR restored toward chow; muscle and epi-fat glucose uptake↑.  
  - Liver: TG normalized; GSH 2.3×; 4-HNE ↓49%.  
  - Temp: no rise 10–200 mg/kg acute.  
  - Biochem: TG↓; BUN mildly↑ still in reference; ALT/AST/CK/creatinine clean.  
- **COI:** Hoehn, Santos, Tucker — financial interest in Continuum Biosciences.  
- **Limits:** Male-only; room-temperature housing (thermoneutrality not fully tested for EE claim); solubility capped dose escalation; short chronic windows (weeks).  
- **Certainty:** Anti-obesity + IR reverse in this model **Probable** (high-quality rodent, not human).

#### Axelrod et al., *EMBO Mol Med* 2020

- **Design:** HFD ±0.1% BAM15; ~85 mg/kg/day intake; tissue enrichment LC-MS; comparison to weight-matched CR.  
- **Results:** Oral availability; preferential lipid-rich tissue enrichment; protects DIO; EE and glycemic benefits; lean mass not sacrificed vs diet matching.  
- **Limits:** Same species/sex biases as field norms.  
- **Certainty:** **Probable** convergent with Alexopoulos.

#### Other disease contexts (summary)

| Context | Model | Direction | Certainty for human use |
|---------|-------|-----------|-------------------------|
| db/db metabolic disease | Chen 2023 | Glycemia, liver TG, glucagon axis improve; lean preserved | **Speculative** human |
| Sarcopenic obesity | Dantas 2022 | Mitophagy/Mfn2; muscle quality | **Speculative** human |
| Sepsis / AKI | Tsuji 2023 JCI | mtDNA/mtROS/neutrophils; mortality link | **Speculative** (different indication) |
| NLRP3 | Hu 2021 | Shared uncoupler class effect | **Probable** mechanism, not a clinical anti-inflammatory claim |
| Cardiomyocyte | Gao 2018 | Biphasic STAT3 / dose | **Warning-relevant** **Probable** in vitro |
| Breast cancer / AML | Zunica etc. | Anti-proliferative | **Speculative** oncology |
| C. elegans | Cho 2022 | Lifespan / neurodegeneration | **Speculative** |

### Negative / null / limiting findings worth equal weight

- Chronic BAM15 liver did **not** show ATP drop or AMPK hyperactivation in Alexopoulos — so “AMPK drug” framing is oversimplified.  
- Solubility, not hyperthermia, stopped acute dose escalation.  
- Controlled-release / liver-targeted **DNP** analogs improved NASH metrics but often **lost** anti-obesity effect — BAM15 is rarer in retaining fat loss + lean preservation among modern uncouplers (niclosamide can hit lean mass; OPC-163493 anti-diabetes without adiposity change).  
- Short t½ is an explicit translational bottleneck (VT News / developers).

---

## 5. Anecdotal / Forum Evidence (Full Evaluation)

| Theme | Consistency | Typical dose/context | Concordance with clinical/preclinical | Certainty ceiling |
|-------|-------------|----------------------|----------------------------------------|-------------------|
| “Safe DNP” marketing | High (vendor/Reddit product posts) | RC 25 mg/mL liquids; oral or SQ/IM claims | **Partial** — mouse thermoneutrality supports *relative* safety story; **not** human proof | **Speculative** as human safety claim |
| Fat loss efficacy | Low–moderate (few detailed logs) | Vendor HED ~50–90 mg/day extrapolated from 10 mg/kg mouse | Literature-silent in humans; mechanism-plausible | **Speculative** |
| Facial/ear heat, “thermic” feel | Moderate in small log threads | Injected ~4–5 mg in one multi-day log; YouTube comment 5 mg | Contradicts “zero thermal” marketing if local heat real; compatible with mild peripheral EE | **Speculative** |
| HR elevation / palpitations | Moderate in same sparse logs | Same low-mg inject range | Mechanistic (EE/autonomic) plausible; mouse papers didn’t feature tachycardia | **Speculative** |
| Acclimation (sides fade over days) | Low–moderate (single threads) | Week-long inject logs | Unknown biology (habituation vs cumulative?) | **Speculative** |
| Blurry vision brief | Low (isolated reports) | With heat/pressure-in-chest reports | Literature silent; treat as stop signal if real | **Speculative** |
| Lethargy | Low (echoes mouse high-dose) | Higher research doses / paste | Partial concordance with animal high-dose behavior | **Speculative** human |
| HED dose calculators (0.8 mg/kg etc.) | High in RC communities | BSA formula mouse→human | **Not validated** for uncouplers; ignores species EE scaling, t½, protein binding | **Speculative** / often **misleading** |
| Stack with GLP-1s | Emerging interest (GLP1forum) | BAM15 “EE” + GLP-1 “intake” | Orthogonal pathways in theory; no combo data | **Speculative** |

**Weighing:** Forum signal is **thin** compared to tren/test/DNP communities. Most “content” is vendor rewrites of Alexopoulos/Axelrod abstracts. The few first-person inject logs matter precisely because they contradict simplistic “no thermal effect whatsoever” marketing — while still not establishing mouse-like safety. Literature silence ≠ absence of human sides; sparse anecdotes ≠ Established risk rates.

---

## 6. Desired Effects — Mechanism Depth

### 6.1 Fat loss / body recomposition

- **Phenotype:** Preferential fat mass reduction; lean mass preserved; food intake unchanged (mouse).  
- **Pathways:** P1 → P2 → P7/P10; adipose NEFA release fuels oxidation elsewhere.  
- **Chain:** Proton leak → more substrate burned per ATP formed → negative energy balance without CNS appetite drug.  
- **Clinical:** Human **Unknown**. Mouse **Probable** (multiple labs, prevention + reversal).  
- **Forum:** Weak logs; strong marketing.  
- **Practical:** Any human effect size and dose are **Speculative**. Expect less “feel” than DNP if thermoneutral.

### 6.2 Energy expenditure / metabolic rate

- **Phenotype:** VO₂↑ for hours matching PK; dark-cycle EE↑ on diet admixture.  
- **Pathways:** P1, P2.  
- **Clinical:** Human **Unknown**. Mouse acute + chronic **Established/Probable**.  
- **Practical:** Short t½ → exposure gaps unless frequent dosing or continuous absorption design.

### 6.3 Insulin sensitivity / glycemic control

- **Phenotype:** GTT reverse; clamp GIR↑; lower fed insulin.  
- **Pathways:** P8, P4 (tissue), P7 (liver fat), P9 (glucagon axis in db/db).  
- **Clinical:** Human **Unknown**. Mouse clamp-quality data **Probable**.  
- **Forum:** Almost silent.

### 6.4 Liver fat / NAFLD phenotype

- **Phenotype:** Hepatic TG normalization, lower inflammatory lipids.  
- **Pathways:** P2, P3, P7, P11.  
- **Clinical:** Human **Unknown** (developers interested in NASH franchise via related molecules).  
- **Certainty mouse:** **Probable**.

### 6.5 Lean mass / sarcopenic obesity angle

- **Phenotype:** Fat↓ without lean↓; improved mito quality control in aged obese muscle models.  
- **Pathways:** P6, P5.  
- **Certainty:** **Probable** mouse; human performance translation **Unknown**. Training interaction **Unknown** (see sides: ATP competition).

### 6.6 Antioxidant / anti-inflammatory

- **Phenotype:** GSH↑, oxidized lipids↓, NLRP3 dampening, sepsis model benefits.  
- **Pathways:** P3, P11–P13.  
- **Certainty:** **Probable** preclinical; not a reason to self-treat infection/inflammation.

---

## 7. Side Effects — Mechanism Depth + Counters

> Even with clean mouse panels, **every protonophore retains a conceptual overdose mode**: uncontrolled uncoupling → ATP failure ± heat. BAM15’s wider window is **relative**, not magic immunity.

### 7.1 Hyperthermia / thermal distress

1. **Phenotype:** Core fever, sweating, heat intolerance (class, DNP-defining). Mouse BAM15: **no core rise** at effective and high solubility-limited doses. Forum: local face/ear heat without confirmed core fever.  
2. **Mechanism:** P1 heat from uncoupled respiration; if heat production > heat loss capacity → core T↑ (**Established** class). BAM15 mouse data suggest heat load stays within compensation at studied exposures (**Probable**). Human capacity **Unknown**. Hypothesized local flush via cutaneous blood flow / mild peripheral uncoupling (**Speculative**, P21).  
3. **Pathway → counter**

| Pathway node | Counter | How it hits the node | Clinical | Forum | Practice notes | Certainty |
|--------------|---------|----------------------|----------|-------|----------------|-----------|
| Excess heat production | **Hard stop / dose cut** | Removes driver | DNP toxicology | Uncoupler community SOP | Any core T↑ or extreme sweating = stop | **Established** logic |
| Heat dissipation | Cool environment, light clothing, fans, cold fluids | ↑ heat loss | Supportive care standards | Common | Avoid hot yoga/sauna on dose | **Probable** |
| Confounded stimulants | Avoid high-dose caffeine/yohimbine/clen stacks | Reduce extra thermogenesis + HR | Mechanistic | Anecdotal | Don’t stack “fat burner kitchen sink” | **Speculative** combo risk |
| Detection | Thermometer (oral/tympanic), subjective heat | Early warning | — | GLP1forum stop rules | Log baseline vs peak | **Probable** practice |
| False reassurance | Do not trust “BAM15 can’t cause heat” marketing | Mouse ≠ human | — | Vendor copy | Local heat already reported | **Established** gap |

### 7.2 Tachycardia / palpitations / “pressure in chest”

1. **Phenotype:** HR↑, palpitations; forum at ~4–5 mg inject.  
2. **Mechanism:** P19 hypothesized — EE↑ demands cardiac output; possible sympathetic tone; high-dose mito stress in cardiomyocytes (P14) is a separate injury path.  
3. **Pathway → counter**

| Pathway node | Counter | How it hits the node | Clinical | Forum | Practice notes | Certainty |
|--------------|---------|----------------------|----------|-------|----------------|-----------|
| EE-driven HR | Dose ↓ / split / stop | Less uncoupling load | — | Logs show acclimation or drop dose | Stop if HR >~+10–15 bpm resting (forum heuristic) | **Speculative** thresholds |
| Sympathetic drive | Avoid concurrent high stimulants | Remove additive chronotropy | Standard | Common sense | | **Probable** interaction logic |
| Anxiety amplification | Quiet measurement, no polypharmacy | Reduce artifact | — | — | | **Speculative** |
| True cardiac injury risk | **Do not use** if structural heart disease; emergency care if chest pain/syncope | Removes exposure | Gao high-dose warning | — | β-blockers are **not** a green-light enabler for uncoupler use | **Speculative** as “stack”; **Probable** as stop criterion |
| Electrolytes | Na/K/Mg repletion if sweating | Membrane excitability | Sports medicine | — | Secondary | **Speculative** for BAM15 |

### 7.3 Fatigue, lethargy, cognitive “detachment”

1. **Phenotype:** Mouse high-dose paste lethargy; forum odd detachment.  
2. **Mechanism:** P20 — ATP supply stress in brain/muscle; vehicle/DMSO effects; hypoglycemia-like substrate mismatch (**Speculative**). Low CNS levels (P23) argue against classic psychoactive, but systemic energy stress can still feel cognitive.  
3. **Pathway → counter**

| Pathway node | Counter | How it hits the node | Clinical | Forum | Practice notes | Certainty |
|--------------|---------|----------------------|----------|-------|----------------|-----------|
| ATP stress | Lower dose; ensure carbohydrate availability | Substrate for glycolysis when OXPHOS inefficient | Mechanistic | — | Don’t run fasted high-intensity first exposures | **Speculative** |
| Over-uncoupling | Stop if profound weakness | Removes cause | — | — | | **Probable** |
| Sleep / recovery load | Prioritize sleep, deload training | Lower ATP demand | — | — | | **Speculative** |
| Nutrient support | Adequate calories (intake not suppressed in mice — don’t force deficit crash) | Match EE | Mouse intake unchanged | — | Aggressive cut + uncoupler = stacked stress | **Speculative** human |

### 7.4 Visual disturbance (blur)

1. **Phenotype:** Minutes of blur with heat (isolated logs).  
2. **Mechanism:** **Unknown**. Hypotheses: BP/HR flux, anxiety hyperventilation, solvent, contaminant, coincident. DNP historically had cataract risk with chronic abuse — **different molecule**, do not import as Established BAM15 risk, but visual change is a hard stop.  
3. **Pathway → counter**

| Pathway node | Counter | How it hits the node | Clinical | Forum | Practice notes | Certainty |
|--------------|---------|----------------------|----------|-------|----------------|-----------|
| Any acute visual change | Immediate discontinuation | Remove exposure | Standard toxicology | Log reports | Medical evaluation if persistent | **Probable** as policy |
| Contaminant | Source control / avoid RC | Quality | — | — | | **Speculative** |

### 7.5 Hepatic stress

1. **Phenotype:** Mouse panels largely clean (ALT/AST/GLDH); liver is major exposure organ (drug concentrates there).  
2. **Mechanism:** High local uncoupling could in theory stress hepatocytes (P1, P7 related); human unknown.  
3. **Pathway → counter**

| Pathway node | Counter | How it hits the node | Clinical | Forum | Practice notes | Certainty |
|--------------|---------|----------------------|----------|-------|----------------|-----------|
| Hepatocyte injury | Baseline + on-drug ALT/AST/GGT | Detection | Standard monitoring | Rare discussion | Stop if enzymes rise | **Probable** monitoring logic |
| Alcohol / oral AAS / high-dose APAP | Avoid concurrent hepatotoxins | Reduce dual hit | Clinical common sense | — | | **Probable** |
| Choline / vitamin E / etc. | Not specific antidotes | — | Weak | — | Don’t fake “liver protect” over monitoring | **Speculative** |

### 7.6 Cardiac injury (high uncoupling)

1. **Phenotype:** In vitro biphasic STAT3 — low protect, high injure (Gao).  
2. **Mechanism:** P14.  
3. **Pathway → counter**

| Pathway node | Counter | How it hits the node | Clinical | Forum | Practice notes | Certainty |
|--------------|---------|----------------------|----------|-------|----------------|-----------|
| High-dose mito stress | Stay at minimal effective exposure; no heroic titration | Avoid injury limb of biphasic curve | In vitro only | — | No human MTD | **Speculative** dose mapping |
| Pre-existing heart disease | Avoid entirely | Risk concentration | Logic | — | | **Probable** caution |
| Monitoring | Resting HR, symptoms; ECG if medical supervision | Detection | — | — | | **Speculative** protocols |

### 7.7 Training interference / muscle ATP competition

1. **Phenotype:** Theoretical reduced work capacity if ATP regeneration strained; mouse lean mass preserved at rest EE doses.  
2. **Mechanism:** P1 reduces ATP-per-substrate efficiency — endurance or glycolytic failure under max load (**Speculative**).  
3. **Pathway → counter**

| Pathway node | Counter | How it hits the node | Clinical | Forum | Practice notes | Certainty |
|--------------|---------|----------------------|----------|-------|----------------|-----------|
| Competition with training | Separate hard sessions from peak exposure; or use off-day EE | Temporal split | — | — | Unknown human t½ | **Speculative** |
| Fueling | Carbs around training | Glycolytic ATP | Sports nutrition | — | | **Probable** general |
| Progressive overload tracking | Watch bar speed / HR drift | Detection | — | — | | **Speculative** |

### 7.8 Dehydration / electrolyte flux

1. **Phenotype:** Not prominent in mouse papers; possible if heat/sweat or higher EE.  
2. **Mechanism:** Increased metabolic water turnover / sweating if thermal.  
3. **Pathway → counter**

| Pathway node | Counter | How it hits the node | Clinical | Forum | Practice notes | Certainty |
|--------------|---------|----------------------|----------|-------|----------------|-----------|
| Fluid loss | Hydration, salt to taste | Replace | Standard | — | | **Speculative** for BAM15 |
| K/Mg loss | Diet quality or electrolytes | Membrane stability | Sports | — | | **Speculative** |

### 7.9 Overdose cascade (class)

1. **Phenotype:** Progressive hyperthermia, tachycardia, diaphoresis, confusion, multi-organ failure (DNP literature).  
2. **Mechanism:** Runaway P1. BAM15 mouse window is wider; **human overdose curve unmapped**.  
3. **Pathway → counter**

| Pathway node | Counter | How it hits the node | Clinical | Forum | Practice notes | Certainty |
|--------------|---------|----------------------|----------|-------|----------------|-----------|
| Runaway uncoupling | Emergency medical care; aggressive cooling | Supportive | DNP case series | Uncoupler lore | No specific antidote | **Established** for class management principles |
| Stacked uncouplers | Never combine BAM15 + DNP + FCCP-class + high niclosamide | Additive protonophore load | Logic | — | Hard rule | **Probable** |
| Redose while peaking | Wait full clearance (multiples of t½) | Avoid accumulation | PK logic | — | Human t½ unknown → extra caution | **Probable** logic |

### 7.10 Research-chemical purity / solvent toxicity

1. **Phenotype:** Infection (if injected), DMSO effects, mislabeled dose.  
2. **Mechanism:** Product failure modes, not BAM15 per se.  
3. **Pathway → counter**

| Pathway node | Counter | How it hits the node | Clinical | Forum | Practice notes | Certainty |
|--------------|---------|----------------------|----------|-------|----------------|-----------|
| Unknown identity | HPLC-tested material only; prefer not injecting | Quality | — | Vendor roulette | Oral still unvalidated | **Speculative** mitigation |
| Injection risk | Avoid non-sterile injectables | Infection control | Medicine 101 | Some still inject | | **Established** infection risk of black-market injectables |

---

## 8. Practical Use

| Parameter | Guidance | Certainty |
|-----------|----------|-----------|
| **Human dose** | **No evidence-based human dose.** Vendor HED (~0.8 mg/kg from 10 mg/kg mouse ≈ 50–90 mg/day) is **Speculative arithmetic**, not a protocol. Mouse effective chronic exposure was continuous dietary ~5–10 µM plasma, often ~50–100+ mg/kg/day range depending on study design — **not** directly scalable. | **Unknown** / HED **Speculative** |
| **Timing** | Mouse t½ ~1.7 h → if ever used under research supervision, **split dosing** or sustained formulation would be needed for steady EE. Peak OCR ~0–2 h post gavage. | **Probable** from mouse PK |
| **Duration / cycling** | Mouse studies: days to ~5–6 weeks. Long-term mito/hormonal adaptation **Unknown**. No established cycle. | **Unknown** |
| **Form** | Highly lipophilic; poor water solubility. Diet/oil/DMSO systems in lab. RC liquids vary. | **Established** chem property |
| **Stacks (mechanistically coherent)** | Protein-sufficient diet to protect lean mass; resistance training (independent lean stimulus); optional metabolic health basics (sleep, fiber). GLP-1 agonists are pathway-orthogonal (intake vs EE) — combo **unstudied**. | **Speculative** synergy |
| **Stacks (risky)** | **Any other uncoupler (DNP especially)**; high-dose sympathomimetics; T3 high-dose; sauna + stimulant + BAM15 thermal load; inject RC cocktails | **Probable** risk logic |
| **Titration philosophy** | If operating in a legal research/clinical development context: start far below any HED guess, single-variable changes, vitals logging. Gym RC self-experimentation remains **evidence-free**. | **Speculative** |

---

## 9. Interactions (PK/PD)

| Agent / class | Interaction | Mechanism | Certainty |
|---------------|-------------|-----------|-----------|
| **DNP / FCCP / other protonophores** | **Additive uncoupling** — dangerous | Same P1 node | **Probable** |
| **Niclosamide / nitazoxanide** | Possible additive mito effects (they have uncoupling activity) | Partial class overlap | **Speculative** magnitude |
| **Thyroid hormone (esp. T3)** | Additive EE / HR / catabolism | Parallel EE | **Speculative** for BAM15 specifically |
| **Stimulants (high caffeine, clen, yohimbine)** | HR + heat load | Autonomic / thermogenic | **Speculative** |
| **GLP-1 RAs** | Orthogonal (intake↓ + EE↑ theory) | Different pathways | **Speculative** combo safety |
| **Insulin / sulfonylureas** | If BAM15 lowers glucose need (mouse), hypo risk if agents not adjusted | PD | **Speculative** human |
| **Hepatotoxic polypharmacy** | Dual liver stress | Liver-enriched drug | **Speculative** |
| **Food** | High-fat vehicle may alter absorption (lipophilic) | Physicochemical | **Speculative** human |
| **CYP/transporter map** | **Unknown** — no full human DDI panel | — | **Unknown** |

---

## 10. Monitoring, Contraindications, Stop Criteria

### Monitoring (if exposure occurs under informed research/clinical framing)

| Signal | Why | Action threshold ideas |
|--------|-----|------------------------|
| Core temperature | Class toxicity | Any unexplained febrile rise → **stop** |
| Resting HR / BP | Forum + cardiac theory | Sustained large HR rise, chest pain → **stop** |
| Subjective heat, sweating, confusion | Early uncoupling toxicity | **stop** |
| Body weight / composition | Efficacy vs lean loss | Unexpected lean loss → reassess |
| CMP: ALT/AST, BUN/Cr, glucose | Liver-enriched; mouse BUN quirk | Enzyme rise or renal change → **stop** |
| CK if myalgia | Muscle stress | Significant rise → **stop** |
| Performance logs | ATP competition | Sudden capacity crash → deload/stop |

### Contraindications (mechanism-based, not a legal label)

- Pregnancy / breastfeeding (**Unknown** teratogenicity; default exclude).  
- Significant cardiovascular disease, uncontrolled arrhythmia, prior uncoupler toxicity.  
- Active febrile illness, heat illness susceptibility.  
- Inability to monitor temperature/HR.  
- Concurrent DNP or multi-uncoupler use.  
- Unreliable product identity.

### Stop criteria (hard)

1. Core temperature elevation attributable to drug.  
2. Chest pain, severe palpitations, syncope, confusion.  
3. Persistent visual changes.  
4. Marked weakness / respiratory distress.  
5. Lab evidence of organ injury.  

---

## 11. Comparative Context

| Comparator | Efficacy (fat/metabolic) | Safety window | Evidence | Convenience | Notes |
|------------|--------------------------|---------------|----------|-------------|-------|
| **BAM15** | Strong mouse fat loss + IR | Wide *in vitro* / mouse thermoneutral | Rodent only | Short t½, poor solubility | Best-in-class *tool* uncoupler profile |
| **DNP** | Proven human fat loss | **Narrow**; deaths | Human historical + modern abuse | Oral | Proof class works; reference toxicity |
| **Controlled-release / liver-targeted DNP** | Often NASH/IR > obesity | Improved vs raw DNP | Rodent ± some clinical exploration of related | Engineered | May sacrifice anti-obesity |
| **Niclosamide** | Mixed; can affect lean | Approved anthelmintic (different dose/use) | Mouse obesity data imperfect | Oral | Not clean lean-sparing story |
| **Nitazoxanide** | NASH fibrosis trials angle | Approved antiparasitic | Clinical in other indications | Oral | Uncoupling secondary property |
| **OPC-163493** | Anti-diabetes rodent; little adiposity effect | Designed drug-like | Rodent | — | Shows uncoupling ≠ automatic fat loss |
| **GLP-1 / dual agonists** | Excellent human fat loss | Established AE profile | Large RCTs | Injectable/oral | Appetite/GI primary; standard of care path |
| **Exercise + diet** | Proven | Safest | Vast | Adherence hard | Still baseline |
| **T3 / clen / DNP stacks (gym)** | Variable | Poor | Anecdote-heavy | Easy to get wrong | Inferior risk/benefit vs modern obesity drugs |

**Positioning:** BAM15 is a **preclinical EE agonist** with an unusually clean mouse body-comp signature. It is **not** a validated consumer fat burner and is **not** automatically “safe DNP.” For human obesity, approved incretin therapies dominate evidence.

---

## 12. Open Questions

Data that would most change this map:

1. **Human SAD/MAD PK/PD** — t½, Cmax, OCR or doubly labeled water EE, core temp, HR.  
2. **Human therapeutic index** vs DNP (fever curve, cardiac telemetry).  
3. **Sex differences** (most obesity work male mice).  
4. **Thermoneutral housing** replications (does EE claim shrink when mice aren’t cold-stressed?).  
5. **Exercise interaction** — VO₂max, strength, recovery.  
6. **Chronic (>6 month) tox** — cardiac, ocular, reproductive, carcinogenic.  
7. **DDI / CYP panel** and food effect.  
8. Whether **longer-half-life analogs** retain BAM15’s lean-sparing thermoneutral profile (main industry bet).  
9. Controlled **forum-grade dose** with third-party purity + vitals — currently missing.  
10. **Cancer relevance** — systemic uncoupling vs tumor-selective risk to host tissues.

---

## 13. Sources

### Primary / peer-reviewed

1. Kenwood BM et al. Identification of a novel mitochondrial uncoupler that does not depolarize the plasma membrane. *Mol Metab.* 2014;3(2):114-123. PMID: 24634817. PMC3953706.  
2. Alexopoulos SJ et al. Mitochondrial uncoupler BAM15 reverses diet-induced obesity and insulin resistance in mice. *Nat Commun.* 2020;11:2397. PMID: 32409697. PMC7224297. (COI: Continuum Biosciences.)  
3. Axelrod CL et al. BAM15-mediated mitochondrial uncoupling protects against obesity and improves glycemic control. *EMBO Mol Med.* 2020;12:e12088.  
4. Xiong G et al. BAM15 as a mitochondrial uncoupler: a promising therapeutic agent for diverse diseases. *Front Endocrinol.* 2023;14:1252141.  
5. Chen SY et al. Targeting negative energy balance with calorie restriction and mitochondrial uncoupling in db/db mice. *Mol Metab.* 2023;69:101684.  
6. Dantas WS et al. Mitochondrial uncoupling attenuates sarcopenic obesity… *J Cachexia Sarcopenia Muscle.* 2022;13:1821-1836.  
7. Tsuji N et al. BAM15 treats mouse sepsis and kidney injury… *J Clin Invest.* 2023;133(7):e152401.  
8. Hu N et al. Chemical mitochondrial uncouplers share common inhibitory effect on NLRP3… *Toxicol Appl Pharmacol.* 2021;414:115426.  
9. Gao JL et al. Characterizations of mitochondrial uncoupling induced by chemical mitochondrial uncouplers in cardiomyocytes. *Free Radic Biol Med.* 2018;124:288-298.  
10. Zunica ERM et al. Breast cancer growth… suppressed by… BAM15. *Cancer Metab.* 2021;9:36.  
11. Firsov AM et al. Protonophoric action of BAM15 on planar bilayers, liposomes, mitochondria, bacteria and neurons. *Bioelectrochemistry.* 2021;137:107673.  
12. Dang CP et al. BAM15… attenuates inflammation in the LPS injection mouse model. *J Innate Immun.* 2021;13:359-375.  
13. Cho I et al. BAM15 relieves neurodegeneration in aged *C. elegans*… *Metabolites.* 2022;12:1129.  
14. Goedeke L, Shulman GI. Therapeutic potential of mitochondrial uncouplers for the treatment of metabolic associated fatty liver disease and NASH. *Mol Metab.* 2021 (review context).  
15. Childress ES et al. Small molecule mitochondrial uncouplers and their therapeutic potential. *J Med Chem.* 2018;61:4641-4655.

### Press / industry context

16. Virginia Tech News (2020) — Santos/Hoehn on BAM15 fat loss without temp rise; half-life limitation; Continuum Biosciences NASH interest.  
17. Pennington Biomedical (Axelrod-related) press on BAM15 obesity potential.

### Forum / anecdotal (pattern sources, not efficacy proof)

18. Reddit r/amino_asylum — BAM15 product guide + HED discussion threads (2025).  
19. Reddit r/PeptideGuide — mechanism/summary posts (vendor-adjacent).  
20. GLP1forum — “BAM 15 Logging” thread (inject ~4 mg reports: heat, HR, blur, acclimation; stop heuristics).  
21. YouTube commentary under BAM15/DNP comparison videos (isolated 5 mg inject remarks).

### Not used

- Other `findings/*` monographs (isolation rule).

---

## 14. Short Boundary

This document maps mechanisms, rodent evidence, and sparse anecdotes for research literacy. It is **not** a prescription, a human dosing protocol, or a safety guarantee. BAM15 has **no published clinical trials**; research-chemical products are unregulated. Mitochondrial uncouplers as a class can kill when dosing outruns physiology — wider mouse windows do not equal human immunity. Decisions about exposure belong to the individual and, where appropriate, qualified clinicians operating under legal frameworks.

---

*End of briefing.*
