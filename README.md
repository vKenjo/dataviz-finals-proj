# SDG 1: No Poverty - Comparative Analysis

## Poverty Rates in Developed Nations vs. Southeast Asia with Focus on the Philippines

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📋 Project Overview

This project analyzes global poverty rates using World Development Indicators (WDI) data from the World Bank, addressing **UN Sustainable Development Goal 1: No Poverty**. The analysis compares poverty reduction trajectories between developed nations and Southeast Asian countries, with special emphasis on the Philippines.

### Key Research Questions

1. How do poverty rates in SEA countries compare to developed nations over time?
2. Why has the Philippines lagged behind its regional peers in poverty reduction?
3. What are the trajectories and velocities of poverty reduction across different country groups?
4. What policy insights can be drawn from successful poverty reduction stories?

---

## 🗂️ Project Structure

```
finals/
├── SDG1_Poverty_Analysis.ipynb  # Main analysis notebook
├── README.md                     # This file
├── data/
│   └── data.csv                 # World Development Indicators data
├── figures/                      # Generated visualizations (auto-created)
│   ├── eda_histogram_poverty_distribution.png
│   ├── eda_boxplot_comparison.png
│   ├── eda_heatmap_sea_temporal.png
│   ├── viz1_timeseries_sea_poverty.png
│   ├── viz2_developed_vs_sea_comparison.png
│   ├── viz3_philippines_deep_dive.png
│   ├── viz6_correlation_heatmap.png
│   └── analysis_summary_dashboard.png
└── output/                       # Exported data tables (auto-created)
    ├── poverty_reduction_summary.csv
    ├── philippines_gap_analysis.csv
    ├── latest_poverty_rates.csv
    └── cleaned_poverty_data.csv
```

---

## 🚀 Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Jupyter Notebook or JupyterLab
- pip package manager

### Installation Steps

1. **Clone or download the repository**
   ```bash
   cd /path/to/finals
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On macOS/Linux
   # or
   .venv\Scripts\activate     # On Windows
   ```

3. **Install required packages**
   ```bash
   pip install pandas numpy matplotlib seaborn plotly scipy scikit-learn statsmodels kaleido
   ```

4. **Launch Jupyter Notebook**
   ```bash
   jupyter notebook SDG1_Poverty_Analysis.ipynb
   ```

5. **Run all cells**
   - Click `Kernel` → `Restart & Run All`
   - Or press `Shift+Enter` to run cells sequentially

---

## 📊 Data Source

**World Development Indicators (WDI)**
- **Source**: World Bank Open Data
- **URL**: https://data.worldbank.org/indicator
- **Indicator**: `SI.POV.DDAY` - Poverty headcount ratio at $2.15 a day (2017 PPP)
- **Coverage**: ~200 countries, 1960-present
- **Format**: CSV

---

## 📈 Visualizations

The notebook generates 6+ polished visualizations:

| # | Visualization | Type | Purpose |
|---|---------------|------|---------|
| 1 | SEA Poverty Trends | Time Series | Show poverty reduction trajectories |
| 2 | Developed vs SEA Comparison | Dual-axis Line + Bar | Compare regional averages |
| 3 | Philippines Deep-Dive | 4-panel Dashboard | Detailed country analysis |
| 4 | Choropleth Map | Interactive (Plotly) | Geographic visualization |
| 5 | Animated Bar Chart | Interactive (Plotly) | Temporal ranking changes |
| 6 | Correlation Heatmap | Matrix | Multi-indicator relationships |

---

## 🔑 Key Findings

1. **Regional Disparity**: Developed nations maintain near-zero poverty (<2%), while SEA shows higher but improving rates

2. **Success Stories**: 
   - Thailand & Malaysia achieved near-zero poverty by mid-2000s
   - Vietnam: 57.5% (1992) → 1.3% (2020) - remarkable 98% reduction

3. **Philippines Challenge**:
   - Slower reduction rate (~1.1 pp/year vs regional ~2.5 pp/year)
   - Consistently above SEA average
   - Latest rate: 8.3% (2018)

4. **SDG 1 Outlook**: Achievable for most SEA countries with targeted interventions

---

## 👥 Team Members

[Add your team member names here]

---

## 📚 References

1. World Bank. (2023). *Poverty and Shared Prosperity 2022*
2. Asian Development Bank. (2023). *Key Indicators for Asia and the Pacific*
3. Philippine Statistics Authority. (2022). *Official Poverty Statistics*
4. United Nations. (2015). *The 2030 Agenda for Sustainable Development*

---

## 📄 License

This project is for educational purposes as part of the Data Visualization course.

---

*Last Updated: December 2024*
