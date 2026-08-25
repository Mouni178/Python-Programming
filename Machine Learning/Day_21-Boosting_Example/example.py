from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
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

base_model = DecisionTreeClassifier(
    max_depth=1,
    random_state=42
)

# AdaBoost Model

model = AdaBoostClassifier(
    estimator=base_model,
    n_estimators=50,
    random_state=42
)

# Train Model

model.fit(X_train, y_train)

# Prediction

y_pred = model.predict(X_test)

print("Predicted:")
print(y_pred)

print("\nActual:")
print(y_test)
# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy)