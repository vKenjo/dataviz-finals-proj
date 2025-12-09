# Presentation Script

## Visualizing Global Poverty Trends: SDG 1 Analysis with Focus on Philippines and ASEAN

**Duration:** 10 minutes  
**Format:** 18 slides  
**Target Audience:** CS ELEC 3C Data Visualization Course

---

## SLIDE 1: Title Slide (30 seconds)

**[Display title slide]**

Good morning/afternoon everyone. Today I'll be presenting our data visualization project on global poverty trends, specifically addressing UN Sustainable Development Goal 1: No Poverty.

Our project analyzes over 60 years of World Development Indicators data across 217 countries, with a special focus on the Philippines and ASEAN region. We'll explore how extreme poverty has evolved globally, what drives successful poverty reduction, and where the Philippines stands in this global context.

Let's begin.

---

## SLIDE 2: The Global Poverty Challenge (45 seconds)

**[Show global poverty statistics]**

The United Nations' Sustainable Development Goal 1 aims to end poverty in all its forms by 2030. Currently, about 700 million people—roughly 9% of the global population—live in extreme poverty, defined as living on less than $2.15 per day.

But here's the remarkable part: we've made unprecedented progress. In 1990, 36% of the world lived in extreme poverty. Today, that's down to just 9%. That means over 1.2 billion people have been lifted out of poverty in just three decades.

However—and this is crucial—this progress has been highly uneven across regions, which is what our analysis explores.

---

## SLIDE 3: Research Questions (45 seconds)

**[Display three-tier framework]**

Our research follows a three-tier analytical framework:

At the **GLOBAL level**, we ask: How has extreme poverty evolved from 1981 to 2024? What are the geographic patterns? And critically, which development indicators correlate most strongly with poverty reduction?

At the **ASEAN REGIONAL level**, we examine: How does the Philippines compare to its neighbors? Which ASEAN countries have been most successful, and where does the region stand relative to global trends?

Finally, at the **PHILIPPINES-SPECIFIC level**, we dive deep: What is the Philippines' current poverty status? How does it perform across multiple development dimensions? And what factors matter most for poverty reduction in our context?

This three-tier approach provides both broad context and specific, actionable insights.

---

## SLIDE 4: Dataset Overview (45 seconds)

**[Show dataset specifications]**

Our analysis uses the World Bank's World Development Indicators—the most comprehensive dataset on global development. It covers 217 countries and territories from 1960 to 2024, with over 1,000 indicators spanning education, health, economy, and infrastructure.

For our analysis, we selected 13 key indicators including poverty headcount, GDP per capita, life expectancy, electricity access, and school enrollment rates.

Now, here's an important reality check: while the World Bank tracks 217 countries, only 169 have poverty measurements. 48 countries lack this data entirely. And even among those with data, the latest available year varies from 2018 to 2024. This data limitation is important context for interpreting our findings.

Despite these gaps, the dataset provides unprecedented insights into global poverty patterns.

---

## SLIDE 5: Methodology - Data Preparation (40 seconds)

**[Display methodology steps]**

Our data preparation involved four key steps:

First, we imported and filtered the raw WDI data, selecting our 13 key development indicators across all 217 countries and 65 years of data.

Second, we systematically documented missing data. We discovered that only 7 of 11 ASEAN countries have poverty data, which constrained our regional analysis.

Third, we categorized countries into regional groups—ASEAN members, developed nations, and global benchmarks—to enable meaningful comparisons.

Finally, we applied statistical techniques including Pearson correlation analysis, time-series trend analysis, and multi-dimensional comparisons. This rigorous approach ensures our conclusions are data-driven, not anecdotal.

---

## SLIDE 6: Methodology - Visualizations (40 seconds)

**[Show visualization types]**

From this prepared data, we created five publication-quality visualizations, each answering specific research questions:

**First**, an interactive choropleth map showing global poverty distribution across 169 countries, revealing geographic patterns at a glance.

