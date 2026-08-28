"""
Random Forest Regression
"""

from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Load Dataset

data = load_diabetes()

X = data.data
y = data.target

# Split Dataset

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create Model

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# Train Model

model.fit(X_train, y_train)

# Prediction

y_pred = model.predict(X_test)

print("Predicted Values:")
print(y_pred)

# Evaluation

mse = mean_squared_error(y_test, y_pred)

r2 = r2_score(y_test, y_pred)

print("\nMean Squared Error:", mse)

print("R2 Score:", r2)