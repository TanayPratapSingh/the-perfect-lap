## WorkPlan

### Milestone 1: Data Acquisition 
Tasks
- M1.T1 — Downloaded the dataset into project workspace (Tanay Singh)
- M1.T2 — Divided the datasets for EDA among all teamates (all members)
- M1.T3 — Discussed and exchanged points about the datasets and identified key variables related to pitstop timings (all members).

### Milestone 2 : Data Cleaning 
- M2.T1 — Handling of missing Data and inconsistent data and all key variables required.(Tanay, Atharva)
- M2.T2 — Conversion of time formats to a similar structure for convenient comparison of different parameters in determining the perfect lap to make a pitstop.(all members)
- M2.T3 — Initiated the process of tackling outliers throughout the variables.(Srikanth, Praveer, Titus)

### Milestone 3: Advanced Data Cleaning & Filtering

- M3.T1 — Loaded core datasets (races, results, pit_stops, drivers, constructors) and filtered races from year ≥ 2000 (Titus, Atharva)
- M3.T2 — Computed first_pit_lap and pit_stop_count features for each driver-race combination (Srikanth, Tanay)
- M3.T3 — Removed drivers with >2 pit stops and early DNFs to ensure data quality (Praveer, Tanay)
- M3.T4 — Saved cleaned files in standardized format for team access (Atharva, Praveer)

### Milestone 4: Data Merging & Integration

- M4.T1 — Merged results + races tables to create race-level features (Tanay, Titus, Srikanth)
- M4.T2 — Integrated drivers + constructors data for team and driver attributes (Praveer, Atharva)
- M4.T3 — Created driver-race-level master table combining all features (all members)

### Milestone 5: Imputation & Validation

- M5.T1 — Implemented RandomForestRegressor for missing pit lap imputation (pre-2012 data) (Atharva, Srikanth)
- M5.T2 — Combined known + imputed values into complete dataset (Atharva, Praveer)
- M5.T3 — Performed train/test split on known rows for validation (Titus, Tanay)
- M5.T4 — Evaluated RandomForest imputation accuracy (Current MAE ≈ 6 laps) (all members)

### Milestone 6: Final Data Preparation & Model Training

- M6.T1 — Finalized cleaned + imputed dataset with engineered features prepared for model training (All members)
- M6.T2 — Trained Decision Tree, Random Forest, and Bagging models (Tanay, Srikanth, Titus)
- M6.T3 — Trained Extra Trees and Gradient Boosting models (Atharva, Praveer)
- M6.T4 — Verified all models ran successfully and produced predicted pit-stop laps; detailed evaluation to follow (All members)

### Milestone 7: Final Position Prediction Model Development

- M7.T1 — Developed model architecture for final position prediction using pit strategy as key feature (Tanay, Atharva)
- M7.T2 — Integrated driver performance metrics, constructor strength, and circuit characteristics as input features (Srikanth, Praveer)
- M7.T3 — Trained position classification model focusing on P1-P5 vs P6+ outcomes (Praveer, Tanay)
- M7.T4 — Validated model accuracy and confidence levels for podium predictions (all members)

### Milestone 8: Complete Strategy Integration

- M8.T1 — Built integrated interface combining pit stop timing + position prediction (Praveer, Atharva)
- M8.T2 — Implemented position model logic module (final_position_model.py) (Srikanth, Titus)
- M8.T3 — Created combined prediction pipeline: pit timing → final position (Praveer, Tanay)
- M8.T4 — Developed position classification styling (P1/podium/points/outside) (all members)

---

## Weekly Tasks

### 2025-10-11
- M1.T1 — Downloaded and organized all 14 F1 CSV files (1950-2020) into the project folder and verified completeness (Tanay Singh)
- M1.T2 —  Divided all 14 datasets among team members (2-3 datasets each) and created separate analysis notebooks for independent exploration (All members)
- M2.T1 — Identified and selected key variables important for pit stop prediction including pit lap number, tire age, position changes, and lap times (All members)

### 2025-10-21
- M2.T2 —  Fixed missing data, corrected errors, and kept only the important columns needed for pit stop prediction (Tanay , Atharva)
- M4.T1 —  Standardized all date and time formats (dates to YYYY-MM-DD, times to milliseconds) across all datasets for consistent comparison (All members)
- M4.T2 — Removed outliers and impossible data points like pit stops at non-existent laps and unrealistic pit durations (Srikanth , Praveer , Titus)

### 2025-10-28
- M3.T1 — Loaded and filtered core datasets for races from year ≥ 2000 to focus on modern F1 era (Tanay, Atharva)
- M3.T2 — Computed derived features: first_pit_lap and pit_stop_count for strategy analysis (Srikanth, Titus)
- M3.T3 — Applied quality filters: removed >2 pit stop races and early DNFs (Praveer, Tanay)

