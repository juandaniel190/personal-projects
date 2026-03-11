# CONTENTSQUARE — SENIOR MANAGER, PRODUCT DATA ANALYST — CASE STUDY PRESENTATION

## PODCAST SIMULATION INSTRUCTIONS FOR NOTEBOOKLM

This document contains the full context for a business case study presentation by Daniel Amezquita, a candidate for the Senior Manager, Product Data Analyst role at Contentsquare. The presentation is structured as a 12-slide investment case analyzing whether Contentsquare should stop, maintain, or increase investment in its CS Apps product line.

**Goal for the podcast:** Simulate a professional walkthrough of Daniel's presentation, narrating each slide with the analytical rigor of a senior product analyst. After the presentation walkthrough, simulate a Q&A panel where four interviewers challenge Daniel with questions from their domain expertise. The tone should be confident, structured, and data-driven — like a McKinsey case presentation to a product leadership team.

---

## SECTION 1: THE CASE AND THE PRESENTER

### Who is Daniel Amezquita?
Daniel is presenting a case study for the Senior Manager, Product Data Analyst position at Contentsquare. He has experience in product analytics, revenue operations, and data-driven strategy. His approach is hypothesis-driven, metrics-first, and he separates facts from inference explicitly. He is interviewing with Contentsquare's Product Research and Insights organization.

### What is Contentsquare?
Contentsquare is a digital experience analytics platform. It helps companies understand how users interact with their websites and apps through session replays, heatmaps, journey analysis, and behavioral analytics. Contentsquare acquired Hotjar (a simpler analytics tool) and Heap (a product analytics platform). The company has two main product lines:
- **CS Digital**: The legacy core product — session replay, heatmaps, journey analysis. This is the established, high-adoption product.
- **CS Apps**: A newer product line that is being cross-sold to existing CS Digital customers. CS Apps is the focus of this entire case study.

### The Business Question
The Product Director wants to know: **Should we stop, maintain, or increase investment in CS Apps?**

Daniel must answer this using a dataset of 185 accounts over 12 months (January–December 2023), evaluating five dimensions:
1. What hypotheses frame the investment decision?
2. What does the data say, and where is data quality a problem?
3. What 2–3 insights answer the question?
4. What additional data would deepen the analysis?
5. What is the strategic recommendation?

---

## SECTION 2: THE PRESENTATION — SLIDE BY SLIDE

### SLIDE 1 — Title Slide
**Title:** Case Study: Senior Manager, Product Data Analyst | Contentsquare
**Subtitle:** Part 1: Investment Decision — Hypothesis & Data Exploration

Daniel opens by framing the case around the Product Director's question. He introduces the three-pillar analytical framework he will use:
- **P1: Acquisition & Growth** — Is CS Apps generating and growing revenue?
- **P2: Adoption & Engagement** — Are clients reaching time-to-value, adopting, and engaging?
- **P3: Retention & ARR** — Will this revenue renew or churn?

This framework ensures he covers the full customer lifecycle from sale to renewal.

---

### SLIDE 2 — Executive Summary
**Title:** Revenue is growing but delivery is broken | increase investment to fix adoption before the renewal cliff

This is the thesis slide. Daniel's core finding:

**CS Apps shows strong revenue traction (+37% ACV, +30% accounts) but a clear gap between selling and delivering value.** Only 15% of accounts are live, 71% have zero certified users, and the health metric is flawed because it blends CS Digital usage into CS Apps health, making non-users appear healthy. The real risk is renewal refusal from non-users with no ROI evidence, not active churn. $16.0M renews in Q4 across 31 accounts, creating concentrated exposure.

