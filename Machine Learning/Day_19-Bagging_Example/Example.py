from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
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

# Base Model

base_model = DecisionTreeClassifier(random_state=42)

# Bagging Model

model = BaggingClassifier(
    estimator=base_model,
    n_estimators=10,
    random_state=42
)

# Train Model

model.fit(X_train, y_train)

# Prediction

y_pred = model.predict(X_test)

print("Predicted:", y_pred)

print("Actual:", y_test)

# Accuracy

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)