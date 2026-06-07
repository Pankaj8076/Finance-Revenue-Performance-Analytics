# 📊 Finance & Revenue Performance Analytics
### Python | Pandas | Matplotlib | Seaborn

---

## 🎯 Project Overview

This project performs end-to-end **Finance & Revenue Analytics** on a B2B sales dataset using Python. It simulates real-world financial analysis tasks performed by a Revenue/Finance Operations Analyst — including KPI reporting, trend analysis, sales performance tracking, and business insights generation.

**Business Context:** Analyzing 120 sales transactions across 4 regions, 6 sales reps, 3 product categories, and 3 customer segments for FY 2024.

---

## 📁 Project Structure

```
Finance-Revenue-Analytics/
│
├── data/
│   └── sales_revenue_data.csv      ← Dataset (120 records, FY 2024)
│
├── outputs/
│   ├── 01_monthly_revenue_trend.png
│   ├── 02_revenue_by_region.png
│   ├── 03_category_performance.png
│   ├── 04_sales_rep_leaderboard.png
│   ├── 05_quarterly_vs_target.png
│   ├── 06_customer_segment_analysis.png
│   └── 07_discount_impact.png
│
├── analysis.py                     ← Main Python script
└── README.md
```

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| **Python 3.x** | Core programming |
| **Pandas** | Data loading, cleaning, transformation |
| **Matplotlib** | Charts and visualizations |
| **Seaborn** | Enhanced chart styling |

---

## 📊 Dataset Details

| Column | Description |
|--------|-------------|
| `order_id` | Unique order identifier |
| `date` | Order date |
| `region` | Sales region (North/South/East/West) |
| `product_category` | Software / Hardware / Services |
| `product_name` | Specific product |
| `sales_rep` | Sales representative name |
| `quantity` | Units ordered |
| `unit_price` | Price per unit (₹) |
| `revenue` | Total revenue (₹) |
| `discount_pct` | Discount % applied |
| `cogs` | Cost of Goods Sold (₹) |
| `customer_segment` | Enterprise / Mid-Market / SMB |

---

## 📈 Analysis Performed

### 1. KPI Summary Dashboard
- Total Revenue, Gross Profit, Gross Margin %
- Average Order Value, Total Orders
- Top Region, Top Sales Rep, Top Category

### 2. Monthly Revenue Trend
- Month-over-month revenue performance
- Revenue vs Gross Profit comparison
- Identifies seasonality and growth trends

### 3. Regional Revenue Analysis
- Revenue comparison across 4 regions
- Market share pie chart
- Regional performance ranking

### 4. Product Category Performance
- Revenue by category (Software, Hardware, Services)
- Gross Margin % by category
- Identifies most profitable vs highest revenue categories

### 5. Sales Rep Leaderboard
- Revenue ranking for all 6 sales reps
- Margin % per rep
- Above/Below average performance segmentation

### 6. Quarterly Revenue vs Target
- Actual vs Target comparison (Q1-Q4)
- Achievement % tracking
- Gap analysis

### 7. Customer Segment Analysis
- Revenue by Enterprise/Mid-Market/SMB
- Margin % and Average Deal Size per segment
- Identifies highest value customer segment

### 8. Discount Impact Analysis
- Revenue and margin by discount band
- Shows how discounts affect profitability
- Business recommendation for discount policy

---

## 🔍 Key Business Insights

```
1. REVENUE PERFORMANCE
   • Annual Revenue    : ₹2.4 Crore
   • Gross Profit      : ₹1.2 Crore
   • Overall Margin    : 50%

2. BEST PERFORMERS
   • Best Month        : December (year-end push)
   • Worst Month       : January (post-holiday slowdown)
   • Top Quarter       : Q4 (highest target achievement)
   • Top Sales Rep     : Rahul Sharma
   • Top Region        : North

3. PRODUCT INSIGHTS
   • Highest Revenue   : Hardware
   • Highest Margin    : Services (60%+ margin)

4. CUSTOMER INSIGHTS
   • Best Segment      : Enterprise (highest revenue + margin)

5. RECOMMENDATIONS
   • Services category should be upsold → highest margins
   • Discount > 10% significantly hurts profitability
   • Rahul Sharma's sales strategy to be shared with team
   • North region playbook to be replicated in other regions
   • January revenue dip → needs promotional campaigns
```

---

## ▶️ How to Run

```bash
# 1. Clone repository
git clone https://github.com/Pankaj8076/Finance-Revenue-Analytics.git
cd Finance-Revenue-Analytics

# 2. Install required libraries
pip install pandas matplotlib seaborn

# 3. Run the analysis
python analysis.py

# 4. View charts in outputs/ folder
```

---

## 📸 Sample Output Charts

> Charts are generated in the `outputs/` folder after running `analysis.py`

| Chart | Description |
|-------|-------------|
| Monthly Revenue Trend | Bar + Line combo chart |
| Regional Analysis | Bar + Pie chart |
| Category Performance | Revenue + Margin comparison |
| Sales Rep Leaderboard | Horizontal bar with above/below avg |
| Quarterly vs Target | Grouped bar + Achievement % |
| Customer Segment | 3-panel segment breakdown |
| Discount Impact | Revenue + Margin by discount band |

---
## 📸 Project Visualizations

### Monthly Revenue Trend
![Monthly Revenue](outputs/01_monthly_revenue_trend.png)

### Revenue by Region  
![Revenue by Region](outputs/02_revenue_by_region.png)

### Sales Rep Leaderboard
![Sales Rep](outputs/04_sales_rep_leaderboard.png)

### Quarterly vs Target
![Quarterly](outputs/05_quarterly_vs_target.png)

## 🚀 Skills Demonstrated

- ✅ Data loading and exploration with Pandas
- ✅ Feature engineering (gross profit, margin %, date features)
- ✅ Groupby aggregations and multi-metric analysis
- ✅ Professional data visualization (7 charts)
- ✅ KPI calculation and business reporting
- ✅ Business insight generation and recommendations
- ✅ Finance domain knowledge (revenue, COGS, margin analysis)

---

## 👤 Author

**Pankaj Hanumant Chavan**
- 📧 pankajhchavan8076@gmail.com
- 💼 [LinkedIn](https://linkedin.com/in/pankaj-h-chavan-8076)
- 🐙 [GitHub](https://github.com/Pankaj8076)

---

## 📌 Related Projects

- [Retail Banking Customer Profitability Analysis](https://github.com/Pankaj8076/Retail-Banking-Customer-Profitability-Risk-Analysis)
- [Telecom Billing & Usage Analytics](https://github.com/Pankaj8076/Telecom-Billing-Usage-Analytics)
- [Finance Operations & Risk Analytics](https://github.com/Pankaj8076/Finance-Operations-Risk-Analytics-project)
