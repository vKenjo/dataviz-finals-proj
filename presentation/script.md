# Presentation Script - SDG 1: No Poverty Analysis
## 10-Minute Presentation Guide

**Total Time: 10 minutes**  
**Slides: 1-16 (excluding backup)**

---

## SLIDE 1: Title Slide (30 seconds)

**[Display slide, wait for attention]**

Good [morning/afternoon], everyone. Today I'll be presenting my data visualization project on **UN Sustainable Development Goal 1: No Poverty**. 

Over the next 10 minutes, I'll show you how data visualization can reveal powerful insights about global poverty trends over the past 33 years, from 1990 to 2023. We'll explore which regions have succeeded, which are struggling, and what factors correlate most strongly with poverty reduction.

Let's begin.

---

## SLIDE 2: The Global Poverty Challenge (45 seconds)

**[Gesture to world map]**

Why does this matter? Currently, approximately **700 million people**—that's 9% of humanity—live in extreme poverty, surviving on less than $2.15 per day. 

While this is a significant challenge, it's also a remarkable achievement: in 1990, that figure was 36%. We've reduced global poverty by **75%** in just three decades.

**[Point to map showing poverty concentration]**

However, as this map shows, progress has been uneven. Success is concentrated in Asia, while Sub-Saharan Africa still struggles. Understanding these disparities is crucial for achieving the UN's goal of **ending poverty by 2030**.

Poverty isn't just about money—it affects **life expectancy, education, health**, and creates cycles that trap families for generations.

**[Transition]** So what questions did we seek to answer?

---

## SLIDE 3: Research Questions (30 seconds)

Our analysis addresses five key questions:

1. **How has poverty evolved** across different regions?
2. **Which countries succeeded** and which struggled—and why?
3. **What development factors**—education, health, infrastructure—correlate most with poverty reduction?
4. **How have countries transitioned** between different poverty levels?
5. And critically: **Will we meet the 2030 target** on our current trajectory?

**[Transition]** To answer these, we needed comprehensive data.

---

## SLIDE 4: Data & Methodology (45 seconds)

**[Point to table]**

We used the **World Bank's World Development Indicators**—the gold standard for global development data. From over 1,400 available indicators, we carefully selected **12 key metrics** across five dimensions:

- Poverty rate (our primary indicator)
- Education: enrollment rates and literacy
- Health: life expectancy and maternal mortality
- Infrastructure: electricity, water, and sanitation access
- Economic: GDP per capita and unemployment

Our dataset covers **200+ countries over 33 years**—that's over 500,000 data points.

**[Acknowledge challenges]**

Of course, data isn't perfect. We had missing values for some countries and years. We addressed this through interpolation for short gaps and excluded countries missing more than half their poverty data. After cleaning, we had robust data for over 150 countries.

**[Transition]** Let me show you what we discovered.

---

## SLIDE 5: Exploratory Analysis - Distributions (30 seconds)

**[Point to histogram]**

First, we explored current poverty distributions. This histogram shows that most countries today have poverty rates below 20%, with a median of just 6.8%. But notice that long tail—some countries still face poverty rates exceeding 60%.

**[Point to box plots]**

The regional comparison reveals where that tail comes from: **Sub-Saharan Africa** has a median poverty rate of 22%, while **East Asia and Pacific** is under 3%. This massive disparity drives our analysis.

**[Transition]** Now, let's dive into the main visualizations.

---

## SLIDE 6: Visualization 1 - Global Poverty Map (1 minute)

**[Point to map, describe color scheme]**

This choropleth map shows the geographic distribution of poverty in 2023. Red indicates high poverty, green indicates low.

**[Highlight regions]**

Notice the clear patterns:
- **East Asia**—almost entirely green. China, Vietnam, Thailand have achieved near-zero poverty.
- **South Asia**—mostly yellow-green, showing good progress but work remaining.
- **Sub-Saharan Africa**—predominantly red. Countries like Madagascar and Mozambique still have over 40% poverty rates.

**[Mention interactivity]**

In the interactive version, you can slide through years from 1990 to 2023 and watch East Asia transform from red to green, while Africa's progress is much slower. It's a powerful visualization of global inequality.

**[Transition]** But how did we get here? Let's look at the trends.

---

## SLIDE 7: Visualization 2 - Regional Trends Over Time (1 minute)

**[Trace the lines with pointer/hand]**

This time series chart tells a dramatic story.

**[Point to East Asia line]**

East Asia—the blue line—shows the steepest decline: from **47% to 2%**. That's a 95% reduction. This is driven almost entirely by **China**, which lifted 850 million people out of poverty—over 70% of the global total.

**[Point to South Asia line]**

South Asia—in orange—also shows strong progress: 44% down to 8%. India and Bangladesh are the success stories here.

**[Point to Sub-Saharan Africa line]**

But Sub-Saharan Africa—the red line—is the challenge. Despite falling from 54% to 35%, the **absolute number** of poor people in Africa has actually **increased** due to population growth. Africa now accounts for 60% of the world's extreme poor, up from 15% in 1990.

**[Point to annotations]**

Notice the annotations: the 2008 financial crisis caused a brief slowdown, and COVID-19 in 2020 pushed 70 million people back into poverty temporarily.

**[Transition]** Let's examine how individual countries moved between poverty categories.

---

## SLIDE 8: Visualization 3 - Sankey Diagram (1 minute)

**[Explain the diagram structure]**

This Sankey diagram shows transitions between poverty categories from 1990 to 2023. On the left are 1990 categories, on the right are 2023 categories. The width of each flow represents the number of countries.

**[Point to categories]**

We defined four categories: Extreme (≥40%), High (20-40%), Moderate (10-20%), and Low (<10%).

**[Trace green flows]**

The **green flows** represent improvement: **78 countries** moved to lower poverty categories. The largest flow is from Moderate to Low—42 countries achieved low poverty.

**[Point to stagnant gray]**

But **18 countries**—shown in gray—remained stuck in the Extreme category. Fourteen of these are in Sub-Saharan Africa.

**[Trace red flows]**

And disturbingly, **12 countries deteriorated**—the red flows. Venezuela collapsed from Low to High due to economic crisis. Syria and Yemen fell from Moderate to Extreme due to civil wars.

**[Key takeaway]**

This visualization powerfully illustrates that while most countries progressed, **conflict and governance failures can reverse decades of gains overnight**.

**[Transition]** So what separates success from failure? Let's look at the correlations.

---

## SLIDE 9: Visualization 4 - What Correlates with Poverty Reduction? (1 minute)

**[Point to table of correlations]**

We calculated statistical correlations between poverty and various development indicators. The results are striking.

**[Emphasize top two]**

The strongest correlation is with **primary school enrollment**: negative 0.78. That's a very strong relationship. Close behind is **electricity access** at negative 0.76.

**[Compare to GDP]**

Interestingly, **GDP per capita** shows only moderate correlation at negative 0.52. This is a critical finding: **education and infrastructure matter more than raw economic growth**.

**[Explain interpretation]**

What this means practically: you can have a rich country with high inequality and persistent poverty—like Nigeria with oil wealth—or a modest-income country with low poverty if growth is inclusive and invested in education and infrastructure—like Vietnam.

**[Key policy implication]**

The policy implication is clear: governments should prioritize **schools and basic services**, not just chase GDP growth numbers.

**[Transition]** Let's dive deeper into the education relationship.

---

## SLIDE 10: Visualization 5 - Education vs. Poverty (45 seconds)

**[Describe the scatter plot]**

This scatter plot shows the relationship between primary school enrollment and poverty. Each bubble is a country—size represents population, colors represent regions.

**[Point to trendline]**

The trendline clearly slopes downward. Statistically, each **1% increase in enrollment** is associated with a **0.83% decrease in poverty**. Education explains **61% of the variance** in poverty rates—that's huge.

**[Highlight examples]**

Look at **Vietnam**—95% enrollment, only 1.3% poverty. Compare that to **Nigeria**—68% enrollment, 39% poverty. The pattern is unmistakable.

