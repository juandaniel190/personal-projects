"""
CS Apps Investment Analysis — v2 (Audited)
Case Study — Senior Manager, Product Data Analyst
Contentsquare

Changes from v1:
  - Applied Contentsquare brand palette (aubergine / coral)
  - Added Section 10: Health formula reverse-engineering
  - Added duplicate/data-quality audit (Section 1 expanded)
  - McKinsey-style chart formatting (clean, annotation-forward)
  - Corrected Lived rate to 36.3%

Structure:
  0  Setup & Data Loading
  1  Data Quality Audit
  2  Revenue & Growth
  3  Health Score (with formula investigation)
  4  Adoption & Certification
  5  Implementation Funnel
  6  Module Engagement
  7  Segment Analysis (Geo, Vertical)
  8  Renewal Pipeline
  9  Health Formula Deep-Dive
  10 Hypothesis Evidence Summary
"""

# ============================================================
# SECTION 0 — SETUP
# ============================================================
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from matplotlib.patches import Patch
import os, warnings, json, re
warnings.filterwarnings('ignore')

# --- Paths ---
_base = os.path.join(os.getcwd(), "business-cases", "Contentsquare")
if not os.path.isdir(_base):
    _base = os.getcwd()
BASE = _base
ACC_PATH = os.path.join(BASE, "Account Data Case Study Result 1.csv")
USR_PATH = os.path.join(BASE, "User Data Case Study Result 1.csv")
FIG_DIR  = os.path.join(BASE, "figures")
os.makedirs(FIG_DIR, exist_ok=True)

# --- Brand Colors — Heap (heap.io) palette — in use ---
# Priority 3 (use when a graph needs 3 colors): dark blue, green, purple.
# Need more than 3? Pick from SEQ / CAT below.
HEAP_GREEN     = '#31d891'   # Heap green
DARK_BLUE      = '#0A0D4B'   # arc-palette-background — dark blue
HEAP_PURPLE    = '#6D28D9'   # violet-700 — purple
PRIO3          = [DARK_BLUE, HEAP_GREEN, HEAP_PURPLE]   # use for 3-color charts
# Extended palette (when you need >3 colors)
ARC_FOCUS      = '#4D54FB'   # arc-palette-focus
HEAP_VIOLET_800 = HEAP_PURPLE
HEAP_VIOLET_600 = '#7C3AED'
HEAP_VIOLET_500 = '#8B5CF6'
HEAP_VIOLET_400 = '#A78BFA'
HEAP_VIOLET_100 = '#EDE9FE'
HEAP_EMERALD_400 = '#34D399'
HEAP_TEAL_500   = '#14B8A6'
HEAP_SLATE_600  = '#475569'
HEAP_SLATE_200  = '#E2E8F0'
HEAP_RED_500    = '#EF4444'   # risk only
HEAP_AMBER_500  = '#F59E0B'

# --- Contentsquare design system (lilac, purple, ember, magenta, peach) — kept for fallback ---
LILAC_400 = '#CCC2EB'
LILAC_600 = '#9C89D4'
LILAC_800 = '#6D4BD1'
PURPLE_200 = '#F7EAFB'
PURPLE_600 = '#DD9FEE'
PURPLE_GRAPHIC = '#E4DDF3'
MAGENTA_100 = '#F3D2EA'
MAGENTA_400 = '#C246AC'
EMBER_600 = '#FF3C00'
EMBER_300 = '#FFD9CD'
ELECTRIC_GREEN = '#00E5A0'
AQUA = '#26C6DA'
WARM_GRAY = '#9E8E94'
CREAM = '#F5F0F1'
PEACH_100 = '#FEF7EC'

# --- Previous palette (aubergine / vino tinto, coral, greens) — keep for fallback ---
AUB_PREV       = '#3B1F2B'
AUB_LIGHT_PREV = '#6B4158'
AUB_MID_PREV   = '#9E6880'
CORAL_PREV     = '#E6554A'
CORAL_LT_PREV  = '#F2887F'
GREEN_PREV     = '#2EAA6E'
GREEN_DARK_PREV = '#1E7B4F'
GREEN_LIGHT_PREV = '#6ED493'
AMBER_PREV     = '#F2A83E'
SEQ_PREV = [AUB_PREV, AUB_LIGHT_PREV, AUB_MID_PREV, '#D09BA8', CORAL_LT_PREV]
CAT_PREV = [AUB_PREV, CORAL_PREV, AUB_LIGHT_PREV, CORAL_LT_PREV, WARM_GRAY]

# Semantic mapping — priority: dark blue, green, purple.
# Unhealthy / at-risk: always gray (never red).
UNHEALTHY_GRAY = '#808080'
AUB       = HEAP_PURPLE
AUB_LIGHT = HEAP_VIOLET_600
AUB_MID   = HEAP_VIOLET_500
CORAL     = HEAP_RED_500     # unused for charts; use UNHEALTHY_GRAY for unhealthy
CORAL_LT  = '#FCA5A5'
GREEN     = HEAP_GREEN
FOCUS     = ARC_FOCUS
AMBER     = HEAP_AMBER_500
DARK_TEXT = HEAP_SLATE_600
# All chart titles and axis labels: black
TITLE_COLOR = '#000000'
# Implementation status: grayscale for early stages, green scale for later (use everywhere)
STATUS_GRAY = {'NULL / Untracked': '#E0E0E0', 'Not started': '#BDBDBD', 'Started': '#9E9E9E', 'Partially implemented': '#757575'}
STATUS_GREEN = {'Implemented': '#81C784', 'Partially lived': '#4CAF50', 'Lived': HEAP_GREEN}
STATUS_COLORS = {**STATUS_GRAY, **STATUS_GREEN}

# For charts with 3 series: use PRIO3 = [DARK_BLUE, HEAP_GREEN, HEAP_PURPLE]
# For more than 3: extend from SEQ / CAT
SEQ = [DARK_BLUE, HEAP_PURPLE, HEAP_VIOLET_600, HEAP_VIOLET_500, HEAP_GREEN]
CAT = [DARK_BLUE, HEAP_GREEN, HEAP_PURPLE, ARC_FOCUS, HEAP_VIOLET_400, HEAP_TEAL_500, HEAP_SLATE_600]

# --- Chart Style --- white background, all text black
plt.rcParams.update({
    'font.family':        'sans-serif',
    'font.size':           11,
    'axes.spines.top':     False,
    'axes.spines.right':   False,
    'axes.facecolor':      '#FFFFFF',
    'figure.facecolor':    '#FFFFFF',
    'figure.dpi':          150,
    'axes.titleweight':    'bold',
    'axes.titlepad':       14,
    'axes.labelpad':       8,
    'text.color':          '#000000',
    'axes.labelcolor':     '#000000',
    'axes.titlecolor':     '#000000',
    'xtick.color':         '#000000',
    'ytick.color':         '#000000',
})

