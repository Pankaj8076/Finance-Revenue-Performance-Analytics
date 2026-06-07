# =============================================================
# FINANCE & REVENUE PERFORMANCE ANALYTICS
# Author  : Pankaj Hanumant Chavan
# Tools   : Python, Pandas, Matplotlib, Seaborn
# Domain  : Finance / Sales Operations
# =============================================================

# ---------------------------------------------------------------
# STEP 1: IMPORT LIBRARIES
# ---------------------------------------------------------------
# Pandas  → work with data (like Excel but in Python)
# Matplotlib → create charts and graphs
# Seaborn → beautiful charts (built on matplotlib)
# OS → work with files and folders

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import os
import warnings
warnings.filterwarnings('ignore')

# ---------------------------------------------------------------
# STEP 2: SETTINGS
# ---------------------------------------------------------------
# Create output folder to save all charts
os.makedirs('outputs', exist_ok=True)

# Set chart style
sns.set_theme(style="whitegrid")
plt.rcParams['figure.dpi'] = 150
plt.rcParams['font.family'] = 'DejaVu Sans'

# Colors we will use in charts
COLORS = {
    'blue'   : '#2196F3',
    'green'  : '#4CAF50',
    'orange' : '#FF9800',
    'red'    : '#F44336',
    'purple' : '#9C27B0',
    'teal'   : '#009688'
}

print("=" * 60)
print("   FINANCE & REVENUE PERFORMANCE ANALYTICS")
print("=" * 60)

# ---------------------------------------------------------------
# STEP 3: LOAD DATA
# ---------------------------------------------------------------
print("\n[1] Loading Data...")

df = pd.read_csv('data/sales_revenue_data.csv')

# Convert date column to proper date format
df['date'] = pd.to_datetime(df['date'])

# Extract month and quarter from date (very useful for analysis)
df['month']   = df['date'].dt.month
df['month_name'] = df['date'].dt.strftime('%b')   # Jan, Feb, etc.
df['quarter'] = df['date'].dt.quarter
df['quarter_name'] = 'Q' + df['quarter'].astype(str)

# Calculate Gross Profit and Gross Margin %
df['gross_profit']  = df['revenue'] - df['cogs']
df['gross_margin_pct'] = (df['gross_profit'] / df['revenue'] * 100).round(2)

print(f"   Total Records Loaded : {len(df)}")
print(f"   Date Range           : {df['date'].min().date()} to {df['date'].max().date()}")
print(f"   Total Revenue        : ₹{df['revenue'].sum():,.0f}")
print(f"   Total Gross Profit   : ₹{df['gross_profit'].sum():,.0f}")
print(f"   Avg Gross Margin     : {df['gross_margin_pct'].mean():.1f}%")

# ---------------------------------------------------------------
# STEP 4: KEY BUSINESS METRICS (KPI SUMMARY)
# ---------------------------------------------------------------
print("\n[2] Calculating KPIs...")

total_revenue      = df['revenue'].sum()
total_profit       = df['gross_profit'].sum()
total_orders       = df['order_id'].nunique()
avg_order_value    = df['revenue'].mean()
avg_margin         = df['gross_margin_pct'].mean()
top_region         = df.groupby('region')['revenue'].sum().idxmax()
top_rep            = df.groupby('sales_rep')['revenue'].sum().idxmax()
top_category       = df.groupby('product_category')['revenue'].sum().idxmax()

print(f"\n   ── KPI SUMMARY ──────────────────────────────")
print(f"   Total Revenue        : ₹{total_revenue:>15,.0f}")
print(f"   Total Gross Profit   : ₹{total_profit:>15,.0f}")
print(f"   Total Orders         : {total_orders:>16}")
print(f"   Avg Order Value      : ₹{avg_order_value:>15,.0f}")
print(f"   Avg Gross Margin     : {avg_margin:>15.1f}%")
print(f"   Top Region           : {top_region:>16}")
print(f"   Top Sales Rep        : {top_rep:>16}")
print(f"   Top Category         : {top_category:>16}")
print(f"   ─────────────────────────────────────────────")

# ---------------------------------------------------------------
# STEP 5: MONTHLY REVENUE TREND
# ---------------------------------------------------------------
print("\n[3] Building Monthly Revenue Trend...")

