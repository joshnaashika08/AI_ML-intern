# AI_ML-intern:
TASK -1:
# Titanic Dataset – Data Cleaning

## 🎯 Aim

To preprocess the raw Titanic dataset by cleaning and transforming features to prepare it for Exploratory Data Analysis and machine learning.
---

## 📌 Objectives

- Handle missing data appropriately
- Drop irrelevant or non-informative features
- Convert categorical variables to numerical format
- Save the cleaned dataset for further use
---

## ✅ Cleaning Summary

1. **Missing Values**:
   - Filled missing `Age` values with the median
   - Filled missing `Embarked` values with the mode
   - Dropped `Cabin` due to excessive missing values

2. **Dropped Columns**:
   - Removed `PassengerId`, `Name`, and `Ticket`

3. **Categorical Conversion**:
   - Converted `Sex` to binary (`0 = male`, `1 = female`)
   - One-hot encoded `Embarked` column (drop-first to avoid multicollinearity)

4. **Saved Cleaned Data**:
   - Output file: `Titanic-Cleaned.csv` located in `Data/` folder
---

## 🧰 Tools Used

- Python
- pandas
- numpy

## 🏁 Conclusion

    The dataset was successfully cleaned by handling missing values, removing irrelevant columns, and encoding categorical features. It is now ready for analysis and modeling.
    

TASK-2:
# Titanic Dataset – Exploratory Data Analysis (EDA)

## 🎯 Aim

To perform **Exploratory Data Analysis (EDA)** on the Titanic dataset in order to uncover patterns, visualize relationships, detect anomalies, and generate insights that can guide future predictive modeling or data preprocessing tasks.
---

## 📌 Objectives

- Understand the structure and types of data in the Titanic dataset
- Summarize the dataset using descriptive statistics
- Visualize distributions of numeric features (e.g., Age, Fare)
- Identify correlations between features using a heatmap
- Detect outliers and missing values
- Make inferences from plots to guide future modeling
---

## 🧰 Tools & Libraries

- Python
- Jupyter Notebook / VS Code
- `pandas` for data manipulation
- `matplotlib` & `seaborn` for visualization
- `numpy` for numerical analysis
---

## 🏁 Conclusion

This EDA provides critical insight into which features are important for survival prediction, and helps shape future modeling, feature engineering, and preprocessing decisions.




