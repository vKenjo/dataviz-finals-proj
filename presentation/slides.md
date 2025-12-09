# Visualizing Global Poverty Trends

## An Analysis of SDG 1 Progress with Focus on the Philippines and ASEAN

**CS ELEC 3C - Data Visualization Project**  
December 10, 2025

---

## Slide 1: Title Slide

# Visualizing Global Poverty Trends

## Addressing UN SDG 1: No Poverty

### Focus: Philippines and ASEAN Region

**World Development Indicators Analysis (1960-2024)**

CS ELEC 3C Data Visualization Project  
December 10, 2025

---

## Slide 2: The Global Poverty Challenge

### UN SDG 1: End Poverty in All Forms by 2030

**Current Status (2023):**

- ~700 million people live in extreme poverty
- ~9% of global population
- Living on <$2.15/day (2017 PPP)

**Historic Achievement:**

- **1990:** 36% in extreme poverty
- **2023:** 9% in extreme poverty
- **Result:** Over 1.2 billion people lifted from poverty

**But progress is uneven...**

---

## Slide 3: Research Questions

### Three-Tier Analysis Framework

**🌍 GLOBAL LEVEL**

- How has extreme poverty evolved globally (1981-2024)?
- What are geographic patterns and regional disparities?
- Which development indicators correlate with poverty reduction?

**🌏 ASEAN REGIONAL**

- How does Philippines compare to other ASEAN countries?
- Which ASEAN countries have been most successful?
- Where does ASEAN stand relative to global trends?

**🇵🇭 PHILIPPINES SPECIFIC**

- What is Philippines' current poverty status?
- How does it perform across development dimensions?
- What factors show strongest correlation with poverty?

---

## Slide 4: Dataset Overview

### World Development Indicators (WDI)

**Source:** World Bank Open Data

**Coverage:**

- **217 countries** and territories
- **1960-2024** (65 years)
- **Over 1,000 indicators** (education, health, economy, infrastructure)

**Our Analysis Uses:**

- Poverty headcount at $2.15/day (%)
- GDP per capita, Life expectancy
- Electricity access, School enrollment
- Population demographics

**Data Reality:**

- 169 countries have poverty data
- 48 countries lack measurements
- Latest year varies: 2018-2024

---

## Slide 5: Methodology - Data Preparation

### From Raw Data to Insights

**1. Data Import & Filtering**

- Selected 13 key development indicators
- Filtered 217 countries across 65 years
- Focused on poverty headcount as primary metric

**2. Handling Missing Data**

- Documented gaps (48 countries without poverty data)
- Used "latest available year" approach
- ASEAN: Only 7 of 11 countries have data

**3. Regional Categorization**

- ASEAN countries (11 members)
- Developed nations comparison
- Global benchmarking

**4. Analysis Techniques**

- Correlation analysis (Pearson r)
- Time-series trend analysis
- Multi-dimensional comparison

---

## Slide 6: Methodology - Visualizations Created

### 5 Publication-Quality Visualizations

**1. Interactive Choropleth Map**

- Global poverty distribution (169 countries)
- Latest available year per country

**2. Time-Series Line Chart**

- ASEAN poverty trends over time
- Philippines highlighted vs. regional average

**3. Correlation Heatmap**

- Poverty vs. development indicators
- Statistical significance testing

**4. Radar Chart**

- Philippines vs. ASEAN multi-dimensional profile
- 6 development dimensions normalized

**5. Interactive Dashboard**

- Philippines deep-dive: poverty, GDP, education, infrastructure
- Temporal evolution across 4 panels

---

## Slide 7: Exploratory Data Analysis (EDA)

### Understanding the Data Landscape

**Distribution Analysis (4 Histograms):**

- Poverty, GDP, Life Expectancy, Electricity Access
- Global vs. ASEAN vs. Philippines positioning

**Key Observations:**

- High global variance (0% to 85%+ poverty)
- Philippines near ASEAN median
- Infrastructure shows inverse relationship with poverty

**Temporal Heatmap:**

- 15 countries (ASEAN prioritized)
- Poverty evolution 1981-2024
- Clear reduction patterns visible

**Regional Boxplots:**

- Global median: 2.7%
- ASEAN median: 5.4%
- Philippines: 5.3%

---

## Slide 8: Global Poverty Landscape 🌍

### Visualization 1: Choropleth Map Results

**Data Coverage:**

- ✅ 169 countries with poverty data
- ❌ 48 countries without measurements

**Global Statistics (Latest Available Year):**

- **Median poverty:** 2.70%
- **Mean poverty:** 14.03%
- **Range:** 0% (developed nations) to 85%+ (Sub-Saharan Africa)

**Geographic Patterns:**

- 🔴 **Sub-Saharan Africa:** Highest concentrations (>40%)
- 🟢 **East Asia:** Success stories (China, Vietnam <1%)
- 🟡 **Latin America:** Moderate (5-15%)
- 🟢 **Europe & North America:** Near-zero (<2%)