The narrative arc:
- Acquisition is strong (revenue is growing) →
- But adoption is fragile (clients aren't going live or engaging) →
- Creating a latent renewal risk: non-adopters face procurement conversations with no ROI evidence

**Three Pillars Summary:**
| Pillar | Status | Summary |
|--------|--------|---------|
| P1: Acquisition & Growth | Strong | +37% ACV, +30% accounts: demand is real |
| P2: Adoption & Engagement | Broken / Ramping-up | 86% not live, 71% zero certified users, shallow engagement |
| P3: Retention & ARR | At Risk | Health metric is unreliable. The real risk: 31 accounts renewing $16M in Q4 with no CS Apps adoption to justify the contract |

**Strategic Recommendations (brief):**
- P1: Focus on strategic segments (Telco, Americas)
- P2: Increase visibility of high-stickiness modules (Workspace, Error Analysis); focus on implementation and integration bottleneck
- P3: Triage the 31 Q4 accounts now: identify which are non-live, assign implementation owners, build the ROI case before renewal conversations start

---

### SLIDE 3 — P1: Acquisition & Growth
**Title:** P1: +37% ACV and +30% accounts in 12 months | demand is real, the problem is not sales

This slide proves that CS Apps is selling well. The problem is not demand — it is what happens after the sale.

**Key Metrics (H1: Revenue & Account Growth):**
| Metric | Jan 2023 | Dec 2023 | Change |
|--------|----------|----------|--------|
| CS Apps ACV | $11M | $15M | +37% |
| Total relationship ACV | $49M | $63M | +29% |
| Number of accounts | 134 | 174 | +30% |
| Mean CS Apps ACV per account (ARPU) | $84K | $89K | +6% |
| CS Apps penetration (Apps / Total ACV) | 23% | 25% | +2pp |

CS Apps ACV is growing faster than total relationship ACV (+37% vs. +29%). While 96% of Apps ACV is cross-sell from CS Digital, 7 net-new accounts contributed $1.2M. However, those net-new accounts churn at 14% (3x portfolio average), indicating CS Apps cannot sustain independent relationships without a Digital anchor.

**H7: High-Value Segment Opportunity:**
| GEO | Accounts | TOTAL_ACV | APPS_ACV | UFR | PEN % |
|-----|----------|-----------|----------|-----|-------|
| EMEA | 121 | 38.6M | 9.2M | 1.4M | 24% |
| AMERICAS | 42 | 22.3M | 4.8M | 6.5M | 22% |
| APJ | 11 | 2.3M | 1.4M | 338K | 63% |
| Grand Total | 174 | 63.1M | 15.5M | 8.2M | 25% |

Key insights:
- Americas has a $6.5M UFR to renew in December, driven by one account in Telco. This account only represents 28% of ACV Apps in America with $4.7M in UFR for December.
- APJ has a high CS Apps penetration of 63%, a playbook to replicate.
- Retail, Telco, and BFSI are the top 3 verticals for CS Apps with 61% of the Total Apps ACV.

**P1 Verdict:** Acquisition is strong. CS Apps is selling well and growing. The problem is not demand; it is what happens after the sale.

---

### SLIDE 4 — P2: Adoption & Engagement
**Title:** P2: 86% of accounts are not live and 71% have zero certified users. Adoption is the broken link

This is the most critical slide. It reveals the delivery failure.

**H4: Implementation Bottleneck**
CS Apps Implementation Status (latest snapshot):
- NULL / Untracked: 48 (28%)
- Not started: 8 (5%)
- Started: 14 (8%)
- Partially implemented: 17 (10%)
- Implemented: 57 (33%)
- Partially lived: 5 (3%)
- Lived: 25 (14%)

Only 25 (14%) are "Lived"; 57 (33%) at "Implemented"; 48 (28%) untracked. **86% are not in production.**

**H6: Shallow Module Engagement**
1 in 4 sessions lands on the Homepage. Users who reach Zoning, Workspace, or Error Analysis show higher engagement; this is a depth-of-usage problem.

| Module | % Sessions | Avg Sess/User | Note |
|--------|-----------|---------------|------|
| Homepage | 25.7% | 2.9 | Navigation, not value |
| Zoning Analysis | 18.2% | 3.8 | Core analytics |
| Journey Analysis | 11.3% | 2.8 | Core analytics |
| Workspace | 7.4% | 4.0 | High stickiness |
| Session Replay | 6.4% | 3.6 | Core analytics |
| Error Analysis | 0.6% | 4.4 | Highest stickiness, lowest reach |

Workspace and Error Analysis are high-stickiness modules (highest avg sessions/user) but have the lowest reach. This is a product surface area problem — the most valuable features are buried.

**H2: Certification & Adoption Gap**
- Certification gap: average 0.7 certified users per account — vs 18 on CS Digital.
- Zero adoption: 71% of accounts (132/185) have no certified CS Apps users.
- Declining engagement: Users grew modestly (455 to 589), but sessions per user fell from 14.5 to 10 in December. Engagement intensity is declining as the base expands.

**P2 Verdict:** Adoption is the broken link. 86% of accounts are not live. Those that are live have 0.69 certified users on average and shallow module engagement.

---

### SLIDE 5 — P3: Retention & ARR
**Title:** P3: $7.2M of the Q4 renewal cliff sits with unhealthy accounts | retention is at risk if adoption is not fixed

**H5: Renewal Pipeline at Risk**

| Fiscal Quarter | UFR | Accts | % Accts Healthy | % UFR Healthy | Renewal Rate | ACV Retained |
|----------------|-----|-------|-----------------|---------------|--------------|--------------|
| Q4-2022 | $5M | 20 | 56% | 57% | 90% | 85% |
| Q1-2023 | $2.7M | 15 | 63% | 55% | 87% | 83% |
| Q2-2023 | $5.1M | 23 | 58% | 88% | 96% | 96% |
| Q3-2023 | $5.4M | 17 | 57% | 62% | 94% | 97% |
| Q4-2023 | $16M | 31 | 54% | 56% | n/a | Target ≥90% |

Important context on how UFR (Up For Renewal) is calculated: For each fiscal quarter, UFR equals the sum of TOTAL_UFR in the LAST MONTH of that quarter only. You do not sum across months within a quarter because accounts that appeared in prior months already renewed. For example, if November shows $8M and December shows $8M, the Q4 UFR is only the December value ($8M), not $16M.

**The current health metric cannot reliably identify Q4 renewal risk.** With $7.2M of the $16M Q4 pipeline sitting in unhealthy accounts, the metric signals exposure but cannot pinpoint where to act. Without a reliable signal, 31 renewals worth $16M enter the quarter without a defensible prioritization framework.

**New Health Score Scenario — Q4-2023 Account Health Breakdown:**
Using a proposed three-pillar composite health score (detailed in the Health KPI slide), the Q4 breakdown changes:

| Category | Accounts | % Accts | UFR | % UFR | Root Cause |
|----------|----------|---------|-----|-------|------------|
| Healthy | 21 | 68% | $12.4M | 78% | — |
| P1 — Not Implemented | 4 | 13% | $1.3M | 8% | Long implementation times |
| P2 — No Certified Users | 6 | 19% | $2.3M | 14% | Implemented but low certified users ratio |
| P3 — Engagement | 0 | 0% | — | — | — |
| Total | 31 | 100% | $16.0M | 100% | — |

This is a scenario analysis based on a proposed segmentation model. The new metric reclassifies accounts more precisely — 5 accounts move from Unhealthy to Healthy, 1 from Healthy to Unhealthy. Zero accounts fail on engagement alone, confirming that where adoption exists, engagement follows.

**P3 Verdict:** The health metric cannot be used as evidence of deterioration. The real retention risk is not active churn. It is renewal refusal: 31 accounts renew $16.0M in Q4 with no CS Apps adoption to justify the contract. Fix implementation now, not after renewals fail.

---

### SLIDE 6 — Strategic Recommendations
**Title:** Five actions close the delivery gap before the Q4 renewal cliff

Five actions close the delivery gap before Q4 2024, with three data pipeline fixes that are prerequisites.

**Priority Actions:**

1. **P2 Adoption (HIGH priority)**
   - Objective: Improve engagement and adoption of the platform
   - KPIs: "Lived" rate: 14% → 40%+; 0 → 3+ certified users/account; Homepage share 26% → 15%
   - Initiatives: Accelerate implementation; Drive certification; In-product activation flows

2. **P3 Retention (MEDIUM priority)**
   - Objective: Secure the Q4 renewal cliff before procurement conversations start
   - KPI: Renewal rate ≥90% on $16.0M Q4 UFR
   - Initiative: Triage 31 Q4 accounts by go-live status; assign owners to non-live

3. **P1 Acquisition (LOW priority)**
   - Objective: Sustain and accelerate revenue and account growth
   - KPI: Benchmark Fashion 73% health
   - Initiative: Segment playbooks (Telco & Americas)

**Data Quality Audit:**
- NULL Implementation Status: 29% (82 accounts), 518 rows untracked — systemic pipeline issue (HIGH)
- Contract Date Array Problem: CONTRACT_START_DATE and CONTRACT_END_DATE store comma-delimited arrays of multiple dates (60% of accounts have 2+ start dates). Cannot compute time-to-live without parsing logic to isolate the CS Apps-specific contract. Blocks cohort analysis and TTL calculations (MEDIUM)
- AVG_WAU_GLOBAL = 0: 156 rows (49 accounts) — breaks health metric for ~27% of base (CRITICAL)

**What Would Deepen This Analysis:**
- Sales: Win/loss data vs. Glassbox/FullStory; cross-sell attach rate into CS Digital base
- CS Team: Renewal outcomes for early cohorts; time-to-go-live by segment
- Market: TAM by vertical — is Telco a ceiling or opportunity?
- Customer: Exit verbatims from churned accounts

---

### SLIDE 7 — Part 2 Title: AI-Era Pricing & Health
**Title:** Part 2: AI-Era Pricing & Health — Monetization & Account Health Redefinition

This is the bonus section Daniel chose to address. The current Contentsquare pricing model has the risk of "Value Leakage," where the client gets massive ROI from AI-driven insights (via Contentsquare's new "Sense" AI product) but the company is not monetizing it because revenue stays flat under session-based pricing.

Three questions frame this section:
1. Should Sense Analyst be priced as a flat-fee add-on, success-based tier, or credit-based model?
2. What analysis determines the right pricing model?
3. How do we redefine account health when AI reduces human time-in-tool?

---

### SLIDE 8 — AI Pricing Recommendation
**Title:** Daily Sense Analyst quotas by tier capture AI value without replacing session pricing

Daniel's recommendation: Introduce daily Sense Analyst query quotas by tier (Quota + Tier model), with Sense Chat included free across all plans. This captures AI value without replacing session-based pricing.

**How the Market Is Pricing AI Today (competitive analysis):**

| Model | How it works | Examples | Assessment |
|-------|-------------|----------|------------|
| Flat-Fee Add-On | Fixed $/year for unlimited AI | Gainsight | Simple but misaligned; leaves value on table |
| Usage / Token-Based | Pay per AI query or token | PostHog, Anthropic API | Transparent but volatile for budgets |
| Outcome-Based | Pay per resolved outcome | Intercom Fin ($0.99/ticket) | Hard to measure in analytics |
| **Quota + Tier (Recommended)** | Daily/monthly cap per tier, upgrade for more | Anthropic Claude, Salesforce Agentforce | Best fit: frequent friction drives upgrades |

Key findings:
- Analytics competitors (Amplitude, Mixpanel, Heap) currently bundle AI into tiers for free because their AI features are lightweight. When AI becomes the primary interface (as Sense Agent intends), bundling alone won't capture the value.
- The Anthropic parallel is instructive: Claude Pro users hit a daily usage cap and must either wait until the next day or upgrade to a higher tier. This creates frequent, low-friction upgrade pressure without fully blocking work.

---

### SLIDE 9 — Pricing Tiers
**Title:** A 5-query daily cap covers ~96% of users and creates natural upgrade friction

Daily Sense Analyst caps by plan; Sense Chat included free on all tiers:

| Tier | Price | Key Feature |
|------|-------|-------------|
| Free | €0/forever | Up to 200K monthly sessions; Session Replay & heatmaps; Sense Chat included; Sense Analyst not included |
| Growth (Most popular) | From €39/month | Starting at 7K monthly sessions; Sense Chat unlimited; Sense Analyst 5 queries/day; Cap resets daily |
| Pro | Let's talk | Starting at 1M monthly sessions; Sense Analyst 25 queries/day; Multi-session replay summaries; Precision filtering, retroactive |
| Enterprise | Let's talk | Custom sessions; Sense Analyst unlimited; Error summaries & data feeds; Unlimited projects |

Why 5/day? Customers average 3 sessions daily; 5 queries/day should cover most workflows while creating a clear upgrade incentive. Cap resets daily. Based on logs data from AI Sense, the optimal amount of queries, tokens, or credits can be calculated (e.g., 1 credit = 1 question, 3 credits = 1 zone analysis).

Why this model wins:
- Captures uncaptured value: Revenue tied to AI usage, not just session volume
- Preserves session pricing: Sessions remain the base layer; Sense quota is additive
- Simple to explain: Global daily cap per tier is transparent and easy for procurement
- Natural upgrade path: Regular friction drives tier upgrades without blocking work

---

### SLIDE 10 — Usage Distribution Analysis
**Title:** Usage is concentrated: top 20% drive 65% of sessions, validating tiered quotas

This slide provides the data evidence for the tiered pricing model.

A histogram of "Distribution of Daily Usage per Account" (Platform Sessions, proxy for AI Query Demand) shows:
- P50: 1/day
- P75: 2/day
- The distribution is heavily right-skewed

Quota Coverage by Tier:
| Tier | % of accounts within daily cap |
|------|-------------------------------|
| Free (No Sense Analyst) | 0% |
| Growth (5/day) | 96% |
| Pro (25/day) | 100% |
| Enterprise (Unlimited) | 100% |

Usage is heavily concentrated: top 20% of accounts drive 65% of sessions. P90 vs. median = 6x.

The subsidization problem: Under a flat-fee model, light users would subsidize heavy users; quota + tier aligns price with usage.

**Why other models were discarded:**
- Flat-Fee Add-On: Usage is too concentrated (top 20% = 65%). Heavy users would be subsidized.
- Success-Based Tier: Cannot prove usage drives outcomes with current data.
- Credit-Based: Cannot test; Sense query logs not available yet.
- Quota + Tier (confirmed): Natural daily breakpoints exist (P50, P75, P90). 5/day creates friction without blocking work.

**Additional data that would sharpen this decision:**
- Sense query logs (type, cost, timestamp): whether different query types cost enough to justify credits
- Query → action taken (export, share): whether usage correlates with outcomes; would revive Success-Based
- Renewal outcomes by usage tier: whether heavy users actually renew at higher rates

---

### SLIDE 11 — Health KPI Redefinition
**Title:** The current health metric masks adoption failure. A three-pillar formula fixes it

This is the methodological backbone of the new health metric Daniel proposes.

**Three Pillars:**

**P1 | Implementation Velocity** (Non-Live only. Dropped once Live.)
- 100 if within implementation window
- Linear decay beyond window
- Measures whether the client is on track to go live

**P2 | Adoption (ACV-Normalized)**
- Formula: Cert / (ACV × α)
- Where α = 1/100,000 (adoption rate per dollar of ACV)
- Normalizes adoption vs. account size — a $500K account needs more certified users than a $50K account

**P3 | Engagement Quality (AI-Aware)**
- Formula: ACV / (WAU + Sense Q/wk) × β
- Where β = 1/500 (engagement sensitivity)
- WAU + Sense Queries/week avoids penalizing accounts that migrate from manual analytics to AI-driven queries via Sense

**Composite Formula:**
- If Non-Live / Partially Live: Score = (0.15 × P1) + (0.25 × P2) + (0.60 × P3)
- If Live: Score = (0.3 × P2) + (0.7 × P3)
- Healthy = Score ≥ 50

**Illustrative Examples (Dummy Data):**
Assumed constants: α = 1/100,000; β = 1/500; Expected implementation window = 90 days

| Account | ACV | Status | Impl Days | WAU | Sense Q/wk | Cert Users | P1 | P2 | P3 | Score |
|---------|-----|--------|-----------|-----|------------|------------|----|----|----|----- |
| A — Acme Corp | $200K | Non-Live | 210 | 2 | 0 | 1 | 0 | 50 | 0 | 15 (Unhealthy) |
| C — Gamma Inc | $200K | Live | — | 20 | 10 | 5 | — | 100 | 87 | 92 (Healthy) |

**Data Required to Validate:**
| Input | Current Estimate | Needed To Calibrate |
|-------|-----------------|---------------------|
| α: adoption rate per $ ACV | 1/100,000 | Distribution of (Cert Users / ACV) across live accounts |
| β: engagement sensitivity | 1/500 | Distribution of ACV / (WAU + Sense Q) ratios; calibrate so P50 account scores ~50 |
| Break-even ratio (P3 = 50) | ~$25K ACV per (WAU+Q) | Recalibrate once Sense query telemetry is available |
| Expected implementation window | TBD | Historical time-to-go-live by account tier |
| Sense Queries/week | Not yet available | Requires Sense query logs at account level, currently proxied by platform sessions |

---

### SLIDE 12 — Q&A
**Title:** Q&A — Juan Daniel Amezquita

---

## SECTION 3: THE INTERVIEW PANEL — PROFILES AND LIKELY QUESTIONS

The interview panel consists of four senior leaders. The session runs from 3:30 PM to 4:30 PM CET.

---

### PANELIST 1: Paula Herrera — Director, Product Research

**Background:** Paula Herrera is the Director of Product Research at Hotjar by Contentsquare. She is based in Barcelona. She holds an MA in Music Business Management from the University of Westminster. Before Contentsquare/Hotjar, she was at GetYourGuide as a senior researcher and team lead. She identifies as an anthropologist and product researcher with a passion for mixed methods. She launched the Customer Insights League (CIL) at GetYourGuide, fostering cross-functional collaboration between research, data, sales, and customer success teams. She has spoken publicly about mastering user interviews, the current state of UX research, and partnering with teams that collect customer knowledge (Sales, Data, CS) to provide a joint point of view that represents customer needs.

**What she cares about:** Research rigor, mixed-methods validation, metric definitions grounded in user behavior (not just business logic), connecting qualitative signals (user interviews, exit verbatims) with quantitative data, democratizing insights, and making research actionable.

**Likely questions from Paula:**

1. **"You built a new health metric with three pillars. How would you validate that this score actually predicts renewal outcomes? What research would you pair with this quantitative model?"**
   - She will want to see that Daniel doesn't rely purely on the formula. She'll expect him to say: "I would pair this with qualitative research — customer exit interviews from churned accounts, renewal conversation recordings from the CS team, and a retrospective validation where we back-test the score against known Q1–Q3 renewal outcomes."

2. **"You say 86% of accounts are not live. But what does 'not live' actually mean to the customer? Have you validated that 'Lived' status in the CRM matches the customer's perception of value delivery?"**
   - This is a metric-definition challenge. Paula will probe whether "Implementation Status" is a reliable field or a CRM artifact. Daniel should acknowledge: "This is a CRM field, and 28% of accounts have NULL values. I would recommend a qualitative validation — interview a sample of accounts classified as 'Implemented' vs. 'Lived' to understand if these stages map to how customers describe their own readiness."

3. **"You mention exit verbatims from churned accounts as 'additional data.' If you had those today, how specifically would they change your analysis?"**
   - She wants to see that Daniel can integrate qualitative data into the analytical framework, not just list it as a wish-list item.

4. **"Your engagement analysis uses sessions and WAU. But how do you know these metrics capture meaningful engagement vs. just page loads? What qualitative signal would tell you the difference?"**
   - This probes whether Daniel understands the difference between behavioral metrics and outcome metrics. She'll want him to reference concepts like "aha moments," time-to-value, and feature adoption depth.

5. **"How would you work with the research team to build the customer voice into this kind of investment decision?"**
   - Testing collaboration and research partnership skills.

---

### PANELIST 2: Claire Marx — Senior Director, Product Insights

**Background:** Claire Marx is the Senior Director of Product Insights at Contentsquare, based in Paris. She studied at HEC Paris. Former colleagues describe her as someone who reorganized and re-motivated a data team, recruited excellent profiles that increased expertise levels, and turned the team into one of the best-performing parts of the organization. She is described as having an all-round skillset: at ease with data analysis, technical discussions with engineers, data interpretation for business stakeholders, and pitching to clients and partners.

**What she cares about:** Data team leadership, insight quality and storytelling, cross-functional communication (engineering, product, commercial), hiring and developing analysts, and ensuring insights translate into business action — not just dashboards.

**Likely questions from Claire:**

1. **"If you were leading a team of 3–4 analysts on this case, how would you have structured the work? What would you delegate, what would you own?"**
   - She's assessing management and prioritization skills. Daniel should describe splitting the work: one analyst on the revenue/acquisition analysis, one on the adoption funnel, one on the renewal pipeline, while he owns the hypothesis framework, quality audit, and executive narrative.

2. **"You identified three data quality issues. How would you prioritize fixing them, and how would you communicate the urgency to engineering?"**
   - She wants to see stakeholder management. Daniel should rank: AVG_WAU_GLOBAL = 0 is CRITICAL (breaks 27% of health scores), NULL Implementation Status is HIGH (blocks the entire adoption analysis), NULL Implementation Status is HIGH (blocks the entire adoption analysis).

3. **"Walk me through how you would present this to a non-technical Product Director in 5 minutes instead of 60."**
   - Testing executive communication. The answer is the Executive Summary slide — thesis first, three pillars with status, five actions, done.

4. **"You recommend a Quota + Tier pricing model. What would the analytics instrumentation look like to measure whether it's working after launch?"**
   - She'll want to hear about A/B testing, conversion funnels (free → growth → pro), upgrade trigger analysis, and query-level telemetry.

5. **"What's missing from this analysis that concerns you the most?"**
   - Intellectual honesty test. Daniel should mention: time-to-go-live cohort analysis (blocked because contract date fields store comma-delimited arrays of multiple contract start dates — 60% of accounts have 2+ dates — and disambiguating which date maps to CS Apps requires additional parsing logic), competitive win/loss data, and the inability to validate the health score against actual renewal outcomes since Q4 hasn't happened yet.

6. **"How would you build the analytics roadmap for CS Apps for the next two quarters?"**
   - Strategic thinking about measurement infrastructure.

---

### PANELIST 3: Mengdi Zhao — Senior Product Data Analyst 2

**Background:** Mengdi Zhao is a Senior Product Data Analyst 2 at Contentsquare. As a peer-level technical interviewer, she will likely focus on methodology, SQL/data logic, statistical rigor, and analytical craftsmanship. She is the person most likely to challenge the technical details of Daniel's calculations.

**What she cares about:** Analytical methodology, statistical validity, data pipeline awareness, metric definitions and edge cases, reproducibility of analysis, and whether Daniel's SQL/Python logic would hold up to scrutiny.

**Likely questions from Mengdi:**

1. **"How did you calculate UFR by quarter? Walk me through the deduplication logic."**
   - This is a trap question because the naive approach (sum across months) is wrong. Daniel should explain: "UFR for a quarter equals the TOTAL_UFR from the last month of that quarter only. You do not sum across months because accounts that appeared in earlier months already renewed. For Q4, that's the December snapshot."

2. **"Your health score uses constants α = 1/100,000 and β = 1/500. How did you arrive at these? What happens to the score distribution if α is off by 2x?"**
   - Sensitivity analysis. Daniel should say: "These are initial estimates calibrated so that a $100K account with 1 certified user scores P2=100, which felt reasonable as a starting point. If α is 2x too high, the P2 distribution shifts left and more accounts appear adoption-unhealthy. That's why I included a calibration table — these constants need to be validated against the distribution of certified users across live accounts."

3. **"You say sessions per user fell from 14.5 to 10. Is that a real engagement decline or just a base-rate effect from adding low-engagement new users?"**
   - Cohort analysis question. Daniel should acknowledge: "This is likely a mix of both. To isolate the effect, I would need cohort-level analysis — segment users by their first active month and track session frequency over time. I would need cohort-level analysis — but this is blocked by the contract date array problem: the CONTRACT_START_DATE field stores multiple comma-separated dates per account (60% of accounts have 2+ dates). I cannot pick a single start date without parsing logic to identify which contract maps to CS Apps specifically. I flagged this as a MEDIUM data quality issue."

4. **"The old health metric classified 54% of Q4 accounts as healthy. Your new metric says 68%. Why should I trust yours more?"**
   - Daniel should explain: "The old metric blends CS Digital usage into CS Apps health, so an account that uses CS Digital heavily but has zero CS Apps certified users can appear healthy. My metric isolates CS Apps adoption explicitly — P1 checks implementation, P2 checks certified users normalized by ACV, P3 checks engagement. The 5 accounts that moved from Unhealthy to Healthy under the new metric were correctly reclassified because they had real adoption. The 1 account that moved from Healthy to Unhealthy was a false positive under the old metric."

5. **"What statistical test would you use to validate whether your health score actually predicts renewal?"**
   - Daniel should reference: "I would use a logistic regression with the health score (or its three pillar components) as predictors and renewal outcome (renewed vs. churned) as the binary dependent variable. I'd also check AUC-ROC to assess discriminative power, and compare it against the old health metric's AUC-ROC. Additionally, I'd segment by account tier to check if the model works equally well for large vs. small accounts."

6. **"You flagged AVG_WAU_GLOBAL = 0 for 49 accounts. Did you exclude them or impute? How does that affect your engagement analysis?"**
   - Edge case handling. Daniel should explain his approach and the impact on results.

---

### PANELIST 4: Ted Ottey — Product Manager Director

**Background:** Ted Ottey is a Product Manager Director at Heap by Contentsquare (Heap was acquired by Contentsquare). He is based in the Greater Philadelphia area. He studied at Rensselaer Polytechnic Institute (both BS and MS). His career progression: UX Designer → Senior UX Designer → Product Manager → Senior Product Manager at Acquia (working on Acquia Lift, a SaaS marketing content personalization product), then Product Manager at Talend (cloud-native ETL), then Principal Product Manager and Senior Product Manager at Heap. Colleagues describe his UX background combined with technical proficiency, and his ability to take customer problems, break them down with a team to achievable milestones, and brainstorm/negotiate with engineers as making him incredibly effective.

**What he cares about:** Product strategy, customer problems translated into roadmap items, UX-informed product decisions, engineering feasibility, go-to-market alignment, and how analytics informs product prioritization.

**Likely questions from Ted:**

1. **"You recommend accelerating implementation and driving certification. From a product perspective, what would you build to make that happen? What does the in-product activation flow look like?"**
   - He wants product thinking, not just analytics. Daniel should describe: onboarding wizards, implementation progress dashboards visible to the CS team, automated nudges when an account stalls at "Partially Implemented" for >30 days, and in-product prompts to certify additional users.

2. **"You showed that Workspace and Error Analysis have the highest stickiness but lowest reach. As a product person, how would I prioritize surfacing those features vs. fixing the implementation bottleneck?"**
   - Trade-off question. Daniel should frame it as sequential: "Fix the implementation bottleneck first — if accounts aren't live, feature discovery is irrelevant. Once live, then surface high-stickiness modules through personalized dashboards, guided tours, or 'Did you know?' prompts."

3. **"The Quota + Tier pricing model is interesting. But how would you handle the transition for existing enterprise customers who currently have unlimited access? Won't they push back?"**
   - GTM and change management. Daniel should acknowledge the risk: "Existing enterprise customers would be grandfathered with unlimited access or a generous cap that exceeds their current usage (using the usage distribution data I showed). The tier structure applies to new contracts and renewals. The data shows P90 usage is 6x the median, so setting Enterprise at 'Unlimited' while Growth is capped at 5/day creates a natural migration path."

4. **"You mention Sense queries per week as a P3 engagement variable, but it's not available yet. How reliable is your health metric without it?"**
   - Feasibility challenge. Daniel should say: "Without Sense query data, P3 relies solely on WAU, which is an imperfect proxy. The formula is designed to be future-proof — once Sense query logs are available, they plug directly into the denominator. In the interim, the metric still improves on the current one because P1 and P2 already isolate the biggest failure modes (implementation and adoption), which is where 100% of unhealthy accounts fail."

5. **"If you could only ship one thing from your recommendation list in the next quarter, what would it be and why?"**
   - Prioritization under constraints. Daniel should say: "Triage the 31 Q4 accounts. It's the highest-leverage, lowest-cost action. It doesn't require product changes — it requires the CS team to identify which of the 31 accounts are non-live, assign implementation owners, and build the ROI case before renewal conversations start. The data already exists to do this today."

6. **"How would this analysis change if Contentsquare decided to make CS Apps a standalone product rather than a cross-sell?"**
   - Strategic scenario. Tests whether Daniel understands the dependency on CS Digital as an anchor.

---

## SECTION 4: KEY METRICS AND TERMINOLOGY

A Senior Manager of Product Data Analytics at a SaaS company like Contentsquare is expected to be fluent in these metrics and concepts. Daniel should naturally weave these into his presentation and Q&A answers.

### Revenue & Business Metrics
- **ACV (Annual Contract Value):** The annualized revenue from a single customer contract. CS Apps ACV grew from $11M to $15M (+37%).
- **ARR (Annual Recurring Revenue):** The annualized run-rate of all active subscriptions. Closely related to ACV in SaaS.
- **ARPU (Average Revenue Per User/Account):** CS Apps ARPU grew from $84K to $89K (+6%).
- **UFR (Up For Renewal):** The dollar value of contracts that will come up for renewal in a given period. Critical for forecasting retention risk.
- **Net Revenue Retention (NRR):** (Starting ARR + Expansion - Contraction - Churn) / Starting ARR. A key SaaS health metric. >100% means existing customers are growing.
- **Gross Revenue Retention (GRR):** (Starting ARR - Contraction - Churn) / Starting ARR. Always ≤100%. Measures the floor of revenue retained.
- **Logo Churn Rate:** Percentage of accounts that cancel in a period.
- **Revenue Churn Rate:** Percentage of ARR lost to cancellations and contractions.
- **Cross-sell Attach Rate:** Percentage of existing CS Digital customers that add CS Apps. 96% of CS Apps ACV comes from cross-sell.
- **Penetration Rate:** CS Apps ACV / Total Relationship ACV. Currently 25%.
- **LTV (Lifetime Value):** Expected total revenue from a customer over their lifetime. LTV = ARPU / Churn Rate.
- **CAC (Customer Acquisition Cost):** Cost to acquire a new customer. LTV:CAC ratio should be >3:1 for healthy SaaS.

### Product & Adoption Metrics
- **Time-to-Value (TTV):** How long it takes a customer to reach their first meaningful outcome after purchase. Directly related to the implementation bottleneck — 86% of accounts are not live, meaning TTV is extremely long or infinite for most CS Apps customers.
- **Time-to-Live (TTL):** The number of days from contract start to "Lived" implementation status. This calculation is blocked by the contract date array problem — CONTRACT_START_DATE stores a comma-delimited list of multiple dates (60% of accounts have 2+ start dates), requiring parsing and disambiguation before TTL can be computed.
- **Implementation Velocity:** Speed at which accounts move through implementation stages. Daniel's P1 pillar measures this.
- **Activation Rate:** Percentage of accounts that complete key onboarding milestones (e.g., going live, certifying first user).
- **Feature Adoption Rate:** Percentage of users or accounts using a specific feature. Workspace has 7.4% session share but highest stickiness.
- **DAU/WAU/MAU (Daily/Weekly/Monthly Active Users):** Standard engagement metrics. AVG_WAU_GLOBAL is used in the dataset.
- **Stickiness (DAU/MAU ratio):** How often users return. Higher stickiness = stronger habit.
- **Session Depth:** Number of pages or modules visited per session. 1 in 4 CS Apps sessions lands on the Homepage — a shallow engagement signal.
- **Certified Users:** Users who have completed product certification/training. Average 0.7 per CS Apps account vs. 18 on CS Digital.

### Cohort Analysis & Retention
- **Cohort Analysis:** Grouping users or accounts by a shared characteristic (e.g., contract start month) and tracking behavior over time. In this dataset, cohort analysis is blocked by the contract date array issue — the CONTRACT_START_DATE field stores multiple comma-separated dates per account, making it impossible to assign a single "cohort start date" without additional data engineering.
- **Retention Curve:** A chart showing what percentage of a cohort remains active over time. Flattens when product-market fit exists.
- **Survival Analysis:** Statistical method to model time-to-event (e.g., time-to-churn). Could be used to validate the health score.
- **Renewal Rate:** Percentage of UFR accounts that successfully renew. Q2-2023 was 96%, Q3 was 94%.
- **Logo Retention vs. Dollar Retention:** Logo retention counts accounts equally; dollar retention weights by ACV. Dollar retention can exceed 100% with expansion.

### Health Scoring & Segmentation
- **Account Health Score:** A composite metric that predicts renewal likelihood. The current metric is flawed (blends CS Digital). Daniel proposes a three-pillar replacement.
- **Leading vs. Lagging Indicators:** Leading indicators predict future outcomes (engagement, adoption). Lagging indicators report past results (churn, renewal). A good health score uses leading indicators.
- **Propensity-to-Churn Model:** A predictive model (often logistic regression or random forest) that scores accounts by their likelihood to churn.
- **Customer Segmentation:** Grouping accounts by shared attributes (e.g., geo, vertical, ACV tier, health status) to prioritize interventions.
- **RFM Analysis (Recency, Frequency, Monetary):** A segmentation framework from e-commerce applicable to SaaS engagement — how recently did the account use the product, how frequently, and how much are they paying?

### Pricing & Monetization
- **Value Leakage:** When a product delivers value to the customer but the company fails to capture it in revenue. The core risk Daniel identifies with AI/Sense.
- **Usage-Based Pricing (UBP):** Pricing tied to consumption (queries, sessions, API calls). Growing trend in SaaS.
- **Quota + Tier Model:** Daniel's recommendation — daily caps per pricing tier that create natural upgrade friction.
- **Price Elasticity:** How sensitive demand is to price changes.
- **Willingness-to-Pay (WTP):** What customers would pay for a feature. Often measured through Van Westendorp or Gabor-Granger surveys.
- **ARPAU (Average Revenue Per Active User):** More precise than ARPU — excludes inactive accounts.

### Data Quality & Governance
- **NULL Rate / Missing Data Rate:** Percentage of records with missing values. Daniel flagged 28–29% NULL rates on critical fields.
- **Data Pipeline Issue:** A systemic problem in how data flows from source systems to the analytics warehouse.
- **Metric Trustworthiness:** Whether a metric can be relied upon for decision-making. Daniel's core argument is that the current health metric is untrustworthy.
- **Survivorship Bias:** Analyzing only surviving accounts (not churned ones) can skew conclusions about what drives success.

### Statistical & Analytical Methods
- **Logistic Regression:** A statistical model for predicting binary outcomes (renew/churn). The method Daniel should reference for validating the health score.
- **AUC-ROC (Area Under the Receiver Operating Characteristic Curve):** Measures how well a model discriminates between positive and negative cases. Higher = better predictive model.
- **Sensitivity Analysis:** Testing how results change when assumptions change (e.g., what if α = 1/50,000 instead of 1/100,000?).
- **A/B Testing:** Randomized experiments to compare two versions of a product change.
- **Pareto Analysis (80/20 Rule):** Daniel's finding that top 20% of accounts drive 65% of sessions is a Pareto observation.

---

## SECTION 5: PRESENTATION FLOW SCRIPT

Here is how Daniel should narrate the presentation from start to finish:

**Opening (30 seconds):**
"Thank you for your time. I'm Daniel Amezquita, and today I'm presenting my analysis of whether Contentsquare should stop, maintain, or increase investment in CS Apps. My answer: increase investment — but redirect it from acquisition to adoption and retention. Let me show you why."

**Executive Summary (2 minutes):**
"CS Apps is growing — 37% ACV growth, 30% more accounts in 12 months. The sales motion is working. But there's a dangerous gap between selling the product and delivering value. Only 15% of accounts are live. 71% have zero certified users. And the health metric that's supposed to tell us which accounts are at risk is flawed — it blends CS Digital usage into CS Apps health, making non-users look healthy. The real risk isn't active churn. It's renewal refusal. 31 accounts renew $16 million in Q4 with no CS Apps adoption to justify the contract."

**P1 — Acquisition (3 minutes):**
"Let's start with the good news. CS Apps ACV grew from $11M to $15M — that's 37%, outpacing the overall portfolio at 29%. We added 40 accounts. Penetration went from 23% to 25%. The Americas region has $6.5M in UFR concentrated in Telco. APJ has 63% penetration — a playbook worth replicating. But here's the critical nuance: 96% of this revenue is cross-sell from CS Digital. The 7 net-new accounts contributed $1.2M but churn at 14% — three times the portfolio average. CS Apps cannot yet stand alone. The verdict: acquisition is strong. The problem is not demand. It's what happens after the sale."

**P2 — Adoption (5 minutes):**
"This is where the case breaks open. 86% of accounts are not in production. Look at the implementation funnel: 28% are NULL — we don't even track their status. Only 14% have reached 'Lived.' And of those that have implemented, the average is 0.69 certified users — compared to 18 on CS Digital. 71% of accounts have zero certified CS Apps users. Engagement is shallow: 1 in 4 sessions lands on the Homepage. But here's the insight — Workspace and Error Analysis have the highest stickiness, 4.0 and 4.4 sessions per user respectively, but the lowest reach. The most valuable features are buried. The verdict: adoption is the broken link. We're selling a product that most customers never use."

**P3 — Retention (4 minutes):**
"Now the question becomes: will this revenue renew? The current health metric says 54% of Q4 accounts are healthy, 56% of UFR. But this metric is unreliable. It blends CS Digital usage into CS Apps health. So I built a scenario using a new three-pillar health score that isolates implementation, adoption, and engagement. The result: 68% of Q4 accounts are actually healthy by this new metric — 21 accounts, $12.4M. The 32% that are unhealthy break down clearly: 13% are failing on implementation — 4 accounts, $1.3M that never went live. 19% are failing on adoption — 6 accounts, $2.3M that implemented but have zero certified users. Zero accounts fail on engagement alone. Where adoption exists, engagement follows. The failure is upstream."

**Recommendations (2 minutes):**
"Five actions. Priority one: fix adoption. Get the lived rate from 14% to 40%. Drive certification from 0 to 3+ users per account. Surface Workspace and Error Analysis. Priority two: secure Q4. Triage those 31 accounts now — identify which are non-live, assign implementation owners, build the ROI case before procurement conversations start. Priority three: sustain acquisition by building segment playbooks for Telco and Americas. And fix three data pipeline issues: the 29% NULL implementation status that makes the adoption funnel untrackable; the contract date array problem where 60% of accounts have multiple comma-separated contract dates in a single field, making time-to-live calculations impossible without disambiguation logic; and the 49 accounts with AVG_WAU_GLOBAL = 0 that break the health metric for 27% of the base."

**Part 2 — AI Pricing (3 minutes):**
"One more thing. Contentsquare is rolling out Sense — an AI analyst. The current pricing model has a value leakage risk: clients get massive ROI from AI-driven insights, but revenue stays flat because we charge by sessions, not by AI usage. I evaluated four pricing models. The recommendation: Quota + Tier. Give everyone Sense Chat for free. Cap Sense Analyst at 5 queries per day on the Growth plan, 25 on Pro, unlimited on Enterprise. The data supports this: the usage distribution shows P50 = 1 session/day, P75 = 2/day. A 5/day cap covers 96% of accounts, creating natural upgrade friction without blocking work. This mirrors how Anthropic prices Claude — daily caps that reset, driving frequent low-friction upgrades."

**Health KPI (2 minutes):**
"Finally, the health metric needs to be rebuilt. The current one masks adoption failure. I propose a three-pillar formula: P1 measures implementation velocity, P2 normalizes certified users by ACV, and P3 measures engagement quality in a way that accounts for AI usage. The formula uses assumed constants that need calibration — I've included a table of what data is needed to validate each one. This isn't a production-ready model. It's a framework designed to replace a metric that currently makes non-users look healthy."

**Close (15 seconds):**
"The bottom line: increase investment in CS Apps, but shift the focus from selling to delivering. The demand is real. The delivery is broken. And the clock is ticking — $16 million renews in Q4."

---

## SECTION 6: KEY PHRASES AND VOCABULARY DANIEL SHOULD USE

During the presentation and Q&A, Daniel should naturally incorporate these phrases to demonstrate senior-level product analytics fluency:

- "We need to separate leading indicators from lagging indicators."
- "The health metric is a lagging indicator masquerading as a leading one."
- "This is a time-to-value problem, not a demand problem."
- "I would validate this with a cohort analysis, but the contract date field stores a comma-delimited array of multiple dates per account — 60% of accounts have two or more contract start dates. Before I can compute time-to-live, I need parsing logic to isolate which date maps to the CS Apps contract specifically."
- "The engagement data shows a depth-of-usage problem — sessions exist, but they're shallow."
- "Net revenue retention is the metric that matters here, and without fixing adoption, NRR will compress."
- "I would back-test this health score against known Q1–Q3 renewal outcomes using logistic regression and measure AUC-ROC."
- "The Pareto distribution in usage validates tiered pricing — the top 20% drive 65% of sessions."
- "We need to instrument the activation funnel: contract signed → implementation started → first certified user → first meaningful session → renewal."
- "This is a cross-sell dependency risk. 96% of revenue is attached to CS Digital. If CS Apps cannot demonstrate independent value, it's a line item that procurement will cut."
- "I flagged three data quality issues because any insight built on unreliable data is a liability, not an asset."
- "The recommendation is: increase investment, but redirect it. The problem is not acquisition — it's activation and retention."
- "Value leakage is the risk: the customer gets the ROI from AI, but we don't capture it in the contract."
- "A sensitivity analysis on the constants would tell us how robust this scoring model is before we ship it."
