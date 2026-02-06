# D1Fit – Division 1 Athlete Readiness Classifier

## Team
- **Tanay Singh** (GitHub: [TanayPratapSingh](https://github.com/TanayPratapSingh))  
- **Praveer Nagaraja Byndoor** (GitHub: [praveerbn](https://github.com/praveerbn))  
- **Atharva Karekar** (GitHub: [ath1812](https://github.com/ath1812))  
- **Titus Kenneth George** (GitHub: [tkenneth2106](https://github.com/tkenneth2106))

## Introduction
Our dataset provides information on individual health and lifestyle factors such as age, height, weight, heart rate, blood pressure, sleep, smoking, diet quality, activity level, and gender. We aim to build a simple tool that classifies whether a person is fit enough to play in “Division 1” league or not based on this information. This tool is being designed for university coaches and staff to identify which athletes can compete at the Division 1 level.

## Key Stakeholders
- **University coaches and athletic staff:** Need a reliable way to identify general Division 1-ready athletes.  
- **Athletes:** Fulfilling expectations of a fair and accurate evaluation of their fitness status ensuring transparency.  
- **University administration:** Benefits from improved athlete selection processes and competitive outcomes.

## Innovation
Our project focuses on applying machine learning to a broader set of parameters bridging the gap between realistic fitness data (e.g., heart rate, blood pressure) and lifestyle factors (e.g., smoking, diet, activity level), allowing for more comprehensive fitness classification.  
Additionally, by focusing on Division 1 athletics, our project introduces a practical application in a university setting where accurate fitness evaluation can directly impact team composition and performance.

## Literature Review
Non-exercise fitness research shows you can estimate cardiorespiratory fitness (VO₂peak) without a treadmill test using easy inputs like age, resting heart rate, body size, and self-reported activity. Classic regression equations (e.g., from large population cohorts) make screening simple and low-cost, but they output a continuous VO₂ value, assume clean inputs, and rarely include calibration or uncertainty. Newer work uses machine-learning on survey/clinic data (e.g., NHANES) to beat those equations by capturing nonlinear patterns, yet it still targets continuous VO₂max for clinical/epi use rather than a coach-ready decision. In sports analytics, ML has also been used for injury risk, readiness, and talent ID with match stats, GPS, and biomechanics; these are operationally interesting but often rely on specialized/high-frequency data and pay less attention to calibration, fairness, and transferability.

**D1Fit** fills the gap by delivering a binary, probability-calibrated readiness decision tailored for coaching. We use simple, widely available inputs (age, BMI/weight/height, heart rate, blood pressure, sleep, diet quality, activity level, smoking, gender) and a pipeline built for messy data (type fixes, imputation, outlier handling, BMI features). The modeling path is transparent and practical—logistic regression as a baseline, then boosted trees—followed by calibration so that “70% ready” behaves like 70% historically. We’ll report class-aware metrics (PR-AUC, macro-F1), show *why* with SHAP explanations, and include small “what-if” guides (e.g., +1 hour sleep or quitting smoking) so coaches can use the outputs in real selection meetings.

## Risks
- **Synthetic Data Bias:** Since the dataset is synthetic, results may not fully generalize to real-world athletes.  
  *Mitigation:* Emphasize limitations in reporting, and if possible, compare patterns with small real datasets.
- **Overfitting:** Models may learn dataset-specific patterns instead of general fitness indicators.  
  *Mitigation:* Use cross-validation and regularization techniques.
- **Fairness Concerns:** Fitness classification may unintentionally reflect biases (e.g., gender or body type).  
  *Mitigation:* Monitor fairness metrics and avoid over-reliance on any single variable.

## Data and Methods

### Data
**Fitness Classification Dataset:**  
<https://www.kaggle.com/datasets/muhammedderric/fitness-classification-dataset-synthetic>

The dataset contains 2,000 rows and 11 columns, covering both numerical and categorical features. The key variables include age, height, weight, heart rate, blood pressure, sleep duration, smoking status, diet quality, activity level, and gender. The target variable is a binary indicator of whether an individual is classified as “fit” or “not fit”.

Although the dataset is synthetic, it was designed to mimic real-world fitness and health data. At this stage, we do not anticipate needing additional datasets, but if comparisons to real-world benchmarks are necessary, we will seek open-source health or fitness datasets.

### Methodology
Our modeling approach begins with preprocessing, where we will handle missing values through imputation, encode categorical variables such as gender, smoking, and diet quality using one-hot encoding, and normalize or standardize continuous features like height, weight, and heart rate to ensure comparability. For modeling, we will start with a simple logistic regression as a baseline, and then apply more advanced ensemble methods such as Random Forests and Gradient Boosting to improve accuracy and robustness. Model performance will be evaluated using accuracy and F1-score as primary metrics. Since this project is focused on identifying Division 1 ready athletes, we will place special emphasis on recall for the “fit” class, ensuring that truly fit athletes are not incorrectly classified as unfit.

## Timeline
| Period        | Activity                                              | Milestone                                                              |
|---------------|-------------------------------------------------------|------------------------------------------------------------------------|
| **9/10 – 9/23** | Stakeholder analysis, EDA and Initial exploration     | Completed stakeholder analysis and data exploration. Additional datasets identified as necessary. |
| **9/24 – 10/8** | Preprocessing and modeling refinements; ML exploration | Model finalization and training.                                       |

## References
- Nes BM et al., 2011 (non-exercise VO₂peak equation; HUNT study).  
- Liu Y et al., 2023 (ML for VO₂max prediction; NHANES).  
- Majumdar A. et al., 2022 (review of ML for injury/readiness in sport).
