# The Perfect Lap: Predicting Optimal Pit Stops for Race Success

## Team Omega
- Tanay Singh (GitHub: TanayPratapSingh)
- Atharva Karekar (GitHub: ath1812)
- Titus Kenneth George Kirubaharan (GitHub: tkenneth2106)
- Praveer Nagaraja Byndoor (GitHub: praveerbn)
- Srikanth Mannepalli (GitHub: srikanthmannepalli0502-cmyk)

---

## Introduction
We want to answer a simple question: **When is the best time to make a pit stop in Formula 1?**  
Our goal is to use race data to predict the lap where a driver should change tires to get the best chance of winning. This is not only about how fast a pit crew works, but about **when** a pit stop should happen.

What makes our project new is that we will build models that test different pit stop timings and show which lap gives the biggest advantage. While teams already think about strategy, we will use long-term data to uncover patterns across many races.

If we are successful, our work will make a difference by showing how much pit stop timing matters. It will also show how smart decisions can save valuable seconds and change the outcome of a race.

---

## Literature Review
Recent studies have begun to use data science to understand pit stop strategy in Formula 1. **Hettmann (2024)** framed the problem as a lap-by-lap decision: should a driver pit now or not? Using race data from 2014–2021, the study built a binary classifier with features such as tyre age, race progress, safety car status, and position changes. The model was tested in simulated races, showing that data-driven methods can support strategic decisions. However, the limitation was clear: the model only gave a yes/no answer for each lap, rather than identifying the exact best lap to stop, which we aim to achieve.  
*(Link: https://search.proquest.com/openview/b75d39187ba4e5b6263fda999c4023ae/1?pq-origsite=gscholar&cbl=2026366&diss=y)*

**Fatima and Johrendt (2023)** took a different approach, using deep learning on data from 2015–2022 to train two models: one to predict finishing position and another to suggest pit stop laps. With 36 race inputs, they showed the potential of neural networks in strategy prediction. Yet their focus remained on individual race outcomes, without systematically comparing how different pit stop timings would change results across many races.  
*(Link: https://scholar.google.com/citations?view_op=list_works&hl=en&hl=en&user=LIgICmcAAAAJ)*

**Our project** builds directly on these foundations. Instead of asking whether to pit now or later, or only predicting outcomes, we aim to **identify the exact lap** that offers the greatest strategic advantage. By testing alternative pit stop timings on historical data, our models will highlight when a stop provides the biggest gain. Unlike earlier work, we shift the focus from binary choices or race-specific forecasts to uncovering broad patterns that reveal how much timing matters. In doing so, we move closer to answering the central question: **when is the best time to make a pit stop in Formula 1?**

---

## Stakeholders
- **Race Engineers (Primary):** Guide drivers during a race and decide when to pit, often under intense time pressure.
- **Drivers:** Depend on the timing of pit calls for performance and race outcome.
- **Formula 1 Teams:** Use model insights to refine long-term strategy.

---

## Data and Methods

### Data
We will use the **Formula 1 World Championship Dataset (1950–2020)**.  
- **Size:** About 250,000 records across 13 linked tables (races, results, lap times, pit stops, etc.).  
- **Features:** Race information, driver details, circuits, lap times, and pit stop data.  
- **Reliability:** Compiles official F1 records and is widely used in research and analysis.  
*(Link: https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020?select=drivers.csv)*

### Methods
1. **Data Preparation**  
   Combine race, lap, and pit stop data. Handle missing values in older races. Create new features (tire age, position at pit stop, and time lost or gained).

2. **Modeling**  
   Test models that predict how pit stop timing affects results. Use approaches like regression and decision trees to find the lap with the most benefit. Explore methods that can simulate race outcomes based on different pit stop choices.

3. **Evaluation**  
   Compare model suggestions against real race results. Measure how close our model’s “perfect lap” is to the strategy that led to winning or strong finishes.

---

## Project Plan
| Period        | Activity                                           | Milestone                          |
|---------------|----------------------------------------------------|------------------------------------|
| 9/24 – 10/8   | Explore data, clean records, create first features | Dataset ready for modeling         |
| 10/9 – 10/22  | Build first models and test on sample races        | First predictions of pit timing    |
| 10/23 – 11/5  | Improve models and test across multiple seasons    | Candidate models finalized         |
| 11/6 – 11/19  | Validate results, check accuracy, build visuals    | Results confirmed and visualized   |
| 11/20 – 12/3  | Write final report and prepare presentation        | Report and presentation submitted  |

---

## Risks
- **Missing Data:** Older races may not have full details.  
  *Plan:* Focus more on modern seasons where records are complete.
- **Complex Factors:** Weather or safety cars affect pit stops but may not be in the dataset.  
  *Plan:* Start with available features and add complexity if possible.
- **Model Accuracy:** Predictions may vary across seasons.  
  *Plan:* Test across many years to avoid overfitting.