**Second**, a time-series line chart tracking ASEAN poverty trends over time, with the Philippines highlighted against the regional average.

**Third**, a correlation heatmap quantifying relationships between poverty and development indicators, with statistical significance testing.

**Fourth**, a radar chart providing a multi-dimensional comparison of the Philippines versus ASEAN average across six development dimensions.

And **fifth**, an interactive dashboard specifically for the Philippines, showing temporal evolution across poverty, GDP, education, and infrastructure.

Each visualization was designed not just to look good, but to answer specific research questions with clarity and statistical rigor.

---

## SLIDE 7: Exploratory Data Analysis (35 seconds)

**[Display EDA findings]**

Before creating our final visualizations, we conducted exploratory data analysis to understand data distributions and patterns.

We created distribution histograms for four key indicators—poverty, GDP, life expectancy, and electricity access—comparing global patterns, ASEAN countries, and the Philippines specifically. This revealed high global variance in poverty rates, ranging from 0% to over 85%.

Our temporal heatmap of 15 countries showed clear poverty reduction patterns over time, with ASEAN countries prioritized in the selection.

Regional boxplots confirmed what we suspected: the global median poverty is 2.7%, ASEAN median is 5.4%, and the Philippines sits at 5.3%—slightly better than ASEAN average but above the global benchmark.

These exploratory findings guided our final analysis.

---

## SLIDE 8: Global Poverty Landscape (50 seconds)

**[Show choropleth map results]**

Now let's examine our first major finding: the global poverty landscape.

Our choropleth map visualization reveals that 169 countries have poverty data, while 48 lack measurements. The global median poverty rate is 2.7%, but the mean is 14%—showing the distribution is skewed by high-poverty outliers.

The geographic patterns are striking: Sub-Saharan Africa shows the highest concentrations, with many countries above 40% poverty. East Asia demonstrates remarkable success stories—China and Vietnam are now below 1%. Latin America shows moderate rates between 5-15%, while Europe and North America have achieved near-zero extreme poverty.

Most importantly, the historical trend is dramatic: in 1981, global average poverty was 17.22%. By 2024, it had fallen to just 4.23%—a reduction of nearly 13 percentage points over 43 years.

This proves poverty reduction is achievable, but the uneven distribution shows the challenge isn't solved everywhere.

---

## SLIDE 9: ASEAN Regional Analysis (50 seconds)

**[Display ASEAN table and trends]**

Zooming into our region, the ASEAN picture shows remarkable diversity.

Of the 11 ASEAN member states, only 7 have poverty data. Among these, the spread is enormous: Malaysia and Thailand have achieved zero extreme poverty—a remarkable accomplishment. The Philippines sits at 5.3%, just below Indonesia at 5.4%. Myanmar is at 10.3%, Lao PDR at 15.7%, and Timor-Leste faces severe challenges at 43.9%.

The ASEAN median of 5.4% is notably higher than the global median of 2.7%. This suggests our region, despite strong economic growth, still has work to do on poverty reduction.

For the Philippines specifically, the 5.3% rate is encouraging—we're performing slightly better than the regional median. However, the existence of zero-poverty ASEAN neighbors like Malaysia and Thailand proves that complete poverty elimination is achievable in our regional context. They provide both inspiration and practical models we can learn from.

The question becomes: what did they do differently?

---

## SLIDE 10: What Drives Poverty Reduction? (1 minute)

**[Show correlation matrix results]**

This slide presents perhaps our most important finding: what actually drives poverty reduction?

We calculated Pearson correlation coefficients between poverty and three key development indicators using our complete dataset. The results challenge conventional wisdom.

**Electricity access** shows a correlation of minus 0.847 with poverty—that's very strong and highly statistically significant.

**Life expectancy** correlates at minus 0.786—also very strong.

But here's the surprise: **GDP per capita** correlates at only minus 0.397—less than half the strength of infrastructure access.

