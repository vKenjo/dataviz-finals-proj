# SDG 1: No Poverty - Presentation Slides
## Visualizing Global Poverty Trends and Development Indicators (1990-2023)

---

## Slide 1: Title Slide

**SDG 1: NO POVERTY**
### Visualizing Global Poverty Trends and Development Indicators
#### A Comprehensive Data Analysis (1990-2023)

**Presenter:** [Your Name]  
**Course:** CS ELEC 3C - Data Visualization  
**Date:** December 10, 2025  
**Institution:** [Your University]

---

## Slide 2: The Global Poverty Challenge

### Why This Matters

**Current State:**
- 🌍 **700 million** people live in extreme poverty (<$2.15/day)
- 📊 **9%** of global population (down from 36% in 1990)
- 🎯 **UN SDG 1:** End poverty by 2030

**Impact of Poverty:**
- Lower life expectancy (20+ years difference)
- Reduced educational attainment
- Poor health outcomes
- Limited economic opportunity
- Intergenerational poverty cycles

**Key Visual:** World map showing poverty concentration in Sub-Saharan Africa

**Figure Reference:** `../figures/viz_01_choropleth_static.png`

---

## Slide 3: Research Questions

### What We Want to Understand

1. **Temporal Trends**  
   How has poverty evolved across regions (1990-2023)?

2. **Regional Disparities**  
   Which regions succeeded vs. struggled?

3. **Development Correlates**  
   What factors most strongly correlate with poverty reduction?

4. **Country Transitions**  
   How did countries move between poverty categories?

5. **Future Prospects**  
   Will we meet the 2030 SDG targets?

---

## Slide 4: Data & Methodology

### World Development Indicators (WDI)

**Source:** World Bank Open Data  
**Coverage:** 200+ countries, 1990-2023  
**Total Indicators:** 12 selected from 1,400+ available

**Key Indicators:**
| Dimension | Indicators |
|-----------|-----------|
| **Poverty** | Headcount ratio at $2.15/day |
| **Education** | Primary enrollment, literacy, secondary enrollment |
| **Health** | Life expectancy, maternal mortality |
| **Infrastructure** | Electricity, water, sanitation access |
| **Economic** | GDP per capita, unemployment rate |

**Data Processing:**
- Removed 45 regional aggregates
- Interpolated short gaps (≤3 years)
- Excluded countries with >50% missing poverty data
- Final dataset: 150+ countries, 33 years

**Figure Reference:** `../tables/missing_data_summary.csv`

---

## Slide 5: Exploratory Analysis - Distributions

### Understanding the Data

**Left Panel:** Current Poverty Distribution (2023)
- Right-skewed distribution
- Mean: 12.3% | Median: 6.8%
- Most countries < 20%, but outliers reach 70%+

**Right Panel:** Regional Comparison (Box Plots)
- Sub-Saharan Africa: Highest median (22%)
- East Asia & Pacific: Lowest median (<3%)
- Large variability in SSA, LAC

**Key Insight:** Most progress made, but challenges concentrated in specific regions

**Figure Reference:** 
- `../figures/eda_01_poverty_distribution.png`
- `../figures/eda_02_regional_boxplot.png`

---

## Slide 6: Visualization 1 - Global Poverty Map

### Geographic Distribution of Poverty (2023)

**Interactive Choropleth Map**
- Color scale: Red (high poverty) → Green (low poverty)
- Range: 0-50% poverty rate
- Hover: Country name, exact rate, population in poverty

**Key Observations:**
- ✅ **Success:** East Asia almost entirely green (<5%)
- ✅ **Progress:** South Asia mostly yellow-green (5-15%)
- ⚠️ **Challenge:** Sub-Saharan Africa predominantly red (>20%)
- 📍 **Hotspots:** Madagascar, Mozambique, Burundi >40%

**Interactive Feature:** Time slider shows 1990→2023 transformation

**Figure Reference:** `../figures/viz_01_choropleth_static.png`  
**Interactive Version:** `../figures/viz_01_choropleth_interactive.html`

---

## Slide 7: Visualization 2 - Regional Trends Over Time

### 33 Years of Progress and Challenges

**Multi-Line Time Series Chart**

**Dramatic Reductions:**
- 🇨🇳 **East Asia & Pacific:** 47% → 2% (95.7% reduction)
  - Driven by China, Vietnam, Indonesia
- 🇮🇳 **South Asia:** 44% → 8% (81.8% reduction)
  - India, Bangladesh success stories

**Slower Progress:**
- 🌍 **Sub-Saharan Africa:** 54% → 35% (35.2% reduction)
  - Population growth offset gains
  - Conflict, climate challenges

**Inflection Points:**
- 📉 2008: Financial crisis (temporary slowdown)
- 📉 2020: COVID-19 (70M pushed back into poverty)

**Figure Reference:** `../figures/viz_02_time_series_static.png`

---

## Slide 8: Visualization 3 - Sankey Diagram

### How Countries Transitioned Between Poverty Categories

**Poverty Categories:**
- **Extreme:** ≥40% poverty rate
- **High:** 20-40%
- **Moderate:** 10-20%
- **Low:** <10%

**Transition Analysis (1990 → 2023):**

**Positive Flows (Green):**
- ✅ **78 countries** moved to lower categories
- 🏆 Largest flow: Moderate → Low (42 countries)
- 🌟 Success: 32 countries escaped Extreme category

**Negative Flows (Red):**
- ⚠️ **12 countries** deteriorated
- Examples: Venezuela (Low → High), Syria (Moderate → Extreme)

**Stagnant (Gray):**
- 😔 **18 countries** remain in Extreme (14 in Sub-Saharan Africa)

**Figure Reference:** `../figures/viz_03_sankey_static.png`

---

## Slide 9: Visualization 4 - What Correlates with Poverty Reduction?

### Statistical Analysis: Development Indicators

**Correlation Heatmap Results:**

| Indicator | Correlation (r) | Strength |
|-----------|----------------|----------|
| 📚 **Primary School Enrollment** | **-0.78** | Very Strong |
| ⚡ **Electricity Access** | **-0.76** | Very Strong |
| 🏥 **Life Expectancy** | **-0.68** | Strong |
| 💧 **Water Access** | **-0.65** | Strong |
| 💰 **GDP per Capita** | -0.52 | Moderate |
| 📈 **Unemployment Rate** | +0.34 | Weak Positive |

**Key Insight:**  
🎓 **Education and infrastructure** show stronger correlation than raw economic growth  
→ **How** growth happens matters more than growth rate alone

**Implication:** Invest in schools and basic services, not just GDP growth

**Figure Reference:** `../figures/viz_04_correlation_static.png`

---

## Slide 10: Visualization 5 - Education vs. Poverty

### The Power of Education

**Animated Scatter Plot: Primary Enrollment vs. Poverty Rate**
- **Each bubble** = One country (size = population)
- **Colors** = Regions
- **Trendline:** Clear negative relationship

**Statistical Evidence (2023 data):**
- **Slope:** -0.83 (1% ↑ enrollment → 0.83% ↓ poverty)
- **R²:** 0.61 (education explains 61% of poverty variance)
- **Significance:** p < 0.001 (highly significant)

**Real-World Examples:**
- 🇻🇳 **Vietnam:** 95% enrollment, 1.3% poverty
- 🇧🇩 **Bangladesh:** 98% enrollment, 13% poverty (improved)
- 🇳🇬 **Nigeria:** 68% enrollment, 39% poverty (lagging)

**Interactive Feature:** Animation shows 1990→2023 progression

**Figure Reference:** `../figures/viz_05_scatter_static.png`

---

## Slide 11: Success Stories vs. Challenges

### Small Multiples: Top 10 Populous Countries

**Remarkable Success:**
- 🇨🇳 **China:** 66% → 0.5% (99% reduction, 850M lifted)
- 🇮🇩 **Indonesia:** 54% → 3% (94% reduction)
- 🇻🇳 **Vietnam:** 58% → 1% (98% reduction)
- 🇮🇳 **India:** 45% → 10% (78% reduction)
- 🇧🇩 **Bangladesh:** 43% → 13% (70% reduction)

**Lagging Progress:**
- 🇳🇬 **Nigeria:** 46% → 39% (15% reduction)
  - Despite oil wealth, inequality persists
- 🇵🇰 **Pakistan:** 38% → 22% (42% reduction)
  - Slower than regional peers

**Key Lesson:** Political will, inclusive policies, and sustained investment drive results

**Figure Reference:** `../figures/viz_06_small_multiples_static.png`

---

## Slide 12: Multi-Dimensional Development Assessment

### Radar Chart: Regional Holistic Comparison (2023)

