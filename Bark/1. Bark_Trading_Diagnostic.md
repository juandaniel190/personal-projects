# Bark.com — Trading Diagnostic

**Prepared for:** LCM Assessment (Feb 2026)
**Data Period:** July 2024 – December 2025 | UK & US Markets | 12 Categories × 3 Channels

---

## Company Context

Bark.com is a London-headquartered services marketplace, founded in 2014, that connects consumers with local professionals across 1,000+ service categories. Its revenue model is lead-based: consumers submit project requests for free, Bark matches them to relevant professionals, and professionals pay per response (PPR) to access the lead. The company operates in 11 markets including the UK (its core market) and the US (its largest growth market), with approximately 265 employees and an estimated annual revenue of $50–100M.

The diagnostic below uses a comparable H2 window (Jul–Dec 2024 vs Jul–Dec 2025) as the primary time range, since it provides a clean year-over-year comparison and eliminates seasonality bias. Full 18-month trends are referenced where useful.

---

## Part 1: UK Country Performance

### Executive Summary

The UK business is experiencing a **revenue and profit contraction** despite growing traffic. H2 2025 revenue fell 16.7% year-over-year to £2.08M (from £2.50M), and profit declined 19.8% to £952K. The core challenge is a **collapsing submission rate** — sessions grew +9.4%, but submissions dropped -8.9%, meaning significantly more traffic is failing to convert into project requests.

### 18-Month Revenue, Profit & Spend Trend

![UK Revenue Trend](chart1_uk_revenue_trend.png)

The chart above reveals a structural shift: the revenue line has settled ~£100K/month lower than the prior-year comparable, while the gap between revenue and spend has narrowed — compressing profit.

### Key Metrics (H2 2024 → H2 2025)

| Metric | H2 2024 | H2 2025 | Δ | YoY % |
|---|---|---|---|---|
| Sessions (Start) | 985,316 | 1,077,620 | +92,304 | **+9.4%** |
| Q1 Pass Rate | 57.3% | 46.2% | -11.1pp | — |
| Submissions | 288,594 | 262,986 | -25,608 | **-8.9%** |
| Submission Rate | 29.3% | 24.4% | -4.9pp | — |
| PPR Revenue | £2,495,309 | £2,079,690 | -£415,619 | **-16.7%** |
| Marketing Spend | £1,309,474 | £1,128,090 | -£181,384 | **-13.9%** |
| APR (Profit) | £1,185,841 | £951,618 | -£234,223 | **-19.8%** |
| Paid Responses | 177,828 | 139,701 | -38,127 | **-21.4%** |

### Diagnosis: The Funnel Is Breaking at the Top

![UK Funnel Slope](chart9_funnel_slope.png)

The slope graph above makes the problem immediately visible: all four funnel rates declined, but the **Q1 Pass Rate** fell the hardest at **-11.2 percentage points** — from 57.3% to 46.2%. This single metric is the root cause of the revenue decline.

![UK Funnel Rates Over Time](chart2_uk_funnel_rates.png)

The monthly view shows the Q1 Pass Rate began diverging from the Submission Rate around May 2025 and accelerated through the summer, reaching its lowest point in Sep–Oct 2025 (below 40% in some months). The Submission Rate followed downward but less sharply, because users who do pass Q1 are actually converting slightly better (Q1→Submit rate improved from 51.1% to 52.9%).

**What this tells us:**

**1. Over half the visitors arriving in H2 2025 abandon the webform before answering the first question.** Since the Q1-to-submission rate actually improved slightly, the problem is specifically at the top of the funnel — users arriving who either aren't intent-qualified or are encountering friction at the very first step.

**2. Revenue per project is declining.** Revenue per released project fell from ~£9.16 in H2 2024 to ~£8.54 in H2 2025, a -6.8% drop. This suggests either a shift in category mix towards lower-value categories, reduced professional willingness to pay for leads, or lower partner contribution.

**3. Paid responses declined -21.4%.** This is steeper than the submission decline (-8.9%), indicating that even among released projects, fewer professionals are choosing to respond with paid credits. This could reflect lower lead quality (linked to the traffic quality issue), supply-side churn, or market saturation.

### Metrics I Would Prioritise

**Primary: Submission Rate (and its sub-component, Q1 Pass Rate).** This is the highest-leverage metric. A 1pp improvement in submission rate at current traffic levels would yield ~10,800 additional submissions per half, which at current monetisation rates translates to roughly £80K–90K in incremental revenue. The Q1 pass rate drop specifically suggests either a traffic quality problem (poor intent from new acquisition channels) or a product/UX issue on the landing page.

**Secondary: Revenue per Released Project (monetisation efficiency).** Even if volume stabilises, declining RPP compresses margins. This metric captures both professional engagement and category mix health.

### Potential Actions

The immediate priority should be diagnosing why the Q1 pass rate collapsed. The two leading hypotheses are: (a) the traffic mix has shifted towards a lower-intent channel (as the Channel 2 analysis in Part 2 will show), and (b) there may have been webform or landing page changes that increased friction. A/B testing the first question and analysing bounce rates by traffic source would clarify this. On the monetisation side, auditing professional response rates by category and testing pricing/credit adjustments could address the RPP decline.

---

## Part 2: Marketing Channel Deep-Dive

### Primary Concern: Channel 2

Channel 2 is the underperforming channel that most urgently requires attention. While it has seen massive volume growth, it is delivering poor-quality traffic that is dragging down the overall UK business.

### Channel Efficiency Comparison

![Channel Scatter](chart4_channel_scatter.png)

This bubble chart captures the full story in a single view. Between H2 2024 and H2 2025:

- **Channel 2** (coral) moved *left and down* — its submission rate dropped from 21% to 14% and ROAS fell from 1.5x to 1.3x, approaching breakeven. It is now the least efficient channel by both measures.
- **Channel 1** (teal) held its position — stable ~28% submission rate and ~1.6x ROAS, but its bubble shrank as budget was redirected.
- **Channel 3** (navy) improved its ROAS from 17.6x to 28.1x, with virtually zero marketing spend — confirming it is organic/SEO traffic.

### Channel 2: Volume vs Conversion Divergence

![Channel 2 Divergence](chart5_ch2_divergence.png)

This is the most telling chart in the entire analysis. Channel 2 sessions surged from ~30K/month in early 2024 to a peak of ~99K in Sep 2025 — a 3.3× increase. But as the bars grew taller, the submission rate (orange line) plummeted from ~23% to ~10%. The two metrics are moving in opposite directions, which is a classic sign of low-quality traffic scaling.

### Revenue Composition by Channel

![Stacked Revenue](chart6_channel_stacked.png)

The stacked area chart shows that despite Channel 2's massive session growth, its revenue contribution (coral band) has remained relatively thin. Channel 1 (teal) continues to generate the majority of revenue, but its share has been shrinking as budget shifted to Channel 2.

### Full Channel Breakdown

| Metric | Channel 1 | Channel 2 | Channel 3 |
|---|---|---|---|
| **Session Share** | 57.8% | 25.0% | 17.2% |
| **Revenue Share** | 67.4% | 15.3% | 17.3% |
| **Spend Share** | 78.0% | 20.6% | 1.4% |
| **Submission Rate** | 28.3% | 17.7% | 37.3% |
| **ROAS** | 1.61 | 1.38 | 23.05 |
| **Profit Margin** | 38.0% | 27.7% | 95.7% |

### H2 YoY Channel Comparison

| Metric | Ch1 H2'24 → H2'25 | Ch2 H2'24 → H2'25 | Ch3 H2'24 → H2'25 |
|---|---|---|---|
| **Sessions** | 653K → 494K (-24.3%) | 166K → 378K (**+127.8%**) | 166K → 205K (+23.5%) |
| **Sub Rate** | 28.7% → 28.0% | 21.0% → **14.2%** | 39.7% → 34.5% |
| **Revenue** | £1.78M → £1.30M (-26.8%) | £300K → £374K (+24.6%) | £413K → £402K (-2.8%) |
| **Spend** | £1.09M → £821K (-24.5%) | £199K → £293K (**+47.0%**) | £23K → £14K (-39.1%) |
| **ROAS** | 1.64 → 1.59 | 1.50 → **1.28** | 17.6 → 28.1 |
| **Profit** | £696K → £484K (-30.5%) | £100K → £81K (**-19.8%**) | £390K → £387K (-0.7%) |

### Why Channel 2 Is the Primary Concern

**1. It has scaled aggressively with deteriorating unit economics.** Sessions grew +127.8% but submission rate collapsed from 21.0% to 14.2%. For every 7 visitors Bark acquires through Channel 2, only 1 submits a project — compared to ~1-in-3 for Channel 3 and ~1-in-3.5 for Channel 1.

**2. Spend grew far faster than revenue.** Marketing spend +47.0% vs revenue +24.6%. ROAS of 1.28 is approaching breakeven.

**3. Profit declined despite massive volume growth.** Channel 2 profit fell -19.8% (£100K → £81K) despite more than doubling sessions. Incremental traffic is net-negative on a per-session basis.

**4. Channel 2 is the root cause of the UK Q1 pass rate collapse.** Channel 2's Q1 pass rate fell from 45.7% to 30.3%. Given that Channel 2 now represents ~35% of total sessions (up from ~17%), its poor conversion is mechanically diluting the blended UK submission rate by 4–5pp.

**5. Revenue per paid response is also declining.** Channel 2's RPR fell from £14.04 to £13.21 (-5.9%), the only channel to see a decline — suggesting the leads are not just low-converting but also lower-value.

### Recommendation

Cap or reduce Channel 2 spend and reallocate budget back to Channel 1. In parallel, conduct a granular analysis of Channel 2 sub-sources — some segments may be performing well while others (e.g., display or broad-match campaigns) drag down the average. Additionally, investing in Channel 3 growth (SEO/content) would improve blended margins even if payback is longer-term.

---

## Part 3: Category Deep-Dive (US Market)

### Part 3a: Category Requiring Most Attention — Web Design

![US Category Waterfall](chart7_us_waterfall.png)