What does this mean practically? Infrastructure access matters **more than twice as much** as income growth for poverty reduction. This is a critical insight that challenges the traditional "grow the economy and poverty will follow" approach.

The health connection at minus 0.786 tells us that healthy populations escape poverty faster—perhaps because health enables work, education, and economic participation.

The takeaway is clear: successful poverty reduction requires a multi-dimensional approach. You can't just grow GDP and hope poverty decreases. You need simultaneous progress in infrastructure access, health systems, AND economic growth. Countries that succeed—like Malaysia and Thailand—invested in all three simultaneously.

---

## SLIDE 11: Philippines in Context (45 seconds)

**[Display radar chart]**

So where does the Philippines fit in this multi-dimensional landscape?

Our radar chart compares the Philippines against the ASEAN average across six development dimensions, with all values normalized to a 0-1 scale for fair comparison.

The Philippines shows a **balanced development profile**. We're comparable to ASEAN average across most indicators. Our strength is in infrastructure, particularly electricity access. Education enrollment rates track closely with regional averages. We're neither a leader nor a laggard—we're right in the middle.

At 5.3% poverty in 2023, we're slightly below the ASEAN median of 5.4%, which is positive. However, we remain above the global median of 2.7%.

The critical insight here: the Philippines has the **foundation** for success. Our development indicators are balanced and comparable to the region. We have clear role models in Malaysia and Thailand who achieved zero poverty with similar starting points. The infrastructure correlation we identified shows us where to focus effort.

The path to 0% poverty isn't theoretical—our neighbors proved it's possible.

---

## SLIDE 12: Philippines Deep Dive (45 seconds)

**[Reference interactive dashboard]**

Our interactive dashboard provides a four-panel deep dive into Philippine development trends over time.

The **poverty panel** shows a declining trajectory over recent decades, but with recent stabilization around 5%. This plateau is worth investigating.

The **economic panel** reveals steady GDP per capita growth—our economy has been expanding consistently.

The **education panel** shows high primary enrollment above 95%, with secondary enrollment steadily improving.

The **infrastructure panel** demonstrates expanding electricity access, which aligns with our correlation finding about infrastructure's importance.

But here's the puzzle this dashboard reveals: Why hasn't our steady GDP growth translated to faster poverty reduction? Indonesia, a similar ASEAN neighbor, achieved an 80.8% poverty reduction. Vietnam, though data is missing in our dataset, is known to have dropped from 50% to under 2%.

This suggests that while our economic growth is real, it may not be **inclusive** enough—the benefits aren't reaching the bottom 5.3% as effectively as they could. This points to distribution and access issues, not just growth issues.

---

## SLIDE 13: Global Progress Tracking (45 seconds)

**[Display success stories and challenges]**

Taking a global view of progress, we categorized 120 countries with sufficient time-series data into three groups:

**54.2%**—65 countries—are **improving**, with greater than 5% poverty reduction. This is the majority, which is encouraging.

**40.8%**—49 countries—are **stable**, with changes within plus or minus 5%.

**5%**—just 6 countries—are **worsening**, with poverty increases greater than 5%.

The top success stories are remarkable: China achieved a 97% poverty reduction—nearly complete elimination. Indonesia, our ASEAN neighbor, achieved 80.8% reduction. Nepal 80.3%, Uzbekistan 77.1%, Guinea 74.7%.

The challenges are concentrated in conflict zones and fragile states: Syria saw a 15.3% increase due to war. Kenya, Malawi, Zambia, and Madagascar also saw increases.

Two insights here: First, the **majority of the world is moving in the right direction**—54% improving is a positive signal. Second, Indonesia's success is particularly relevant for the Philippines. We share similar regional context, development challenges, and starting conditions. If they reduced poverty by 80.8%, what can we learn from their approach?

---

## SLIDE 14: Key Findings Summary (50 seconds)

**[Display four-quadrant summary]**

Let me synthesize our key findings across four dimensions:

**At the GLOBAL level**: Poverty dropped from 17.22% to 4.23% between 1981 and 2024. Over 1 billion people escaped extreme poverty. But 700 million remain, so the job isn't finished.

**Our CRITICAL INSIGHTS** from statistical analysis: Infrastructure access (correlation -0.847) matters more than GDP growth (-0.397) for poverty reduction. Health outcomes matter enormously (correlation -0.786). Success is demonstrably possible—Malaysia, Thailand, and Indonesia proved it. And the majority—54%—of countries are actively improving.

**For the PHILIPPINES specifically**: At 5.3% poverty, we're below ASEAN median but above global median. Our development indicators are balanced—we're not failing in any dimension, but not excelling either. Most importantly, we have a clear path to 0% poverty by following regional models.

**For ASEAN as a region**: The diversity is striking—0% in Malaysia and Thailand versus 43.9% in Timor-Leste. Our regional median of 5.4% exceeds the global median of 2.7%, indicating regional improvement potential.

The overarching conclusion: poverty elimination is not aspirational—it's achievable. But it requires the right approach: infrastructure + health + inclusive growth simultaneously.

---

## SLIDE 15: Policy Recommendations (1 minute)

**[Display recommendations]**

Based on our data-driven analysis, here are evidence-based policy recommendations:

**For the Philippines**, four priorities:

**First**, accelerate infrastructure investment. Given the strongest correlation at -0.847, this is the highest-impact lever. Expand beyond electricity to include digital infrastructure, transport networks, and water systems. Infrastructure enables economic participation.

**Second**, learn from success stories. Malaysia and Thailand achieved zero poverty—study their strategies systematically. Indonesia reduced poverty by 80.8%—what specific policies drove that? These aren't distant examples; they're ASEAN neighbors with similar contexts.

**Third**, strengthen health systems. The life expectancy correlation of -0.786 tells us health investment pays poverty reduction dividends. Focus on primary healthcare access, particularly in underserved areas.

**Fourth**, move beyond GDP-centric policies. Our data shows GDP correlation is only -0.397—much weaker than infrastructure. This means economic growth alone won't eliminate the remaining 5.3%. We need targeted interventions focused on distribution and access, not just aggregate growth.

**For the ASEAN region**: Support Timor-Leste, which faces 43.9% poverty, through coordinated regional assistance. Establish a formal best-practice sharing mechanism—Malaysia and Thailand have expertise to share. Improve data collection—4 countries lack poverty measurements, making progress tracking impossible. Address regional inequality—our median of 5.4% should be brought down to global levels of 2.7%.

These aren't theoretical recommendations—they're directly derived from statistical patterns in our data.

---

## SLIDE 16: Limitations & Future Work (45 seconds)

**[Display limitations transparently]**

In the spirit of scientific rigor, let me acknowledge our limitations and outline future research directions.

**Data limitations**: 22% of countries lack poverty data entirely. Within ASEAN, only 7 of 11 countries have measurements. The "latest year" approach means we're comparing 2024 data for some countries with 2018 data for others. National-level data masks important sub-national disparities—poverty in Metro Manila versus Mindanao, for example.

**Methodological constraints**: Correlation does not prove causation. While we found strong correlations, we haven't established causal mechanisms. Our analysis is cross-sectional comparison, not panel regression. We're limited to available WDI indicators—important factors like governance quality, corruption, social protection systems aren't captured.

**Future research should include**: First, causal analysis using panel regression and instrumental variables to move from correlation to causation. Second, sub-national mapping—where exactly is poverty concentrated within countries? Third, forecasting to project 2030 SDG trajectories. Fourth, multi-dimensional poverty measures beyond just income. Fifth, machine learning to identify poverty risk factors. Sixth, climate vulnerability analysis. And seventh, a specific Vietnam case study to understand their remarkable success.

These limitations don't invalidate our findings, but they define the boundaries of what we can confidently claim.