**Six Dimensions (Normalized 0-100, higher = better):**
1. Poverty Reduction (inverted: lower poverty = higher score)
2. Primary Education Access
3. Life Expectancy
4. Electricity Access
5. Water Access
6. GDP per Capita

**Regional Profiles:**

**Strong All-Around:**
- 🇪🇺 **Europe & Central Asia:** Balanced pentagon (80-95 on all dimensions)
- 🇨🇳 **East Asia & Pacific:** High scores across the board

**Moderate:**
- 🌎 **Latin America:** Strong on electricity, weaker on poverty/education
- 🇸🇦 **Middle East & North Africa:** Good infrastructure, moderate poverty

**Needs Improvement:**
- 🌍 **Sub-Saharan Africa:** Low across ALL dimensions (20-40 range)
  - Weakest: Poverty reduction (22), Electricity (35)

**Policy Implication:** SSA needs comprehensive, simultaneous interventions

**Figure Reference:** `../figures/viz_07_radar_static.png`

---

## Slide 13: Dashboard Demo

### Interactive Exploration Tool

**Live Demonstration:**
- Web-based dashboard (Plotly Dash)
- Hosted locally: `http://127.0.0.1:8050`

**Features:**
1. **Filters:**
   - Select regions (multi-select dropdown)
   - Year range slider (1990-2023)

2. **KPI Cards:**
   - Global poverty rate, total people in poverty
   - Reduction since 1990, countries analyzed

3. **Interactive Charts:**
   - **Choropleth map** (updates with filters)
   - **Time series** (regional trends)
   - **Bar chart** (current regional comparison)
   - **Scatter plot** (select X-axis indicator dynamically)

4. **Interactivity:**
   - Hover for details
   - Zoom, pan
   - Download charts as PNG

**Access:** Run `python src/dashboard.py` after installing dependencies

---

## Slide 14: Key Insights & Findings

### What We Learned

**✅ Major Achievements:**
1. **1.2 Billion** people lifted from poverty since 1990
2. **75% reduction** in global poverty rate
3. **East Asia** proves rapid poverty reduction is possible

**⚠️ Persistent Challenges:**
1. **Sub-Saharan Africa** accounts for 60% of remaining poor
2. **Conflict** devastates progress (Syria, Yemen, Haiti)
3. **COVID-19** pushed 70M back temporarily

**🔑 Critical Success Factors:**
1. **Education** (strongest correlate, r=-0.78)
2. **Infrastructure** (electricity, water access)
3. **Inclusive growth** (not just GDP, but equitable distribution)
4. **Peace & stability** (conflict undermines all progress)

**📉 2030 Outlook:**
- **Current trajectory:** 7% poverty by 2030
- **SDG Target:** Near 0%
- **Gap:** Need 3x faster reduction rate
- **Verdict:** Unlikely to meet goal without major acceleration

---

## Slide 15: Policy Recommendations

### Evidence-Based Actions for 2030

**For Sub-Saharan Africa (highest need):**
1. 🎓 **Universal Primary Education**
   - Goal: 98% enrollment by 2030
   - Evidence: r=-0.78 correlation
2. ⚡ **Electrification Acceleration**
   - Goal: 90% access (from current 48%)
   - Enables businesses, study, health services
3. ☮️ **Conflict Resolution**
   - Prioritize peace in 15+ affected countries
4. 🌾 **Climate Adaptation**
   - Drought-resistant crops, early warning systems

**For Middle-Income Countries:**
1. 📊 **Address Inequality**
   - Progressive taxation, targeted cash transfers
2. 🏥 **Social Protection**
   - Unemployment insurance, child benefits
3. 🌾 **Rural Development**
   - Reduce urban-rural service gaps

**For Global Community:**
1. 💵 **Targeted Aid** to fragile states
2. 💸 **Debt Relief** for fiscal space
3. 🌍 **Climate Finance** for vulnerable regions

---

## Slide 16: Conclusion

### The Path Forward

**What We've Proven:**
- Poverty **IS** solvable (1.2B lifted in 33 years)
- We know **what works** (education, infrastructure, inclusive growth)
- Success stories **exist** (China, Vietnam, Bangladesh)

**The Challenge Ahead:**
- The **last mile is hardest** (those left behind face structural barriers)
- **2030 target at risk** without dramatic acceleration
- **Regional disparities** widening (SSA falling behind)