**Historical Trend:**

- **1981:** 17.22% average → **2024:** 4.23% average
- **Reduction:** 12.99 percentage points over 43 years

---

## Slide 9: ASEAN Regional Analysis 🌏

### Visualization 2: ASEAN Poverty Trends

**ASEAN Poverty Rates (Latest Available):**

| Country        | Poverty Rate |
| -------------- | ------------ |
| 🟢 Malaysia    | 0.0%         |
| 🟢 Thailand    | 0.0%         |
| 🟡 Philippines | **5.3%**     |
| 🟡 Indonesia   | 5.4%         |
| 🟠 Myanmar     | 10.3%        |
| 🟠 Lao PDR     | 15.7%        |
| 🔴 Timor-Leste | 43.9%        |

**Missing Data:** Cambodia, Vietnam, Singapore, Brunei

**Key Findings:**

- **ASEAN median:** 5.4% (higher than global 2.7%)
- **Success stories:** Malaysia, Thailand achieved 0%
- **Philippines:** Slightly below ASEAN median, above global
- **Wide disparity:** 0% to 43.9% range

---

## Slide 10: What Drives Poverty Reduction? 📊

### Visualization 3: Correlation Analysis

**Actual Correlation Coefficients (Pearson r):**

| Development Indicator     | Correlation with Poverty |
| ------------------------- | ------------------------ |
| ⚡ **Electricity Access** | **r = -0.847\***         |
| 🏥 **Life Expectancy**    | **r = -0.786\***         |
| 💰 **GDP per Capita**     | r = -0.397\*\*           |

**\*p < 0.001, **p < 0.01\*

### 🔑 Critical Insights

**1. Infrastructure >> Income**

- Electricity access (r=-0.847) correlates **2x stronger** than GDP (r=-0.397)
- Access matters more than income growth alone

**2. Health is Wealth**

- Life expectancy (r=-0.786) shows very strong link
- Healthy populations escape poverty faster

**3. Multi-Dimensional Approach Required**

- No single factor sufficient
- Simultaneous progress needed: infrastructure + health + economy

---

## Slide 11: Philippines in Context 🇵🇭

### Visualization 4: Multi-Dimensional Comparison

**Philippines vs. ASEAN Average (Radar Chart)**

**Current Status (2023):**

- **Poverty Rate:** 5.3%
- **Position:** Slightly below ASEAN median (5.4%)
- **But:** Above global median (2.7%)

**Multi-Dimensional Profile:**

- ✅ **Comparable** across most indicators
- ✅ **Strength:** Infrastructure/electricity access
- ➡️ **Balanced:** Education enrollment similar to ASEAN
- ➡️ **Neither leader nor laggard** in region

**Key Takeaway:**
Philippines has foundation for success—balanced development profile with clear path to Malaysia/Thailand levels (0%)

---

## Slide 12: Philippines Deep Dive 🇵🇭

### Visualization 5: Interactive Dashboard

**Four-Panel Analysis (Poverty, GDP, Education, Infrastructure)**

**Poverty Trend:**

- Declining trajectory over decades
- Recent stabilization around 5%

**Economic Growth:**

- Steady GDP per capita increase
- But slower poverty reduction relative to growth

**Education:**

- High primary enrollment (>95%)
- Secondary enrollment improving

**Infrastructure:**

- Electricity access expanding
- Strong correlation with poverty reduction

**Critical Question:** Why hasn't GDP growth translated to faster poverty reduction like in Indonesia (-80.8%) or Vietnam?

---

## Slide 13: Global Progress Tracking 📈

### Who's Succeeding? Who's Struggling?

**Progress Categories (120 countries with time-series data):**

- 🟢 **Improving** (>5% reduction): 65 countries (54.2%)
- 🟡 **Stable** (±5%): 49 countries (40.8%)
- 🔴 **Worsening** (>5% increase): 6 countries (5.0%)

**🏆 Top 5 Success Stories:**

1. 🇨🇳 China: -97.0% reduction
2. 🇮🇩 Indonesia: -80.8% reduction _(ASEAN neighbor!)_
3. 🇳🇵 Nepal: -80.3% reduction
4. 🇺🇿 Uzbekistan: -77.1% reduction
5. 🇬🇳 Guinea: -74.7% reduction

**⚠️ Top 5 Challenges:**

1. 🇸🇾 Syria: +15.3% increase (conflict)
2. 🇰🇪 Kenya: +14.9% increase
3. 🇲🇼 Malawi: +10.8% increase
4. 🇿🇲 Zambia: +8.7% increase
5. 🇲🇬 Madagascar: +7.5% increase

---

## Slide 14: Key Findings Summary

### What the Data Reveals

**🌍 GLOBAL ACHIEVEMENTS**

