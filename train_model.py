import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv("data/customer_churn.csv")

# Convert TotalCharges to numeric
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df.dropna(inplace=True)

# Encode target
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

# Drop customerID
df.drop(['customerID'], axis=1, inplace=True)

# One-hot encode categorical variables
df = pd.get_dummies(df, drop_first=True)

# Scale numeric columns
scaler = StandardScaler()
df[['MonthlyCharges', 'TotalCharges']] = scaler.fit_transform(df[['MonthlyCharges', 'TotalCharges']])

# Split data
X = df.drop("Churn", axis=1)
y = df["Churn"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save model
with open("models/logistic_model.pkl", "wb") as f:
    pickle.dump(model, f)

# Save column names
with open("models/columns.pkl", "wb") as f:
    pickle.dump(X.columns.tolist(), f)

print("✅ Model trained and saved successfully.")
