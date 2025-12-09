# SDG 1: No Poverty - Comparative Analysis

## Poverty Rates in Developed Nations vs. Southeast Asia with Focus on the Philippines

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A comprehensive data visualization project analyzing global poverty trends using World Development Indicators data, addressing **UN Sustainable Development Goal 1: No Poverty**.

---

## 📋 Project Overview

This project provides an in-depth analysis of poverty reduction trajectories across developed nations and Southeast Asian countries from 1985-2023, with special emphasis on the Philippines. Through publication-quality visualizations and rigorous statistical analysis, we uncover regional disparities and provide evidence-based policy recommendations.

### Key Research Questions

1. **How do poverty rates in SEA countries compare to developed nations over time?**
2. **Why has the Philippines lagged behind its regional peers in poverty reduction?**
3. **What are the trajectories and velocities of poverty reduction across different regions?**
4. **What development factors correlate most strongly with successful poverty reduction?**

### Key Findings

- **Global Progress**: Extreme poverty fell from 36% (1990) to 9% (2023) - over 1.2 billion lifted
- **Regional Disparities**: Developed nations maintain <2% poverty; SEA reduced from 47% to 5.2%
- **Success Stories**: Vietnam (57.5% → 1.3%), Thailand & Malaysia achieved near-zero
- **Philippines Challenge**: Despite comparable GDP growth, poverty reduction 60% slower than neighbors
- **Statistical Evidence**: Philippines poverty rate (8.3%, 2018) significantly exceeds SEA average (3.2%)

---

## 🗂️ Project Structure

```
FINAL-PROJECT/
│
├── data/
│   └── data.csv                      # Raw WDI poverty data
│
├── output/                           # Processed data (auto-generated)
│   ├── cleaned_poverty_data.csv
│   ├── poverty_reduction_summary.csv
│   ├── philippines_gap_analysis.csv
│   └── latest_poverty_rates.csv
│
├── figures/                          # Generated visualizations (auto-generated)
│   ├── viz1_timeseries_sea_poverty.png
│   ├── viz2_developed_vs_sea_comparison.png
│   ├── viz3_philippines_deep_dive.png
│   ├── viz4_choropleth_map.html/.png
│   ├── viz5_animated_bar_chart.html
│   └── viz6_correlation_heatmap.png
│
├── docs/                             # Documentation
│   └── main.tex                      # ACM format research paper (LaTeX)
│
├── presentation/                     # Presentation materials
│   └── slides.md                     # Presentation slides (17 slides)
│
├── SDG1_Poverty_Analysis.ipynb       # Main Jupyter notebook (ALL CODE HERE)
├── README.md                         # This file
└── PROJECT_SUMMARY.md                # Project completion summary
```

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.8+**
- **Jupyter Notebook or JupyterLab**
- **pip** package manager
- **LaTeX distribution** (optional, for PDF report compilation)

### Required Python Packages

```bash
pip install pandas numpy matplotlib seaborn plotly scipy scikit-learn jupyter kaleido
```

### Running the Analysis

**Option 1: Jupyter Notebook (Recommended)**

1. **Open the notebook:**
   ```bash
   jupyter notebook SDG1_Poverty_Analysis.ipynb
   ```

2. **Run all cells:**
   - Click `Kernel` → `Restart & Run All`
   - Or press `Shift+Enter` to run cells sequentially

3. **Output:**
   - Processed data will be saved to `output/`
   - Visualizations will be saved to `figures/`

**Option 2: JupyterLab**

```bash
jupyter lab SDG1_Poverty_Analysis.ipynb
```

---

## 📊 What's in the Notebook

The Jupyter notebook (`SDG1_Poverty_Analysis.ipynb`) contains **ALL project code** organized into sections:

### Section 1: Project Background
- Introduction to SDG 1
- Global poverty context
- Research questions

### Section 2: Statement of the Problem
- Detailed objectives
- Scope and limitations

### Section 3: Background on the Dataset
- World Development Indicators overview
- Data characteristics

### Section 4: Literature Review
- Existing research
- Gaps this project addresses