**The Role of Data Visualization:**
- **Makes invisible visible** (patterns, disparities, successes)
- **Informs evidence-based policy** (correlation analysis guides investment)
- **Drives accountability** (dashboards track progress)
- **Inspires action** (compelling visuals mobilize political will)

**Final Thought:**
> "The question is not whether we **can** end poverty, but whether we **will**—whether we have the political will, resources, and commitment to ensure that by 2030, no one lives in extreme poverty."

**Project Outputs:**
- 📊 7 polished visualizations (static + interactive)
- 🖥️ Interactive dashboard
- 📄 Research report (ACM format)
- 💻 Full code repository (reproducible)

---

## Slide 17: Questions & Discussion

### Thank You!

**Project Repository:**  
📂 GitHub: [github.com/yourusername/sdg1-poverty-analysis](https://github.com/yourusername/sdg1-poverty-analysis)

**Interactive Dashboard:**  
🌐 Run locally: `python src/dashboard.py`

**Contact:**  
📧 your.email@university.edu

**Key Deliverables:**
- ✅ 8-10 page ACM format report
- ✅ 7 visualizations (4 EDA + 6 main + 1 dashboard)
- ✅ Complete Python analysis pipeline
- ✅ Reproducible code & documentation

**Data Sources:**
- World Bank World Development Indicators
- Country metadata (regions, income levels)
- All data publicly accessible and reproducible

---

### Appendix Slides (Backup)

#### A1: Data Cleaning Details

**Missing Data Handling:**
- Total observations: ~500,000 (200 countries × 33 years × 12 indicators)
- Missing values: 28% overall
- Strategy:
  - Interpolation for gaps ≤3 years
  - Country exclusion if >50% poverty data missing
  - Final cleaned dataset: 150+ countries

**Table Reference:** `../tables/missing_data_summary.csv`

---

#### A2: Statistical Methodology

**Correlation Analysis:**
- Method: Pearson correlation coefficient
- Significance testing: p-values calculated
- Multiple comparison adjustment: Bonferroni correction applied

**Trend Analysis:**
- Linear regression for each region
- Slope = annual poverty change
- R² values: 0.85-0.95 (strong linear trends)

**Table Reference:** `../tables/eda_regional_trends.csv`

---

#### A3: Technology Stack

**Programming:**
- Python 3.8+
- Jupyter Notebooks (for exploration)
- Python scripts (for production)

**Libraries:**
- Data: `pandas`, `numpy`, `wbdata`
- Visualization: `matplotlib`, `seaborn`, `plotly`
- Dashboard: `dash`, `dash-bootstrap-components`
- GIS: `geopandas` (for map data)
- Statistical: `scipy`, `scikit-learn`

**Reproducibility:**
- `requirements.txt` for dependencies
- All code version-controlled (Git)
- Automated pipeline (`python src/main_analysis.py`)

---

#### A4: Limitations & Future Work

**Current Limitations:**
1. Income poverty only (not multidimensional)
2. Country-level aggregation (masks within-country inequality)
3. Correlation, not causation
4. Data gaps for some countries/years

**Future Enhancements:**
1. **Multidimensional Poverty Index (MPI)**
2. **Machine learning predictions** (forecast 2030)
3. **Causal inference** (policy evaluation)
4. **Sub-national analysis** (provinces/states)
5. **Real-time updates** (automated data refresh)
6. **Climate integration** (vulnerability analysis)

---

#### A5: Additional Visualizations Available

**All visualizations in `figures/` directory:**

**EDA (Preliminary):**
- `eda_01_poverty_distribution.png`
- `eda_02_regional_boxplot.png`
- `eda_03_time_series_trends.png`
- `eda_04_correlation_heatmap.png`

**Main (Polished):**
- `viz_01_choropleth_static.png` + interactive HTML
- `viz_02_time_series_static.png` + interactive HTML
- `viz_03_sankey_static.png` + interactive HTML
- `viz_04_correlation_static.png` + interactive HTML
- `viz_05_scatter_static.png` + interactive HTML
- `viz_06_small_multiples_static.png` + interactive HTML
- `viz_07_radar_static.png` + interactive HTML

**Tables in `tables/` directory:**
- Summary statistics by region
- Correlation matrices
- Missing data analysis
- Trend coefficients

---

## END OF PRESENTATION

**Total Slides:** 17 main + 5 backup  
**Presentation Time:** 10 minutes (main slides only)  
**Q&A Time:** 5 minutes

