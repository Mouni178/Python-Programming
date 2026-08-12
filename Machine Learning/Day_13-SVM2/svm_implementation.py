"""
SVM Classification using Scikit-learn
"""

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Load Dataset

data = datasets.load_iris()

X = data.data
y = data.target

# Split Dataset

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Feature Scaling

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)

# Create SVM Model

model = SVC(kernel="linear")

# Train Model

model.fit(X_train, y_train)

# Prediction

y_pred = model.predict(X_test)

# Accuracy

accuracy = accuracy_score(y_test, y_pred)

print("Predictions:")
print(y_pred)

print("Actual:")
print(y_test)

print("Accuracy:", accuracy)