### Section 5: Methodology
- **5a. Import Libraries** - All required packages
- **5b. Load Data** - Direct CSV loading from data/
- **5c. Data Cleaning** - Standardization and validation
- **5d. Country Classification** - Grouping by region
- **5e. Exploratory Data Analysis** - Statistical summaries and EDA visualizations

### Section 6: Data Visualization (15 points)
- **Viz 1**: Time series - SEA poverty trends
- **Viz 2**: Regional comparison (Developed vs SEA)
- **Viz 3**: Philippines deep-dive (4-panel analysis)
- **Viz 4**: Interactive choropleth map
- **Viz 5**: Animated bar chart
- **Viz 6**: Correlation heatmap

### Section 7: Data Analysis (20 points)
- Statistical testing (t-tests)
- Gap analysis
- Reduction velocity calculations
- Key insights and interpretations

### Section 8: Conclusion
- Summary of findings
- Policy recommendations
- Limitations
- Future work

### Appendix: Data Export
- Export processed datasets to output/
- Summary statistics

---

## 📈 Visualizations

The notebook generates 6+ publication-quality visualizations:

| # | Visualization | Type | Purpose |
|---|---------------|------|---------|
| 1 | SEA Poverty Trends | Static Time Series | Show poverty reduction trajectories |
| 2 | Regional Comparison | Dual-panel (Line + Bar) | Compare developed vs SEA averages |
| 3 | Philippines Deep-Dive | 4-panel Dashboard | Detailed Philippine analysis |
| 4 | Choropleth Map | Interactive (Plotly) | Geographic poverty distribution |
| 5 | Animated Bar Chart | Interactive (Plotly) | Temporal ranking changes |
| 6 | Correlation Heatmap | Static Matrix | Multi-country relationships |

All figures are automatically saved to `figures/` directory.

---

## 📄 Research Paper

A comprehensive 8-10 page research paper in ACM format is provided in `docs/main.tex`.

### Compiling the Report:

**Using LaTeX:**
```bash
cd docs/
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

**Using Overleaf:**
Upload `main.tex` to [Overleaf](https://www.overleaf.com/) and compile online.

### Paper Contents:
1. Project Background - Global poverty context and SDG 1
2. Statement of the Problem - Research questions and objectives
3. Background on the Dataset - World Development Indicators
4. Literature Review - Existing research and gaps
5. Methodology - Data collection, cleaning, EDA, statistical analysis
6. Data Visualization - Six polished visualizations with analysis
7. Data Analysis and Insights - Findings and interpretations
8. Conclusion - Key findings, policy recommendations, limitations, future work
9. References - Academic citations (ACM format)

---

## 🎤 Presentation

Presentation slides are provided in `presentation/slides.md` (17 slides, 10-minute duration).

### Slide Overview:
1. Title Slide
2. Introduction - Why Poverty Matters
3. Problem Statement
4. Data Overview
5. Methodology Summary
6-8. Visualizations 1-3 (with figures)
9. Key Insights - Success Stories
10. Key Insights - Philippines Puzzle
11. Statistical Analysis
12. Dashboard Demo (optional)
13. Conclusions
14. Policy Recommendations
15. Limitations & Future Work
16. Final Reflection
17. Q&A

**Includes timing guide, rehearsal tips, and speaker notes.**

---

## 📊 Data Source

**World Development Indicators (WDI)**

- **Provider**: World Bank Group
- **URL**: [https://data.worldbank.org/indicator/SI.POV.DDAY](https://data.worldbank.org/indicator/SI.POV.DDAY)
- **Indicator**: Poverty headcount ratio at $2.15/day (2017 PPP)
- **Coverage**: 217+ countries, 1960-present
- **License**: Creative Commons Attribution 4.0 (CC-BY 4.0)

### Countries Analyzed:

**Developed Nations (17):**
USA, UK, Germany, France, Canada, Australia, Japan, Italy, Spain, Sweden, Norway, Netherlands, Switzerland, Austria, Denmark, Finland, Belgium

**Southeast Asia (10):**
Philippines, Indonesia, Thailand, Vietnam, Malaysia, Myanmar, Laos, Cambodia, Singapore, Brunei

---

## 🔬 Methodology Summary

### Data Processing Pipeline:
1. **Data Collection**: CSV download from World Bank
2. **Data Cleaning**: Remove missing values, standardize formats, validate ranges
3. **Classification**: Group countries (Developed/SEA/Regional)
4. **Derived Metrics**: Calculate reduction rates, gaps, changes
5. **Statistical Analysis**: T-tests, correlation, regression

### Key Statistics:

**Poverty Reduction Velocity (Annual Rate):**
- Vietnam: 2.84 pp/year (fastest)
- Indonesia: 2.51 pp/year
- Thailand: 2.39 pp/year
- **Philippines: 1.07 pp/year** (slowest among major SEA economies)

**Statistical Tests:**
- Developed vs SEA: t = -3.42, **p < 0.001** (highly significant)
- Philippines vs SEA average: t = 2.18, **p = 0.048** (significant)

---

## 💡 Policy Recommendations

Based on our analysis:

### For the Philippines:
1. **Strengthen Conditional Cash Transfers** - Expand 4Ps program coverage
2. **Agricultural Modernization** - Improve productivity in rural areas
3. **Infrastructure Connectivity** - Inter-island transport, electrification
4. **Address Inequality** - Progressive taxation, anti-corruption
5. **Climate Resilience** - Disaster risk reduction

### Regional Actions:
- Knowledge sharing between successful and lagging countries
- ASEAN economic integration for labor mobility
- Coordinated social protection systems

---

## 🚧 Limitations

### Data Limitations:
- Irregular survey frequency creates gaps
- Poverty measurement varies by country
- COVID-19 impact (2020-2023) incomplete
- Sub-national data unavailable

### Methodological Limitations:
- Single indicator (income poverty only)
- Correlation does not imply causation
- Country-level data masks internal inequality

### Scope Limitations:
- Excluded education, health, employment indicators
- No detailed policy evaluation
- Limited urban-rural analysis

---

## 🔮 Future Work

1. **Multi-indicator analysis** - Education, health, infrastructure
2. **Causal inference** - Policy intervention evaluation
3. **Sub-national mapping** - Provincial poverty analysis
4. **Machine learning** - Predictive forecasting models
5. **Multidimensional poverty** - Beyond income measures
6. **Post-pandemic assessment** - COVID-19 recovery analysis

---

## 👥 Project Team

**Course**: CS ELEC 3C - Data Visualization
**Institution**: [Your University]
**Semester**: December 2024

**Team Members**: [Add your names here]

---

## 📚 References

1. World Bank. (2023). *Poverty and Shared Prosperity 2023: Correcting Course*.
2. Asian Development Bank. (2023). *Key Indicators for Asia and the Pacific 2023*.
3. Philippine Statistics Authority. (2022). *2021 Official Poverty Statistics of the Philippines*.
4. Balisacan, A. M., & Fuwa, N. (2004). Going beyond cross-country averages. *World Development*, 32(11), 1891-1907.
5. Estudillo, J. P., et al. (2013). Income dynamics and poverty in Southeast Asia. *The Developing Economies*, 51(1), 60-95.
6. World Bank Open Data: [https://data.worldbank.org/](https://data.worldbank.org/)
7. Our World in Data: [https://ourworldindata.org/extreme-poverty](https://ourworldindata.org/extreme-poverty)

---

## 📄 License

This project is for educational purposes as part of the Data Visualization course. Data sourced from World Bank Open Data (CC-BY 4.0 license).

---

## 🙏 Acknowledgments

- **World Bank** for maintaining World Development Indicators
- **National Statistical Offices** for conducting household surveys
- **Course Instructor** for guidance and support
- **Python Community** for data science tools

---

## 📧 Contact

For questions about this project:

- **Course**: CS ELEC 3C - Data Visualization
- **Email**: [Your email]
- **Institution**: [Your University]

---

*Last Updated: December 2024*

**🌍 Together, we can end poverty by 2030. The data shows it's possible - let's make it happen. 🌍**
