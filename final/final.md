# The Perfect Lap: Predicting Optimal Pit Stops for Race Success

## Introduction

This project addresses a fundamental question in Formula 1 racing: *When is the optimal time to make a pit stop?* Our goal is to leverage historical race data to predict the lap where a driver should take a pit stop to maximize their chances of achieving the best possible race outcome. This analysis is a decision that can determine race outcomes in a sport where milliseconds matter.

**Primary Stakeholder:**

- Race Engineers (Primary): Guide drivers during a race and decide when to pit, often under intense time pressure.
- Drivers: Depend on the timing of pit calls for performance and race outcome.
- Formula 1 Teams: Use model insights to refine long-term strategy.

The significance of this problem lies in the complexity of pit stop timing. Teams must balance multiple factors: tire degradation, track position, fuel weight, weather conditions, and competitor strategies. While teams currently rely on experience and real-time telemetry, our project aims to uncover historical patterns across many races that can inform better strategic decisions. By building predictive models that identify the optimal pit lap based on race conditions, driver characteristics, and circuit features, we provide race engineers with an additional analytical tool to complement their expertise.

## Literature Review

Recent studies have begun to use data science to understand pit stop strategy in Formula 1. **Hettmann (2024)** framed the problem as a lap-by-lap decision: should a driver pit now or not? Using race data from 2014–2021, the study built a binary classifier with features such as tyre age, race progress, safety car status, and position changes. The model was tested in simulated races, showing that data-driven methods can support strategic decisions. However, the limitation was clear: the model only gave a yes/no answer for each lap, rather than identifying the exact best lap to stop, which we aim to achieve.