# Group revenue by month
month_order  = ['Jan','Feb','Mar','Apr','May','Jun',
                 'Jul','Aug','Sep','Oct','Nov','Dec']

monthly = (df.groupby('month_name')
             .agg(revenue=('revenue','sum'),
                  profit=('gross_profit','sum'),
                  orders=('order_id','count'))
             .reindex(month_order)
             .reset_index())

fig, ax1 = plt.subplots(figsize=(14, 6))

# Bar chart - Revenue
bars = ax1.bar(monthly['month_name'], monthly['revenue'],
               color=COLORS['blue'], alpha=0.85, label='Revenue', zorder=2)

# Line chart - Profit (secondary)
ax2 = ax1.twinx()
ax2.plot(monthly['month_name'], monthly['profit'],
         color=COLORS['green'], marker='o', linewidth=2.5,
         markersize=7, label='Gross Profit', zorder=3)

# Labels on bars
for bar in bars:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height + 5000,
             f'₹{height/100000:.1f}L', ha='center', va='bottom',
             fontsize=8, fontweight='bold', color='#1565C0')

ax1.set_xlabel('Month', fontsize=12)
ax1.set_ylabel('Revenue (₹)', fontsize=12, color=COLORS['blue'])
ax2.set_ylabel('Gross Profit (₹)', fontsize=12, color=COLORS['green'])
ax1.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'₹{x/100000:.0f}L'))
ax2.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'₹{x/100000:.0f}L'))

lines2, labels2 = ax2.get_legend_handles_labels()
lines1, labels1 = ax1.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=10)

plt.title('Monthly Revenue & Gross Profit Trend (2024)', fontsize=15, fontweight='bold', pad=15)
plt.tight_layout()
plt.savefig('outputs/01_monthly_revenue_trend.png', bbox_inches='tight')
plt.close()
print("   Saved → outputs/01_monthly_revenue_trend.png")

# ---------------------------------------------------------------
# STEP 6: REVENUE BY REGION
# ---------------------------------------------------------------
print("\n[4] Analysing Revenue by Region...")

region_df = (df.groupby('region')
               .agg(revenue=('revenue','sum'),
                    profit=('gross_profit','sum'),
                    orders=('order_id','count'))
               .sort_values('revenue', ascending=False)
               .reset_index())

region_df['margin_pct'] = (region_df['profit'] / region_df['revenue'] * 100).round(1)

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Left: Bar chart - Revenue by Region
region_colors = [COLORS['blue'], COLORS['green'], COLORS['orange'], COLORS['purple']]
bars = axes[0].bar(region_df['region'], region_df['revenue'],
                   color=region_colors, edgecolor='white', linewidth=1.5)

for bar, val in zip(bars, region_df['revenue']):
    axes[0].text(bar.get_x() + bar.get_width()/2,
                 bar.get_height() + 10000,
                 f'₹{val/100000:.1f}L', ha='center', fontsize=10, fontweight='bold')

axes[0].set_title('Revenue by Region', fontsize=13, fontweight='bold')
axes[0].set_ylabel('Revenue (₹)')
axes[0].yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'₹{x/100000:.0f}L'))

# Right: Pie chart - Revenue share
wedges, texts, autotexts = axes[1].pie(
    region_df['revenue'],
    labels=region_df['region'],
    colors=region_colors,
    autopct='%1.1f%%',
    startangle=90,
    wedgeprops=dict(edgecolor='white', linewidth=2))

for text in autotexts:
    text.set_fontsize(11)
    text.set_fontweight('bold')

axes[1].set_title('Revenue Share by Region', fontsize=13, fontweight='bold')