### 2025-11-04
- M4.T1 — Created initial merge of results + races tables with proper key matching (Titus, Srikanth)
- M4.T2 — Added driver and constructor information to create comprehensive dataset (Praveer, Atharva)
- M4.T3 — Finalized driver-race-level master table with all integrated features (all members)

### 2025-11-11
- M5.T1 — Developed and trained RandomForestRegressor model for missing pit lap imputation (Atharva, Srikanth)
- M5.T2 — Applied imputation to pre-2012 data and combined with known values (Tanay, Praveer)
- M5.T3 & M5.T4 — Validated imputation accuracy through train/test split; identified MAE ≈ 6 laps requiring track feature enhancement (all members)

### 2025-11-19
- M6.T1 — Completed preparation of final dataset with all required features and imputed values (All members)
- M6.T2 — Trained Decision Tree, Random Forest, and Bagging models on the finalized dataset (Tanay, Srikanth, Titus)
- M6.T3 — Trained Extra Trees and Gradient Boosting models and saved initial outputs (Atharva, Praveer)
- M6.T4 — Reviewed predictions from all five models and confirmed that training completed without errors (All members)

### 2025-11-26
- M7.T1 — Architected final position prediction model responding to feedback received during project presentation (Tanay, Atharva)
- M7.T2 — Engineered feature set combining optimal pit lap with driver/constructor/circuit features (Srikanth, Praveer)
- M7.T3 — Trained classification model for P1-P20 position predictions with focus on top 5 positions (Titus, Tanay)

### 2025-12-03
- M7.T4 — Validated position prediction accuracy; achieved reliable podium vs non-podium classification (all members)
- M8.T1 — Created integrated application interface with 3-step prediction flow (Praveer, Atharva)
- M8.T2 — Implemented final position model logic as separate module for maintainability (Srikanth, Tanay)

### 2025-12-10
- M8.T3 — Completed end-to-end pipeline testing: user input → pit lap → final position (Praveer, Atharva)
- M8.T4 — Finalized UI with position-based styling (Gold/Silver/Green/Gray) and confidence indicators (all members)

---

## Logs 

### 2025-10-11
- (All) M1.T1 — Team meeting: identified pit_stops (lap, duration), lap_times (pace), and results (finishing position) as critical for pit prediction.

### 2025-10-21
- (All) M2.T2 — Verified time format consistency across pit_stops, lap_times, and results tables
- (All) M2.T1, M2.T2, M2.T3 — Data cleaning complete: removed 200 corrupted records, 98% of data retained; 900+ valid races (2010-2020) identified for modeling

### 2025-10-28
- (Praveer, Atharva) M3.T1 — Successfully filtered 20+ years of race data (2000-2020), reducing dataset from 25,000+ to 15,000 relevant races
- (Srikanth, Titus) M3.T2 — Feature engineering complete: first_pit_lap and pit_stop_count computed for 95% of races
- (Praveer, Tanay) M3.T3 — Quality control: removed 1,200 anomalous records (>2 stops, early DNFs)

### 2025-11-04
- (All) M4.T1-T3 — Master table creation successful: 14,000+ driver-race records with 45 features integrated from 5 source tables

### 2025-11-11
- (Tanay, Srikanth) M5.T1 — RandomForest imputation model trained on 8,000 known pit lap records
- (Atharva, Titus, Praveer) M5.T4 — Imputation validation: MAE = 6 laps identified as break point; team decision to add track features for improved accuracy

### 2025-11-19
- (Tanay, Praveer) M6.T1 — Final dataset validated after confirming consistency of engineered features and imputed pit-lap values.
- (Atharva, Titus) M6.T2 & M6.T3 — Trained all five models (Decision Tree, Random Forest, Bagging, Extra Trees, Gradient Boosting) and verified that predictions were generated correctly without errors.
- (All) M6.T4 — Reviewed initial outputs across all models; full evaluation and comparison scheduled for the next stage.

### 2025-11-26
- (Tanay, Atharva) M7.T1 — Successfully addressed professor's feedback by creating position prediction model architecture
- (All) M7.T2 — Feature engineering complete: pit strategy now feeds into position prediction as primary strategic input

### 2025-12-03
- (All) M7.T4 — Model evaluation: 75% accuracy for podium prediction, 85% for points vs non-points classification
- (Praveer, Atharva, Tanay) M8.T1 — Integrated interface deployed combining both models in single workflow

### 2025-12-10
- (Atharva, Praveer, Srikanth) M8.T3 — Complete strategy integration tested: pit timing (MAE 2.78 laps) → position prediction operational
- (Praveer) M8.T4 — Business value demonstrated: "Will this pit strategy lead to podium/points finish?" question answered