- ✅ Poverty dropped from 17.22% → 4.23% (1981-2024)
- ✅ Over 1 billion people lifted from poverty
- ⚠️ But 700 million still in extreme poverty

**📊 CRITICAL INSIGHTS**

1. **Infrastructure > Income:** Electricity (r=-0.847) beats GDP (r=-0.397)
2. **Health Matters:** Life expectancy correlation r=-0.786
3. **Success is Possible:** Malaysia, Thailand, Indonesia prove it
4. **Majority Improving:** 54% of countries reducing poverty

**🇵🇭 PHILIPPINES POSITION**

- At 5.3%, below ASEAN median but above global
- Balanced development indicators
- Clear path to 0% following regional models

**🌏 ASEAN DIVERSITY**

- Wide range: 0% (Malaysia, Thailand) to 43.9% (Timor-Leste)
- Regional median 5.4% > global median 2.7%

---

## Slide 15: Policy Recommendations

### Evidence-Based Actions for Impact

**🇵🇭 FOR PHILIPPINES**

1. **Accelerate Infrastructure**
   - Strongest correlation (r=-0.847) with poverty reduction
   - Expand beyond electricity: digital, transport, water
2. **Learn from Success Stories**
   - Study Malaysia, Thailand path to 0%
   - Adopt Indonesia's strategies (-80.8% reduction)
3. **Strengthen Health Systems**
   - Life expectancy correlation (r=-0.786) critical
   - Invest in primary healthcare access
4. **Beyond GDP Growth**
   - Focus on distribution and access, not just income
   - Targeted interventions for remaining 5.3%

**🌏 FOR ASEAN REGION**

1. **Support Timor-Leste** (43.9% poverty) with coordinated aid
2. **Share Best Practices** from Malaysia, Thailand
3. **Improve Data Collection** (4 countries missing data)
4. **Address Regional Inequality** (median 5.4% > global 2.7%)

---

## Slide 16: Limitations & Future Work

### What We Know, What We Need

**📉 DATA LIMITATIONS**

- 48 countries (22%) lack poverty data
- ASEAN gaps: Only 7 of 11 countries measured
- Temporal mismatch: "Latest" = different years (2018-2024)
- National aggregates mask sub-national disparities

**🔄 METHODOLOGICAL CONSTRAINTS**

- Correlation ≠ Causation (need causal analysis)
- Cross-sectional comparisons, not panel regression
- Limited to available WDI indicators

**🔬 FUTURE RESEARCH DIRECTIONS**

1. **Causal Analysis:** Panel regression, instrumental variables
2. **Sub-National Data:** Within-country poverty mapping
3. **Forecasting:** Project 2030 SDG trajectories
4. **Multi-Dimensional Poverty:** Beyond income measures
5. **Machine Learning:** Predict poverty risk factors
6. **Climate Integration:** Analyze vulnerability to shocks
7. **Vietnam Case Study:** Obtain alternative data sources
8. **Policy Effectiveness:** Link specific interventions to outcomes

---

## Slide 17: Conclusion

### The Path Forward to SDG 1

**✅ WHAT WE'VE PROVEN**

- Poverty elimination is **ACHIEVABLE** (not aspirational)
- Infrastructure + Health > Income growth alone
- Regional success stories provide roadmaps
- Philippines has foundation and clear examples to follow

**🎯 THE 2030 CHALLENGE**

- Global average 4.23% → Need to reach near-zero
- Philippines 5.3% → Clear path to 0% exists
- 700 million people still waiting
- 6 years remaining to deadline

**💡 CRITICAL INSIGHT FROM DATA**

> "The question is not WHETHER poverty can be eliminated—the data shows it can—but WHETHER we will summon the political will and resource allocation to complete the journey."

**🇵🇭 PHILIPPINES OPPORTUNITY**

- Balanced development indicators ✓
- Regional role models (Malaysia, Thailand) ✓
- Strong infrastructure correlation identified ✓
- **Foundation is set—execution is next**

**Hope + Urgency = Action**

---

## Slide 18: Thank You

# Questions?

**Project Materials:**

- 📊 Interactive Dashboard: `viz_05_philippines_dashboard.html`
- 🗺️ Global Map: `viz_01_choropleth.html`
- 📈 All Visualizations: `/figures` directory
- 📄 Full Report: `docs/main.tex` (ACM format)
- 💻 Code: `FINAL_PROJECT.ipynb`

**Data Source:**
World Bank World Development Indicators  
https://data.worldbank.org/

**Key Figures to Remember:**

- Global: 17.22% → 4.23% (1981-2024)
- Philippines: 5.3% (2023)
- Correlation: Electricity r=-0.847, GDP r=-0.397
- ASEAN: 0% (Malaysia, Thailand) to 43.9% (Timor-Leste)

---

**CS ELEC 3C - Data Visualization Project**  
December 10, 2025