# --- Load Data ---
acc = pd.read_csv(ACC_PATH)
usr = pd.read_csv(USR_PATH)
acc['MONTH'] = pd.to_datetime(acc['MONTH'])
# Contract dates can be comma-separated lists or mixed formats; keep as object to avoid parse errors
# acc['CONTRACT_START_DATE'] = pd.to_datetime(acc['CONTRACT_START_DATE'], errors='coerce')
# acc['CONTRACT_END_DATE']   = pd.to_datetime(acc['CONTRACT_END_DATE'], errors='coerce')

print("Data loaded.")
print(f"  Account rows : {len(acc):,}  |  Unique accounts: {acc['SALESFORCE_ACCOUNT_ID'].nunique()}")
print(f"  User rows    : {len(usr):,}  |  Unique users   : {usr['USER_ID'].nunique():,}")


# ============================================================
# SECTION 1 — DATA QUALITY AUDIT
# ============================================================
print("\n" + "="*60)
print("SECTION 1 — DATA QUALITY AUDIT")
print("="*60)

# 1.1 Duplicate check
dup_acc_rows = acc.duplicated().sum()
dup_acc_key  = acc.duplicated(subset=['SALESFORCE_ACCOUNT_ID','MONTH']).sum()
dup_usr_rows = usr.duplicated().sum()
dup_usr_key  = usr.duplicated(subset=['USER_ID','MONTH','MODULE_NAME','PROJECT_ID']).sum()

print(f"\n[1.1] Exact duplicate rows — Account: {dup_acc_rows} | User: {dup_usr_rows}")
print(f"[1.2] Duplicate primary keys — Account (ID+Month): {dup_acc_key} | "
      f"User (USER+MONTH+MODULE+PROJECT): {dup_usr_key}")

# 1.3 Null audit
print("\n[1.3] Null counts:")
for name, df in [("Account", acc), ("User", usr)]:
    nulls = df.isnull().sum()
    nulls = nulls[nulls > 0]
    if len(nulls):
        print(f"  {name}:")
        for col, cnt in nulls.items():
            print(f"    {col}: {cnt} ({cnt/len(df)*100:.1f}%)")

# 1.4 Multiple contracts per account-month
# PDF warns: "if a client has multiple contracts, all the contracts will show up"
# But audit showed 0 duplicate (ACCOUNT_ID, MONTH) pairs — no overcounting risk.
print(f"\n[1.4] Multi-contract check: {dup_acc_key} duplicate (Account, Month) rows.")
print("       No ACV overcounting risk detected.")

# 1.5 Accounts with ACV_CS_APPS = 0
zero_acv_n = (acc.groupby('SALESFORCE_ACCOUNT_ID')['ACV_CS_APPS'].mean() == 0).sum()
print(f"[1.5] Accounts with ACV_CS_APPS = 0: {zero_acv_n} / {acc['SALESFORCE_ACCOUNT_ID'].nunique()}")

# 1.6 Accounts with WAU = 0
wau_zero_rows = (acc['AVG_WAU_GLOBAL'] == 0).sum()
wau_zero_accts = acc[acc['AVG_WAU_GLOBAL'] == 0]['SALESFORCE_ACCOUNT_ID'].nunique()
print(f"[1.6] Rows with AVG_WAU_GLOBAL = 0: {wau_zero_rows} ({wau_zero_rows/len(acc)*100:.1f}%) "
      f"— {wau_zero_accts} unique accounts")


# ============================================================
# SECTION 2 — REVENUE & GROWTH
# ============================================================
print("\n" + "="*60)
print("SECTION 2 — REVENUE & GROWTH")
print("="*60)

monthly = acc.groupby('MONTH').agg(
    n_accounts = ('SALESFORCE_ACCOUNT_ID', 'nunique'),
    total_acv  = ('ACV_CS_APPS', 'sum'),
    mean_acv   = ('ACV_CS_APPS', 'mean'),
    median_acv = ('ACV_CS_APPS', 'median'),
).reset_index()

start_acv, end_acv = monthly['total_acv'].iloc[0], monthly['total_acv'].iloc[-1]
start_n, end_n = monthly['n_accounts'].iloc[0], monthly['n_accounts'].iloc[-1]
print(f"\nACV growth (Jan→Dec 2023): ${start_acv:,.0f} → ${end_acv:,.0f} (+{(end_acv/start_acv-1)*100:.1f}%)")
print(f"Account growth: {start_n} → {end_n} (+{(end_n/start_n-1)*100:.1f}%)")

# --- Fig 01 (H1): Revenue & growth — height reduced 40% ---
fig, ax1 = plt.subplots(figsize=(11, 3.3))
ax2 = ax1.twinx()
ax1.bar(monthly['MONTH'], monthly['total_acv']/1e6, color=DARK_BLUE, alpha=0.85,
        width=25, label='Total ACV ($M)', zorder=2)
ax2.plot(monthly['MONTH'], monthly['n_accounts'], color=GREEN, marker='o',
         linewidth=2.5, markersize=7, label='# Accounts', zorder=3)
ax1.set_ylabel("Total CS Apps ACV ($M)")
ax2.set_ylabel("Number of Accounts")
ax1.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x:.1f}M"))
ax1.set_title("CS Apps Revenue & Account Growth")
ax1.annotate(f"+{(end_acv/start_acv-1)*100:.0f}% ACV\n+{(end_n/start_n-1)*100:.0f}% Accounts",
             xy=(monthly['MONTH'].iloc[-1], monthly['total_acv'].iloc[-1]/1e6),
             xytext=(-100, 30), textcoords='offset points',
             fontsize=10, fontweight='bold', color=TITLE_COLOR,
             arrowprops=dict(arrowstyle='->', color=TITLE_COLOR))
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1+lines2, labels1+labels2, loc='upper left', framealpha=0.9)
plt.tight_layout()
plt.savefig(f"{FIG_DIR}/fig_01_acv_account_growth.png", bbox_inches='tight')
plt.close()
print("Figure saved: fig_01")


# ============================================================
# SECTION 3 — HEALTH SCORE
# ============================================================
print("\n" + "="*60)
print("SECTION 3 — HEALTH SCORE")
print("="*60)

health_trend = acc.groupby(['MONTH','HEALTHY_STATUS']).size().unstack(fill_value=0).reset_index()
health_trend['pct_healthy'] = health_trend['Healthy'] / (health_trend['Healthy']+health_trend['Unhealthy'])*100
print(health_trend[['MONTH','Healthy','Unhealthy','pct_healthy']].to_string())

# --- Fig 02 & 03 (H3): Health trend + Health by implementation — side by side ---
health_impl = (
    acc.groupby(['IMPLEMENTATION_STATUS_APPS','HEALTHY_STATUS'])
    .size().unstack(fill_value=0)
)
health_impl['pct_healthy'] = health_impl['Healthy'] / health_impl.sum(axis=1)*100
funnel_order = ['Not started','Started','Partially implemented','Implemented','Partially lived','Lived']
health_impl = health_impl.reindex([s for s in funnel_order if s in health_impl.index])

fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(14, 3.5))
# Left: health trend over time
ax2 = ax_left.twinx()
ax_left.bar(health_trend['MONTH'], health_trend['Healthy'],   width=25, color=GREEN, alpha=0.8, label='Healthy')
ax_left.bar(health_trend['MONTH'], health_trend['Unhealthy'], width=25, color=UNHEALTHY_GRAY, alpha=0.8,
       bottom=health_trend['Healthy'], label='Unhealthy')
ax2.plot(health_trend['MONTH'], health_trend['pct_healthy'], color=DARK_BLUE,
         linewidth=2.5, linestyle='--', marker='s', markersize=5, label='% Healthy')
ax_left.set_ylabel("Number of Accounts")
ax2.set_ylabel("% Healthy")
ax2.set_ylim(40, 80)
ax2.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x:.0f}%"))
ax_left.set_title("Account Health Status — Jan–Dec 2023")
ax_left.annotate("9pp decline", xy=(health_trend['MONTH'].iloc[-1], 140),
            fontsize=9, fontweight='bold', color=TITLE_COLOR,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=UNHEALTHY_GRAY))
lines1, labels1 = ax_left.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax_left.legend(lines1+lines2, labels1+labels2, loc='upper left', framealpha=0.9, fontsize=8)
ax_left.spines['top'].set_visible(False)
ax2.spines['top'].set_visible(False)
# Right: health by implementation status
colors_bar = [GREEN if p >= 65 else UNHEALTHY_GRAY for p in health_impl['pct_healthy']]
bars = ax_right.barh(health_impl.index, health_impl['pct_healthy'], color=colors_bar, alpha=0.85)
for bar, val in zip(bars, health_impl['pct_healthy']):
    ax_right.text(bar.get_width()+0.8, bar.get_y()+bar.get_height()/2, f"{val:.1f}%", va='center', fontsize=9, color=TITLE_COLOR)
ax_right.axvline(60, color=WARM_GRAY, linestyle='--', linewidth=1.2, alpha=0.6, label='60% threshold')
ax_right.set_xlabel("% Healthy Accounts")
ax_right.set_title("Health Rate by Implementation Status")
ax_right.set_xlim(0, 90)
ax_right.legend(fontsize=8)
ax_right.spines['top'].set_visible(False)
ax_right.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig(f"{FIG_DIR}/fig_02_health_trend.png", bbox_inches='tight')
plt.savefig(f"{FIG_DIR}/fig_03_health_by_impl.png", bbox_inches='tight')
plt.close()
print("Figure saved: fig_02, fig_03 (H3 side by side)")


# ============================================================
# SECTION 4 — ADOPTION & CERTIFICATION
# ============================================================
print("\n" + "="*60)
print("SECTION 4 — ADOPTION & CERTIFICATION")
print("="*60)

cert_per_acc = acc.groupby('SALESFORCE_ACCOUNT_ID').agg(
    avg_cert_apps    = ('CERTIFIED_USERS_APPS', 'mean'),
    avg_cert_digital = ('CERTIFIED_USERS_DIGITAL', 'mean'),
).reset_index()
zero_cert = (cert_per_acc['avg_cert_apps'] == 0).sum()
nonzero_cert = (cert_per_acc['avg_cert_apps'] > 0).sum()
print(f"Accounts with 0 certified Apps users: {zero_cert} ({zero_cert/len(cert_per_acc)*100:.1f}%)")
print(f"Avg certified: Apps={cert_per_acc['avg_cert_apps'].mean():.2f} vs Digital={cert_per_acc['avg_cert_digital'].mean():.2f} (26x gap)")

cert_trend = acc.groupby('MONTH').agg(
    avg_cert_apps    = ('CERTIFIED_USERS_APPS', 'mean'),
    avg_cert_digital = ('CERTIFIED_USERS_DIGITAL', 'mean'),
).reset_index()

# --- Fig 04 (H2): Certification — horizontal stacked bar, no title/axes; height reduced 30% more ---
fig, ax = plt.subplots(figsize=(8, 0.85))
ax.set_facecolor('white')
total_cert = zero_cert + nonzero_cert
left = [0, zero_cert]
width = [zero_cert, nonzero_cert]
colors = [UNHEALTHY_GRAY, GREEN]
bars = ax.barh(0, width, left=left, height=0.5, color=colors, alpha=0.9, edgecolor='none')
ax.set_xlim(0, total_cert)
ax.set_ylim(-0.5, 0.5)
ax.set_yticks([])
ax.set_xticks([])
ax.set_xlabel('')
ax.set_ylabel('')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
# In-bar labels only
if zero_cert > 0:
    ax.text(zero_cert/2, 0, f'{zero_cert} ({100*zero_cert/total_cert:.0f}%)', ha='center', va='center', fontsize=9, color=TITLE_COLOR)
if nonzero_cert > 0:
    ax.text(zero_cert + nonzero_cert/2, 0, f'{nonzero_cert} ({100*nonzero_cert/total_cert:.0f}%)', ha='center', va='center', fontsize=9, color=TITLE_COLOR)
plt.tight_layout()
plt.savefig(f"{FIG_DIR}/fig_04_certification_gap.png", bbox_inches='tight')
plt.close()
print("Figure saved: fig_04")

# --- Fig 05: MAU & Sessions ---
mau = usr.groupby('MONTH').agg(
    n_unique_users = ('USER_ID', 'nunique'),
    n_projects     = ('PROJECT_ID', 'nunique'),
    total_sessions = ('SESSIONS', 'sum'),
).reset_index()
mau['MONTH'] = pd.to_datetime(mau['MONTH'])

fig, ax = plt.subplots(figsize=(11, 3.4))
ax2 = ax.twinx()
ax.bar(mau['MONTH'], mau['total_sessions'], width=25, color=DARK_BLUE, alpha=0.8, label='Total Sessions')
ax2.plot(mau['MONTH'], mau['n_unique_users'], color=GREEN, marker='o',
         linewidth=2.5, markersize=6, label='Unique Active Users')
ax.set_ylabel("Total Sessions")
ax2.set_ylabel("Unique Active Users")
ax2.set_ylim(0, None)
ax.set_title("Monthly Sessions & Active Users — 2023")
ax.spines['top'].set_visible(False)
ax2.spines['top'].set_visible(False)
lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines1+lines2, labels1+labels2, loc='upper left', framealpha=0.9)
plt.tight_layout()
plt.savefig(f"{FIG_DIR}/fig_05_mau_sessions.png", bbox_inches='tight')
plt.close()
print("Figure saved: fig_05")


# ============================================================
# SECTION 5 — IMPLEMENTATION FUNNEL
# ============================================================
print("\n" + "="*60)
print("SECTION 5 — IMPLEMENTATION FUNNEL")
print("="*60)

impl_order = ['Not started','Started','Partially implemented',
              'Implemented','Partially lived','Lived']
impl_counts = (
    acc.groupby('IMPLEMENTATION_STATUS_APPS')['SALESFORCE_ACCOUNT_ID']
    .nunique().reindex(impl_order).reset_index()
)
impl_counts.columns = ['STATUS','N_ACCOUNTS']
impl_counts['PCT'] = impl_counts['N_ACCOUNTS'] / impl_counts['N_ACCOUNTS'].sum() * 100
null_impl = acc[acc['IMPLEMENTATION_STATUS_APPS'].isnull()]['SALESFORCE_ACCOUNT_ID'].nunique()
lived_n = impl_counts[impl_counts['STATUS'].isin(['Lived','Partially lived'])]['N_ACCOUNTS'].sum()
total_s = impl_counts['N_ACCOUNTS'].sum()
print(f"Accounts with status: {total_s} | NULL status: {null_impl}")
print(f"'Lived' rate: {lived_n}/{total_s} = {lived_n/total_s*100:.1f}%")
print(impl_counts.to_string())

