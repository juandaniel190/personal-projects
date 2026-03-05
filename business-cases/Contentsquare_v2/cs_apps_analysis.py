"""
CS Apps Investment Analysis — v3 (Rebuilt from scratch)
Case Study — Senior Manager, Product Data Analyst
Contentsquare

KEY CORRECTIONS FROM v2:
  - ACV_CS_APPS is the correct Apps revenue column (not TOTAL_ACTIVE_ACV)
  - CS Digital ACV = TOTAL_ACTIVE_ACV - ACV_CS_APPS
  - TOTAL_UFR is deduplicated: one row per account per fiscal quarter (last month)
  - All penetration metrics use ACV_CS_APPS / TOTAL_ACTIVE_ACV

Structure:
  0  Setup & Data Loading
  1  Data Quality Audit
  2  Pillar 1 — Value Creation (Revenue & Growth)
  3  Pillar 2 — Value Delivery (Adoption & Engagement)
  4  Pillar 3 — Value Protection (Retention & Renewals)
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
import os, warnings
warnings.filterwarnings('ignore')

# --- Paths ---
BASE = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE, "data")
ACC_PATH = os.path.join(DATA_DIR, "Account Data Case Study Result 1.csv")
USR_PATH = os.path.join(DATA_DIR, "User Data Case Study Result 1.csv")
FIG_DIR  = os.path.join(BASE, "figures")
os.makedirs(FIG_DIR, exist_ok=True)

# --- Brand Colors ---
C_PRIMARY   = "#2D1A4E"   # Aubergine / dark purple
C_SECONDARY = "#FF6B6B"   # Coral
C_ACCENT    = "#4ECDC4"   # Teal
C_LIGHT     = "#A8A0B5"   # Muted lavender
C_BG        = "#FAFAFA"
C_GRID      = "#E8E8E8"
PALETTE = [C_PRIMARY, C_SECONDARY, C_ACCENT, "#F4A261", "#E76F51", "#264653"]

# --- Style ---
plt.rcParams.update({
    'figure.facecolor': C_BG, 'axes.facecolor': C_BG,
    'axes.edgecolor': C_GRID, 'axes.grid': True,
    'grid.color': C_GRID, 'grid.alpha': 0.5,
    'font.family': 'sans-serif', 'font.size': 10,
    'axes.spines.top': False, 'axes.spines.right': False,
})

def fmt_dollar(x, _=None):
    if abs(x) >= 1e6: return f"${x/1e6:.1f}M"
    if abs(x) >= 1e3: return f"${x/1e3:.0f}K"
    return f"${x:,.0f}"

def save_fig(fig, name):
    path = os.path.join(FIG_DIR, name)
    fig.savefig(path, dpi=150, bbox_inches='tight', facecolor=C_BG)
    plt.close(fig)
    print(f"  → Saved {path}")

# ============================================================
# SECTION 0b — DATA LOADING
# ============================================================
acc = pd.read_csv(ACC_PATH)
usr = pd.read_csv(USR_PATH)

acc['MONTH'] = pd.to_datetime(acc['MONTH'])
usr['MONTH'] = pd.to_datetime(usr['MONTH'])

# Derived column: CS Digital ACV
acc['ACV_DIGITAL'] = acc['TOTAL_ACTIVE_ACV'] - acc['ACV_CS_APPS']

print(f"Account data: {acc.shape[0]} rows, {acc['SALESFORCE_ACCOUNT_ID'].nunique()} unique accounts")
print(f"User data: {usr.shape[0]} rows, {usr['USER_ID'].nunique()} unique users")
print(f"Date range: {acc['MONTH'].min()} → {acc['MONTH'].max()}")

# ============================================================
# SECTION 1 — DATA QUALITY AUDIT
# ============================================================
print("\n" + "="*60)
print("SECTION 1 — DATA QUALITY AUDIT")
print("="*60)

# 1a. Duplicate checks
dup_exact_acc = acc.duplicated().sum()
dup_exact_usr = usr.duplicated().sum()
dup_key_acc = acc.groupby(['SALESFORCE_ACCOUNT_ID','MONTH']).size()
dup_key_acc_count = (dup_key_acc > 1).sum()
dup_key_usr = usr.groupby(['USER_ID','MONTH','MODULE_NAME','PROJECT_ID']).size()
dup_key_usr_count = (dup_key_usr > 1).sum()

print(f"Exact duplicate rows — Account: {dup_exact_acc}, User: {dup_exact_usr}")
print(f"Duplicate (Account, Month) keys: {dup_key_acc_count}")
print(f"Duplicate (User, Month, Module, Project) keys: {dup_key_usr_count}")

# 1b. NULL analysis
print("\nNULL counts — Account data:")
for col in acc.columns:
    n = acc[col].isna().sum()
    if n > 0:
        print(f"  {col}: {n} ({n/len(acc)*100:.1f}%)")

# 1c. Zero WAU check
zero_wau = acc[acc['AVG_WAU_GLOBAL'] == 0]
print(f"\nRows with AVG_WAU_GLOBAL = 0: {len(zero_wau)} ({zero_wau['SALESFORCE_ACCOUNT_ID'].nunique()} accounts)")

# 1d. ACV_CS_APPS = 0 check
zero_apps = acc[acc['ACV_CS_APPS'] == 0]
print(f"Rows with ACV_CS_APPS = 0: {len(zero_apps)} ({zero_apps['SALESFORCE_ACCOUNT_ID'].nunique()} accounts)")

# 1e. UFR duplication pattern
ufr_nonzero = acc[acc['TOTAL_UFR'] > 0].copy()
ufr_per_aq = ufr_nonzero.groupby(['SALESFORCE_ACCOUNT_ID','FISCAL_QUARTER']).size()
print(f"\nUFR duplication: months per account-quarter range = {ufr_per_aq.min()} to {ufr_per_aq.max()}")
print("  → TOTAL_UFR is repeated for every month within a fiscal quarter.")
print("  → All UFR analyses use ONE row per account-quarter (last month) to avoid overcounting.")

# ============================================================
# SECTION 2 — PILLAR 1: VALUE CREATION (Revenue & Growth)
# ============================================================
print("\n" + "="*60)
print("SECTION 2 — PILLAR 1: VALUE CREATION")
print("="*60)

# --- 2a. Monthly ACV Trend ---
monthly = acc.groupby('MONTH').agg(
    n_accounts=('SALESFORCE_ACCOUNT_ID','nunique'),
    total_acv=('TOTAL_ACTIVE_ACV','sum'),
    apps_acv=('ACV_CS_APPS','sum'),
    mean_apps_acv=('ACV_CS_APPS','mean'),
    median_apps_acv=('ACV_CS_APPS','median'),
).reset_index()
monthly['digital_acv'] = monthly['total_acv'] - monthly['apps_acv']
monthly['penetration'] = monthly['apps_acv'] / monthly['total_acv'] * 100

print("\n--- Monthly CS Apps ACV & Penetration ---")
for _, r in monthly.iterrows():
    print(f"  {r['MONTH'].strftime('%b %Y')}: "
          f"Accounts={r['n_accounts']}, "
          f"Apps ACV=${r['apps_acv']/1e6:.2f}M, "
          f"Total ACV=${r['total_acv']/1e6:.2f}M, "
          f"Penetration={r['penetration']:.1f}%")

jan = monthly.iloc[0]
dec = monthly.iloc[-1]
apps_growth = (dec['apps_acv'] / jan['apps_acv'] - 1) * 100
total_growth = (dec['total_acv'] / jan['total_acv'] - 1) * 100
acct_growth = (dec['n_accounts'] / jan['n_accounts'] - 1) * 100

print(f"\n--- Year-over-Year Summary (Jan → Dec 2023) ---")
print(f"  CS Apps ACV: ${jan['apps_acv']/1e6:.2f}M → ${dec['apps_acv']/1e6:.2f}M (+{apps_growth:.0f}%)")
print(f"  Total ACV:   ${jan['total_acv']/1e6:.2f}M → ${dec['total_acv']/1e6:.2f}M (+{total_growth:.0f}%)")
print(f"  Accounts:    {int(jan['n_accounts'])} → {int(dec['n_accounts'])} (+{acct_growth:.0f}%)")
print(f"  Penetration: {jan['penetration']:.1f}% → {dec['penetration']:.1f}% (+{dec['penetration']-jan['penetration']:.1f}pp)")
print(f"  Mean Apps ACV/account: ${jan['mean_apps_acv']:,.0f} → ${dec['mean_apps_acv']:,.0f}")

# --- FIGURE 1: ACV & Account Growth ---
fig, ax1 = plt.subplots(figsize=(10, 5))
ax2 = ax1.twinx()

months_str = monthly['MONTH'].dt.strftime('%b')
x = range(len(monthly))

# Stacked bar: Apps ACV + Digital ACV
ax1.bar(x, monthly['apps_acv']/1e6, color=C_PRIMARY, label='CS Apps ACV', width=0.6, zorder=3)
ax1.bar(x, monthly['digital_acv']/1e6, bottom=monthly['apps_acv']/1e6, color=C_LIGHT, label='CS Digital + Other ACV', width=0.6, zorder=3)

# Line: number of accounts
ax2.plot(x, monthly['n_accounts'], color=C_SECONDARY, marker='o', linewidth=2, markersize=5, label='# Accounts', zorder=4)

ax1.set_xticks(x)
ax1.set_xticklabels(months_str, rotation=0)
ax1.set_ylabel('ACV ($M)')
ax2.set_ylabel('Number of Accounts', color=C_SECONDARY)
ax2.set_ylim(0, monthly['n_accounts'].max() * 1.25)   # start from zero
ax1.set_title('CS Apps ACV Growth & Account Expansion (2023)', fontsize=13, fontweight='bold', pad=15)

# Annotations
ax1.annotate(f'Apps: ${dec["apps_acv"]/1e6:.1f}M\n(+{apps_growth:.0f}% YoY)',
             xy=(11, dec['apps_acv']/1e6/2), fontsize=8, ha='center', color='white', fontweight='bold')
ax2.annotate(f'{int(dec["n_accounts"])} accounts\n(+{acct_growth:.0f}%)',
             xy=(11, dec['n_accounts']), xytext=(9.5, dec['n_accounts']+8),
             fontsize=8, color=C_SECONDARY, fontweight='bold',
             arrowprops=dict(arrowstyle='->', color=C_SECONDARY, lw=1))

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left', framealpha=0.9, fontsize=8)
fig.tight_layout()
save_fig(fig, 'fig_01_acv_account_growth.png')

# --- FIGURE 1b: Penetration Trend ---
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(x, monthly['penetration'], color=C_PRIMARY, marker='o', linewidth=2.5, markersize=6, zorder=3)
ax.fill_between(x, monthly['penetration'], alpha=0.1, color=C_PRIMARY)
ax.set_xticks(x)
ax.set_xticklabels(months_str, rotation=0)
ax.set_ylabel('CS Apps % of Total ACV')
ax.set_title('CS Apps Wallet Penetration (% of Total Contentsquare ACV)', fontsize=13, fontweight='bold', pad=15)
ax.set_ylim(20, 28)

for i, (mo, pen) in enumerate(zip(months_str, monthly['penetration'])):
    ax.annotate(f'{pen:.1f}%', xy=(i, pen), xytext=(0, 8), textcoords='offset points',
                fontsize=7, ha='center', color=C_PRIMARY)

ax.axhline(y=jan['penetration'], color=C_LIGHT, linestyle='--', linewidth=1, alpha=0.7)
ax.annotate(f'Jan: {jan["penetration"]:.1f}%', xy=(0.5, jan['penetration']),
            fontsize=7, color=C_LIGHT, va='bottom')

fig.tight_layout()
save_fig(fig, 'fig_01b_penetration_trend.png')


# --- 2b. Segment Analysis (Dec 2023) — using TOTALS not means ---
print("\n--- Segment Analysis (Dec 2023) ---")
dec_data = acc[acc['MONTH'] == acc['MONTH'].max()].copy()

# By Vertical
vert = dec_data.groupby('VERTICAL').agg(
    n_accounts=('SALESFORCE_ACCOUNT_ID','nunique'),
    sum_apps_acv=('ACV_CS_APPS','sum'),
    sum_total_acv=('TOTAL_ACTIVE_ACV','sum'),
    n_healthy=('HEALTHY_STATUS', lambda x: (x=='Healthy').sum()),
).reset_index()
vert['apps_penetration'] = (vert['sum_apps_acv'] / vert['sum_total_acv'] * 100).round(1)
vert['pct_healthy'] = (vert['n_healthy'] / vert['n_accounts'] * 100).round(0)
vert = vert.sort_values('sum_apps_acv', ascending=False)

print("\nBy Vertical:")
for _, r in vert.iterrows():
    print(f"  {r['VERTICAL']}: n={r['n_accounts']}, "
          f"Apps ACV=${r['sum_apps_acv']/1e6:.2f}M, "
          f"Total ACV=${r['sum_total_acv']/1e6:.2f}M, "
          f"Penetration={r['apps_penetration']:.0f}%, "
          f"Health={r['pct_healthy']:.0f}%")

# By Geo
geo = dec_data.groupby('GEO').agg(
    n_accounts=('SALESFORCE_ACCOUNT_ID','nunique'),
    sum_apps_acv=('ACV_CS_APPS','sum'),
    sum_total_acv=('TOTAL_ACTIVE_ACV','sum'),
    n_healthy=('HEALTHY_STATUS', lambda x: (x=='Healthy').sum()),
).reset_index()
geo['apps_penetration'] = (geo['sum_apps_acv'] / geo['sum_total_acv'] * 100).round(1)
geo['pct_healthy'] = (geo['n_healthy'] / geo['n_accounts'] * 100).round(0)

print("\nBy Geo:")
for _, r in geo.iterrows():
    print(f"  {r['GEO']}: n={r['n_accounts']}, "
          f"Apps ACV=${r['sum_apps_acv']/1e6:.2f}M, "
          f"Total ACV=${r['sum_total_acv']/1e6:.2f}M, "
          f"Penetration={r['apps_penetration']:.0f}%, "
          f"Health={r['pct_healthy']:.0f}%")

# --- FIGURE 8: Segment Analysis ---
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Vertical chart (top 8 by total Apps ACV)
top_vert = vert.head(8)
ax = axes[0]
y_pos = range(len(top_vert))
bars = ax.barh(y_pos, top_vert['sum_apps_acv']/1e6, color=C_PRIMARY, height=0.6, zorder=3)
ax.set_yticks(y_pos)
ax.set_yticklabels(top_vert['VERTICAL'].values, fontsize=8)
ax.set_xlabel('Total CS Apps ACV ($M)')
ax.set_title('CS Apps ACV by Vertical (Dec 2023)', fontsize=11, fontweight='bold')
for i, (v, t, pen, hlth) in enumerate(zip(top_vert['sum_apps_acv']/1e6,
                                            top_vert['sum_total_acv']/1e6,
                                            top_vert['apps_penetration'],
                                            top_vert['pct_healthy'])):
    ax.annotate(f'Apps: ${v:.1f}M / Total: ${t:.1f}M | Pen: {pen:.0f}% | Health: {hlth:.0f}%',
                xy=(v + 0.05, i), fontsize=7, va='center')
ax.invert_yaxis()

# Geo chart
ax = axes[1]
bars = ax.bar(range(len(geo)), geo['sum_apps_acv']/1e6, color=[C_PRIMARY, C_ACCENT, C_SECONDARY], width=0.5, zorder=3)
ax.set_xticks(range(len(geo)))
ax.set_xticklabels(geo['GEO'].values)
ax.set_ylabel('Total CS Apps ACV ($M)')
ax.set_title('CS Apps ACV by Geo (Dec 2023)', fontsize=11, fontweight='bold')
for i, (v, t, pen, hlth) in enumerate(zip(geo['sum_apps_acv']/1e6,
                                            geo['sum_total_acv']/1e6,
                                            geo['apps_penetration'],
                                            geo['pct_healthy'])):
    ax.annotate(f'${v:.1f}M / ${t:.1f}M\nPen: {pen:.0f}%\nHealth: {hlth:.0f}%',
                xy=(i, v + 0.1), fontsize=8, ha='center', va='bottom')

fig.tight_layout()
save_fig(fig, 'fig_08_segment_analysis.png')


# ============================================================
# SECTION 3 — PILLAR 2: VALUE DELIVERY (Adoption & Engagement)
# ============================================================
print("\n" + "="*60)
print("SECTION 3 — PILLAR 2: VALUE DELIVERY")
print("="*60)

# --- 3a. Implementation Status ---
latest_per_account = acc.sort_values('MONTH').groupby('SALESFORCE_ACCOUNT_ID').last().reset_index()
n_total = len(latest_per_account)

impl_dist = latest_per_account['IMPLEMENTATION_STATUS_APPS'].value_counts(dropna=False)
print(f"\n--- Implementation Status (latest snapshot, {n_total} accounts) ---")
for status, count in impl_dist.items():
    label = status if pd.notna(status) else "NULL / Untracked"
    print(f"  {label}: {count} ({count/n_total*100:.0f}%)")

n_lived = impl_dist.get('Lived', 0)
n_partially_lived = impl_dist.get('Partially lived', 0)
n_implemented = impl_dist.get('Implemented', 0)
n_null = latest_per_account['IMPLEMENTATION_STATUS_APPS'].isna().sum()
print(f"\n  → Lived: {n_lived} ({n_lived/n_total*100:.0f}%)")
print(f"  → NOT in production (all others): {n_total - n_lived} ({(n_total-n_lived)/n_total*100:.0f}%)")

# --- FIGURE 6: Implementation Funnel ---
status_order = ['NULL / Untracked', 'Not started', 'Started', 'Partially implemented',
                'Implemented', 'Partially lived', 'Lived']
status_counts = []
for s in status_order:
    if s == 'NULL / Untracked':
        status_counts.append(n_null)
    else:
        status_counts.append(impl_dist.get(s, 0))

colors_impl = [C_LIGHT, '#E8D5B5', '#F4A261', '#E76F51', C_SECONDARY, C_ACCENT, C_PRIMARY]

fig, ax = plt.subplots(figsize=(10, 5))
bars = ax.barh(range(len(status_order)), status_counts, color=colors_impl, height=0.6, zorder=3)
ax.set_yticks(range(len(status_order)))
ax.set_yticklabels(status_order, fontsize=9)
ax.set_xlabel('Number of Accounts')
ax.set_title(f'CS Apps Implementation Status ({n_total} accounts)', fontsize=13, fontweight='bold', pad=15)
ax.invert_yaxis()

for i, (c, s) in enumerate(zip(status_counts, status_order)):
    pct = c / n_total * 100
    ax.annotate(f'{c} ({pct:.0f}%)', xy=(c + 0.5, i), fontsize=9, va='center', fontweight='bold')

# Highlight: only 15% live
ax.axvline(x=0, color='black', linewidth=0.5)
fig.text(0.95, 0.05, f'Only {n_lived} accounts ({n_lived/n_total*100:.0f}%) are fully live in production',
         fontsize=9, ha='right', style='italic', color=C_SECONDARY)

fig.tight_layout()
save_fig(fig, 'fig_06_implementation_funnel.png')


# --- 3b. Certification Gap ---
mean_cert_apps = latest_per_account['CERTIFIED_USERS_APPS'].mean()
mean_cert_digital = latest_per_account['CERTIFIED_USERS_DIGITAL'].mean()
zero_cert_apps = (latest_per_account['CERTIFIED_USERS_APPS'] == 0).sum()
pct_zero_cert = zero_cert_apps / n_total * 100

print(f"\n--- Certification Gap ---")
print(f"  Mean certified users (Apps):    {mean_cert_apps:.2f}")
print(f"  Mean certified users (Digital): {mean_cert_digital:.1f}")
print(f"  Ratio Digital/Apps: {mean_cert_digital/mean_cert_apps:.0f}x")
print(f"  Accounts with 0 certified Apps users: {zero_cert_apps}/{n_total} ({pct_zero_cert:.1f}%)")

# Avg sessions per user per month
avg_sessions = usr['SESSIONS'].mean()
print(f"  Avg sessions per user per month: {avg_sessions:.2f}")

# --- FIGURE 4: Certification Gap ---
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Left: bar comparison
ax = axes[0]
ax.bar([0], [mean_cert_apps], color=C_PRIMARY, width=0.4, label='CS Apps', zorder=3)
ax.bar([1], [mean_cert_digital], color=C_LIGHT, width=0.4, label='CS Digital', zorder=3)
ax.set_xticks([0, 1])
ax.set_xticklabels(['CS Apps', 'CS Digital'])
ax.set_ylabel('Avg Certified Users per Account')
ax.set_title('Certification: Apps vs Digital', fontsize=11, fontweight='bold')
ax.annotate(f'{mean_cert_apps:.2f}', xy=(0, mean_cert_apps), xytext=(0, mean_cert_apps + 1),
            fontsize=10, ha='center', fontweight='bold', color=C_PRIMARY)
ax.annotate(f'{mean_cert_digital:.1f}', xy=(1, mean_cert_digital), xytext=(1, mean_cert_digital + 1),
            fontsize=10, ha='center', fontweight='bold', color=C_LIGHT)
ax.annotate(f'{mean_cert_digital/mean_cert_apps:.0f}x gap', xy=(0.5, mean_cert_digital/2),
            fontsize=12, ha='center', fontweight='bold', color=C_SECONDARY, style='italic')

# Right: distribution
ax = axes[1]
cert_dist = latest_per_account['CERTIFIED_USERS_APPS'].value_counts().sort_index()
ax.bar(cert_dist.index, cert_dist.values, color=C_PRIMARY, zorder=3)
ax.set_xlabel('# Certified CS Apps Users')
ax.set_ylabel('Number of Accounts')
ax.set_title(f'Distribution of CS Apps Certified Users\n({pct_zero_cert:.0f}% have zero)', fontsize=11, fontweight='bold')

fig.tight_layout()
save_fig(fig, 'fig_04_certification_gap.png')


# --- 3c. Module Engagement ---
print(f"\n--- Module Engagement ---")
module_stats = usr.groupby('MODULE_NAME').agg(
    total_sessions=('SESSIONS','sum'),
    unique_users=('USER_ID','nunique'),
).reset_index()
module_stats['pct_sessions'] = (module_stats['total_sessions'] / module_stats['total_sessions'].sum() * 100).round(1)
# avg sessions per user-month (each user-month is one observation)
module_sessions_per_user_month = usr.groupby('MODULE_NAME')['SESSIONS'].mean().reset_index()
module_sessions_per_user_month.columns = ['MODULE_NAME', 'avg_sessions_per_user_month']
module_stats = module_stats.merge(module_sessions_per_user_month, on='MODULE_NAME', how='left')
module_stats = module_stats.sort_values('total_sessions', ascending=False)

for _, r in module_stats.head(10).iterrows():
    print(f"  {r['MODULE_NAME']}: {r['pct_sessions']}% of sessions, "
          f"avg {r['avg_sessions_per_user_month']:.2f} sessions/user/month, "
          f"{r['unique_users']} unique users")

# --- FIGURE 7: Module Engagement ---
top_modules = module_stats.head(10)
fig, ax = plt.subplots(figsize=(10, 5))
colors_mod = [C_LIGHT if m == 'Homepage' else C_PRIMARY for m in top_modules['MODULE_NAME']]
bars = ax.barh(range(len(top_modules)), top_modules['pct_sessions'], color=colors_mod, height=0.6, zorder=3)
ax.set_yticks(range(len(top_modules)))
ax.set_yticklabels(top_modules['MODULE_NAME'].values, fontsize=9)
ax.set_xlabel('% of Total Sessions')
ax.set_title('CS Apps Module Engagement (Top 10)', fontsize=13, fontweight='bold', pad=15)
ax.invert_yaxis()

for i, (pct, avg) in enumerate(zip(top_modules['pct_sessions'], top_modules['avg_sessions_per_user_month'])):
    ax.annotate(f'{pct}% | avg {avg} sessions/user', xy=(pct + 0.3, i), fontsize=8, va='center')

fig.text(0.95, 0.05, 'Homepage = navigation, not value. 1 in 4 sessions stays on Homepage.',
         fontsize=8, ha='right', style='italic', color=C_SECONDARY)

fig.tight_layout()
save_fig(fig, 'fig_07_module_engagement.png')


# --- 3d. MAU / Sessions trend ---
print(f"\n--- Monthly Active Users Trend ---")
mau = usr.groupby('MONTH').agg(
    unique_users=('USER_ID','nunique'),
    total_sessions=('SESSIONS','sum'),
).reset_index()
mau['sessions_per_user'] = (mau['total_sessions'] / mau['unique_users']).round(2)

for _, r in mau.iterrows():
    print(f"  {r['MONTH'].strftime('%b %Y')}: {r['unique_users']} users, "
          f"{r['total_sessions']} sessions, {r['sessions_per_user']} sess/user")

# --- FIGURE 5: MAU & Sessions ---
fig, ax1 = plt.subplots(figsize=(10, 5))
ax2 = ax1.twinx()

x = range(len(mau))
months_str = mau['MONTH'].dt.strftime('%b')

ax1.bar(x, mau['unique_users'], color=C_PRIMARY, width=0.5, label='Unique Users', zorder=3)
ax2.plot(x, mau['sessions_per_user'], color=C_SECONDARY, marker='o', linewidth=2, label='Sessions/User', zorder=4)

ax1.set_xticks(x)
ax1.set_xticklabels(months_str)
ax1.set_ylabel('Unique Users')
ax2.set_ylabel('Sessions per User', color=C_SECONDARY)
ax1.set_title('Monthly Active Users & Engagement Depth (2023)', fontsize=13, fontweight='bold', pad=15)

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left', framealpha=0.9, fontsize=8)

fig.tight_layout()
save_fig(fig, 'fig_05_mau_sessions.png')


# ============================================================
# SECTION 4 — PILLAR 3: VALUE PROTECTION (Retention & Health)
# ============================================================
print("\n" + "="*60)
print("SECTION 4 — PILLAR 3: VALUE PROTECTION")
print("="*60)

# --- 4a. Health Trend ---
health_monthly = acc.groupby('MONTH').agg(
    n_accounts=('SALESFORCE_ACCOUNT_ID','nunique'),
    n_healthy=('HEALTHY_STATUS', lambda x: (x=='Healthy').sum()),
).reset_index()
health_monthly['pct_healthy'] = (health_monthly['n_healthy'] / health_monthly['n_accounts'] * 100).round(1)

print("\n--- Health Status Trend ---")
for _, r in health_monthly.iterrows():
    print(f"  {r['MONTH'].strftime('%b %Y')}: {r['pct_healthy']}% healthy "
          f"({int(r['n_healthy'])}/{int(r['n_accounts'])})")

# --- FIGURE 2: Health Trend ---
fig, ax = plt.subplots(figsize=(10, 4))
x = range(len(health_monthly))
months_str = health_monthly['MONTH'].dt.strftime('%b')

ax.plot(x, health_monthly['pct_healthy'], color=C_PRIMARY, marker='o', linewidth=2.5, markersize=6, zorder=3)
ax.fill_between(x, health_monthly['pct_healthy'], alpha=0.1, color=C_PRIMARY)
ax.set_xticks(x)
ax.set_xticklabels(months_str)
ax.set_ylabel('% Accounts Healthy')
ax.set_title('Account Health Trend (2023)', fontsize=13, fontweight='bold', pad=15)
ax.set_ylim(45, 70)

for i, pct in enumerate(health_monthly['pct_healthy']):
    ax.annotate(f'{pct}%', xy=(i, pct), xytext=(0, 8), textcoords='offset points',
                fontsize=7, ha='center', color=C_PRIMARY)

# Peak annotation
peak_idx = health_monthly['pct_healthy'].idxmax()
peak_val = health_monthly['pct_healthy'].max()
ax.annotate(f'Peak: {peak_val}%', xy=(peak_idx, peak_val), xytext=(peak_idx + 1, peak_val + 3),
            fontsize=8, color=C_SECONDARY, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=C_SECONDARY))

fig.tight_layout()
save_fig(fig, 'fig_02_health_trend.png')


# --- 4b. Health by Implementation Status ---
print("\n--- Health by Implementation Status ---")
impl_health = latest_per_account.groupby('IMPLEMENTATION_STATUS_APPS').agg(
    n=('SALESFORCE_ACCOUNT_ID','count'),
    n_healthy=('HEALTHY_STATUS', lambda x: (x=='Healthy').sum()),
).reset_index()
impl_health['pct_healthy'] = (impl_health['n_healthy'] / impl_health['n'] * 100).round(1)
impl_health = impl_health.sort_values('pct_healthy', ascending=False)
for _, r in impl_health.iterrows():
    label = r['IMPLEMENTATION_STATUS_APPS'] if pd.notna(r['IMPLEMENTATION_STATUS_APPS']) else "NULL"
    print(f"  {label}: {r['pct_healthy']}% healthy ({r['n_healthy']}/{r['n']})")

# --- FIGURE 3: Health by Implementation ---
fig, ax = plt.subplots(figsize=(10, 5))
impl_h = impl_health.sort_values('pct_healthy', ascending=True)
colors_h = [C_PRIMARY if pct >= 50 else C_SECONDARY for pct in impl_h['pct_healthy']]
ax.barh(range(len(impl_h)), impl_h['pct_healthy'], color=colors_h, height=0.6, zorder=3)
ax.set_yticks(range(len(impl_h)))
labels = [s if pd.notna(s) else 'NULL / Untracked' for s in impl_h['IMPLEMENTATION_STATUS_APPS']]
ax.set_yticklabels(labels, fontsize=9)
ax.set_xlabel('% Accounts Healthy')
ax.set_title('Health Rate by Implementation Status', fontsize=13, fontweight='bold', pad=15)
ax.axvline(x=50, color=C_SECONDARY, linestyle='--', linewidth=1, alpha=0.5)

for i, (pct, n) in enumerate(zip(impl_h['pct_healthy'], impl_h['n'])):
    ax.annotate(f'{pct}% (n={n})', xy=(pct + 1, i), fontsize=8, va='center')

fig.tight_layout()
save_fig(fig, 'fig_03_health_by_impl.png')


# --- 4c. Renewal Pipeline (UFR) ---
print("\n--- Renewal Pipeline (UFR — deduplicated) ---")
# Dedup: one row per account per fiscal quarter (last month)
ufr_all = acc[acc['TOTAL_UFR'] > 0].copy()
ufr_deduped = ufr_all.sort_values('MONTH').groupby(['SALESFORCE_ACCOUNT_ID','FISCAL_QUARTER']).last().reset_index()

ufr_by_q = ufr_deduped.groupby('FISCAL_QUARTER').agg(
    total_ufr=('TOTAL_UFR','sum'),
    n_accounts=('SALESFORCE_ACCOUNT_ID','nunique'),
    n_healthy=('HEALTHY_STATUS', lambda x: (x=='Healthy').sum()),
    n_unhealthy=('HEALTHY_STATUS', lambda x: (x=='Unhealthy').sum()),
    total_apps_acv=('ACV_CS_APPS','sum'),
    total_acv=('TOTAL_ACTIVE_ACV','sum'),
).reset_index()
ufr_by_q['pct_healthy_accounts'] = (ufr_by_q['n_healthy'] / ufr_by_q['n_accounts'] * 100).round(1)

# UFR from healthy vs unhealthy
ufr_health = ufr_deduped.groupby(['FISCAL_QUARTER','HEALTHY_STATUS'])['TOTAL_UFR'].sum().unstack(fill_value=0)
if 'Healthy' in ufr_health.columns and 'Unhealthy' in ufr_health.columns:
    ufr_by_q = ufr_by_q.merge(
        ufr_health.rename(columns={'Healthy':'ufr_healthy','Unhealthy':'ufr_unhealthy'}).reset_index(),
        on='FISCAL_QUARTER'
    )
    ufr_by_q['pct_ufr_healthy'] = (ufr_by_q['ufr_healthy'] / ufr_by_q['total_ufr'] * 100).round(1)

print("\nFiscal Quarter | Total UFR | # Accounts | % Healthy Accounts | % UFR Healthy")
for _, r in ufr_by_q.iterrows():
    print(f"  {r['FISCAL_QUARTER']}: ${r['total_ufr']/1e6:.1f}M | "
          f"{int(r['n_accounts'])} accounts | "
          f"{r['pct_healthy_accounts']}% healthy | "
          f"{r.get('pct_ufr_healthy', 'N/A')}% UFR healthy")

total_ufr_year = ufr_by_q['total_ufr'].sum()
total_ufr_unhealthy = ufr_by_q['ufr_unhealthy'].sum() if 'ufr_unhealthy' in ufr_by_q.columns else 0
print(f"\n  Total UFR (all quarters): ${total_ufr_year/1e6:.1f}M")
print(f"  UFR from unhealthy accounts: ${total_ufr_unhealthy/1e6:.1f}M ({total_ufr_unhealthy/total_ufr_year*100:.1f}%)")

# --- FIGURE 9: Renewal Pipeline ---
fig, ax = plt.subplots(figsize=(10, 5))
quarters = ufr_by_q['FISCAL_QUARTER'].values
x = range(len(quarters))
q_labels = [f"FQ {q}" for q in quarters]

if 'ufr_healthy' in ufr_by_q.columns:
    ax.bar(x, ufr_by_q['ufr_healthy']/1e6, color=C_PRIMARY, label='UFR — Healthy', width=0.5, zorder=3)
    ax.bar(x, ufr_by_q['ufr_unhealthy']/1e6, bottom=ufr_by_q['ufr_healthy']/1e6,
           color=C_SECONDARY, label='UFR — Unhealthy', width=0.5, zorder=3)
else:
    ax.bar(x, ufr_by_q['total_ufr']/1e6, color=C_PRIMARY, width=0.5, zorder=3)

ax.set_xticks(x)
ax.set_xticklabels(q_labels, fontsize=8)
ax.set_ylabel('Total UFR ($M)')
ax.set_title('Renewal Pipeline by Fiscal Quarter (Deduplicated)', fontsize=13, fontweight='bold', pad=15)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'${x:.0f}M'))

for i, r in ufr_by_q.iterrows():
    ax.annotate(f'${r["total_ufr"]/1e6:.1f}M\n{int(r["n_accounts"])} accts\n{r["pct_healthy_accounts"]}% healthy',
                xy=(i, r['total_ufr']/1e6 + 0.3), fontsize=7, ha='center', va='bottom')

ax.legend(loc='upper left', framealpha=0.9, fontsize=8)
fig.tight_layout()
save_fig(fig, 'fig_09_renewal_pipeline.png')


# --- 4d. Health Formula Investigation ---
print("\n--- Health Formula Investigation ---")
# Health is defined as ACV/WAU ratio
dec_data_h = acc[acc['MONTH'] == acc['MONTH'].max()].copy()
dec_data_h = dec_data_h[dec_data_h['AVG_WAU_GLOBAL'] > 0].copy()
dec_data_h['acv_per_wau'] = dec_data_h['TOTAL_ACTIVE_ACV'] / dec_data_h['AVG_WAU_GLOBAL']

healthy = dec_data_h[dec_data_h['HEALTHY_STATUS'] == 'Healthy']['acv_per_wau']
unhealthy = dec_data_h[dec_data_h['HEALTHY_STATUS'] == 'Unhealthy']['acv_per_wau']

print(f"  Healthy accounts — Median ACV/WAU: ${healthy.median():,.0f}, Mean: ${healthy.mean():,.0f}")
print(f"  Unhealthy accounts — Median ACV/WAU: ${unhealthy.median():,.0f}, Mean: ${unhealthy.mean():,.0f}")
print(f"  → Lower ACV/WAU = Healthier (more users per dollar)")

# Find best threshold
best_acc, best_thresh = 0, 0
for t in range(10000, 200000, 1000):
    preds = ['Healthy' if x <= t else 'Unhealthy' for x in dec_data_h['acv_per_wau']]
    correct = sum(1 for p, a in zip(preds, dec_data_h['HEALTHY_STATUS']) if p == a)
    score = correct / len(dec_data_h)
    if score > best_acc:
        best_acc, best_thresh = score, t
print(f"  Best-fit threshold: ${best_thresh:,} (accuracy: {best_acc*100:.1f}%)")
print(f"  → Health metric uses TOTAL ACV and GLOBAL WAU — it conflates CS Digital with CS Apps usage")

# --- FIGURE 10: Health Formula ---
fig, ax = plt.subplots(figsize=(10, 5))
ax.scatter(dec_data_h[dec_data_h['HEALTHY_STATUS']=='Healthy']['acv_per_wau']/1e3,
           dec_data_h[dec_data_h['HEALTHY_STATUS']=='Healthy']['TOTAL_ACTIVE_ACV']/1e3,
           color=C_PRIMARY, alpha=0.5, s=40, label='Healthy', zorder=3)
ax.scatter(dec_data_h[dec_data_h['HEALTHY_STATUS']=='Unhealthy']['acv_per_wau']/1e3,
           dec_data_h[dec_data_h['HEALTHY_STATUS']=='Unhealthy']['TOTAL_ACTIVE_ACV']/1e3,
           color=C_SECONDARY, alpha=0.5, s=40, label='Unhealthy', zorder=3)
ax.axvline(x=best_thresh/1e3, color='black', linestyle='--', linewidth=1, alpha=0.7)
ax.annotate(f'Threshold: ${best_thresh/1e3:.0f}K\n({best_acc*100:.1f}% accuracy)',
            xy=(best_thresh/1e3, ax.get_ylim()[1]*0.9), fontsize=8, ha='left')
ax.set_xlabel('ACV / WAU ($K)')
ax.set_ylabel('Total Active ACV ($K)')
ax.set_title('Health Status vs. ACV/WAU Ratio', fontsize=13, fontweight='bold', pad=15)
ax.legend(loc='upper right', fontsize=8)
ax.set_xlim(0, 300)
fig.tight_layout()
save_fig(fig, 'fig_10_health_formula.png')


# ============================================================
# SECTION 5 — SUMMARY PRINT
# ============================================================
print("\n" + "="*60)
print("SUMMARY — KEY METRICS")
print("="*60)
print(f"""
PILLAR 1 — VALUE CREATION:
  CS Apps ACV: ${jan['apps_acv']/1e6:.2f}M → ${dec['apps_acv']/1e6:.2f}M (+{apps_growth:.0f}%)
  Total Relationship ACV: ${jan['total_acv']/1e6:.2f}M → ${dec['total_acv']/1e6:.2f}M (+{total_growth:.0f}%)
  Accounts: {int(jan['n_accounts'])} → {int(dec['n_accounts'])} (+{acct_growth:.0f}%)
  Penetration: {jan['penetration']:.1f}% → {dec['penetration']:.1f}% (+{dec['penetration']-jan['penetration']:.1f}pp)
  Mean Apps ACV/account: ${dec['mean_apps_acv']:,.0f}

