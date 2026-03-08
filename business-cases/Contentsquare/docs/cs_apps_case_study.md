# CS Apps — Investment Decision Analysis

**Case Study: Senior Manager, Product Data Analyst — Contentsquare**

---

## Part 1: Investment Decision — Hypothesis & Data Exploration

The Product Director wants to know: **should we stop, maintain, or increase investment in CS Apps?**

1. What hypotheses frame the investment decision?
2. What does the data say, and where is data quality a problem?
3. What 2–3 insights answer the question?
4. What additional data would deepen the analysis?
5. What is the strategic recommendation?

**Context:** CS Apps is Contentsquare's mobile application analytics product, extending CS Digital (web) to native iOS/Android apps. Capabilities include mobile heatmaps, session replay, journey analysis, and Zoning Analysis — all tagless. Clients commit to 24-month contracts. At renewal, procurement evaluates price, ROI, usage, legal, and compliance factors.

---

## Executive Summary

**Revenue is growing but delivery is broken | increase investment to fix adoption before the renewal cliff.**

CS Apps shows strong revenue traction (+37% ACV, +30% accounts) but a clear gap between **selling and delivering value**. Only **15% of accounts are live**, **71% have zero certified users**, and the **health metric is flawed** because it blends CS Digital usage into CS Apps health, making non-users appear healthy. The real risk is **renewal refusal from non-users with no ROI evidence**, not active churn. **$16.0M renews in Q4 across 31 accounts**, creating concentrated exposure.

**Story flow:**

- Acquisition is strong (revenue is growing)  
- → but adoption is fragile (clients aren't going live or engaging)  
- → creating a latent renewal risk: non-adopters face procurement conversations with no ROI evidence.

**Three pillars:**

| Pillar | Core Question | Status | Summary |
|---|---|---|---|
| **P1: Acquisition & Growth** | Is CS Apps generating and growing revenue? | **Strong** | +37% ACV, +30% accounts: demand is real |
| **P2: Adoption & Engagement** | Are clients reaching time-to-value, adopting, and engaging? | **Broken / Ramping-up** | 86% not live, 71% zero certified users, shallow engagement |
| **P3: Retention & ARR** | Will this revenue renew or churn? | **At Risk** | Health metric is unreliable. The real risk: 31 accounts renewing $16.0M in Q4 with no CS Apps adoption to justify the contract |

**Priority actions by pillar:**

- **P1:** Focus on strategic segments (e.g. Telco, Americas).
- **P2:** Increase visibility of high-stickiness modules (Workspace, Error Analysis); focus on implementation and integration bottleneck.
- **P3:** Triage the 31 Q4 accounts now: identify which are non-live, assign implementation owners, and build the ROI case before renewal conversations start.

---

## P1: +37% ACV and +30% accounts in 12 months | demand is real, the problem is not sales

*P1 Acquisition & Growth: Is CS Apps generating and growing revenue meaningfully?*

### Data Scope Note

This dataset covers **only accounts with active CS Apps contracts**. `TOTAL_ACTIVE_ACV` for each account represents their full Contentsquare spend (CS Apps + CS Digital + other add-ons). We do not know how many CS Digital-only accounts exist. The analysis measures **wallet penetration**: how large a share of each account's total Contentsquare spend is CS Apps — and whether that share is growing.

---

### H1 | Revenue & Account Growth

| Metric | Jan 2023 | Dec 2023 | Change |
|---|---|---|---|
| Total CS Apps ACV | $11.3M | $15.5M | **+37%** |
| Total relationship ACV (all products) | $48.7M | $62.9M | +29% |
| Number of accounts | 134 | 174 | **+30%** |
| Mean CS Apps ACV per account | ~$84K | ~$89K | Stable |
| **CS Apps penetration (Apps / Total ACV)** | **23.1%** | **24.6%** | **+1.5pp** |

CS Apps ACV is growing faster than total relationship ACV (+37% vs. +29%). This means CS Apps is increasing its share of the Contentsquare wallet — penetration grew from 23.1% to 24.6% over the year.

![ACV & Account Growth](../figures/fig_01_acv_account_growth.png)

---

### H1b — Wallet Penetration Trend (Jan → Dec 2023)

Penetration = CS Apps ACV / Total Contentsquare ACV for the same accounts.

| Month | CS Apps ACV | Total ACV | CS Apps Penetration |
|---|---|---|---|
| Jan 2023 | $11.26M | $48.69M | 23.1% |
| Feb 2023 | $11.46M | $48.39M | 23.7% |
| Mar 2023 | $11.45M | $48.53M | 23.6% |
| Apr 2023 | $11.58M | $49.51M | 23.4% |
| May 2023 | $11.59M | $50.54M | 22.9% |
| Jun 2023 | $11.84M | $51.65M | 22.9% |
| Jul 2023 | $12.87M | $56.28M | 22.9% |
| Aug 2023 | $13.07M | $56.78M | 23.0% |
| Sep 2023 | $13.51M | $57.24M | 23.6% |
| Oct 2023 | $14.51M | $59.80M | 24.3% |
| Nov 2023 | $14.77M | $60.38M | 24.5% |
| **Dec 2023** | **$15.48M** | **$62.88M** | **24.6%** |

**Reading:** Penetration dips mid-year (May–Jul) as new accounts enter with large CS Digital contracts. By H2, CS Apps recovers and outpaces total growth. CS Apps still represents roughly 1 in 4 dollars of these clients' Contentsquare spend.

---

### H7 | High-Value Segment Opportunity

The segment tables show CS Apps ACV and the total Contentsquare relationship. **CS Apps % of relationship** = wallet penetration per segment.

**By Vertical (Dec 2023):**

| Vertical | Accounts | Mean CS Apps ACV | Mean Total ACV | CS Apps % | % Healthy |
|---|---|---|---|---|---|
| Telco | 10 | $272K | $940K | **29%** | 50% |
| Energy, Util & Resources | 8 | $100K | $275K | **36%** | 25% |
| General Retailer | 46 | $96K | $392K | 24% | 46% |
| BFSI | 26 | $92K | $298K | 31% | 58% |
| **Luxury** | **2** | **$90K** | **$1,369K** | **7%** | 100% |
| Food & Beverages | 14 | $82K | $262K | 31% | 57% |
| M&A | 8 | $65K | $330K | 20% | 50% |
| Travel, Leisure & Logistics | 15 | $62K | $237K | 26% | 67% |

**By Geo (Dec 2023):**

| Geo | Accounts | Mean CS Apps ACV | Mean Total ACV | CS Apps % | % Healthy |
|---|---|---|---|---|---|
| Americas | 42 | $115K | $530K | **22%** | 43% |
| EMEA | 121 | $76K | $319K | 24% | 57% |
| APJ | 11 | $129K | $206K | **63%** | 64% |

**What this reveals:** Luxury is the outlier (7% penetration, $1.37M mean total). Telco ($940K total, 29% Apps) and Americas ($530K total, 22% Apps) have the most value at stake where adoption failure threatens the full relationship. APJ has 63% penetration — Apps is central there.

![Segment Analysis](../figures/fig_08_segment_analysis.png)

**Pillar 1 verdict:** CS Apps is growing and increasing wallet penetration (+1.5pp in 2023). The adoption failure in Pillar 2 puts the full Contentsquare relationship at risk in segments like Telco and Americas.

---

## P2: 86% of accounts are not live and 71% have zero certified users. Adoption is the broken link

*P2 Adoption & Engagement: Are clients reaching time-to-value, adopting, and engaging?*

### H4 | Implementation Bottleneck

Of 185 unique accounts, 53 (29%) have no implementation status tracked. The table shows the **latest snapshot** per account.

| Current Status | Accounts | % of Total (185) |
|---|---|---|
| NULL / Untracked | 53 | 29% |
| Not started | 8 | 4% |
| Started | 14 | 8% |
| Partially implemented | 18 | 10% |
| **Implemented** | **60** | **32%** |
| Partially lived | 5 | 3% |
| **Lived** | **27** | **15%** |

Only **27 accounts (15%)** are in "Lived" status. The largest group — 60 accounts (32%) — is at "Implemented" but has not gone live. **85% of CS Apps buyers are not actively using the product in production.**

![Implementation Status Distribution](../figures/fig_06_implementation_funnel.png)

---

### H2 | Certification & Adoption Gap

| Metric | CS Apps | CS Digital | Gap |
|---|---|---|---|
| Avg certified users per account | **0.69** | **18.1** | **26x** |
| Accounts with 0 certified users | **71.4%** (132/185) | — | — |
| Avg sessions per user per month | **2.84** | — | Low |

71% of accounts have zero certified CS Apps users. The same clients average 18 certified CS Digital users. Clients are buying but not embedding the product.

![Certification Gap](../figures/fig_04_certification_gap.png)

---

### H6 | Shallow Module Engagement

| Module | % of Sessions | Avg Sessions/User | Note |
|---|---|---|---|
| **Homepage** | **25.7%** | 2.94 | Navigation, not value |
| Zoning Analysis | 18.2% | 3.81 | Core analytics |
| Journey Analysis | 11.3% | 2.76 | Core analytics |
| Workspace | 7.4% | **4.03** | High stickiness |
| Session Replay | 6.4% | 3.60 | Core analytics |
| Error Analysis | 0.6% | **4.36** | Highest stickiness, lowest reach |

1 in 4 sessions is on the Homepage. Users who reach Zoning, Workspace, or Error Analysis show higher engagement.

![Module Engagement](../figures/fig_07_module_engagement.png)

**Pillar 2 verdict:** Value Delivery is the broken link. 85% of accounts are not live; those that are live have almost no certified users and shallow engagement.

---

## P3: $7.2M of the Q4 renewal cliff sits with unhealthy accounts | retention is at risk if adoption is not fixed

*P3 Retention & ARR: Will the revenue CS Apps has created survive renewal, or is it at risk of churn?*

### H3 — Declining Account Health (context)

Health peaked in Q1 (~63%) and declined through H2 to **54%** in Dec 2023. **Key anomaly:** Accounts with "Not started" or "Started" implementation show *higher* health rates (67–71%) than "Lived" accounts (58%). This exposes the core flaw: the health metric blends CS Digital usage into CS Apps health, so non-users can appear healthy. The trend is untrustworthy until the formula is fixed.

![Health Trend](../figures/fig_02_health_trend.png)

---

### H5 | Renewal Pipeline at Risk

| Fiscal Quarter | Total UFR | Renewing Accounts | % Accounts Healthy | % UFR Healthy |
|---|---|---|---|---|
| FQ 2022-11-01 | $5.0M | 20 | 60% | 57% |
| FQ 2023-02-01 | $2.8M | 16 | 62% | 58% |
| FQ 2023-05-01 | $5.1M | 23 | 87% | 88% |
| FQ 2023-08-01 | $5.4M | 17 | 59% | 62% |
| **FQ 2023-11-01** | **$16.0M** | **31** | **54%** | **55.7%** |

Overall health scores don't predict renewals. What matters is whether the cohort of renewing accounts is healthy — and that signal is flashing red. Q4 enters with only 55.7% of renewing ACV held by healthy accounts, with **$16.0M at stake** (47% of the full-year pipeline).

**P3 verdict:** The health metric cannot be used as evidence of deterioration. The real retention risk is not active churn. It is renewal refusal: 31 accounts renew $16.0M in Q4 with no CS Apps adoption to justify the contract. Fix implementation now, not after renewals fail.

![Renewal Pipeline](../figures/fig_09_renewal_pipeline.png)

---

### H8 — Health Metric Conflation (data quality)

| Status | Median ACV/WAU | Mean ACV/WAU |
|---|---|---|
| Healthy | **$22,311** | $32,961 |
| Unhealthy | **$71,667** | $132,522 |

**Lower ACV/WAU = Healthier.** Accounts with "Not started" CS Apps implementation still have CS Digital WAU counted in `AVG_WAU_GLOBAL`. Their high Digital usage pushes ACV/WAU down, making them appear "healthy" despite zero CS Apps value.

![Health Formula](../figures/fig_10_health_formula.png)

---

## Five actions close the delivery gap before the Q4 renewal cliff

*Five actions close the delivery gap before Q4 2024*, with three data pipeline fixes that are prerequisites.

### OKR-style actions

| Pillar | Priority | Objective | KPIs | Initiatives |
|---|---|---|---|---|
| **P2 Adoption** | High | Improve engagement and adoption of the platform | "Lived" rate: 14% → 40%+; 0 → 3+ certified users/account; Homepage share 26% → 15% | Accelerate implementation, Drive certification, In-product activation flows |
| **P3 Retention** | Medium | Secure the Q4 renewal cliff before procurement conversations start | Renewal rate ≥90% on $16.0M Q4 UFR | Triage 31 Q4 accounts by go-live status; assign owners to non-live |
| **P1 Acquisition** | Low | Sustain and accelerate revenue and account growth | Benchmark Fashion 73% health | Segment playbooks (Telco & Americas) |

---

### Data Quality Audit

| Issue | Stat | Impact |
|---|---|---|
| NULL Implementation Status | 29% (82 accounts) | **HIGH** — 518 rows untracked; systemic pipeline issue |
| NULL Contract Dates | 29% start · 28% end | **MEDIUM** — Blocks cohort analysis and time-to-live calculations |
| AVG_WAU_GLOBAL = 0 | 156 rows (49 accounts) | **CRITICAL** — Breaks health metric for ~27% of base |

Additional checks: 0 duplicate (Account, Month) keys; 100 duplicate (User, Month, Module, Project) rows (0.4% of user data). UFR analyses are deduplicated (one observation per account per fiscal quarter).

---

### What Would Deepen This Analysis

| Area | Items |
|---|---|
| **Sales** | Win/loss data vs. Glassbox / FullStory; Cross-sell attach rate into CS Digital base |
| **CS Team** | Renewal outcomes for early cohorts; Time-to-go-live by segment |
| **Market** | TAM by vertical — is Telco a ceiling or opportunity? |
| **Customer** | Exit verbatims from churned accounts |

---

## Part 2: AI-Era Pricing & Health

**Monetization & Account Health Redefinition**

The current CSQ pricing model has the risk of "Value Leakage": the client gets massive ROI from AI-driven insights but we are not monetizing it as revenue stays flat.

1. Should Sense Analyst be priced as a flat-fee add-on, success-based tier, or credit-based model?
2. What analysis determines the right pricing model?
3. How do we redefine account health when AI reduces human time-in-tool?

---

## Daily Sense Analyst quotas by tier capture AI value without replacing session pricing

*How do we capture the extra value Sense delivers per session?*

**Recommendation:** Introduce daily Sense Analyst query quotas by tier **(Quota + Tier model)**, with Sense Chat included free across all plans. This captures AI value without replacing session-based pricing.

### How the Market Is Pricing AI Today

| Model | How It Works | Companies | Verdict for CS |
|---|---|---|---|
| **Flat-Fee Add-On** | Fixed $/year for unlimited AI | Gainsight | Simple but misaligned; leaves value on table |
| **Usage / Token-Based** | Pay per AI query or token | PostHog, Anthropic API | Transparent but volatile for budgets |
| **Outcome-Based** | Pay per resolved outcome | Intercom Fin ($0.99/ticket) | Hard to measure in analytics |
| **Quota + Tier** | Daily/monthly cap per tier, upgrade for more | Anthropic Claude, Salesforce Agentforce | **Best fit — frequent friction drives upgrades** |

**Key findings:**

- Analytics competitors (Amplitude, Mixpanel, Heap) bundle AI into tiers for free; when AI becomes the primary interface, bundling alone won't capture the value.
- The Anthropic parallel: Claude Pro users hit a daily cap and must wait or upgrade — creating frequent, low-friction upgrade pressure without fully blocking work.

---

## A 5-query daily cap covers ~96% of users and creates natural upgrade friction

*Daily Sense Analyst caps by plan; Sense Chat included free on all tiers*

### Pricing tiers (proposed)

| Tier | Price | Sessions | Sense Chat | Sense Analyst |
|---|---|---|---|---|
| **Free** | €0 / forever | Up to 200K/month | Included | Not included |
| **Growth** | From €39/month | Starting at 7K | Unlimited | **5 queries/day*** |
| **Pro** | Let's talk | Starting at 1M | Unlimited | 25 queries/day |
| **Enterprise** | Let's talk | Custom | Unlimited | Unlimited |

\* **Why 5/day?** Customers average ~3 sessions daily; 5 queries/day is an estimate that covers most workflows while creating a clear upgrade incentive. Cap resets daily. Optimal level can be refined with Sense query logs (queries, tokens, or credits).

![Why 5/day? (Quota rationale)](../figures/fig_14_quota_rationale.png)

### Why this model wins

1. **Captures uncaptured value** — Revenue tied to AI usage, not just session volume.
2. **Preserves session pricing** — Sessions remain the base layer; Sense quota is additive.
3. **Simple to explain** — Global daily cap per tier is transparent for procurement.
4. **Natural upgrade path** — Regular friction drives tier upgrades without blocking work.

### How it works

A Growth analyst runs 5 Sense Analyst queries; the 6th is blocked with: *"Your team hit today's 5-query limit. Upgrade to Pro for 25/day, or cap resets tomorrow."* No work is lost — they wait or upgrade.

---

## Data Behind Pricing

### Distribution of daily usage and quota coverage

- **Distribution of daily usage per account** (platform sessions as proxy for AI query demand): P50 ≈ 0.6, P75 ≈ 2; a **5/day cap covers ~96%** of accounts.
- **Quota coverage by tier:** Free (no Sense Analyst) 0%; Growth (5/day) 95.7%; Pro (25/day) 99.5%; Enterprise (unlimited) 100%.

### Why did we discard all other models?

| Model | What the data says | Verdict |
|---|---|---|
| **Flat-Fee Add-On** | Usage too concentrated (top 20% = 65% of sessions). Heavy users would be subsidized. | Eliminated |
| **Success-Based Tier** | No correlation between usage and health (r = 0.09, p = 0.33). Can't prove usage drives outcomes. | Eliminated |
| **Credit-Based** | Cannot test — Sense query logs not available yet. | Needs more data |
| **Quota + Tier** | Natural daily breakpoints (P50, P75, 5/day cap). | **Confirmed** |

### Additional data that would sharpen this decision?

| Data | What it would tell us |
|---|---|
| Sense query logs (type, cost, timestamp) | Whether different query types cost enough to justify credits |
| Query → action taken (export, share) | Whether usage correlates with outcomes — would revive Success-Based |
| Renewal outcomes by usage tier | Whether heavy users actually renew at higher rates |

![Pricing Decision Analysis](../figures/fig_13_pricing_decision_analysis.png)

---

## The current health metric masks adoption failure. A three-pillar formula fixes it

*The current health metric masks adoption failure. A new three-pillar formula accounts for AI engagement.*

### Formula

**If Non-Live / Partially Live:**

```
Score = (0.15 × P1) + (0.25 × P2) + (0.60 × P3)
```

**If Live:**

```
Score = (0.3 × P2) + (0.7 × P3)
```

**Healthy = Score ≥ 50**

---

### Pillars

| Pillar | Description |
|---|---|
| **P1 \| Implementation Velocity** | Non-Live only. Dropped once Live. Score = 100 if within expected implementation window; decreases linearly beyond the window. |
| **P2 \| Adoption (ACV-Normalized)** | `P2 = min( Certified Users / (ACV × α) , 1 ) × 100`. Normalizes adoption vs account size. |
| **P3 \| Engagement Quality (AI-Aware)** | `P3 = max( 0 , 100 − ACV / (WAU + Sense Queries/week) × β )`. WAU + Sense Queries/week to avoid penalizing AI migration. |

---

### Illustrative Examples (Dummy Data)

*Assumed constants: α = 1/100,000 · β = 1/500 · Expected implementation window = 90 days*

| Account | ACV | Status | Impl Days | WAU | Sense Q/wk | Cert Users | P1 | P2 | P3 | Score |
|---|---|---|---|---|---|---|---|---|---|---|
| A — Acme Corp | $200K | Non-Live | 210 | 2 | 0 | 1 | 0 | 50 | 0 | **15 ⚠** |
| B — Beta Co | $400K | Live | — | 10 | 5 | 1 | — | 25 | 47 | **39 ⚠** |
| C — Gamma Inc | $200K | Live | — | 20 | 10 | 5 | — | 100 | 87 | **92 ✓** |
| D — Delta SA | $500K | Live | — | 3 | 2 | 6 | — | 100 | 0 | **38 ⚠** |
| E — Echo Ltd | $120K | Non-Live | 75 | 3 | 1 | 2 | 85 | 100 | 40 | **67 ✓** |

---

### Data Required to Validate

| Input | Current Estimate | Needed To Calibrate |
|---|---|---|
| **α** — adoption rate per $ ACV | 1/100,000 | Distribution of (Cert Users / ACV) across live accounts |
| **β** — engagement sensitivity | 1/500 | Distribution of ACV / (WAU + Sense Q) ratios; calibrate so P50 account scores ~50 |
| Break-even ratio (P3 = 50) | ~$25K ACV per (WAU+Q) | Recalibrate once Sense query telemetry is available |
| Expected implementation window | TBD | Historical time-to-go-live by account tier |
| Sense Queries/week | **Not yet available** | Sense query logs at account level — currently proxied by platform sessions |

---

## Q&A

**Juan Daniel Amézquita**
