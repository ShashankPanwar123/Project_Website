import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load your dataset
df = pd.read_csv("train.csv")

# 🔥 Adjust these based on your actual dataset columns
df = df.rename(columns={
    "Age": "age",
    "Annual_Premium": "premium",
    "Vehicle_Age": "vehicle_age",
    "Response": "response"
})

# Convert categorical → numeric
df["vehicle_age"] = df["vehicle_age"].map({
    "< 1 Year": 0,
    "1-2 Year": 1,
    "> 2 Years": 2
})

# Features & target
X = df[["age", "premium", "vehicle_age"]]
y = df["response"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("✅ Model trained successfully!")