PILLAR 2 — VALUE DELIVERY:
  Implementation: {n_lived} Lived ({n_lived/n_total*100:.0f}%), {n_implemented} stuck at Implemented
  Certification: {pct_zero_cert:.0f}% accounts have 0 certified Apps users
  Apps cert users/acct: {mean_cert_apps:.2f} vs Digital: {mean_cert_digital:.1f} ({mean_cert_digital/mean_cert_apps:.0f}x gap)
  Homepage share: {module_stats.iloc[0]['pct_sessions']}% of sessions (navigation, not value)

PILLAR 3 — VALUE PROTECTION:
  Health: {health_monthly.iloc[0]['pct_healthy']}% → {health_monthly.iloc[-1]['pct_healthy']}% (declining)
  Total UFR (year): ${total_ufr_year/1e6:.1f}M
  UFR at risk (unhealthy): ${total_ufr_unhealthy/1e6:.1f}M ({total_ufr_unhealthy/total_ufr_year*100:.1f}%)
  Q4 FQ 2023-11-01: ${ufr_by_q.iloc[-1]['total_ufr']/1e6:.1f}M across {int(ufr_by_q.iloc[-1]['n_accounts'])} accounts
  Health metric uses TOTAL ACV / GLOBAL WAU — conflates Digital usage
""")

print("✓ Analysis complete. All figures saved to ./figures/")
