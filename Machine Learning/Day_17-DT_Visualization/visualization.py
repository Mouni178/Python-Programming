"""
Decision Tree Visualization
"""

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

# Load Dataset

data = load_iris()

X = data.data
y = data.target

# Create Model

model = DecisionTreeClassifier(
    criterion="entropy",
    max_depth=3,
    random_state=42
)

# Train Model

model.fit(X, y)

# Visualize Tree

plt.figure(figsize=(15, 8))

plot_tree(
    model,
    feature_names=data.feature_names,
    class_names=data.target_names,
    filled=True
)

plt.show()