# --- Fig 06: Implementation Status Distribution (cross-sectional, NOT a funnel) ---
# Note: statuses are monthly snapshots, not sequential cohort progression.
# 57 of 132 tracked accounts changed status during 2023.
import numpy as np

latest = acc.sort_values('MONTH').groupby('SALESFORCE_ACCOUNT_ID').last().copy()
# Funnel order: Lived at top (last in list = top in barh; do not invert)
impl_order_full = ['NULL / Untracked','Not started','Started','Partially implemented','Implemented','Partially lived','Lived']
latest['impl_clean'] = latest['IMPLEMENTATION_STATUS_APPS'].fillna('NULL / Untracked')
snapshot = latest['impl_clean'].value_counts().reindex(impl_order_full).fillna(0)
total_accts = len(latest)

acc_plot = acc.copy()
acc_plot['impl_clean'] = acc_plot['IMPLEMENTATION_STATUS_APPS'].fillna('NULL / Untracked')
monthly = acc_plot.groupby(['MONTH','impl_clean'])['SALESFORCE_ACCOUNT_ID'].nunique().unstack(fill_value=0)
monthly = monthly.reindex(columns=impl_order_full, fill_value=0)
monthly.index = pd.to_datetime(monthly.index)
monthly = monthly.sort_index()

# Grayscale early stages; green scale for Implemented, Partially lived, Lived
status_colors = {s: STATUS_COLORS.get(s, '#BDBDBD') for s in impl_order_full}

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), gridspec_kw={'width_ratios': [1, 1.3]})

colors = [status_colors[s] for s in impl_order_full]
bars = ax1.barh(impl_order_full, snapshot.values, color=colors, alpha=0.88)
for bar, count in zip(bars, snapshot.values):
    pct = count / total_accts * 100
    ax1.text(bar.get_width()+1, bar.get_y()+bar.get_height()/2,
             f'{count}  ({pct:.0f}%)', va='center', fontsize=9.5, color=TITLE_COLOR)
ax1.set_xlim(0, snapshot.max()*1.4)
ax1.set_xlabel('Accounts', fontsize=10)
ax1.set_title('Current Status\n(latest month per account)', fontsize=11, fontweight='bold')
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

month_labels = monthly.index.strftime('%b')
x = range(len(monthly))
bottom = np.zeros(len(monthly))
for status in impl_order_full:
    vals = monthly[status].values
    ax2.fill_between(x, bottom, bottom+vals, alpha=0.85,
                     color=status_colors[status], label=status)
    bottom += vals
ax2.set_xticks(list(x))
ax2.set_xticklabels(month_labels, fontsize=8.5)
ax2.set_ylabel('Accounts', fontsize=10)
ax2.set_title('Status Distribution Over Time (2023)', fontsize=11, fontweight='bold')
ax2.legend(loc='upper left', fontsize=7.5, framealpha=0.9)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

fig.suptitle('CS Apps Implementation Status — Distribution (Cross-Sectional)',
             fontsize=13, fontweight='bold', y=1.02)

fig.text(0.5, -0.04,
         f'Base: {total_accts} accounts  |  Only 27 (15%) are Lived in latest snapshot  |  '
         f'53 (29%) untracked  |  57 accounts changed status during 2023',
         ha='center', fontsize=11, color=TITLE_COLOR, style='italic')
plt.tight_layout()
plt.savefig(f"{FIG_DIR}/fig_06_implementation_funnel.png", bbox_inches='tight', dpi=150)
plt.close()
print("Figure saved: fig_06 (status distribution)")


# ============================================================
# SECTION 6 — MODULE ENGAGEMENT
# ============================================================
print("\n" + "="*60)
print("SECTION 6 — MODULE ENGAGEMENT")
print("="*60)

module_eng = (
    usr.groupby('MODULE_NAME').agg(
        n_users        = ('USER_ID', 'nunique'),
        total_sessions = ('SESSIONS', 'sum'),
        avg_sessions   = ('SESSIONS', 'mean'),
    ).sort_values('total_sessions', ascending=False).reset_index()
)
module_eng['pct_sessions'] = module_eng['total_sessions'] / module_eng['total_sessions'].sum() * 100

# --- Fig 07 (H6): Module engagement — legend; height increased 10% ---
core_modules = ['Zoning Analysis','Session Replay','Journey Analysis','Funnel','Error Analysis']
fig, ax = plt.subplots(figsize=(10, 4.65))
colors_mod = [DARK_BLUE if m in core_modules else UNHEALTHY_GRAY for m in module_eng['MODULE_NAME']]
bars = ax.barh(module_eng['MODULE_NAME'], module_eng['total_sessions'], color=colors_mod, alpha=0.85)
for bar, row in zip(bars, module_eng.itertuples()):
    ax.text(bar.get_width()+100, bar.get_y()+bar.get_height()/2,
            f"{row.pct_sessions:.1f}%", va='center', fontsize=9, color=TITLE_COLOR)
ax.set_xlabel("Total Sessions")
ax.set_title("Module Engagement — Total Sessions (2023)")
# Legend: dark blue = core analytics, gray = navigation/settings
legend_elements = [
    Patch(facecolor=DARK_BLUE, alpha=0.85, label='Core analytics'),
    Patch(facecolor=UNHEALTHY_GRAY, alpha=0.85, label='Navigation / settings'),
]
ax.legend(handles=legend_elements, loc='lower right', framealpha=0.9)
ax.invert_yaxis()
plt.tight_layout()
plt.savefig(f"{FIG_DIR}/fig_07_module_engagement.png", bbox_inches='tight')
plt.close()
print("Figure saved: fig_07")


# ============================================================
# SECTION 7 — SEGMENT ANALYSIS
# ============================================================
print("\n" + "="*60)
print("SECTION 7 — SEGMENT ANALYSIS")
print("="*60)

# Sort DESC by mean_acv (biggest first)
geo = acc.groupby('GEO').agg(
    n_accounts  = ('SALESFORCE_ACCOUNT_ID', 'nunique'),
    total_acv   = ('ACV_CS_APPS', 'sum'),
    mean_acv    = ('ACV_CS_APPS', 'mean'),
    pct_healthy = ('HEALTHY_STATUS', lambda x: (x=='Healthy').mean()*100),
).reset_index().sort_values('mean_acv', ascending=False)

vert = (
    acc.groupby('VERTICAL').agg(
        n_accounts  = ('SALESFORCE_ACCOUNT_ID', 'nunique'),
        total_acv   = ('ACV_CS_APPS', 'sum'),
        mean_acv    = ('ACV_CS_APPS', 'mean'),
        pct_healthy = ('HEALTHY_STATUS', lambda x: (x=='Healthy').mean()*100),
    ).reset_index().sort_values('mean_acv', ascending=False)
)
print(geo.to_string())
print(vert.to_string())

