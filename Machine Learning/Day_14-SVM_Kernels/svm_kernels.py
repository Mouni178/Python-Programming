"""
SVM Kernels
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

# Split Data

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Scaling

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)


# Linear Kernel

model_linear = SVC(kernel="linear")

model_linear.fit(X_train, y_train)

prediction_linear = model_linear.predict(X_test)

print("Linear Kernel Accuracy:")
print(accuracy_score(y_test, prediction_linear))


# Polynomial Kernel

model_poly = SVC(kernel="poly")

model_poly.fit(X_train, y_train)

prediction_poly = model_poly.predict(X_test)

print("\nPolynomial Kernel Accuracy:")
print(accuracy_score(y_test, prediction_poly))


# RBF Kernel

model_rbf = SVC(kernel="rbf")

model_rbf.fit(X_train, y_train)

prediction_rbf = model_rbf.predict(X_test)

print("\nRBF Kernel Accuracy:")
print(accuracy_score(y_test, prediction_rbf))


# Sigmoid Kernel

model_sigmoid = SVC(kernel="sigmoid")

model_sigmoid.fit(X_train, y_train)

prediction_sigmoid = model_sigmoid.predict(X_test)

print("\nSigmoid Kernel Accuracy:")
print(accuracy_score(y_test, prediction_sigmoid))