"""
K-Nearest Neighbors (KNN)
"""
# What is KNN?
# KNN stands for K-Nearest Neighbors.
# It is a supervised Machine Learning algorithm.
# It can be used for Classification and Regression.
# Basic Idea
# KNN predicts the output of a new data point by looking
# at the K nearest data points in the training dataset.
# What does K mean?
# K represents the number of nearest neighbors considered
# for making the prediction.
# Example:
# K = 3
# The algorithm looks at the 3 nearest data points.
# How KNN Works
# Step 1:
# Choose the value of K.
# Step 2:
# Calculate the distance between the new data point
# and all training data points.
# Step 3:
# Find the K nearest data points.
# Step 4:
# For Classification:
# Choose the class that occurs most frequently
# among the K neighbors.
# Step 5:
# For Regression:
# Calculate the average value of the K neighbors.
# Distance
# KNN commonly uses Euclidean Distance.
# Euclidean Distance:
# Distance between two points is calculated based on
# the difference between their feature values.
# Example:
# Point A = (2, 3)
# Point B = (5, 7)
# KNN Classification Example
# Suppose we want to classify a new fruit.
# K = 3
# Nearest neighbors:
# Apple
# Apple
# Orange
# Apple occurs 2 times.
# Orange occurs 1 time.
# Prediction = Apple
# Choosing 
# Small K:
# - Sensitive to noise
# - Can cause overfitting
# Large K:
# - More stable
# - Can cause underfitting
# Usually, an odd value of K is preferred
# for binary classification to reduce the chance of a tie.
# Feature Scaling
# Feature scaling is important for KNN because KNN
# uses distance calculations.
# If one feature has very large values,
# it can dominate the distance calculation.

# Advantages of KNN
# - Simple to understand
# - Easy to implement
# - No complex training process
# - Can be used for classification and regression

# Disadvantages of KNN
# - Can be slow for large datasets
# - Sensitive to feature scaling
# - Sensitive to irrelevant features
# - Choosing the correct K is important

# Applications
# - Recommendation Systems
# - Pattern Recognition
# - Image Classification
# - Customer Classification
# - Medical Diagnosis
print("KNN Notes Completed!")