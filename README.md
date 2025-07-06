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

Task-3:

# 🏠 Housing Price Prediction - Linear Regression

## 📌 Objective
   Build a **Multiple Linear Regression** model using `Housing.csv` to predict house prices based on features like area, bedrooms, and amenities.

## 🧠 Learning Type
- Supervised Learning (Regression)
- Algorithm: Linear Regression
- Library: scikit-learn

## 🔧 Steps Performed
- Preprocessed categorical variables
- Split data into training and testing sets
- Trained and evaluated the model
- Visualized simple regression (area vs price)
- Interpreted feature coefficients

## 📂 Output Files
- `evaluation_metrics.txt`: MAE, MSE, R² values
- `regression_plot.png`: Area vs Price plot
- `feature_coefficients.csv`: Feature importance

## ✅ Conclusion
The model predicts house prices based on multiple features and reveals which variables most influence pricing.

TASK-4:

# 🔍 Logistic Regression - Binary Classification

## 📌 Objective
   Build a **binary classifier** using Logistic Regression to predict diagnoses (Malignant or Benign) based on tumor features from the breast cancer dataset.
---
## 🧰 Tools & Libraries
- Python
- pandas, numpy
- scikit-learn
- matplotlib, seaborn
---
## 🧠 Learning Type
- **Supervised Learning**
- **Classification Task**
- Algorithm: **Logistic Regression**
---
## 🪜 Steps Performed
1. Loaded and preprocessed the dataset  
2. Converted diagnosis labels (`M`, `B`) to binary (1, 0)  
3. Split data into training and testing sets  
4. Standardized features using `StandardScaler`  
5. Trained a Logistic Regression model  
6. Evaluated using confusion matrix, precision, recall, and ROC-AUC  
7. Tuned threshold manually  
8. Visualized the **sigmoid function**
---
## ✅ Conclusion
The model effectively classifies tumors as benign or malignant and provides interpretable feature impacts. Logistic Regression offers a reliable and explainable approach to medical diagnostics.

TASK_5:

# 🧠 Tree-Based Models on Heart Disease Dataset

This project explores decision tree-based algorithms to classify heart disease presence using the `heart.csv` dataset.

## Objective:
        Build and evaluate tree-based models for heart disease prediction using Decision Tree and Random Forest.  Visualize decision flow with Graphviz and interpret feature importance with cross-validation metrics.

## 🛠️ Tools & Libraries
- Python 3.9
- Scikit-learn
- Pandas, Seaborn, Matplotlib
- Graphviz (for visualization)
  
## 📊 What Was Done
- Trained a **Decision Tree Classifier** and visualized it using **Graphviz**
- Prevented overfitting using `max_depth`
- Built a **Random Forest Classifier** and compared performance
- Extracted and plotted **feature importances**
- Evaluated models using **confusion matrix**, **classification report**, and **cross-validation**

## 📌 Key Insights
- Random Forests significantly improve accuracy by reducing overfitting
- Features like `cp`, `thalach`, and `exang` had the most impact on predictions

## ✅ Output
Visuals are saved in the `output/` folder:
- `decision_tree_graphviz.png` – Visualized Decision Tree
- `random_forest_feature_importance.png` – Feature Importance Plot