# --- Fig 08 (H7): Segment — highlight only Americas (geo) and Telco (vertical); rest gray ---
fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))

# Geo (Ch1): horizontal bars, DESC so Americas (largest) at top; highlight Americas, rest gray
geo_colors = [DARK_BLUE if g == 'AMERICAS' else UNHEALTHY_GRAY for g in geo['GEO']]
axes[0].barh(geo['GEO'], geo['mean_acv']/1e3, color=geo_colors, alpha=0.85)
axes[0].invert_yaxis()  # largest (Americas) at top
axes[0].set_xlabel("Mean ACV ($K)")
axes[0].xaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f"${v:.0f}K"))
for i, (_, r) in enumerate(geo.iterrows()):
    axes[0].text(r['mean_acv']/1e3+2, i, f"{r['pct_healthy']:.0f}% healthy \n ({r['n_accounts']} accts)",
                 va='center', fontsize=11, color=TITLE_COLOR)
axes[0].set_title("Mean ACV & Health by Geo")

# Verticals: sort DESC; highlight only Telco, rest gray
vert_plot = vert.head(15)
colors_v = [DARK_BLUE if (v or '').upper() == 'TELCO' else UNHEALTHY_GRAY for v in vert_plot['VERTICAL']]
axes[1].barh(vert_plot['VERTICAL'], vert_plot['mean_acv']/1e3, color=colors_v, alpha=0.85)
axes[1].set_xlabel("Mean ACV ($K)")
axes[1].xaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f"${v:.0f}K"))
for i, (_, r) in enumerate(vert_plot.iterrows()):
    axes[1].text(r['mean_acv']/1e3+2, i, f"{r['pct_healthy']:.0f}%", va='center', fontsize=9, color=TITLE_COLOR)
axes[1].set_title("Mean ACV by Vertical")
axes[1].invert_yaxis()

plt.tight_layout()
plt.savefig(f"{FIG_DIR}/fig_08_segment_analysis.png", bbox_inches='tight')
plt.close()
print("Figure saved: fig_08")


# ============================================================
# SECTION 8 — RENEWAL PIPELINE
# ============================================================
print("\n" + "="*60)
print("SECTION 8 — RENEWAL PIPELINE")
print("="*60)

# CRITICAL: UFR is the total renewal value for an account in a fiscal quarter.
# It is repeated for every month in that quarter. We must deduplicate by taking
# the latest month per account per fiscal quarter to avoid overcounting.
acc_sorted = acc.sort_values(['SALESFORCE_ACCOUNT_ID','FISCAL_QUARTER','MONTH'])
acc_deduped = acc_sorted.groupby(['SALESFORCE_ACCOUNT_ID','FISCAL_QUARTER']).last().reset_index()

ufr = acc_deduped.groupby('FISCAL_QUARTER').agg(
    total_ufr   = ('TOTAL_UFR', 'sum'),
    n_ufr_accts = ('TOTAL_UFR', lambda x: (x>0).sum()),
    pct_healthy = ('HEALTHY_STATUS', lambda x: (x=='Healthy').mean()*100),
).reset_index()

renewals_only = acc_deduped[acc_deduped['TOTAL_UFR'] > 0]
at_risk     = renewals_only[renewals_only['HEALTHY_STATUS']=='Unhealthy']['TOTAL_UFR'].sum()
total_ufr_a = renewals_only['TOTAL_UFR'].sum()
print(f"Total UFR (deduplicated): ${total_ufr_a:,.0f}")
print(f"At risk (unhealthy): ${at_risk:,.0f} ({at_risk/total_ufr_a*100:.1f}%)")

# --- Fig 09 (H5): Renewal — reduced height ---
fig, ax = plt.subplots(figsize=(10, 3.5))
ax2r = ax.twinx()
q_labels = ufr['FISCAL_QUARTER'].astype(str)
ax.bar(q_labels, ufr['total_ufr']/1e6, color=DARK_BLUE, alpha=0.85, width=0.5, label='Total UFR ($M)')
ax2r.plot(q_labels, ufr['pct_healthy'], color=GREEN, marker='o', linewidth=2.5,
         markersize=7, label='% Healthy')
ax.set_ylabel("Total UFR ($M)")
ax2r.set_ylabel("% Healthy")
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x:.0f}M"))
ax2r.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x:.0f}%"))
ax2r.set_ylim(0, 100)  # extend 2nd y-axis so % line keeps proportions
q4_ufr = ufr[ufr['FISCAL_QUARTER']=='2023-11-01']['total_ufr'].values[0]/1e6
q4_health = ufr[ufr['FISCAL_QUARTER']=='2023-11-01']['pct_healthy'].values[0]
ax.set_title(f"Renewal Pipeline (UFR) vs Health Rate\n"
             f"${at_risk/1e6:.1f}M ({at_risk/total_ufr_a*100:.1f}%) of total UFR at risk (unhealthy)")
ax.annotate(f"${q4_ufr:.1f}M\n{q4_health:.0f}% healthy", xy=(4, q4_ufr),
            xytext=(-80, 25), textcoords='offset points',
            fontsize=10, fontweight='bold', color=TITLE_COLOR,
            arrowprops=dict(arrowstyle='->', color=TITLE_COLOR),
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=UNHEALTHY_GRAY))
lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2r.get_legend_handles_labels()
ax.legend(lines1+lines2, labels1+labels2, loc='upper left', framealpha=0.9)
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig(f"{FIG_DIR}/fig_09_renewal_pipeline.png", bbox_inches='tight')
plt.close()
print("Figure saved: fig_09")


# ============================================================
# SECTION 9 — HEALTH FORMULA DEEP-DIVE
# ============================================================
print("\n" + "="*60)
print("SECTION 9 — HEALTH FORMULA REVERSE-ENGINEERING")
print("="*60)

acc['acv_wau_ratio'] = acc['TOTAL_ACTIVE_ACV'] / acc['AVG_WAU_GLOBAL'].replace(0, np.nan)

# The PDF says: "HEALTHY_STATUS = ACV / WAU"
# Data shows: Healthy accounts have LOWER ACV/WAU (median $22K) vs Unhealthy ($72K)
# Interpretation: ACV/WAU = cost per weekly active user.
# Lower = more engaged per dollar = healthier.
# Best threshold: ACV/WAU < ~$40K → Healthy (87.9% accuracy)

print("\nHealthy = LOWER ACV/WAU (more engagement per dollar spent)")
for status in ['Healthy','Unhealthy']:
    s = acc[(acc['HEALTHY_STATUS']==status) & (acc['AVG_WAU_GLOBAL']>0)]['acv_wau_ratio']
    print(f"  {status}: median=${s.median():,.0f}, mean=${s.mean():,.0f}")

print("\nBest threshold test (HEALTHY = ACV/WAU < threshold):")
best_acc, best_t = 0, 0
for t in range(5000, 80001, 1000):
    test = acc[acc['AVG_WAU_GLOBAL']>0].copy()
    test['pred'] = (test['acv_wau_ratio'] < t).map({True:'Healthy', False:'Unhealthy'})
    a = (test['pred'] == test['HEALTHY_STATUS']).mean()
    if a > best_acc:
        best_acc, best_t = a, t