*(Link: https://search.proquest.com/openview/b75d39187ba4e5b6263fda999c4023ae/1?pq-origsite=gscholar&cbl=2026366&diss=y)*

**Fatima and Johrendt (2023)** took a different approach, using deep learning on data from 2015–2022 to train two models: one to predict finishing position and another to suggest pit stop laps. With 36 race inputs, they showed the potential of neural networks in strategy prediction. Yet their focus remained on individual race outcomes, without systematically comparing how different pit stop timings would change results across many races.

*(Link: https://scholar.google.com/citations?view_op=list_works&hl=en&hl=en&user=LIgICmcAAAAJ)*

**Our project** builds directly on these foundations. Instead of asking whether to pit now or later, or only predicting outcomes, we aim to **identify the exact lap** that offers the greatest strategic advantage. By testing alternative pit stop timings on historical data, our models will highlight when a stop provides the biggest gain. Unlike earlier work, we shift the focus from binary choices or race-specific forecasts to uncovering broad patterns that reveal how much timing matters. In doing so, we move closer to answering the central question: **when is the best time to make a pit stop in Formula 1?**

## Data and Methods

### Data

We utilized the Formula 1 World Championship Dataset (1950–2020), a comprehensive collection of official F1 records widely used in research and analysis. The dataset is available on Kaggle at: [Formula 1 World Championship Dataset](https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020)

#### Dataset Characteristics

- **Size:** Approximately 250,000 records across 13 linked tables
- **Tables Used:** races, results, pitstops, drivers, constructors, and custom track_features
- **Temporal Scope:** Filtered to races from year 2000 onwards to focus on modern F1 era
- **Final Dataset:** 14,000+ driver-race records with 45 integrated features after cleaning

#### Data Cleaning

The raw F1 data presented several challenges requiring systematic cleaning:

- **Invalid Pit Stop Records:** Removed unrealistic pit laps (below lap 1 or above lap 40) as these represent data entry errors - actual F1 pit stops occur within this range.
- **Missing Target Variables:** Imputed data with missing first pit lap values since this is our prediction target.
- **Race Quality Filtering:** Removed drivers with excessive pit stops (>2 per race) and early DNFs (Did Not Finish) to focus on normal strategic patterns.
- **Pit strategy:** grid position, race year, circuit characteristics, and team/driver identifiers

#### Imputation Strategy

A critical challenge involved missing pit stop information, particularly for races before 2012 when data collection was less systematic. Simply deleting these rows would have reduced our dataset from 10,000 to only 3,000 records, severely limiting model training.

We implemented a Random Forest-based imputation approach to estimate missing pit stop laps. This method was selected because Random Forest effectively handles complex non-linear patterns (such as "high tire wear + long race = earlier pit stop"), works with mixed categorical and numerical features, and provides reasonable uncertainty estimates.

The imputation model used six key predictors: driver ID, constructor ID, race year, starting grid position, total race laps, and circuit ID.

### Methods

#### Feature Engineering

After extensive testing of various feature combinations, we selected the following final feature set:

1. **year and round:** Capture changes in regulations and tire strategies over time
2. **circuitId:** Each track has different tire wear characteristics and pit lane configurations
3. **driverId and constructorId:** Different drivers and teams follow distinct strategic patterns
4. **grid:** Starting position influences early race decisions and undercut/overcut strategies
5. **laps:** Total race length defines pit window boundaries
6. **pit_stop_count:** Number of planned stops influences timing of first stop
7. **track_length_km and race_distance_km:** Track characteristics influence stint length optimization
8. **tyre_deg_level:** Quantifies how quickly tires degrade on each circuit
9. **pit_lane_loss:** Time penalty for entering the pit lane, varies by circuit

#### Model Pipeline

Our modeling pipeline consisted of:

1. **Data Preprocessing:** Feature scaling, encoding categorical variables, handling missing values
2. **Model Training:** Testing multiple algorithms with cross-validation
3. **Hyperparameter Tuning:** Grid search for optimal parameters
4. **Model Evaluation:** Using MAE, RMSE, and R² metrics
5. **Feature Importance Analysis:** SHAP values for interpretability

#### Algorithm Selection

We tested four algorithms based on their suitability for regression with tabular data:

- **Decision Tree:** Baseline model providing interpretable rules
- **Random Forest:** Ensemble method reducing overfitting through bootstrap aggregation
- **Extra Trees:** Higher randomization for potentially better generalization
- **Gradient Boosting:** Sequential error correction for improved accuracy

We deliberately avoided neural networks and SVMs because they are computationally expensive and generally less effective for structured tabular data with mixed feature types compared to tree-based ensembles.

## Supporting Files

The following Jupyter notebooks contain detailed analyses supporting this report:

1. **mergeData.ipynb:** Data loading, initial exploration, and merging of the 13 F1 tables
2. **data_cleaning.ipynb:** Handling missing values, removing outliers, filtering to post-2000 races
3. **impute_pits.ipynb:** Random Forest imputation for missing pit lap values with validation metrics
4. **model_ET:** Trained and Tested Extra Trees model
5. **model_catboost:** Trained and Tested catboost model
6. **model_gbr:** Trained and Tested gradient descent model
7. **randomForestModel:** Trained and Tested Random forest model
8. **Verify_imputer:** Validation of imputed values
9. **F1_random_forest_model:** Final position rf model based on optimal pit lap
10. **Team_omega_rf_app:** Main Interface output

## Results

### Model Performance

We trained and evaluated four different machine learning algorithms to predict optimal F1 pit stop timing. All models were tested using identical data splits and evaluation metrics to ensure fair comparison.

| Model | MAE | RMSE | R² |
|-------|-----|------|-----|
| Random Forest | **2.78** | **3.65** | **0.87** |
| Extra Trees | 3.12 | 4.01 | 0.84 |
| Gradient Boosting | 3.45 | 4.23 | 0.82 |
| Decision Tree | 4.89 | 5.97 | 0.71 |

### Feature Importance Analysis

SHAP (SHapley Additive exPlanations) analysis revealed the following feature importance hierarchy. The most influential features were: laps (total race length), pit_stop_count (planned number of stops), year (capturing rule changes), round (season timing), and grid (starting position). Driver and constructor identities had smaller importance values, suggesting that pit decisions are driven more by race structure and conditions than by individual driver or team preferences. This finding has practical implications: it suggests that race engineers should weight situational factors more heavily than historical driver-specific patterns when making pit timing decisions.

## Deployment Files

- **team_omega_complete_predictor.py** - Production Streamlit web application
- **final_position_model.py** - Extended model for final race position prediction
- **f1_random_forest_model.pkl** - Serialized trained Random Forest model for deployment
- **model_features.pkl** - Feature names and preprocessing specifications

## Guide to Run the Project

1. Install Streamlit: `pip install streamlit`
2. Run command: `streamlit run team_omega_rf_app.py`

## Discussion

This project successfully achieved its primary goal of developing predictive models for optimal pit stop timing in Formula 1 racing. By analyzing 20 years of race data and engineering domain-relevant features, we created models that capture the complex relationships governing pit strategy decisions.

The results directly address our stakeholder needs. Race engineers require rapid, data-informed guidance during races when split-second decisions can determine outcomes. Our Random Forest model provides predictions that encode patterns from thousands of historical race-driver combinations, supplementing engineers' real-time telemetry and experience with historical pattern recognition. The SHAP analysis additionally offers interpretability, allowing engineers to understand which factors most strongly influence the model's recommendations.

The finding that race structure features outweigh driver/team identity in importance has strategic implications. It suggests that while teams may have distinct strategic philosophies, the optimal pit window is largely determined by circuit characteristics, race length, and planned stop count. This insight encourages engineers to adapt their strategies more dynamically to race conditions rather than relying heavily on historical team tendencies.

The imputation strategy proved crucial for maintaining dataset size. Without it, we would have lost approximately 70% of our data, significantly compromising model training. The 6-lap MAE for imputed values, while not negligible, is acceptable given that pit windows in F1 typically span 10-15 laps, and strategic variation between drivers in the same race often exceeds this margin.

## Limitations

**Missing Real-Time Variables:** Our model does not incorporate live race factors such as weather changes, safety car deployments, or real-time tire degradation telemetry. These dynamic elements significantly influence actual pit decisions and represent information asymmetry between our static model and real race conditions.

**Imputation Uncertainty:** The 6-lap MAE for imputed pit stops introduces noise into training data. While we validated the imputation model, some imputed values may not reflect actual historical decisions, potentially teaching the model incorrect patterns.

**Historical Data Relevance:** F1 regulations change frequently. Tire compounds, pit stop rules, and car aerodynamics have evolved substantially over our 2000-2020 dataset period. Patterns from early 2000s races may not apply to current regulations, potentially diluting model accuracy for contemporary strategy prediction.

**Single-Stop Focus:** Our model predicts only the first pit stop lap, not complete multi-stop strategies. In races with 2-3 stops, the timing of subsequent stops depends on the first stop's timing, creating interdependencies our current approach does not capture.

**Competitor Interactions:** Pit strategy is often reactive to competitor actions. Our model does not incorporate opponent positions, gap sizes, or predicted competitor pit windows, which race engineers heavily consider in real-world decisions.

## Future Work

**Real-Time Integration:** Develop a system that combines our historical pattern model with live telemetry feeds, updating predictions as race conditions evolve. This would require streaming data infrastructure and dynamic model updating capabilities.

**Multi-Stop Strategy Modeling:** Extend the approach to predict complete pit strategies rather than just the first stop. This could involve sequence-to-sequence models or reinforcement learning approaches that optimize cumulative race time across multiple stops.

**Competitor Simulation:** Incorporate game-theoretic elements that model competitor behavior. Predicting when rivals will pit enables strategic undercuts and overcuts, a key element of modern F1 strategy.

## References

Hettmann, N. (2024). Data-driven pit stop strategy in Formula 1. *ProQuest Dissertations*. Retrieved from https://search.proquest.com/openview/b75d39187ba4e5b6263fda999c4023ae/

Fatima, S., & Johrendt, J. (2023). Deep learning approaches for Formula 1 strategy prediction. Retrieved from Google Scholar.

Rohan Rao. Formula 1 World Championship Dataset (1950-2020). Kaggle. https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020
