import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

df = pd.read_csv("/Users/macbook/Documents/GitHub/Educational-Resource-Allocation-for-Bangladesh/backend/data/education_data.csv")

features = ["Total_Students", "Female_Students", "Disabled_Students", "Teachers", "Budget", "Pass_Rate", "Internet_Access"]
target_dropout, target_completion, target_tsr = "Dropout_Rate", "Completion_Rate", "TSR"

X = df[features]
y_dropout, y_completion, y_tsr = df[target_dropout], df[target_completion], df[target_tsr]

X_train, X_test, y_dropout_train, y_dropout_test = train_test_split(X, y_dropout, test_size=0.2, random_state=42)
X_train, X_test, y_completion_train, y_completion_test = train_test_split(X, y_completion, test_size=0.2, random_state=42)
X_train, X_test, y_tsr_train, y_tsr_test = train_test_split(X, y_tsr, test_size=0.2, random_state=42)

dropout_model = RandomForestRegressor(n_estimators=100, random_state=42).fit(X_train, y_dropout_train)
completion_model = RandomForestRegressor(n_estimators=100, random_state=42).fit(X_train, y_completion_train)
tsr_model = RandomForestRegressor(n_estimators=100, random_state=42).fit(X_train, y_tsr_train)

joblib.dump(dropout_model, "/Users/macbook/Documents/GitHub/Educational-Resource-Allocation-for-Bangladesh/backend/data/models/dropout_model.pkl")
joblib.dump(completion_model, "/Users/macbook/Documents/GitHub/Educational-Resource-Allocation-for-Bangladesh/backend/data/models/completion_model.pkl")
joblib.dump(tsr_model, "/Users/macbook/Documents/GitHub/Educational-Resource-Allocation-for-Bangladesh/backend/data/models/tsr_model.pkl")
