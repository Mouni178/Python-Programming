"""
Decision Tree Classification using Scikit-learn
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load Dataset
data = load_iris()

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

model = DecisionTreeClassifier(
    criterion="entropy",
    random_state=42
)

# Train Model

model.fit(X_train, y_train)

# Prediction

y_pred = model.predict(X_test)

print("Predicted Values:")
print(y_pred)

print("\nActual Values:")
print(y_test)

# Accuracy

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy)