# D1Fit – Current Vision

## Project
**D1Fit – Division 1 Athlete Readiness Classifier**

## Stakeholders
- **Primary Stakeholder:** University coaches and athletic staff who must quickly assess which athletes can compete at the Division 1 level.
- **Secondary Stakeholders:**
  - Sponsors (investment in players’ future)
  - University administration (consistent selection process and better competitive outcomes)
  - Recruitment officers / scouts (use fitness classification to shortlist potential recruits)

## Problem Statement
Coaches often rely on subjective or inconsistent screening to decide if an athlete is “Division 1 ready.” We have basic biometrics and lifestyle data, but there is no simple, data-driven tool that turns these inputs into a consistent readiness decision.

## Solution
Build a binary classifier that predicts D1 readiness (fit vs. not fit for D1) using age, height, weight/BMI, heart rate, blood pressure, sleep, nutrition quality, activity level, smoking status, and gender.

### The tool will:
- Output a calibrated probability and a clear **Yes / Not Yes** recommendation.
- Provide simple explanations (top factors) and what-if guidance.
- Handle messy, mixed-type data (missing values, outliers, inconsistent categories).
