"""
Random Forest
"""
# What is Random Forest?
# Random Forest is a supervised Machine Learning algorithm.
# It is an Ensemble Learning technique that combines
# multiple Decision Trees to make a final prediction.
# Random Forest can be used for:
# 1. Classification
# 2. Regression
# Why is it called Random Forest?
# Random Forest creates many Decision Trees.
# Each tree is trained using random samples of the data
# and random subsets of features.
# Many Decision Trees
#        ↓
#      Forest
#        ↓
# Combine Predictions
#        ↓
# Final Prediction
# Relationship with Bagging

# Random Forest is based on the idea of Bagging.

# It uses:
# - Bootstrap samples
# - Multiple Decision Trees
# - Aggregation of predictions


# How Random Forest Works

# Step 1:
# Select random samples from the original dataset.

# Step 2:
# Create multiple bootstrap datasets.

# Step 3:
# Build a Decision Tree for each dataset.

# Step 4:
# At each split, consider a random subset of features.

# Step 5:
# Each tree makes a prediction.

# Step 6:
# Combine the predictions of all trees.


# Classification

# Random Forest uses majority voting.

# Example:

# Tree 1 -> Cat
# Tree 2 -> Dog
# Tree 3 -> Dog
# Tree 4 -> Dog
# Tree 5 -> Cat

# Final Prediction -> Dog


# Regression

# Random Forest usually takes the average
# of predictions from all trees.

# Example:

# Tree 1 -> 100
# Tree 2 -> 110
# Tree 3 -> 120

# Final Prediction:
# (100 + 110 + 120) / 3
# = 110


# Important Parameters

# n_estimators
# Number of Decision Trees in the forest.

# Example:
# n_estimators = 100
# means the forest contains 100 trees.


# max_depth
# Maximum depth of each Decision Tree.

# Larger depth:
# More complex model.

# Smaller depth:
# Simpler model.


# min_samples_split
# Minimum number of samples required to split a node.


# min_samples_leaf
# Minimum number of samples required in a leaf node.


# max_features
# Number of features considered when looking
# for the best split.


# random_state
# Makes the results reproducible.


# Advantages

# - High accuracy
# - Reduces overfitting compared with a single Decision Tree
# - Handles large datasets
# - Can be used for classification and regression
# - Works with many features
# - Less sensitive to noise than a single Decision Tree


# Disadvantages

# - Uses more memory
# - Can be slower than a single Decision Tree
# - Less interpretable than a single Decision Tree
# - Large forests can be computationally expensive


# Decision Tree vs Random Forest

# Decision Tree:
# One tree
# Easy to understand
# Can overfit easily

# Random Forest:
# Many trees
# More stable
# Usually better generalization


# Random Forest vs Bagging

# Bagging:
# Combines multiple models using bootstrap samples.

# Random Forest:
# Uses Bagging with multiple Decision Trees
# and random feature selection at each split.


# Applications

# - Fraud Detection
# - Medical Diagnosis
# - Customer Churn Prediction
# - Credit Risk Prediction
# - Image Classification
# - Recommendation Systems


print("Random Forest Completed!")