# CS ELEC 3C – Data Visualization Project

## SDG 1: No Poverty - Comprehensive Project Implementation Guide

---

## 🎯 PROJECT OVERVIEW

**Project Title**: Visualizing Global Poverty Trends and Development Indicators (1990-2023)

**SDG Focus**: SDG 1 - No Poverty

**Objective**: Analyze and visualize World Development Indicators (WDI) data to understand poverty reduction trends across regions and identify correlations with key development indicators using advanced visualization techniques including interactive dashboards, Sankey diagrams, and unique chart types.

---

## 📋 COMPLETE PROJECT REQUIREMENTS

### 1. PROJECT BACKGROUND (10 points)

**Requirements:**

- Introduce the nature and importance of the project
- Describe the global issue (extreme poverty)
- State SDG 1 and its importance
- Explain relevance to global development and policy

**Content to Include:**

- Current state of global poverty (~9% of world population in extreme poverty)
- Historical context (from ~36% in 1990 to ~9% in 2023)
- Regional disparities (Sub-Saharan Africa vs. East Asia success)
- Why this matters: poverty affects health, education, life expectancy, economic growth
- UN SDG 1 targets: End extreme poverty by 2030

---

### 2. STATEMENT OF THE PROBLEM (10 points)

**Primary Research Question:**
"How has extreme poverty (living on <$2.15/day) evolved across world regions from 1990-2023, and what development indicators demonstrate the strongest correlation with successful poverty reduction?"

**Specific Objectives:**

1. Analyze poverty rate trends across 6 major world regions
2. Identify countries with most/least progress in poverty reduction
3. Examine correlations between poverty and:
   - Primary education enrollment rates
   - Healthcare access (maternal mortality, life expectancy)
   - Infrastructure development (electricity, sanitation access)
   - Economic indicators (GDP per capita, unemployment)
4. Compare urban vs. rural poverty trends
5. Visualize poverty reduction pathways using Sankey diagrams

**Scope:**

- **Time Frame**: 1990-2023 (primary focus)
- **Geographic Coverage**: All available countries, grouped by:
  - World Bank regions (6 regions)
  - Income classifications (Low, Lower-middle, Upper-middle, High)
- **Key Indicators**: 8-10 WDI indicators (specified below)

**Limitations:**

- Data availability varies by country and year
- Some countries lack poverty data for certain periods
- Rural/urban breakdown limited for some nations
- COVID-19 impact may show data anomalies (2020-2022)
- Poverty threshold definition changed over time (acknowledge this)

---

### 3. BACKGROUND ON THE DATASET (10 points)

**Dataset Name**: World Development Indicators (WDI)