**[Note interactivity]**

The animated version shows this relationship strengthening over time as more countries invested in education.

**[Transition]** Now let's look at specific country stories.

---

## SLIDE 11: Success Stories vs. Challenges (1 minute)

**[Overview the small multiples]**

These small charts show poverty trends for the 10 most populous countries—representing over half of humanity.

**[Point to success stories]**

The success stories are remarkable:
- **China**: 66% to 0.5%—essentially eliminated extreme poverty
- **Indonesia**: 54% to 3%—a 94% reduction
- **Vietnam**: 58% to 1%—stunning achievement
- **India**: 45% to 10%—still work to do, but massive progress
- **Bangladesh**: 43% to 13%—steady improvement

**[Point to challenges]**

But then we have **Nigeria**: only 46% to 39%. Despite being Africa's largest economy and an oil exporter, poverty persists. Why? Inequality, corruption, and underinvestment in education and infrastructure.

**[Key lesson]**

The lesson: **political will and inclusive policies matter**. It's not about natural resources or starting conditions—it's about choices governments make.

**[Transition]** Let's take a holistic view of regional development.

---

## SLIDE 12: Multi-Dimensional Development Assessment (45 seconds)

**[Explain radar chart]**

This radar chart compares regions across six dimensions simultaneously. The larger the polygon, the better the overall development.

**[Point to strong performers]**

**Europe & Central Asia** has a large, balanced pentagon—strong on all dimensions. **East Asia** is similar, though slightly weaker on life expectancy due to rapid aging.

**[Point to Sub-Saharan Africa]**

**Sub-Saharan Africa** has the smallest polygon, scoring low on everything: poverty reduction, education, infrastructure. The scores are in the 20-40 range while others are 80-95.

**[Policy implication]**

This visualization shows that Africa doesn't need just one intervention—it needs **comprehensive, simultaneous investment** across education, health, and infrastructure. No silver bullet exists.

**[Transition]** Now I'd like to show you the interactive dashboard briefly.

---

## SLIDE 13: Dashboard Demo (1 minute)

**[If live demo works]**

I've built an interactive web dashboard that lets you explore this data dynamically.

**[Demonstrate key features quickly]**

- **Filters**: Select specific regions or adjust the year range
- **KPI cards**: Show current global statistics
- **Interactive map**: Updates in real-time based on your selections
- **Time series**: Compare regional trends
- **Scatter plot**: Choose any indicator for the X-axis to explore different correlations

**[Mention accessibility]**

After installation, anyone can run this locally by typing `python src/dashboard.py`. All code is documented and reproducible.