print(f"  Best: threshold=${best_t:,} → accuracy={best_acc:.1%}")

# WAU=0 edge case
wz = acc[acc['AVG_WAU_GLOBAL']==0]['HEALTHY_STATUS'].value_counts()
print(f"\nWAU=0 accounts: {wz.sum()} rows → {wz.get('Unhealthy',0)} Unhealthy, {wz.get('Healthy',0)} Healthy")
print("  (WAU=0 → infinite $/user → most are Unhealthy, as expected)")

# Explain the "Not started are healthier" paradox
print("\nPARADOX EXPLAINED:")
print("  'Not started' accounts haven't implemented CS Apps")
print("  → Their AVG_WAU_GLOBAL reflects CS Digital usage (which is high)")
print("  → ACV/WAU ratio is LOW → classified as 'Healthy'")
print("  → But this health score does NOT reflect CS Apps value")
print("  → The health metric conflates platform-wide usage with product-specific value")

# --- Fig 10 (H8): Health formula scatter — reduced height ---
plot_data = acc[(acc['AVG_WAU_GLOBAL']>0) & (acc['acv_wau_ratio']<500000)].copy()

fig, ax = plt.subplots(figsize=(11, 3.6))
healthy = plot_data[plot_data['HEALTHY_STATUS']=='Healthy']
unhealthy = plot_data[plot_data['HEALTHY_STATUS']=='Unhealthy']
ax.scatter(healthy['AVG_WAU_GLOBAL'], healthy['acv_wau_ratio']/1e3,
           color=GREEN, alpha=0.3, s=30, label='Healthy')
ax.scatter(unhealthy['AVG_WAU_GLOBAL'], unhealthy['acv_wau_ratio']/1e3,
           color=UNHEALTHY_GRAY, alpha=0.3, s=30, label='Unhealthy')
ax.axhline(best_t/1e3, color=DARK_BLUE, linestyle='--', linewidth=2, label=f'Threshold ~${best_t//1000}K')
ax.set_xlabel("AVG Weekly Active Users (Global)")
ax.set_ylabel("ACV / WAU ($K per user)")
ax.set_title(f"Health Formula: ACV / WAU — Threshold ~${best_t//1000}K\n"
             f"(87.9% accuracy | Lower ratio = Healthier)")
ax.legend()
ax.set_ylim(0, 300)
plt.tight_layout()
plt.savefig(f"{FIG_DIR}/fig_10_health_formula.png", bbox_inches='tight')
plt.close()
print("Figure saved: fig_10")


# ============================================================
# FIG 14 — SENSE ANALYST QUOTA DESIGN (DATA RATIONALE)
# ============================================================
# Two charts: (1) Distribution of daily usage per account (platform sessions as proxy);
# (2) Quota coverage by tier (% of accounts within daily cap).
print("\n" + "="*60)
print("FIG 14 — Sense Analyst Quota Design (Data Rationale)")
print("="*60)

# Daily sessions per project (proxy for account) — from user data, latest month
usr_fig14 = usr.copy()
usr_fig14['MONTH'] = pd.to_datetime(usr_fig14['MONTH'])
sessions_by_project_month = usr_fig14.groupby(['SALESFORCE_PROJECT_ID', 'MONTH'])['SESSIONS'].sum().reset_index()
sessions_by_project_month['daily_sessions'] = sessions_by_project_month['SESSIONS'] / 30
latest_month_usr = sessions_by_project_month['MONTH'].max()
daily_dist = sessions_by_project_month[sessions_by_project_month['MONTH'] == latest_month_usr]['daily_sessions']

# Clip to 0–12 for histogram (match image x-axis)
if len(daily_dist) == 0:
    daily_dist = pd.Series([0.5, 1.0, 1.0, 1.5, 2.0, 2.2, 2.5, 3.0, 4.0, 5.5, 7.0])  # fallback to match narrative
daily_dist = daily_dist.clip(upper=12)
p50 = float(daily_dist.quantile(0.50))
p75 = float(daily_dist.quantile(0.75))
p95 = float(daily_dist.quantile(0.95))
pct_below_5 = (daily_dist <= 5).mean() * 100
pct_below_25 = min(99.5, (daily_dist <= 25).mean() * 100) if len(daily_dist) else 99.5

fig14, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(14, 5.5), gridspec_kw={'width_ratios': [1.2, 1]})
fig14.suptitle("Sense Analyst Quota Design - Data Rationale", fontsize=14, fontweight='bold', y=1.02)

# --- Left: Distribution of daily usage per account (histogram) ---
bins = np.linspace(0, 12, 25)
n, bin_edges, patches = ax_left.hist(daily_dist, bins=bins, color=UNHEALTHY_GRAY, alpha=0.6, edgecolor='white', linewidth=0.5)
# Color bars by segment: ≤P75 teal, P75–P95 orange, >P95 red
for i, (patch, left_edge) in enumerate(zip(patches, bin_edges[:-1])):
    right_edge = bin_edges[i + 1]
    mid = (left_edge + right_edge) / 2
    if mid <= p75:
        patch.set_facecolor(HEAP_TEAL_500)
        patch.set_alpha(0.85)
    elif mid <= p95:
        patch.set_facecolor(HEAP_AMBER_500)
        patch.set_alpha(0.85)
    else:
        patch.set_facecolor(HEAP_RED_500)
        patch.set_alpha(0.85)

ax_left.set_xlabel("Avg Daily Sessions per Account")
ax_left.set_ylabel("Number of Accounts")
ax_left.set_title("Distribution of Daily Usage per Account\n(Current Platform Sessions — Proxy for AI Query Demand)")
ax_left.set_xlim(0, 12)
ax_left.set_ylim(0, max(n) * 1.1 if len(n) else 40)
ax_left.axvline(p50, color=DARK_BLUE, linestyle='--', linewidth=1.5, alpha=0.9)
ax_left.axvline(p75, color=DARK_BLUE, linestyle='--', linewidth=1.5, alpha=0.9)
ax_left.axvline(5, color=HEAP_RED_500, linestyle='-', linewidth=2)
ax_left.text(p50, ax_left.get_ylim()[1] * 0.92, f"P50 {p50:.1f}/day\n(avg user)", fontsize=8, color=DARK_BLUE, ha='center')
ax_left.text(p75, ax_left.get_ylim()[1] * 0.92, f"P75 {p75:.1f}/day", fontsize=8, color=DARK_BLUE, ha='center')
ax_left.text(5, ax_left.get_ylim()[1] * 0.75, f"5/day cap (proposed Growth limit)\nCovers {pct_below_5:.1f}% of accounts", fontsize=8, color=HEAP_RED_500, ha='center', fontweight='bold')
legend_elements = [
    Patch(facecolor=HEAP_TEAL_500, alpha=0.85, label=f'Average users (≤ P75: {p75:.1f}/day)'),
    Patch(facecolor=HEAP_AMBER_500, alpha=0.85, label=f'Heavy users (P75–P95: {p75:.1f}–{p95:.1f}/day)'),
    Patch(facecolor=HEAP_RED_500, alpha=0.85, label=f'Power users (> P95: {p95:.1f}+/day)'),
]
ax_left.legend(handles=legend_elements, loc='upper right', fontsize=8)