---

## SLIDE 17: Conclusion (50 seconds)

**[Display conclusion with key quote]**

Let me conclude with the big picture.

**What we've proven**: Poverty elimination is not aspirational—it's achievable. The data proves this. Infrastructure and health matter more than income growth alone. Regional success stories provide practical roadmaps. And the Philippines has both the foundation and clear examples to follow.

**The 2030 Challenge**: We have 6 years to reach the SDG deadline. Global average is 4.23%—we need near-zero. Philippines at 5.3% has a clear path to 0% based on Malaysia and Thailand models. But 700 million people globally are still waiting.

Here's our critical insight, and I'll quote from our analysis: "The question is not WHETHER poverty can be eliminated—the data shows it can—but WHETHER we will summon the political will and resource allocation to complete the journey."

For the Philippines specifically, the opportunity is clear: We have balanced development indicators—check. We have regional role models who started where we are—check. We've identified the strongest correlation factors, particularly infrastructure—check. The foundation is set. What's needed now is execution.

The data provides both hope and urgency. Hope because remarkable progress has been achieved and we know what works. Urgency because we're 6 years from the 2030 deadline and 700 million people are counting on us.

---

## SLIDE 18: Thank You / Q&A (Remaining time)

**[Display final slide with resources]**

Thank you for your attention. I'm happy to take questions.

**[Prepared Q&A responses below]**

---

## ANTICIPATED Q&A RESPONSES

### Q: "Why is the Philippines' poverty reduction slower than Indonesia's?"

**A:** Great question. While our analysis shows correlation patterns, not causation, we can point to some differences in the data. Indonesia invested heavily in rural infrastructure—electricity, roads, irrigation—starting in the 1990s. They also implemented aggressive rice price stabilization policies that protected rural incomes. Their poverty reduction accelerated dramatically after the 1997 Asian Financial Crisis recovery.

For the Philippines, our GDP growth has been strong, but our correlation analysis suggests it hasn't been as inclusive. The infrastructure correlation of -0.847 suggests Indonesia's infrastructure focus may have been key. Future research with panel regression could establish whether this is causal, but the correlation is suggestive.

---

### Q: "How confident are you in the data given the missing countries?"

**A:** Excellent methodological question. We have 169 of 217 countries with poverty data—that's 78% coverage. More importantly, those 169 countries represent over 95% of the global population. The missing 48 countries are mostly small island nations, microstates, or conflict zones where data collection is infeasible.

For ASEAN specifically, the 7 of 11 coverage is limiting, and I acknowledge that. Missing Vietnam is particularly frustrating given their known success story. However, the 7 we have represent the region's largest economies and populations.

The correlations we calculated used all available data points across years and countries—tens of thousands of observations—so they're statistically robust. But yes, complete coverage would be better, and we documented these gaps transparently in our limitations section.

---

### Q: "What about inequality within countries? Doesn't that matter?"

**A:** Absolutely critical point. Our analysis uses national-level aggregates, which masks within-country inequality. A country can have low average poverty but high inequality and concentrated pockets of extreme poverty.

This is actually a recognized limitation of the $2.15/day extreme poverty line—it measures the bottom but not the distribution. Future work should incorporate Gini coefficients, income quintile shares, and sub-national data.

For the Philippines specifically, we know poverty rates vary dramatically—Metro Manila versus Eastern Visayas versus BARMM. Our national 5.3% masks that variation. A sub-national analysis would be a valuable extension of this work, and the data exists in PSA's Family Income and Expenditure Survey to do it.

---

### Q: "Why did you focus on electricity access when other infrastructure might matter too?"

**A:** We analyzed electricity access because it had the best data coverage in the WDI dataset—most countries report it consistently. But you're absolutely right that other infrastructure matters.

The correlation of -0.847 for electricity is likely a **proxy** for broader infrastructure development. Countries that achieve high electricity access typically also invest in roads, water systems, telecommunications, etc. Electricity is measurable and correlates with this broader bundle.