**[If demo doesn't work]**

I've prepared an interactive dashboard—shown here in screenshots—that allows users to filter by region, adjust time ranges, and explore different indicator correlations dynamically. The full version is available in the project repository.

**[Transition]** Let me summarize the key insights.

---

## SLIDE 14: Key Insights & Findings (1 minute)

**[Structure: achievements, challenges, success factors]**

**Major Achievements:**
- **1.2 billion people** lifted from poverty since 1990
- A **75% reduction** in the global poverty rate
- **East Asia proved** it's possible—from 47% to 2% in one generation

**Persistent Challenges:**
- **Sub-Saharan Africa** now has 60% of the world's extreme poor
- **Conflict devastates** progress—Syria, Yemen, Haiti saw poverty spike
- **COVID-19** temporarily reversed progress, pushing 70 million back

**Critical Success Factors** we identified:
1. **Education** is paramount—strongest correlation at negative 0.78
2. **Infrastructure** enables everything—electricity, water, sanitation
3. **Inclusive growth** matters more than GDP growth alone
4. **Peace and stability**—conflict undermines all other progress

**[Address the 2030 target]**

Now, the tough question: **Will we meet the 2030 goal** of ending extreme poverty?

**[Pause for effect]**

Based on current trajectories: **unlikely**. We're on track for about 7% poverty in 2030, not the near-zero target. We'd need to **triple our reduction rate**—from 0.3 to 1.3 percentage points per year. Possible, but requires dramatic acceleration.

**[Transition]** So what should we do?

---

## SLIDE 15: Policy Recommendations (1 minute)

**[Frame as evidence-based]**

Based on our analysis, here are evidence-based recommendations:

**For Sub-Saharan Africa**—where the challenge is greatest:

1. **Universal primary education** by 2030. Our data shows education has the strongest impact.
2. **Accelerate electrification** from 48% to 90%. Electricity enables businesses, healthcare, and study.
3. **Prioritize conflict resolution** in the 15+ affected countries. Nothing else works without peace.
4. **Climate adaptation**—drought-resistant crops, early warning systems for the most vulnerable region.

**For middle-income countries:**

Focus on **inequality**—progressive taxation and targeted cash transfers. And strengthen **social safety nets**—unemployment insurance, child benefits.

**For the global community:**

**Target aid** to the most fragile states. Provide **debt relief** so countries can invest in social programs. And scale up **climate finance** for vulnerable regions.

**[Emphasize evidence]**

These aren't just opinions—they're guided by the statistical correlations and regional comparisons we've seen in the data.

**[Transition]** Let me conclude.

---

## SLIDE 16: Conclusion (1 minute)

**[Start with optimism]**

Here's what we've **proven**: Poverty **is solvable**. We lifted 1.2 billion people in 33 years. We know **what works**—education, infrastructure, inclusive growth. And we have **success stories** to learn from: China, Vietnam, Bangladesh.

**[Acknowledge the challenge]**

But the **last mile will be the hardest**. Those remaining 700 million face structural barriers: conflict, climate change, weak governance, geographic isolation. And our 2030 target is at serious risk.

**[Regional reality]**

Regional disparities are widening. While East Asia celebrates near-zero poverty, Sub-Saharan Africa is falling further behind.

**[Role of data visualization]**

**This is where data visualization matters.** It **makes the invisible visible**—patterns, disparities, success stories. It **informs evidence-based policy**—our correlation analysis guides where to invest. It **drives accountability**—dashboards track progress transparently. And compelling visuals **inspire action** and mobilize political will.

**[Final thought - pause before reading]**

I'll leave you with this thought:

> "The question is not whether we **can** end poverty—we've proven we can. The question is whether we **will**—whether we have the political will, the resources, and the commitment to ensure that by 2030, no one lives in extreme poverty."

**[Project summary]**

This project has delivered:
- Seven polished, publication-quality visualizations
- An interactive dashboard for ongoing exploration
- A comprehensive research report in ACM format
- And fully reproducible code

**[Closing]**

Thank you. I'm happy to take your questions.

---

## SLIDE 17: Questions & Discussion

**[Display contact slide, wait for questions]**

---

## HANDLING Q&A (Anticipated Questions)

### **Q: Why did you focus on $2.15/day? Isn't that arbitrary?**

**A:** Great question. The $2.15 threshold is the World Bank's international poverty line, adjusted for purchasing power parity. It's based on the national poverty lines of the poorest countries. While it's not perfect, it's the global standard that allows cross-country comparison over time. For deeper analysis, we'd want to look at multidimensional poverty indices that include health and education deprivations, which I mention as future work.

### **Q: You mentioned correlation doesn't equal causation. How confident are you about education causing poverty reduction?**

**A:** You're right to push on this. Our analysis shows strong correlation, but we can't definitively prove causation with observational data. However, there's extensive experimental and quasi-experimental literature—including randomized controlled trials—that does establish causal links between education and income. Our findings align with that literature. For this project, we're cautious to say "correlates with" rather than "causes," but the weight of evidence is strong.

### **Q: COVID-19 seems to have had less impact than expected. Why?**

**A:** Indeed, initial projections estimated 100+ million would fall into poverty. The actual figure was closer to 70 million, with partial recovery by 2023. The main reasons were unprecedented social protection responses—governments deployed cash transfers, expanded unemployment benefits, and implemented food assistance programs at a scale never seen before. It's a reminder that policy responses matter enormously.

### **Q: What can we as students/individuals do about global poverty?**

**A:** Excellent question. Direct individual actions include supporting effective charities (organizations like GiveDirectly provide cash transfers to the extreme poor). But more impactfully, advocate for evidence-based policies—contact representatives about foreign aid, trade policies, and climate action. As future tech professionals, you can contribute skills: volunteer for data analysis for NGOs, build tools for development organizations, or ensure the technologies you create don't exacerbate inequality. And perhaps most importantly: stay informed and vote for leaders committed to global development.

### **Q: Why didn't Nigeria reduce poverty despite oil wealth?**

**A:** Nigeria is a textbook case of the "resource curse." Despite being Africa's largest economy and a major oil exporter, poverty persists due to several factors: extreme inequality (oil wealth concentrated among elites), corruption that diverts resources from social programs, underinvestment in education and infrastructure, and regional conflicts. It illustrates our finding that GDP growth alone doesn't reduce poverty—inclusive growth with investment in human capital does. Countries like Botswana show it's possible to manage resource wealth well, but it requires strong institutions and governance.

### **Q: Is the dashboard available publicly?**

**A:** Currently it runs locally after installing dependencies (`pip install -r requirements.txt` then `python src/dashboard.py`). For public deployment, I'd need to host it on a platform like Heroku or Streamlit Cloud. The full code is in my GitHub repository, so anyone can run it themselves or I can deploy it if there's interest. It's fully open-source.

### **Q: What was the most surprising finding?**

**A:** I'd say two things surprised me: First, how much **stronger** the education correlation was compared to GDP—it really challenges the assumption that economic growth alone solves poverty. Second, the **Sankey diagram** showing that 12 countries actually got worse. Seeing Venezuela and Syria's collapses visualized so clearly was powerful—it shows how fragile progress can be and why peace and governance matter so much.

---

## TIMING BREAKDOWN

| Slide | Topic | Time | Cumulative |
|-------|-------|------|-----------|
| 1 | Title | 0:30 | 0:30 |
| 2 | Challenge | 0:45 | 1:15 |
| 3 | Research Q's | 0:30 | 1:45 |
| 4 | Data/Methods | 0:45 | 2:30 |
| 5 | EDA | 0:30 | 3:00 |
| 6 | Map | 1:00 | 4:00 |
| 7 | Time Series | 1:00 | 5:00 |
| 8 | Sankey | 1:00 | 6:00 |
| 9 | Correlation | 1:00 | 7:00 |
| 10 | Education | 0:45 | 7:45 |
| 11 | Countries | 1:00 | 8:45 |
| 12 | Radar | 0:45 | 9:30 |
| 13 | Dashboard | 1:00 | 10:30 |
| 14 | Insights | 1:00 | 11:30 |
| 15 | Recommendations | 1:00 | 12:30 |
| 16 | Conclusion | 1:00 | 13:30 |

**Note:** Total is 13:30 with buffer. For strict 10-minute limit, shorten slides 13-15 by 15-20 seconds each.

---

## PRESENTATION TIPS

**Delivery:**
- **Speak clearly and at moderate pace** (not rushed)
- **Make eye contact** with audience, not just reading slides
- **Use hand gestures** to point to charts/data
- **Pause for emphasis** before key statistics
- **Show enthusiasm** for the topic—your passion makes it engaging

**Technical:**
- **Test equipment** beforehand (laptop, projector, clicker)
- **Have backup** (PDF on USB drive if live dashboard fails)
- **Practice transitions** between slides (should be smooth)
- **Time yourself** during rehearsal

**Handling Nerves:**
- **Deep breaths** before starting
- **Know your first 2-3 sentences by heart** (confident start sets tone)
- **Remember: you know this material better than anyone in the room**
- **If you lose place, glance at slide title** to reorient

**Interactive Elements:**
- If doing **live demo**, have it **pre-loaded** and ready
- If demo fails, **don't panic**—refer to screenshots and move on
- **Invite questions** at natural break points if time allows

---

## GOOD LUCK!

You've done the hard work of analysis and visualization. Now just share what you've learned clearly and confidently. The data tells a powerful story—let it shine through!

