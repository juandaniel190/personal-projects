# CS Apps — Investment Decision Analysis

**Case Study: Senior Manager, Product Data Analyst — Contentsquare**

---

## Executive Summary

CS Apps shows strong revenue traction (+37% ACV, +30% accounts in 12 months) but faces a structural disconnect between selling and delivering value. Only 15% of accounts are currently live in production, 71% have zero certified users, and the health rate has declined from 63% to 54% in 10 months. $13.1M in renewal pipeline (37.9% of total) sits with unhealthy accounts, with a $16.3M Q4 cliff where 44% of UFR is at risk.

The health metric itself is unreliable — it uses platform-wide WAU (`AVG_WAU_GLOBAL`) rather than CS Apps-specific WAU, masking the true adoption problem.

**Recommendation: Increase investment — conditionally.**  The thesis is not "grow faster" but "fix the value delivery chain before the renewal cliff converts into churn."

> *CS Apps are creating value (revenue is growing) → but failing to deliver it (clients aren't going live or engaging) → which puts value protection at risk (renewals are deteriorating).*

---

## Context

CS Apps is Contentsquare's mobile application analytics product, extending CS Digital (web) to native iOS/Android apps. Capabilities include mobile heatmaps, session replay, journey analysis, and Zoning Analysis — all tagless. Clients commit to 24-month contracts. At renewal, procurement evaluates price, ROI, usage, legal, and compliance factors.

---

## Part 1 — Investment Decision: Stop / Maintain / Increase?

### 1.1 Problem Framing

The Product Director needs a data-driven recommendation for the CPO:

| Option | Description |
|---|---|
| **Stop** | Discontinue investment in CS Apps |
| **Maintain** | Keep current investment level |
| **Increase** | Accelerate investment and build a growth case |

### 1.2 Analytical Framework

The analysis is structured around three pillars that form a causal chain — each pillar feeds the next:

| Pillar | Core Question | Hypotheses |
|---|---|---|
| **Value Creation** | Is CS Apps generating and growing revenue? | H1 (Revenue & Growth), H7 (Segment Opportunity) |
| **Value Delivery** | Are clients reaching time-to-value, adopting, and engaging? | H4 (Implementation), H2 (Certification), H6 (Module Engagement) |
| **Value Protection** | Will this revenue renew or churn? | H3 (Health Decline), H5 (Renewal Pipeline), H8 (Health Formula Flaw) |

> **Reading this analysis:** If Value Creation is strong but Value Delivery is broken, then Value Protection will inevitably deteriorate. The investment decision depends on whether the delivery gap is fixable — and whether there is time to fix it before renewals hit.

### 1.3 Data Quality Audit

Before testing hypotheses, the data was audited for reliability.

**Findings:**

| Check | Result | Impact |
|---|---|---|
| Exact duplicate rows | 0 (Account), 0 (User) | No risk |
| Duplicate (Account, Month) keys | 0 | No ACV overcounting |
| Duplicate (User, Month, Module, Project) | 100 rows | Minor — 0.4% of user data |
| NULL `IMPLEMENTATION_STATUS_APPS` | 518 rows (28.7%) — 82 accounts | High — limits implementation analysis |
| NULL `CONTRACT_START_DATE` | 535 rows (29.7%) | Medium |
| NULL `CONTRACT_END_DATE` | 507 rows (28.1%) | Medium |
| NULL `USER_POSITION` | 2,089 rows (8.1%) | Medium |
| Rows with `AVG_WAU_GLOBAL` = 0 | 156 rows — 49 accounts | Critical for health metric |

**Note on UFR:** `TOTAL_UFR` is the total upcoming fiscal renewal value for an account in a given fiscal quarter. It is repeated for every month within that quarter. All UFR analyses in this document are deduplicated (one observation per account per fiscal quarter, latest month) to avoid overcounting.

> The PDF warns "if a client has multiple contracts, all the contracts will show up." Audit confirmed **0 duplicate (Account, Month) pairs** — no overcounting risk in ACV sums. The null pattern for implementation status is consistent across all months (~27–34%), indicating a systemic data pipeline issue, not a timing artifact.

---

## Pillar 1 — Value Creation (Revenue & Growth)

> *Is CS Apps generating and growing revenue meaningfully?*

### H1 — Revenue & Account Growth | INVEST

| Metric | Jan 2023 | Dec 2023 | Change |
|---|---|---|---|
| Total CS Apps ACV | $11.3M | $15.5M | **+37.4%** |
| Number of Accounts | 134 | 174 | **+29.9%** |
| Mean ACV per account | ~$84K | ~$89K | Stable |

Revenue is growing driven by new account acquisition, not price increases. The median ACV remains stable around $60K, suggesting consistent deal sizes with the growth coming from volume.

![ACV & Account Growth](./figures/fig_01_acv_account_growth.png)

---

### H7 — High-Value Segment Opportunity | OPPORTUNITY

| Vertical | Accounts | Mean ACV | % Healthy |
|---|---|---|---|
| **Telco** | 13 | **$234K** | 52.9% |
| General Retailer | 47 | $92K | 59.7% |
| Energy/Utilities | 9 | $84K | 52.9% |
| Fashion | 18 | $59K | **73.0%** |

| Geo | Accounts | Mean ACV | % Healthy |
|---|---|---|---|
| **Americas** | 46 | **$113K** | 51.9% |
| APJ | 12 | $92K | 62.0% |
| EMEA | 127 | $74K | 62.0% |

Telco delivers 2.8x the average ACV but only 53% health. Americas is the highest-ACV geo but the least healthy (52%). Fashion, with lower ACV, leads with 73% health — suggesting a playbook problem, not a product problem.

![Segment Analysis](./figures/fig_08_segment_analysis.png)

**Pillar 1 verdict:** Value Creation is strong. CS Apps is selling well and growing. The problem is not demand — it's what happens after the sale.

---

## Pillar 2 — Value Delivery (Time to Value, Adoption & Engagement)

> *Are clients actually reaching go-live, using the product, and extracting value?*

### H4 — Implementation Bottleneck | CAUTION

Of 185 unique accounts, 53 (29%) have no implementation status tracked at all. The table below shows the **latest snapshot** — where each account stands as of its most recent month in the data. These are cross-sectional statuses, not cohort progressions through a funnel.

| Current Status | Accounts | % of Total (185) |
|---|---|---|
| NULL / Untracked | 53 | 29% |
| Not started | 8 | 4% |
| Started | 14 | 8% |
| Partially implemented | 18 | 10% |
| **Implemented** | **60** | **32%** |
| Partially lived | 5 | 3% |
| **Lived** | **27** | **15%** |

Only **27 accounts (15% of total base)** are currently in "Lived" status. The largest group — 60 accounts (32%) — sits at "Implemented" but has not gone live. Combined with 53 untracked accounts, **85% of CS Apps buyers are not actively using the product in production.** Of the 132 tracked accounts, 57 changed status at least once during 2023, indicating some movement — but not enough to materially shift the go-live rate.

![Implementation Status Distribution](./figures/fig_06_implementation_funnel.png)

---

### H2 — Certification & Adoption Gap | CAUTION

| Metric | CS Apps | CS Digital | Gap |
|---|---|---|---|
| Avg certified users per account | **0.69** | **18.1** | **26x** |
| Accounts with 0 certified users | **71.4%** (132/185) | — | — |
| Avg sessions per user per month | **2.84** | — | Low |

71% of accounts have zero certified CS Apps users. The same clients average 18 certified CS Digital users. Clients are buying but not embedding the product. The 2.84 avg sessions/user/month confirms shallow engagement.

![Certification Gap](./figures/fig_04_certification_gap.png)

---

### H6 — Shallow Module Engagement | CAUTION

| Module | % of Sessions | Avg Sessions/User | Note |
|---|---|---|---|
| **Homepage** | **25.7%** | 2.94 | Navigation, not value |
| Zoning Analysis | 18.2% | 3.81 | Core analytics |
| Journey Analysis | 11.3% | 2.76 | Core analytics |
| Workspace | 7.4% | **4.03** | High stickiness |
| Session Replay | 6.4% | 3.60 | Core analytics |
| Error Analysis | 0.6% | **4.36** | Highest stickiness, lowest reach |

1 in 4 sessions is on the Homepage. Users who reach Zoning, Workspace, or Error Analysis show higher engagement. This is a depth-of-usage problem: users land but don't navigate to the modules that deliver value.

![Module Engagement](./figures/fig_07_module_engagement.png)

**Pillar 2 verdict:** Value Delivery is the broken link. 85% of accounts are not live. Those that are live have almost no certified users and shallow engagement. The product is being sold but not delivered.

---

## Pillar 3 — Value Protection (Retention)

> *Will the revenue CS Apps has created survive renewal, or is it at risk of churn?*

### H3 — Declining Account Health | RISK

| Period | % Healthy | Trend |
|---|---|---|
| Jan 2023 | 56.0% | — |
| Feb–Jun 2023 (peak) | ~63.4% | Improving |
| Jul 2023 | 58.4% | Inflection point |
| Dec 2023 | **54.0%** | -9pp from peak |

Health peaked in Q1 and has declined continuously through H2. As the cohort grows, health is deteriorating — the product is adding accounts faster than it is making them successful.

![Health Trend](./figures/fig_02_health_trend.png)

**Key anomaly:** Accounts with "Not started" or "Started" implementation show *higher* health rates (67–71%) than "Lived" accounts (58%). This is explained by the health formula investigation (H8 below).


---

### H5 — Renewal Pipeline at Risk | HIGH RISK

| Fiscal Quarter | Total UFR | Renewing Accounts | % Accounts Healthy | % UFR Healthy |
|---|---|---|---|---|
| FQ 2022-11-01 | $5.0M | 20 | 60% | 57% |
| FQ 2023-02-01 | $2.8M | 16 | 62% | 58% |
| FQ 2023-05-01 | $5.1M | 23 | 87% | 88% |
| FQ 2023-08-01 | $5.4M | 17 | 59% | 62% |
| **FQ 2023-11-01** | **$16.3M** | **33** | **58%** | **56%** |

The Q4 pipeline is $16.3M with 33 renewing accounts, and only 56% of that UFR value is healthy. Across all quarters, **$13.1M of total UFR (37.9%) sits with unhealthy accounts.** The Q4 concentration ($16.3M = 47% of the full-year renewal pipeline) amplifies the risk.

![Renewal Pipeline](./figures/fig_09_renewal_pipeline.png)

---

### H8 — Health Metric Conflation | DATA QUALITY

The case study defines `HEALTHY_STATUS` as "a ratio between ACV and WAU (ACV/WAU)." Reverse-engineering the formula against the data:

| Status | Median ACV/WAU | Mean ACV/WAU |
|---|---|---|
| Healthy | **$22,311** | $32,961 |
| Unhealthy | **$71,667** | $132,522 |

**Lower ACV/WAU = Healthier.** The ratio represents cost-per-weekly-active-user. An account paying $100K with 50 WAU ($2K/user) is "healthy"; one paying $100K with 2 WAU ($50K/user) is "unhealthy." The best-fit threshold is **~$40,000 (87.9% accuracy).**

**The paradox explained:** Accounts with "Not started" CS Apps implementation still have their CS Digital WAU counted in `AVG_WAU_GLOBAL`. Their high Digital usage pushes ACV/WAU down, making them appear "healthy" — even though they derive zero value from CS Apps. The health metric conflates platform-wide engagement with product-specific value.

**Edge case:** 156 rows (8.7%) have `AVG_WAU_GLOBAL` = 0. Of these, 128 are "Unhealthy" (as expected — infinite $/user) and 28 are "Healthy" (unexplained without additional data).

![Health Formula](./figures/fig_10_health_formula.png)

> **Implication for the investment case:** The declining health rate (63% → 54%) may partially reflect a compositional effect — new accounts enter with high CS Digital WAU (appearing healthy) but as they adopt CS Apps and potentially reduce Digital usage, their WAU shifts and the ratio worsens. A CS Apps-specific health metric is needed to accurately assess product adoption.

**Pillar 3 verdict:** Value Protection is deteriorating. Health is declining, $13.1M in renewals is at risk, and the health metric itself is unreliable — meaning the true risk may be worse than reported.

---

## 1.6 Synthesis & Recommendation

> **Increase investment — conditionally.**

**The chain:**

| Pillar | Status | Summary |
|---|---|---|
| Value Creation | **Strong** | +37% ACV, +30% accounts — demand is real |
| Value Delivery | **Broken** | 85% not live, 71% zero certified users, shallow engagement |
| Value Protection | **Deteriorating** | Health declining, $13.1M at-risk UFR, flawed health metric |

**The situation in one sentence:** CS Apps is selling well but failing to convert sales into healthy, engaged accounts, and a $16.3M Q4 renewal cliff is approaching (44% of that UFR is unhealthy).

**Investment thesis:** Invest to fix the value delivery chain before Q4 renewals convert into churn.

**Priority actions:**

| # | Action | Pillar | Target | Rationale |
|---|---|---|---|---|
| 1 | **Accelerate implementation** | Delivery | "Lived" rate from 15% → 40%+ | 60 accounts (32%) stall at "Implemented"; 53 (29%) untracked |
| 2 | **Drive certification** | Delivery | 1 → 3+ certified users/account | 71% of accounts have 0 certified users |
| 3 | **In-product activation** | Delivery | Reduce Homepage share from 26% to 15% | Guide users to Zoning, Session Replay, Error Analysis |
| 4 | **Segment playbooks** | Creation | Telco & Americas | Highest ACV, worst health — benchmark against Fashion |
| 5 | **Rebuild health metric** | Protection | CS Apps-specific WAU | Current metric masks adoption failure with Digital usage |

---

### 1.7 Additional Data Needed

**Quantitative (not available in this dataset):**

- CS Apps-specific WAU (not global WAU) to compute a product-specific health score
- NPS / CSAT survey data per account
- Time-to-live (days from contract start to "Lived" status)
- Churn/renewal outcome data from prior cohorts
- Product usage funnel events (module visit sequences per user)
- CS Apps ACV as % of total contract at renewal

**Qualitative / Internal:**

- Customer success manager notes on blocked implementations
- Root cause for 29% of accounts missing implementation status
- Competitive context: what are clients using instead/alongside CS Apps?

**Market:**

- Competitor benchmarks (Mixpanel, Amplitude, UXCam, Heap for mobile)
- Mobile analytics adoption benchmarks by vertical

---

## Next Steps

- [ ] Part 1 — Validate figures and finalize recommendations
- [ ] Part 2 — Account Health redefinition for AI era (Sense Agent)
- [ ] Part 2 — Monetization challenge: AI pricing model
- [ ] Deck — Build presentation structure (20-min restitution)

---


