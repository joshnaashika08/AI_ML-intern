import pandas as pd
import os

# Set the path to the data folder relative to this script
data_path = os.path.join(os.path.dirname(__file__), '..', 'Data', 'Titanic-Dataset.csv')

# Read the dataset
df = pd.read_csv(data_path)

# Preview the original shape
print(f"Original shape: {df.shape}")

# ---------------------------
# 🔹 Basic Cleaning Steps
# ---------------------------

# 1. Drop duplicates
df.drop_duplicates(inplace=True)

# 2. Handle missing values
# Fill missing Age with median
if 'Age' in df.columns:
    df['Age'].fillna(df['Age'].median(), inplace=True)

# Fill missing Embarked with mode
if 'Embarked' in df.columns:
    df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# Drop Cabin if too many missing values
if 'Cabin' in df.columns:
    missing_ratio = df['Cabin'].isnull().mean()
    if missing_ratio > 0.5:
        df.drop('Cabin', axis=1, inplace=True)

# 3. Convert Sex to numerical (Male=0, Female=1)
if 'Sex' in df.columns:
    df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

# 4. Convert Embarked to numerical (C=0, Q=1, S=2)
if 'Embarked' in df.columns:
    df['Embarked'] = df['Embarked'].map({'C': 0, 'Q': 1, 'S': 2})

# ---------------------------
# ✅ Save Cleaned Data
# ---------------------------
# Create output path
output_path = os.path.join(os.path.dirname(__file__), '..', 'Data', 'Titanic-Cleaned.csv')

# Save the cleaned data
df.to_csv(output_path, index=False)
print(f"Cleaned dataset saved to: {output_path}")
print(f"New shape: {df.shape}")