plt.suptitle('Regional Revenue Performance Analysis', fontsize=15, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('outputs/02_revenue_by_region.png', bbox_inches='tight')
plt.close()
print("   Saved → outputs/02_revenue_by_region.png")

# ---------------------------------------------------------------
# STEP 7: PRODUCT CATEGORY PERFORMANCE
# ---------------------------------------------------------------
print("\n[5] Analysing Product Category Performance...")

cat_df = (df.groupby('product_category')
            .agg(revenue=('revenue','sum'),
                 profit=('gross_profit','sum'),
                 orders=('order_id','count'))
            .sort_values('revenue', ascending=False)
            .reset_index())

cat_df['margin_pct'] = (cat_df['profit'] / cat_df['revenue'] * 100).round(1)

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Left: Horizontal bar - Revenue
cat_colors = [COLORS['blue'], COLORS['green'], COLORS['orange']]
h_bars = axes[0].barh(cat_df['product_category'], cat_df['revenue'],
                       color=cat_colors, edgecolor='white')

for bar, val in zip(h_bars, cat_df['revenue']):
    axes[0].text(bar.get_width() + 30000, bar.get_y() + bar.get_height()/2,
                 f'₹{val/100000:.1f}L', va='center', fontsize=11, fontweight='bold')

axes[0].set_title('Revenue by Product Category', fontsize=13, fontweight='bold')
axes[0].set_xlabel('Revenue (₹)')
axes[0].xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'₹{x/100000:.0f}L'))

# Right: Margin % comparison
axes[1].bar(cat_df['product_category'], cat_df['margin_pct'],
            color=cat_colors, edgecolor='white')

for i, (cat, margin) in enumerate(zip(cat_df['product_category'], cat_df['margin_pct'])):
    axes[1].text(i, margin + 0.5, f'{margin}%', ha='center', fontsize=11, fontweight='bold')

axes[1].set_title('Gross Margin % by Category', fontsize=13, fontweight='bold')
axes[1].set_ylabel('Gross Margin %')
axes[1].set_ylim(0, max(cat_df['margin_pct']) + 10)

plt.suptitle('Product Category Performance Dashboard', fontsize=15, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('outputs/03_category_performance.png', bbox_inches='tight')
plt.close()
print("   Saved → outputs/03_category_performance.png")

# ---------------------------------------------------------------
# STEP 8: SALES REP PERFORMANCE (LEADERBOARD)
# ---------------------------------------------------------------
print("\n[6] Building Sales Rep Leaderboard...")

rep_df = (df.groupby('sales_rep')
            .agg(revenue=('revenue','sum'),
                 profit=('gross_profit','sum'),
                 orders=('order_id','count'))
            .sort_values('revenue', ascending=True)
            .reset_index())

rep_df['margin_pct']   = (rep_df['profit'] / rep_df['revenue'] * 100).round(1)
rep_df['avg_deal_size'] = (rep_df['revenue'] / rep_df['orders']).round(0)

fig, ax = plt.subplots(figsize=(12, 7))

bar_colors = [COLORS['red'] if r < rep_df['revenue'].mean()
              else COLORS['green'] for r in rep_df['revenue']]

h_bars = ax.barh(rep_df['sales_rep'], rep_df['revenue'],
                  color=bar_colors, edgecolor='white', height=0.6)

for bar, val, margin in zip(h_bars, rep_df['revenue'], rep_df['margin_pct']):
    ax.text(bar.get_width() + 20000, bar.get_y() + bar.get_height()/2,
            f'₹{val/100000:.1f}L  |  {margin}% margin',
            va='center', fontsize=10, fontweight='bold')

# Average line
avg_rev = rep_df['revenue'].mean()
ax.axvline(x=avg_rev, color='navy', linestyle='--', linewidth=1.5, label=f'Avg: ₹{avg_rev/100000:.1f}L')

ax.set_title('Sales Representative Performance Leaderboard 2024',
             fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel('Total Revenue (₹)', fontsize=12)
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'₹{x/100000:.0f}L'))
ax.legend(fontsize=10)

# Color legend
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor=COLORS['green'], label='Above Average'),
                   Patch(facecolor=COLORS['red'],   label='Below Average')]
ax.legend(handles=legend_elements + ax.get_legend_handles_labels()[0],
          fontsize=10, loc='lower right')

plt.tight_layout()
plt.savefig('outputs/04_sales_rep_leaderboard.png', bbox_inches='tight')
plt.close()
print("   Saved → outputs/04_sales_rep_leaderboard.png")

# ---------------------------------------------------------------
# STEP 9: QUARTERLY REVENUE vs TARGET
# ---------------------------------------------------------------
print("\n[7] Quarterly Revenue vs Target Analysis...")

quarterly = (df.groupby('quarter_name')
               .agg(revenue=('revenue','sum'),
                    profit=('gross_profit','sum'))
               .reset_index())

# Define quarterly targets (business assumption)
targets = {'Q1': 2000000, 'Q2': 2500000, 'Q3': 3000000, 'Q4': 3500000}
quarterly['target']       = quarterly['quarter_name'].map(targets)
quarterly['achievement']  = (quarterly['revenue'] / quarterly['target'] * 100).round(1)
quarterly['gap']          = quarterly['revenue'] - quarterly['target']

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

x      = range(len(quarterly))
width  = 0.35

# Left: Grouped bar - Revenue vs Target
bars1 = axes[0].bar([i - width/2 for i in x], quarterly['revenue'],
                     width, label='Actual Revenue', color=COLORS['blue'], alpha=0.9)
bars2 = axes[0].bar([i + width/2 for i in x], quarterly['target'],
                     width, label='Target', color=COLORS['orange'], alpha=0.9)

for bar in bars1:
    axes[0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 20000,
                 f'₹{bar.get_height()/100000:.1f}L', ha='center', fontsize=9, fontweight='bold')

axes[0].set_xticks(list(x))
axes[0].set_xticklabels(quarterly['quarter_name'])
axes[0].set_title('Quarterly Revenue vs Target', fontsize=13, fontweight='bold')
axes[0].set_ylabel('Revenue (₹)')
axes[0].yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'₹{x/100000:.0f}L'))
axes[0].legend()

# Right: Achievement % gauge
ach_colors = [COLORS['green'] if a >= 100 else COLORS['red'] for a in quarterly['achievement']]
bars3 = axes[1].bar(quarterly['quarter_name'], quarterly['achievement'],
                     color=ach_colors, edgecolor='white')

axes[1].axhline(y=100, color='navy', linestyle='--', linewidth=2, label='100% Target')
for bar, val in zip(bars3, quarterly['achievement']):
    axes[1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                 f'{val}%', ha='center', fontsize=12, fontweight='bold')

axes[1].set_title('Quarterly Target Achievement %', fontsize=13, fontweight='bold')
axes[1].set_ylabel('Achievement %')
axes[1].legend()

plt.suptitle('Quarterly Performance Review', fontsize=15, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('outputs/05_quarterly_vs_target.png', bbox_inches='tight')
plt.close()
print("   Saved → outputs/05_quarterly_vs_target.png")

# ---------------------------------------------------------------
# STEP 10: CUSTOMER SEGMENT ANALYSIS
# ---------------------------------------------------------------
print("\n[8] Customer Segment Analysis...")

seg_df = (df.groupby('customer_segment')
            .agg(revenue=('revenue','sum'),
                 profit=('gross_profit','sum'),
                 orders=('order_id','count'))
            .sort_values('revenue', ascending=False)
            .reset_index())

seg_df['margin_pct']    = (seg_df['profit'] / seg_df['revenue'] * 100).round(1)
seg_df['avg_deal_size'] = (seg_df['revenue'] / seg_df['orders']).astype(int)

fig, axes = plt.subplots(1, 3, figsize=(16, 6))

seg_colors = [COLORS['blue'], COLORS['green'], COLORS['orange']]

# Revenue
axes[0].bar(seg_df['customer_segment'], seg_df['revenue'], color=seg_colors)
for i, val in enumerate(seg_df['revenue']):
    axes[0].text(i, val + 10000, f'₹{val/100000:.1f}L', ha='center', fontweight='bold')
axes[0].set_title('Revenue by Segment', fontweight='bold')
axes[0].yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'₹{x/100000:.0f}L'))

# Margin %
axes[1].bar(seg_df['customer_segment'], seg_df['margin_pct'], color=seg_colors)
for i, val in enumerate(seg_df['margin_pct']):
    axes[1].text(i, val + 0.3, f'{val}%', ha='center', fontweight='bold')
axes[1].set_title('Gross Margin % by Segment', fontweight='bold')
axes[1].set_ylabel('Margin %')

# Avg Deal Size
axes[2].bar(seg_df['customer_segment'], seg_df['avg_deal_size'], color=seg_colors)
for i, val in enumerate(seg_df['avg_deal_size']):
    axes[2].text(i, val + 1000, f'₹{val/1000:.0f}K', ha='center', fontweight='bold')
axes[2].set_title('Avg Deal Size by Segment', fontweight='bold')
axes[2].yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'₹{x/1000:.0f}K'))