Web Design experienced the largest absolute revenue decline of any US category, losing **£605,893** in H2 revenue YoY — accounting for **34.7% of the total US revenue decline** of £1.75M. Personal Trainers was the second largest decliner at -£383K. Only Motivational Speaking grew.

### Web Design vs Motivational Speaking — Trend Contrast

![Category Contrast](chart8_us_category_contrast.png)

These side-by-side panels highlight the divergence. Web Design (left, coral) shows revenue declining alongside collapsing revenue per project (dashed line fell from ~£57 to ~£36). Motivational Speaking (right, teal) shows the opposite: revenue and rev/project both climbed steadily.

### Web Design Deep-Dive

| Metric | H2 2024 | H2 2025 | Δ | YoY % |
|---|---|---|---|---|
| PPR Revenue | £1,245,188 | £639,295 | -£605,893 | **-48.7%** |
| Sessions | 148,506 | 99,176 | -49,330 | -33.2% |
| Submissions | 24,224 | 14,916 | -9,308 | -38.4% |
| Rev per Project | ~£55 | ~£47 | -£8 | -14.5% |
| Response Rate | ~95% | ~85% | -10pp | — |
| Profit | £399,614 | £322,279 | -£77,335 | -19.4% |

**Volume collapse across all channels.** Channel 1 revenue halved (£922K → £451K), Channel 2 fell from £238K to £152K, and Channel 3 from £85K to £36K. This is not a channel-specific issue — it is a structural demand decline.

**Seller disengagement is accelerating.** Revenue per released project fell from ~£57 (Jul 2024) to ~£36 (Dec 2025). Response rate also dropped from ~95%+ to ~78% by Dec 2025. Professionals are pulling back from this category — likely because web design has become increasingly commoditised through AI tools and no-code platforms.

**Profit held up better (-19.4%) than revenue (-48.7%)** because marketing spend was cut sharply (£846K → £317K), making the category more profitable per pound spent even as volume shrank.

### Impact on the Total US Portfolio

The US market overall declined -31.0% in H2 revenue (£5.15M → £3.55M). Web Design and Personal Trainers together account for **56.6%** of total US revenue loss. At the industry level, Marketing & Technology (-48.7%), Legal & Business (-57.5%), and Health & Wellbeing (-54.1%) are the hardest-hit verticals.

### Part 3b: Category That Has Grown — Motivational Speaking

Motivational Speaking is the only US category that grew, and it grew substantially: **revenue more than doubled** from £136K to £289K (+113.1%), and profit surged from £40K to £165K (+314.9%).

| Metric | H2 2024 | H2 2025 | Δ | YoY % |
|---|---|---|---|---|
| PPR Revenue | £135,715 | £289,224 | +£153,509 | **+113.1%** |
| Submissions | 4,778 | 6,148 | +1,370 | +28.7% |
| Paid Responses | 5,316 | 10,055 | +4,739 | **+89.1%** |
| Rev per Project | £30.15 | £55.08 | +£24.93 | **+82.7%** |
| Response Rate | ~68% | ~83% | +15pp | — |
| Profit | £39,701 | £164,728 | +£125,027 | **+314.9%** |

### What Drove This Growth

**The main driver is dramatically improved monetisation, not just volume growth.** Revenue per released project nearly doubled (£30 → £55), meaning each project generated far more paid professional responses. Paid responses grew +89.1% while project volume grew only +16.7%.

**The response rate increased from ~68% to ~83%.** More released projects received at least one professional response — a signal of stronger supply-side engagement. More professionals are finding value in this category and choosing to pay to respond.

**Spend grew modestly relative to revenue.** Marketing spend increased from £96K to £125K (+30.2%), but revenue grew 113%. ROAS improved substantially, suggesting a virtuous cycle: better lead quality → more professional responses → higher revenue per project.

**Channel 1 drove the majority of the growth.** Channel 1 revenue went from £103K to £211K (+104%), with paid responses jumping from 4,050 to 7,308. Channel 2 also grew strongly (£28K → £70K).

The growth likely reflects a structural demand tailwind — corporate events, team-building, and the growing speaking/coaching economy — combined with Bark successfully building a professional supply base willing to pay premium credit rates for high-value leads.

---

## Summary of Key Findings

| # | Finding | Impact | Priority |
|---|---|---|---|
| 1 | UK submission rate collapsing (29.3% → 24.4%) driven by Q1 pass rate drop of -11.2pp | Revenue -16.7%, Profit -19.8% in H2 | **Critical** |
| 2 | Channel 2 scaling with deteriorating unit economics (ROAS 1.28, sub rate 14.2%) | Diluting blended performance, net-negative marginal ROI | **Critical** |
| 3 | US Web Design in structural decline (-48.7% rev, seller disengagement) | 35% of total US revenue loss | **High** |
| 4 | US Personal Trainers collapsing (-54.1% revenue, RPP halved) | Second-largest driver of US decline | **High** |
| 5 | Motivational Speaking thriving on monetisation improvement (+113% revenue) | Playbook for category health: supply engagement → RPP growth | **Opportunity** |