**Source**: World Bank Open Data (https://data.worldbank.org/indicator)

**Dataset Characteristics:**

- **Time Span**: 1960-present (we focus on 1990-2023)
- **Coverage**: ~200+ countries and territories
- **Indicators**: 1,400+ indicators across multiple themes
- **Structure**:
  - Columns: Country Name, Country Code, Indicator Name, Indicator Code, Year, Value
  - Format: Long format (one row per country-indicator-year)

**Organization:**

- Grouped by themes: Poverty, Education, Health, Environment, Economy, Infrastructure
- Standardized country codes (ISO 3-letter codes)
- Annual updates with historical revisions

**Secondary Datasets:**

- Country classifications by region (World Bank regional groupings)
- Income level classifications (updated annually)
- Population data for weighted averages

**Access Methods:**

1. World Bank API (`wbdata` Python library)
2. Bulk CSV downloads from data.worldbank.org
3. Kaggle datasets (preprocessed versions)

---

### 4. LITERATURE REVIEW (10 points)

**Required Sources to Review:**

1. **World Bank Poverty and Shared Prosperity Reports (2020-2024)**

   - Key findings on global poverty trends
   - Methodology for poverty measurement
   - Regional analysis and projections

2. **UN SDG Progress Reports**

   - Official tracking of SDG 1 targets
   - Country-level progress assessments
   - Challenges and success stories

3. **Our World in Data - "Global Extreme Poverty"**

   - Interactive visualizations and historical trends
   - Data quality discussions
   - Comparative analysis approaches

4. **Academic Papers** (Search Google Scholar):

   - "Poverty reduction in China: trends and drivers" (World Bank)
   - "Sub-Saharan Africa poverty trap analysis"
   - "Education and poverty: systematic review"

5. **Existing Dashboards:**
   - World Bank Poverty & Equity Data Portal
   - Gapminder poverty visualizations
   - UNDP Human Development Index dashboards

**Analysis Points:**

- What visualization techniques did they use?
- What insights did they uncover?
- What gaps exist in their analysis that your project will address?
- How will your visualizations (Sankey, interactive dashboard) add value?

---

## 🔬 METHODOLOGY

### 5a. DATASET - KEY INDICATORS (Specify 8-10)

**Primary Indicator:**

1. **SI.POV.DDAY** - Poverty headcount ratio at $2.15/day (% of population)

**Education Indicators:** 2. **SE.PRM.NENR** - Primary school enrollment rate (% net) 3. **SE.SEC.ENRR** - Secondary school enrollment rate (% gross) 4. **SE.ADT.LITR.ZS** - Adult literacy rate (% ages 15+)

**Health Indicators:** 5. **SH.STA.MMRT** - Maternal mortality ratio (per 100,000 live births) 6. **SP.DYN.LE00.IN** - Life expectancy at birth (years)

**Infrastructure Indicators:** 7. **EG.ELC.ACCS.ZS** - Access to electricity (% of population) 8. **SH.H2O.SMDW.ZS** - Access to safely managed drinking water (%) 9. **SH.STA.SMSS.ZS** - Access to safely managed sanitation (%)

**Economic Indicators:** 10. **NY.GDP.PCAP.CD** - GDP per capita (current US$) 11. **SL.UEM.TOTL.ZS** - Unemployment rate (% of labor force)

**Demographic:** 12. **SP.URB.TOTL.IN.ZS** - Urban population (% of total)

**Justification:** Each indicator represents a dimension of development that directly or indirectly affects poverty: education creates opportunities, health enables productivity, infrastructure supports economic activity, and economic growth provides resources for poverty alleviation.

---

### 5b. DATA PREPARATION (Must Document All Steps)

**Step 1: Data Collection**

```python
# Download using World Bank API
import wbdata
import pandas as pd
from datetime import datetime

# Define indicators
indicators = {
    'SI.POV.DDAY': 'poverty_headcount',
    'SE.PRM.NENR': 'primary_enrollment',
    'EG.ELC.ACCS.ZS': 'electricity_access',
    # ... add all indicators
}

# Set date range
start_date = datetime(1990, 1, 1)
end_date = datetime(2023, 12, 31)

# Fetch data
df = wbdata.get_dataframe(indicators,
                          date=(start_date, end_date),
                          convert_date=True)
```

**Step 2: Data Cleaning**

- Remove aggregates (World, regions) from country-level analysis
- Identify missing value patterns
- Document missingness (% missing per indicator per region)
- Decision rules for handling missing data:
  - Time series interpolation for gaps <3 years
  - Forward/backward fill for edge years
  - Drop countries with >50% missing data for key indicators

**Step 3: Regional/Income Classification**

```python
# Add region and income level metadata
regions = pd.read_csv('country_regions.csv')  # from World Bank
df = df.merge(regions, on='country_code', how='left')
```

**Step 4: Derived Variables**
Create new calculated fields:

- `poverty_reduction_rate` = (poverty_1990 - poverty_2023) / poverty_1990 \* 100
- `decade_change` = poverty change by decade
- `people_in_poverty` = poverty_rate \* population (absolute numbers)
- `normalized_indicators` = z-scores for correlation analysis

**Step 5: Data Validation**

- Check for outliers (values outside reasonable ranges)
- Verify country codes match ISO standards
- Ensure temporal consistency (no future dates)

**Documentation Required:**

- Summary statistics before/after cleaning
- Number of records removed and why
- Missingness analysis table

---

### 5c. EXPLORATORY DATA ANALYSIS (EDA) (15 points)

**Required: 3-4 Preliminary Visualizations**

**EDA Visualization 1: Distribution Analysis**

- **Histogram**: Current poverty rate distribution (2023)
  - Show frequency of countries in different poverty bands
  - Identify concentration points

**EDA Visualization 2: Regional Trends**

- **Box Plot**: Poverty rate by region (2023)
  - Show median, quartiles, outliers
  - Compare variability across regions

**EDA Visualization 3: Time Series Overview**

- **Line Plot**: Average poverty by region (1990-2023)
  - Identify which regions improved most
  - Spot trend reversals or plateaus

**EDA Visualization 4: Correlation Preview**

- **Scatter Matrix**: Quick look at relationships
  - Poverty vs. GDP, education, electricity
  - Identify potential strong correlations

**Statistical Summaries to Include:**

- Mean, median, std dev for all indicators (by region)
- Correlation matrix (Pearson correlation coefficients)
- Trend analysis (linear regression slopes for time series)
- Outlier identification (countries >3 std dev from mean)

---

### 5d. DATA VISUALIZATION (15 points)

**REQUIRED: 4-6 Polished, Professional Visualizations + Interactive Dashboard**

---

#### **VISUALIZATION 1: Interactive Choropleth Map**

**Type**: Geographic heatmap with time slider

**Specifications:**

- **Tool**: Plotly Express or Folium
- **Data**: Poverty headcount ratio by country
- **Features**:
  - Color scale: Red (high poverty 40%+) → Yellow (moderate 10-40%) → Green (low <10%)
  - Interactive hover tooltip showing:
    - Country name
    - Exact poverty rate
    - Population in poverty
    - Year
  - Time slider: 1990-2023
  - Play button for animated progression
- **Purpose**: Show geographic distribution and how it evolved

**Technical Implementation:**

```python
import plotly.express as px

fig = px.choropleth(df,
                    locations="country_code",
                    color="poverty_rate",
                    hover_name="country_name",
                    animation_frame="year",
                    color_continuous_scale="RdYlGn_r",
                    range_color=[0, 50])
```

---

#### **VISUALIZATION 2: Multi-Line Time Series Dashboard**

**Type**: Interactive line chart with region selector

**Specifications:**

- **Tool**: Plotly with Dash or Streamlit
- **X-axis**: Years (1990-2023)
- **Y-axis**: Poverty rate (%)
- **Lines**: One per region (6 regions)
- **Features**:
  - Legend with region names
  - Checkbox to show/hide regions
  - Highlight on hover
  - Annotations for key events (2008 financial crisis, COVID-19)
  - Secondary Y-axis option (show absolute numbers)
- **Insights to highlight**:
  - East Asia's dramatic decline
  - Sub-Saharan Africa's slower progress
  - Latin America's volatility

---

#### **VISUALIZATION 3: Sankey Diagram - Poverty Reduction Flow**

**Type**: Sankey diagram showing poverty category transitions

**Specifications:**

- **Tool**: Plotly or D3.js
- **Purpose**: Show how countries moved between poverty categories

**Structure:**

- **Left nodes (1990)**:
  - Extreme poverty (>40%)
  - High poverty (20-40%)
  - Moderate poverty (10-20%)
  - Low poverty (<10%)
- **Right nodes (2023)**: Same categories
- **Flows**: Width = number of countries transitioning
- **Colors**:
  - Green flows = improvement
  - Red flows = deterioration
  - Gray = no change

**Implementation:**

```python
import plotly.graph_objects as go

fig = go.Figure(data=[go.Sankey(
    node = dict(
      label = ["Extreme 1990", "High 1990", "Moderate 1990", "Low 1990",
               "Extreme 2023", "High 2023", "Moderate 2023", "Low 2023"],
      color = ["red", "orange", "yellow", "green",
               "red", "orange", "yellow", "green"]
    ),
    link = dict(
      source = [0, 0, 1, 1, 2, 2, 3],  # Source nodes
      target = [4, 5, 5, 6, 6, 7, 7],  # Target nodes
      value = [15, 25, 30, 40, 25, 35, 45]  # Flow volumes
    ))])
```

---

#### **VISUALIZATION 4: Correlation Heatmap**

**Type**: Interactive correlation matrix

**Specifications:**

- **Tool**: Seaborn + Plotly for interactivity
- **Variables**: Poverty rate vs. all other indicators
- **Features**:
  - Color scale: Blue (negative correlation) to Red (positive)
  - Annotated cells with correlation coefficients
  - Hover for exact values and p-values
  - Hierarchical clustering to group related indicators

**Expected Insights:**

- Strong negative correlation: education, electricity access
- Moderate negative: healthcare access, GDP per capita
- Positive correlation: unemployment, rural population %

---

#### **VISUALIZATION 5: Scatter Plot with Regression - Education vs. Poverty**

**Type**: Animated bubble scatter plot

**Specifications:**

- **Tool**: Plotly Express
- **X-axis**: Primary school enrollment rate (%)
- **Y-axis**: Poverty rate (%)
- **Bubble size**: Population
- **Bubble color**: Region
- **Animation**: Year (1990-2023)
- **Features**:
  - Regression line with confidence interval
  - Country labels on hover
  - Play button for time progression
  - Outlier highlighting

**Purpose**: Demonstrate the education-poverty relationship dynamically

---

#### **VISUALIZATION 6: Small Multiples - Top 10 Countries**

**Type**: Faceted line charts

**Specifications:**

- **Layout**: 2x5 grid
- **Countries**: Top 10 by population or most improved
  - China, India, Indonesia, Bangladesh, Nigeria, Ethiopia, Brazil, Vietnam, Philippines, Pakistan
- **Each panel**:
  - Line showing poverty trend 1990-2023
  - Shaded area showing confidence intervals
  - Annotation of % reduction
  - Mini flag icon or country name

**Purpose**: Show individual country stories within regional trends

---

#### **VISUALIZATION 7: Radial/Spider Chart - Multi-Dimensional Development**

**Type**: Radar chart comparing regions

**Specifications:**

- **Axes** (6-8):
  - Poverty reduction (% change)
  - Education access
  - Healthcare improvement
  - Infrastructure development
  - GDP growth
  - Life expectancy gain
- **Series**: One polygon per region
- **Features**:
  - Semi-transparent fills
  - Interactive legend
  - Normalized scales (0-100)

**Purpose**: Holistic view of regional development across all dimensions

---

### **COMPREHENSIVE INTERACTIVE DASHBOARD**

**Platform**: Plotly Dash or Streamlit

**Dashboard Structure:**

**Section 1: Overview Panel**

- KPI cards showing:
  - Global poverty rate (current)
  - Total people in poverty (current)
  - Change since 1990
  - Projection to 2030
- World map (choropleth)

**Section 2: Regional Deep Dive**

- Dropdown: Select region
- Multi-line chart: Poverty trends for countries in region
- Bar chart: Ranking of countries within region
- Table: Detailed statistics

**Section 3: Correlation Explorer**

- X-axis dropdown: Select indicator 1
- Y-axis dropdown: Select indicator 2
- Scatter plot updates dynamically
- Correlation coefficient displayed
- Regression line toggle

**Section 4: Country Comparison**

- Multi-select: Choose 2-5 countries
- Side-by-side comparison:
  - Line charts for all indicators
  - Bar chart: 1990 vs 2023 comparison
  - Percentage change metrics

**Section 5: Sankey Flow**

- Full-screen Sankey diagram
- Toggle: 1990-2023, 2000-2023, or custom range
- Click on flows for country details

**Interactivity Features:**

- All charts linked (click on map → updates other charts)
- Download buttons for data/images
- Date range slider (global filter)
- Reset button
- Dark/light theme toggle

---

## 📊 DATA ANALYSIS SECTION (20 points)

**Requirements: Interpret visualizations and extract insights**

### Analysis Framework:

**1. Global Trends**

- Document poverty reduction: ~36% (1990) → ~9% (2023)
- Identify inflection points (Asian financial crisis, 2008 recession, COVID-19)
- Calculate rate of reduction per decade
- Project to 2030: Will SDG 1 target be met?

**2. Regional Analysis**
For each region, answer:

- What was the poverty rate in 1990 vs 2023?
- What was the % reduction?
- Which sub-regions/countries drove the change?
- What obstacles remain?

**Expected Regional Findings:**

- **East Asia & Pacific**: Dramatic success (China reduced from 66% to <1%)
- **South Asia**: Significant progress (India, Bangladesh)
- **Sub-Saharan Africa**: Slowest progress, highest current rates (~40%)
- **Latin America**: Moderate progress with reversals
- **Middle East & North Africa**: Mixed results
- **Europe & Central Asia**: Already low rates, maintained

**3. Correlation Insights**
From your heatmap and scatter plots:

- **Strong negative correlations** (expected):
  - Primary education enrollment: r = -0.75 to -0.85
  - Electricity access: r = -0.70 to -0.80
  - Life expectancy: r = -0.65 to -0.75
- **Moderate correlations**:
  - GDP per capita: r = -0.50 to -0.60 (wealth ≠ always less poverty)
  - Healthcare access: r = -0.60 to -0.70

**Key Insight**: Education and infrastructure show stronger correlation than raw GDP growth → policy implication: invest in human capital and basic services

**4. Unexpected Findings**
Identify and explain:

- **Countries that defy trends**:
  - Vietnam: Low GDP but rapid poverty reduction (why?)
  - Resource-rich nations with persistent poverty (why?)
- **Urban-rural gaps**: How do they differ by region?
- **Poverty traps**: Countries stuck at high rates despite decades
- **Reversals**: Countries where poverty increased (conflict zones, economic collapse)

**5. Success Stories vs. Challenges**

**Success Case Study: China**

- Reduced 850M people from poverty
- Methods: Economic reforms, infrastructure, education
- Visualize the trajectory and compare to similar starting points

**Success Case Study: Bangladesh**

- Reduced from 43% to 13% poverty
- Focus: Microfinance, education, health
- Lessons for other South Asian nations

**Challenge Case Study: Sub-Saharan Africa**

- Why has progress been slower?
- Data shows: Conflict, rapid population growth, climate vulnerability
- What correlates with success within the region? (Botswana, Ghana, Rwanda)

**6. Answer Research Questions Explicitly**

**Q1: Which regions made most/least progress?**

- Answer with specific numbers and visualizations
- Cite your line charts and bar graphs

**Q2: What correlates with poverty reduction?**

- Answer with correlation coefficients
- Reference scatter plots and heatmap
- Discuss causation vs correlation

**Q3: Urban vs rural differences?**

- If data available, show disparities
- Connect to infrastructure access

---

## 🎯 CONCLUSION SECTION (10 points)

### Structure:

**1. Key Findings Summary**

- Restate main insights (3-5 bullet points)
- Quantify achievements: "Global poverty fell 75% since 1990"
- Highlight disparities: "But 700M still in extreme poverty, 60% in SSA"

**2. SDG 1 Progress Assessment**

- Current trajectory: Will we end poverty by 2030?
- Answer: Unlikely without acceleration, especially in Africa
- What needs to change?

**3. Policy Recommendations**
Based on your data:

- **For low-progress regions**:
  - Prioritize basic education and infrastructure
  - Evidence: Your correlation analysis
- **For middle-income countries**:
  - Address inequality (urban-rural gaps)
  - Social safety nets
- **Global community**:
  - Targeted aid to countries with structural barriers
  - Climate adaptation support (poverty-climate nexus)

**4. Limitations**
Be transparent:

- **Data limitations**:
  - Missing data for some countries/years
  - Poverty threshold definitions evolved
  - Self-reported surveys vary in quality
- **Methodological limitations**:
  - Correlation ≠ causation
  - Aggregated data masks within-country inequality
  - Short-term shocks (COVID) affect trends
- **Scope limitations**:
  - Didn't include multidimensional poverty
  - Focused on income poverty only
  - Limited qualitative context

**5. Future Work**

- Include multidimensional poverty index (MPI)
- Machine learning for poverty prediction
- Causal inference analysis (what policies actually work?)
- Real-time dashboard with monthly updates
- Sub-national analysis (provinces/states)
- Integration with climate data

**6. Final Reflection**

- The bigger picture: poverty is solvable (we've proven it)
- But the last mile is hardest (those left behind face structural barriers)
- Data visualization's role: makes invisible visible, drives action

---

## 📦 DELIVERABLES CHECKLIST

### ✅ Final Report (8-10 pages, ACM format)

**Required Sections:**

1. ✅ Project Background (1 page)
2. ✅ Statement of Problem (0.5 page)
3. ✅ Dataset Description (0.5 page)
4. ✅ Literature Review (1 page)
5. ✅ Methodology (2-3 pages)
   - Dataset specification
   - Data preparation steps
   - EDA with 3-4 prelim charts
   - Main visualizations (4-6 polished, embedded)
6. ✅ Data Analysis (2-3 pages)
7. ✅ Conclusion (0.5-1 page)
8. ✅ References (APA/ACM format)

**Formatting:**

- ACM template (2-column format)
- All visualizations embedded with captions
- Figure numbers and references in text
- Clear section headings
- Page numbers

### ✅ Code and Data Repository (GitHub or ZIP)

**Repository Structure:**

```
sdg1-poverty-visualization/
│
├── README.md                 # Setup instructions, project overview
├── requirements.txt          # Python dependencies
├── environment.yml           # Conda environment (optional)
│
├── data/
│   ├── raw/                  # Original downloaded data
│   ├── processed/            # Cleaned datasets
│   └── metadata/             # Country classifications, regions
│
├── notebooks/
│   ├── 01_data_collection.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda.ipynb
│   └── 04_visualizations.ipynb
│
├── src/
│   ├── data_processing.py    # Data cleaning functions
│   ├── visualizations.py     # Chart generation functions
│   └── utils.py              # Helper functions
│
├── visualizations/
│   ├── static/               # PNG/PDF exports of charts
│   └── interactive/          # HTML files for interactive charts
│
├── dashboard/
│   └── app.py                # Streamlit/Dash dashboard code
│
└── report/
    └── final_report.pdf      # The submitted report
```

**README.md Must Include:**

- Project title and team members
- Installation instructions
- How to run the code
- How to view the dashboard
- Data sources and download links
- Project structure explanation

### ✅ 10-Minute Presentation

**Slide Structure (10-12 slides):**

1. **Title Slide**: Project name, team, date
2. **Introduction**: SDG 1, why poverty matters (1 min)
3. **Problem Statement**: Research questions (30 sec)
4. **Data Overview**: WDI dataset, indicators chosen (30 sec)
5. **Methodology**: Brief data prep summary (30 sec)
6. **Visualization 1**: Choropleth map demo (1 min)
7. **Visualization 2**: Time series trends (1 min)
8. **Visualization 3**: Sankey diagram (1 min)
9. **Visualization 4**: Correlation analysis (1 min)
10. **Dashboard Demo**: Live interaction (2 min)
11. **Key Insights**: Main findings (1 min)
12. **Conclusion**: Policy recommendations, limitations (1 min)

**Presentation Tips:**

- Rehearse timing
- Have backup (PDF of dashboard if live demo fails)
- Assign roles: who presents what
- Prepare for Q&A (anticipate questions about data, methodology)

---

## 🎯 GRADING RUBRIC ALIGNMENT

### How to Score "EXCELLENT" in Each Category:

**Project Background & SDG Rationale (10 points)**
✅ **To get EXCELLENT:**

- Compelling narrative about poverty's global impact
- Clear explanation of why SDG 1 matters
- Connect to real-world consequences (health, education, conflict)
- Use statistics (800M out of poverty since 1990, but 700M remain)
- Strong opening that engages reader

**Statement of the Problem (10 points)**
✅ **To get EXCELLENT:**

- Crystal-clear research questions (listed above)
- Specific, measurable objectives
- Well-defined scope (geography, time, indicators)
- Honest about limitations
- Shows deep understanding of context

**Dataset Description & Preparation (10 points)**
✅ **To get EXCELLENT:**

- Comprehensive description of WDI
- Justify every indicator choice
- Document every cleaning step with code
- Show before/after statistics
- Explain rationale for handling missing data

**Literature Review (10 points)**
✅ **To get EXCELLENT:**

- Review 5-7 quality sources
- Critically analyze their approaches
- Explain what inspires your project
- Identify gaps your work fills
- Organize by themes (not chronological list)

**Exploratory Data Analysis (15 points)**
✅ **To get EXCELLENT:**

- 4+ well-chosen preliminary visualizations
- Statistical summaries for all indicators
- Identify outliers and explain them
- Insightful commentary on patterns
- Smooth transition to main visualizations

**Visualization Techniques (15 points)**
✅ **To get EXCELLENT:**

- 6+ diverse, polished visualizations
- Interactive dashboard fully functional
- Include unique charts (Sankey, radar)
- Professional design: colors, labels, legends
- Appropriate chart choice for each insight
- Clear figure captions and numbering

**Analysis and Insights (20 points - HIGHEST WEIGHT)**
✅ **To get EXCELLENT:**

- Deep, original insights (not just describing charts)
- Answer all research questions explicitly
- Connect findings to SDG goals
- Identify unexpected patterns and explain them
- Compare success stories and challenges
- Discuss causation vs. correlation carefully
- Link back to literature review

**Conclusion / Clarity (10 points)**
✅ **To get EXCELLENT:**

- Strong summary of key findings
- Honest discussion of limitations
- Thoughtful policy recommendations
- Ideas for future work
- Overall report is well-written, clear, flows logically

---

## 🛠️ TECHNICAL IMPLEMENTATION GUIDE

### Python Environment Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install pandas numpy matplotlib seaborn plotly dash streamlit
pip install wbdata geopandas folium scipy scikit-learn
pip install jupyter notebook ipykernel

# For ACM format report (LaTeX)
# Install LaTeX: https://www.latex-project.org/get/
```

### Key Libraries and Their Use:

**Data Collection:**

- `wbdata`: World Bank API access
- `pandas`: Data manipulation
- `requests`: API calls if needed

**Data Processing:**

- `pandas`: Cleaning, filtering, merging
- `numpy`: Numerical operations
- `scipy`: Statistical tests

**Visualization:**

- `matplotlib` + `seaborn`: Static, publication-quality charts
- `plotly`: Interactive charts, choropleth maps
- `geopandas`: Geographic data handling
- `folium`: Alternative for maps

**Dashboard:**

- `streamlit`: Fastest for prototyping
- `dash`: More customizable, production-ready

### Sankey Diagram Code Template:

```python
import plotly.graph_objects as go
import pandas as pd

# Prepare data: categorize countries by poverty level in 1990 and 2023
def categorize_poverty(rate):
    if pd.isna(rate):
        return None
    elif rate >= 40:
        return "Extreme"
    elif rate >= 20:
        return "High"
    elif rate >= 10:
        return "Moderate"
    else:
        return "Low"

# Create flow data
df['category_1990'] = df['poverty_1990'].apply(categorize_poverty)
df['category_2023'] = df['poverty_2023'].apply(categorize_poverty)

# Count transitions
flow_data = df.groupby(['category_1990', 'category_2023']).size().reset_index(name='count')

# Create Sankey
fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = ["Extreme (1990)", "High (1990)", "Moderate (1990)", "Low (1990)",
               "Extreme (2023)", "High (2023)", "Moderate (2023)", "Low (2023)"],
      color = ["darkred", "red", "orange", "green",
               "darkred", "red", "orange", "green"]
    ),
    link = dict(
      source = [...],  # Map categories to node indices
      target = [...],  # Map categories to node indices
      value = flow_data['count'].tolist(),
      color = "rgba(0,0,0,0.2)"
  ))])

fig.update_layout(title_text="Poverty Category Transitions (1990-2023)",
                  font_size=12, height=600)
fig.show()
```

### Dashboard Code Template (Streamlit):

```python
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide", page_title="SDG 1 Poverty Dashboard")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('data/processed/poverty_data.csv')
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("Filters")
selected_region = st.sidebar.multiselect("Select Region(s)",
                                          options=df['region'].unique(),
                                          default=df['region'].unique())

year_range = st.sidebar.slider("Year Range", 1990, 2023, (1990, 2023))

# Filter data
filtered_df = df[
    (df['region'].isin(selected_region)) &
    (df['year'] >= year_range[0]) &
    (df['year'] <= year_range[1])
]

# Main dashboard
st.title("🌍 SDG 1: Global Poverty Visualization Dashboard")

# KPI Cards
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Global Poverty Rate", "9.2%", "-75% since 1990")
with col2:
    st.metric("People in Poverty", "700M", "-850M since 1990")
with col3:
    st.metric("Regions Improved", "5/6", "+83%")
with col4:
    st.metric("2030 Target Gap", "400M", "Off track")

# Choropleth Map
st.header("Geographic Distribution")
fig_map = px.choropleth(filtered_df[filtered_df['year']==2023],
                         locations="country_code",
                         color="poverty_rate",
                         hover_name="country_name",
                         color_continuous_scale="RdYlGn_r",
                         title="Poverty Rate by Country (2023)")
st.plotly_chart(fig_map, use_container_width=True)

# Time Series
st.header("Regional Trends Over Time")
fig_line = px.line(filtered_df, x='year', y='poverty_rate',
                    color='region',
                    title="Poverty Rate by Region (1990-2023)")
st.plotly_chart(fig_line, use_container_width=True)

# Scatter Plot
st.header("Education vs. Poverty")
fig_scatter = px.scatter(filtered_df[filtered_df['year']==2023],
                          x='primary_enrollment', y='poverty_rate',
                          size='population', color='region',
                          hover_name='country_name',
                          title="Primary Enrollment vs. Poverty Rate (2023)")
st.plotly_chart(fig_scatter, use_container_width=True)
```

---

## 📅 RECOMMENDED TIMELINE

**Week 1: Foundation (Days 1-7)**

- Day 1-2: Finalize problem statement, read project requirements
- Day 3-4: Literature review, gather 5-7 sources
- Day 5-7: Data collection, initial exploration, set up GitHub repo

**Week 2: Data Work (Days 8-14)**

- Day 8-10: Data cleaning and preparation
- Day 11-12: EDA and preliminary visualizations
- Day 13-14: Document methodology section, review with team

**Week 3: Visualizations (Days 15-21)**

- Day 15-16: Create choropleth map
- Day 17: Create time series charts
- Day 18: Create Sankey diagram
- Day 19: Create correlation heatmap and scatter plots
- Day 20: Build interactive dashboard
- Day 21: Test all visualizations, gather feedback

**Week 4: Report & Presentation (Days 22-28)**

- Day 22-24: Write analysis section (interpret visualizations)
- Day 25: Write background, problem, dataset, conclusion sections
- Day 26: Create presentation slides
- Day 27: Practice presentation, refine dashboard
- Day 28: Final review, submit all deliverables

---

## ✅ FINAL CHECKLIST BEFORE SUBMISSION

### Report:

- [ ] All 7 sections complete and well-written
- [ ] 8-10 pages in ACM format
- [ ] All visualizations embedded with clear captions
- [ ] Figure numbers referenced in text
- [ ] No spelling/grammar errors
- [ ] References properly formatted
- [ ] PDF generated successfully

### Code Repository:

- [ ] README with clear instructions
- [ ] All code runs without errors
- [ ] Requirements.txt includes all dependencies
- [ ] Data sources documented
- [ ] Code is commented and organized
- [ ] Visualizations can be reproduced

### Dashboard:

- [ ] All features work (no broken links/buttons)
- [ ] Loads within 10 seconds
- [ ] Works in Chrome/Firefox
- [ ] Screenshots included in report
- [ ] URL/access instructions provided

### Presentation:

- [ ] 10-12 slides prepared
- [ ] Timing rehearsed (10 minutes)
- [ ] Dashboard demo prepared
- [ ] All team members know their parts
- [ ] Backup plan if tech fails

---

## 🎓 ADDITIONAL TIPS FOR EXCELLENCE

1. **Tell a Story**: Don't just present data—narrate poverty's journey
2. **Use Real Examples**: Mention specific countries by name
3. **Quantify Everything**: Use numbers, percentages, absolute changes
4. **Show Contrasts**: Success vs. challenge, then vs. now, rich vs. poor
5. **Be Honest**: Acknowledge data limitations and uncertainty
6. **Think Policy**: Every insight should suggest action
7. **Design Matters**: Clean, professional visualizations beat flashy ones
8. **Test Early**: Don't wait until the last day to run code
9. **Collaborate**: Use GitHub for version control and teamwork
10. **Ask for Feedback**: Show drafts to peers/professor

---

## 🔗 USEFUL RESOURCES

**Data Sources:**

- World Bank Open Data: https://data.worldbank.org/
- Our World in Data: https://ourworldindata.org/extreme-poverty
- UN SDG Database: https://unstats.un.org/sdgs/dataportal

**Visualization Inspiration:**

- Gapminder: https://www.gapminder.org/
- World Bank Poverty Portal: https://pip.worldbank.org/
- Tableau Public Gallery: Search "poverty" or "SDG"

**Learning Resources:**

- Plotly Documentation: https://plotly.com/python/
- Streamlit Tutorials: https://docs.streamlit.io/
- Seaborn Gallery: https://seaborn.pydata.org/examples/index.html

**ACM Format:**

- Template: https://www.acm.org/publications/proceedings-template
- LaTeX on Overleaf: https://www.overleaf.com/

---

## 🎯 SUCCESS CRITERIA SUMMARY

Your project will be successful if:

✅ **Addresses SDG 1 meaningfully** - Clear connection to poverty reduction
✅ **Uses 8-10 relevant WDI indicators** - Justified choices
✅ **Includes 6+ diverse visualizations** - Including Sankey and interactive dashboard
✅ **Provides deep insights** - Not just descriptive, but analytical
✅ **Professional quality** - Could be presented at a conference
✅ **Reproducible** - Anyone can run your code and get same results
✅ **Well-documented** - Clear explanations throughout
✅ **Policy-relevant** - Actionable recommendations

---

## 💡 FINAL NOTES

This project is an opportunity to:

- Develop data science skills (collection, cleaning, visualization, analysis)
- Understand a critical global issue (poverty affects 700M people)
- Create portfolio-worthy work (showcase on GitHub, LinkedIn)
- Practice professional communication (report, presentation, code)

Remember: **The goal is not just to complete an assignment, but to generate genuine insights that could inform real-world policy decisions.**

Good luck! 🚀

---

**Project prepared by:** [Your Team Name]
**Date:** [Submission Date]
**Course:** CS ELEC 3C - Data Visualization
**Institution:** [Your University]