plt.suptitle('Customer Segment Performance Analysis', fontsize=15, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('outputs/06_customer_segment_analysis.png', bbox_inches='tight')
plt.close()
print("   Saved → outputs/06_customer_segment_analysis.png")

# ---------------------------------------------------------------
# STEP 11: DISCOUNT IMPACT ANALYSIS
# ---------------------------------------------------------------
print("\n[9] Discount Impact Analysis...")

# Bucket discounts into groups
df['discount_group'] = pd.cut(df['discount_pct'],
                               bins=[-1, 0, 5, 10, 100],
                               labels=['No Discount', '1-5%', '6-10%', '>10%'])

disc_df = (df.groupby('discount_group', observed=True)
             .agg(revenue=('revenue','sum'),
                  margin=('gross_margin_pct','mean'),
                  orders=('order_id','count'))
             .reset_index())

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

disc_colors = [COLORS['green'], COLORS['blue'], COLORS['orange'], COLORS['red']]

axes[0].bar(disc_df['discount_group'], disc_df['revenue'], color=disc_colors)
for i, val in enumerate(disc_df['revenue']):
    axes[0].text(i, val + 10000, f'₹{val/100000:.1f}L', ha='center', fontweight='bold')
axes[0].set_title('Revenue by Discount Band', fontweight='bold')
axes[0].yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'₹{x/100000:.0f}L'))

axes[1].plot(disc_df['discount_group'], disc_df['margin'],
             marker='o', color=COLORS['red'], linewidth=2.5, markersize=10)
for i, val in enumerate(disc_df['margin']):
    axes[1].text(i, val + 0.5, f'{val:.1f}%', ha='center', fontweight='bold', fontsize=11)
axes[1].set_title('Margin % by Discount Band', fontweight='bold')
axes[1].set_ylabel('Avg Gross Margin %')

plt.suptitle('Discount Impact on Revenue & Margin', fontsize=15, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('outputs/07_discount_impact.png', bbox_inches='tight')
plt.close()
print("   Saved → outputs/07_discount_impact.png")

# ---------------------------------------------------------------
# STEP 12: FINAL BUSINESS INSIGHTS SUMMARY
# ---------------------------------------------------------------
print("\n" + "=" * 60)
print("   BUSINESS INSIGHTS SUMMARY")
print("=" * 60)

best_month   = monthly.loc[monthly['revenue'].idxmax(), 'month_name']
worst_month  = monthly.loc[monthly['revenue'].idxmin(), 'month_name']
best_quarter = quarterly.loc[quarterly['achievement'].idxmax(), 'quarter_name']
best_segment = seg_df.loc[seg_df['revenue'].idxmax(), 'customer_segment']
best_margin_cat = cat_df.loc[cat_df['margin_pct'].idxmax(), 'product_category']

print(f"""
   1. REVENUE PERFORMANCE
      • Annual Revenue         : ₹{total_revenue:,.0f}
      • Annual Gross Profit    : ₹{total_profit:,.0f}
      • Overall Margin         : {avg_margin:.1f}%

   2. BEST & WORST PERFORMERS
      • Best Month             : {best_month}
      • Worst Month            : {worst_month}
      • Best Quarter           : {best_quarter}
      • Top Sales Rep          : {top_rep}
      • Top Region             : {top_region}

   3. PRODUCT INSIGHTS
      • Highest Revenue        : {top_category}
      • Highest Margin         : {best_margin_cat}

   4. CUSTOMER INSIGHTS
      • Best Segment (Revenue) : {best_segment}

   5. KEY RECOMMENDATIONS
      • Focus on {worst_month} to improve revenue in slow months
      • {top_rep} strategies should be shared with team
      • {top_region} region model to be replicated elsewhere
      • High discounts (>10%) significantly reduce margins
        → Review discount policy for SMB segment
""")

print("=" * 60)
print("   ANALYSIS COMPLETE! All charts saved in /outputs/")
print("=" * 60)
print("\n   Charts Generated:")
print("   01_monthly_revenue_trend.png")
print("   02_revenue_by_region.png")
print("   03_category_performance.png")
print("   04_sales_rep_leaderboard.png")
print("   05_quarterly_vs_target.png")
print("   06_customer_segment_analysis.png")
print("   07_discount_impact.png")