That said, electricity specifically is foundational—it enables refrigeration for agriculture, lighting for evening study, power for small businesses. It's both directly impactful and indicative of broader infrastructure investment.

Ideally, we'd analyze roads, water, internet access separately, but data coverage is much spottier. Electricity gave us the broadest comparable dataset.

---

### Q: "How do you account for COVID-19's impact on poverty?"

**A:** Important context. The World Bank documented that 2020 saw the first increase in extreme poverty in a generation due to COVID-19—estimates suggested 70-100 million people fell back into poverty.

Our data uses "latest available year" which varies by country—some 2018, some 2023, some 2024. Countries with 2023-2024 data reflect post-COVID recovery to some extent. The Philippines' 5.3% figure is from 2023, so it includes COVID impact and partial recovery.

The 1981 to 2024 trend shows overall dramatic reduction despite COVID. It's a temporary setback in a decades-long positive trajectory. But it does underscore poverty progress fragility—a single shock can reverse years of gains. This argues for social protection systems and economic resilience, not just poverty reduction measures.

---

### Q: "What's the single most important action the Philippines should take?"

**A:** Based purely on our data analysis: **infrastructure investment**, specifically expanding access in the bottom poverty quintile.

The correlation coefficient of -0.847 is remarkably strong for social science. While correlation isn't causation, the magnitude suggests it's worth testing. Targeted infrastructure expansion—electricity, internet, transport—in underserved areas would likely have high poverty reduction impact.

But—and this is crucial—it can't be infrastructure **alone**. The health correlation of -0.786 and the moderate GDP correlation suggest we need simultaneous action: infrastructure + health + inclusive economic policies.

If I had to pick **one** action, it's infrastructure because it's the strongest correlation and it's actionable—we can measure it, track it, and invest in it directly. But holistically, the data argues for a three-pillar approach.

---

### Q: "Are the visualizations available for us to interact with?"

**A:** Yes! All our visualizations are in the `/figures` directory:

- The interactive choropleth map is `viz_01_choropleth.html`—you can open it in any browser and hover over countries
- The Philippines dashboard is `viz_05_philippines_dashboard.html`—also fully interactive
- Static visualizations (trends, correlation matrix, radar chart) are PNG files
- All the code to generate them is in `FINAL_PROJECT.ipynb`

The interactive ones use Plotly, so you can zoom, pan, hover for details. Feel free to explore them—that's the advantage of data viz over static tables.

---

## TIMING CHECKPOINT

**Total presentation time should be approximately:**

- Slides 1-7 (Intro & Methodology): ~5 minutes
- Slides 8-13 (Results): ~4.5 minutes
- Slides 14-18 (Findings & Conclusion): ~2.5 minutes
- **Total: ~12 minutes of content**

For a 10-minute presentation slot, remove Slide 7 (EDA details) and condense Slide 16 (limitations) to save ~1.5 minutes.

---

## PRESENTATION TIPS

**Delivery Notes:**

1. **Speak to the data, not the slides** - audience can read; you provide insight
2. **Use "we" for findings** - shows team collaboration
3. **Pause after key statistics** - let numbers sink in (e.g., "17.22% to 4.23%... pause... that's over a billion people")
4. **Point to visualizations** - "As you can see on the choropleth map..." (if displaying)
5. **Maintain eye contact** - don't read slides verbatim
6. **End strong** - the closing quote is powerful; deliver it with conviction

**If running over time:**

- Skip Slide 7 (EDA) - it's setup, not findings
- Condense Slide 16 (limitations) to 20 seconds
- Tighten Q&A responses to 30 seconds each

**If running under time:**

- Expand Slide 12 (Philippines dashboard) with more detailed interpretation
- Add personal reflection in conclusion about Philippines' potential
- During Q&A, volunteer to discuss methodology in more depth

---

**END OF PRESENTATION SCRIPT**