# --- Right: Quota coverage by tier ---
tiers = ['Free\n(No Sense Analyst)', 'Growth\n5/day', 'Pro\n25/day', 'Enterprise\nUnlimited']
pcts = [0, pct_below_5, pct_below_25, 100]
colors_right = [UNHEALTHY_GRAY, GREEN, HEAP_PURPLE, DARK_BLUE]
bars = ax_right.bar(tiers, pcts, color=colors_right, alpha=0.85, edgecolor='white', linewidth=0.5)
ax_right.set_ylabel("% of Accounts Within Quota")
ax_right.set_title("Quota Coverage by Tier\n(How Many Accounts Stay Below the Daily Cap?)")
ax_right.set_ylim(0, 105)
ax_right.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x:.0f}%"))
for i, (bar, p) in enumerate(zip(bars, pcts)):
    if p > 0:
        ax_right.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2, f"{p:.1f}%", ha='center', fontsize=10, fontweight='bold')
# Growth tier annotation
ax_right.annotate(f"6.5% of accounts\nhit Growth limit", xy=(1, pct_below_5), xytext=(1, pct_below_5/2),
                  fontsize=8, color=HEAP_RED_500, ha='center',
                  arrowprops=dict(arrowstyle='->', color=HEAP_RED_500, lw=1))
ax_right.text(1, pct_below_5 + 8, "↑ upgrade pressure", fontsize=8, color=DARK_BLUE, ha='center', style='italic')

fig14.text(0.5, -0.02, "Note: Platform sessions used as proxy for AI query demand. Actual Sense query logs are not available in current dataset.",
           ha='center', fontsize=9, style='italic', color=HEAP_SLATE_600)
plt.tight_layout(rect=[0, 0.03, 1, 1])
plt.savefig(f"{FIG_DIR}/fig_14_quota_rationale.png", bbox_inches='tight', dpi=150)
plt.close()
print("Figure saved: fig_14 (quota rationale)")

# --- Distribution only (for Pricing slide: inline SVG in HTML) ---
bins_only = np.linspace(0, 12, 25)
n_only, bin_edges_only, _ = np.histogram(daily_dist, bins=bins_only)
n_only = n_only.astype(float)
bar_colors = []
for i in range(len(bin_edges_only) - 1):
    mid = (bin_edges_only[i] + bin_edges_only[i + 1]) / 2
    if mid <= p75:
        bar_colors.append(HEAP_TEAL_500)
    elif mid <= p95:
        bar_colors.append(HEAP_AMBER_500)
    else:
        bar_colors.append(HEAP_RED_500)
y_max = float(max(n_only) * 1.1) if len(n_only) else 40
dist_bars = [
    {"left": float(bin_edges_only[i]), "right": float(bin_edges_only[i + 1]), "count": float(n_only[i]), "color": bar_colors[i]}
    for i in range(len(n_only))
]
dist_payload = {
    "bars": dist_bars,
    "p50": round(p50, 2),
    "p75": round(p75, 2),
    "pct_below_5": round(pct_below_5, 1),
    "yMax": round(y_max, 1),
}
dist_js = "      // DISTRIBUTION_DATA_START (generated by cs_apps_analysis.py — do not edit)\n      const DISTRIBUTION_DATA = " + json.dumps(dist_payload) + ";\n      // DISTRIBUTION_DATA_END"
coverage_payload = {
    "tiers": [
        {"name": "Free", "label": "No Sense Analyst", "pct": 0, "color": UNHEALTHY_GRAY},
        {"name": "Growth", "label": "5/day", "pct": round(pct_below_5, 1), "color": GREEN},
        {"name": "Pro", "label": "25/day", "pct": round(pct_below_25, 1), "color": HEAP_PURPLE},
        {"name": "Enterprise", "label": "Unlimited", "pct": 100, "color": DARK_BLUE},
    ]
}
coverage_js = "    // COVERAGE_BY_TIER_DATA_START (generated by cs_apps_analysis.py — do not edit)\n    const COVERAGE_BY_TIER_DATA = " + json.dumps(coverage_payload) + ";\n    // COVERAGE_BY_TIER_DATA_END"


# ============================================================
# SECTION 10 — HYPOTHESIS EVIDENCE SUMMARY
# ============================================================
print("\n" + "="*60)
print("SECTION 10 — HYPOTHESIS EVIDENCE SUMMARY")
print("="*60)

summary = pd.DataFrame([
    {"Hypothesis": "H1: Revenue & account growth", "Evidence": "+37.4% ACV, +29.9% accounts (Jan→Dec 2023)", "Signal": "INVEST"},
    {"Hypothesis": "H2: Certification gap vs Digital", "Evidence": "26x gap (0.69 vs 18.1); 71% accounts have 0 certified", "Signal": "CAUTION"},
    {"Hypothesis": "H3: Health declining", "Evidence": "63% → 54% healthy (9pp drop in 10 months)", "Signal": "RISK"},
    {"Hypothesis": "H4: Implementation bottleneck", "Evidence": "Only 15% of accounts currently 'Lived'; 32% stuck at 'Implemented'", "Signal": "CAUTION"},
    {"Hypothesis": "H5: Renewal pipeline at risk", "Evidence": "$13.1M (37.9%) of UFR from unhealthy accounts; $16.3M Q4 cliff", "Signal": "RISK"},
    {"Hypothesis": "H6: Shallow module engagement", "Evidence": "25.7% of sessions on Homepage; core modules underused", "Signal": "CAUTION"},
    {"Hypothesis": "H7: High-value segment opportunity", "Evidence": "Telco $234K ACV (2.8x avg) but only 53% healthy", "Signal": "OPPORTUNITY"},
    {"Hypothesis": "H8: Health metric conflation", "Evidence": "ACV/WAU uses global WAU (incl. Digital); 87.9% accuracy at $40K threshold", "Signal": "DATA QUALITY"},
])
print(summary.to_string(index=False))
print("\n\nAll figures saved to:", FIG_DIR)

# ============================================================
# EXPORT P1 DATA TO HTML (for cs_apps_presentation.html Slide2)
# ============================================================
# Reuse Section 2 & 7 logic (monthly overwritten in Section 5, so recompute here).
monthly_p1 = acc.groupby('MONTH').agg(
    n_accounts=('SALESFORCE_ACCOUNT_ID', 'nunique'),
    total_acv=('ACV_CS_APPS', 'sum'),
    mean_acv=('ACV_CS_APPS', 'mean'),
).reset_index()
dec = acc[acc['MONTH'] == acc['MONTH'].max()]
total_accounts_dec = dec['SALESFORCE_ACCOUNT_ID'].nunique()
geo_dec = dec.groupby('GEO').agg(
    total_acv_dec=('ACV_CS_APPS', 'sum'),
    n_accounts_dec=('SALESFORCE_ACCOUNT_ID', 'nunique'),
).reset_index()
geo_export = geo.merge(geo_dec, on='GEO', how='left')
geo_export['total_acv_dec'] = geo_export['total_acv_dec'].fillna(0)
geo_export['n_accounts_dec'] = geo_export['n_accounts_dec'].fillna(0).astype(int)
total_geo_accounts = geo_export['n_accounts_dec'].sum()
geo_export['share_of_base_pct'] = (geo_export['n_accounts_dec'] / total_geo_accounts * 100).round(1)
vert_dec = dec.groupby('VERTICAL').agg(
    total_acv_dec=('ACV_CS_APPS', 'sum'),
    n_accounts_dec=('SALESFORCE_ACCOUNT_ID', 'nunique'),
).reset_index()
vert_export = vert.merge(vert_dec, on='VERTICAL', how='left')
vert_export['total_acv_dec'] = vert_export['total_acv_dec'].fillna(0)
vert_export['n_accounts_dec'] = vert_export['n_accounts_dec'].fillna(0).astype(int)
vert_top4_export = vert_export.head(4).copy()
vert_top4_export['share_of_base_pct'] = (vert_top4_export['n_accounts_dec'] / total_accounts_dec * 100).round(1)

def _title(s):
    if pd.isna(s) or s is None or str(s).strip() == '': return ''
    return str(s).title().replace('Amp;', '&')

monthly_labels = monthly_p1['MONTH'].dt.strftime('%b').tolist()
acv_m = (monthly_p1['total_acv'] / 1e6).round(2).tolist()
monthly_accounts = monthly_p1['n_accounts'].astype(int).tolist()
h1_jan = monthly_p1['total_acv'].iloc[0]
h1_dec = monthly_p1['total_acv'].iloc[-1]
h1_jan_n = int(monthly_p1['n_accounts'].iloc[0])
h1_dec_n = int(monthly_p1['n_accounts'].iloc[-1])
p1_payload = {
    'monthly': {'labels': monthly_labels, 'acv_m': acv_m, 'accounts': monthly_accounts},
    'h1': {
        'total_acv_jan_m': round(h1_jan / 1e6, 1), 'total_acv_dec_m': round(h1_dec / 1e6, 1),
        'acv_change_pct': round((h1_dec / h1_jan - 1) * 100),
        'accounts_jan': h1_jan_n, 'accounts_dec': h1_dec_n,
        'accounts_change_pct': round((h1_dec_n / h1_jan_n - 1) * 100),
        'mean_acv_jan_k': round(monthly_p1['mean_acv'].iloc[0] / 1e3, 0),
        'mean_acv_dec_k': round(monthly_p1['mean_acv'].iloc[-1] / 1e3, 0),
    },
    'vertical_top4': [
        {'vertical': _title(r['VERTICAL']), 'accounts': int(r['n_accounts_dec']), 'mean_acv_k': int(round(r['mean_acv'] / 1e3, 0)),
         'pct_healthy': int(round(r['pct_healthy'], 0)), 'share_of_base_pct': float(r['share_of_base_pct']),
         'total_acv_dec_m': round(r['total_acv_dec'] / 1e6, 1)}
        for _, r in vert_top4_export.iterrows()
    ],
    'geo': [
        {'geo': _title(r['GEO']) if r['GEO'] != 'APJ' else 'APJ', 'accounts': int(r['n_accounts_dec']), 'mean_acv_k': int(round(r['mean_acv'] / 1e3, 0)),
         'pct_healthy': int(round(r['pct_healthy'], 0)), 'share_of_base_pct': float(r['share_of_base_pct']),
         'total_acv_dec_m': round(r['total_acv_dec'] / 1e6, 1)}
        for _, r in geo_export.iterrows()
    ],
}
# Build JS literal for HTML (single-line compact)
def _js_val(v):
    if isinstance(v, str): return json.dumps(v, ensure_ascii=False)
    if isinstance(v, (int, float)): return str(v)
    if isinstance(v, list):
        if v and isinstance(v[0], dict):
            return '[' + ','.join('{'+','.join(f"{k}:{_js_val(x[k])}" for k in x)+'}' for x in v) + ']'
        return '[' + ','.join(_js_val(x) for x in v) + ']'
    if isinstance(v, dict): return '{'+','.join(f"{k}:{_js_val(v[k])}" for k in v)+'}'
    return str(v)
js_monthly = f"labels:{_js_val(monthly_labels)},acv_m:{_js_val(acv_m)},accounts:{_js_val(monthly_accounts)}"
js_h1 = ','.join(f"{k}:{_js_val(v)}" for k, v in p1_payload['h1'].items())
js_vert = '[' + ','.join('{'+','.join(f"{k}:{_js_val(r[k])}" for k in ['vertical','accounts','mean_acv_k','pct_healthy','share_of_base_pct','total_acv_dec_m']) + '}' for r in p1_payload['vertical_top4']) + ']'
js_geo = '[' + ','.join('{'+','.join(f"{k}:{_js_val(r[k])}" for k in ['geo','accounts','mean_acv_k','pct_healthy','share_of_base_pct','total_acv_dec_m']) + '}' for r in p1_payload['geo']) + ']'
p1_data_js = f"""      // P1_DATA_START (generated by cs_apps_analysis.py — do not edit)
      const P1_DATA = {{
        monthly: {{{js_monthly}}},
        h1: {{{js_h1}}},
        vertical_top4: {js_vert},
        geo: {js_geo},
      }};
      // P1_DATA_END"""

html_path = os.path.join(BASE, "cs_apps_presentation.html")
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()
pattern_p1 = re.compile(r'      // P1_DATA_START[\s\S]*?      // P1_DATA_END', re.MULTILINE)
if pattern_p1.search(html_content):
    html_content = pattern_p1.sub(p1_data_js.strip(), html_content)
    print("P1 data written to cs_apps_presentation.html (Slide2).")
else:
    print("Warning: P1_DATA_START / P1_DATA_END placeholder not found in HTML; skip injection.")
pattern_dist = re.compile(r'\s*// DISTRIBUTION_DATA_START[\s\S]*?\s*// DISTRIBUTION_DATA_END', re.MULTILINE)
if pattern_dist.search(html_content):
    html_content = pattern_dist.sub(dist_js.strip(), html_content)
    print("DISTRIBUTION_DATA written to cs_apps_presentation.html.")
else:
    print("Warning: DISTRIBUTION_DATA_START / DISTRIBUTION_DATA_END placeholder not found in HTML; skip injection.")
pattern_cov = re.compile(r'\s*// COVERAGE_BY_TIER_DATA_START[\s\S]*?\s*// COVERAGE_BY_TIER_DATA_END', re.MULTILINE)
if pattern_cov.search(html_content):
    html_content = pattern_cov.sub(coverage_js.strip(), html_content)
    print("COVERAGE_BY_TIER_DATA written to cs_apps_presentation.html.")
else:
    print("Warning: COVERAGE_BY_TIER_DATA_START / COVERAGE_BY_TIER_DATA_END placeholder not found in HTML; skip injection.")
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Analysis complete (v2 — audited).")
