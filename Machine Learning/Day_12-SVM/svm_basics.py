"""
Support Vector Machine (SVM)
"""

# What is SVM?
# SVM stands for Support Vector Machine.
# It is a supervised Machine Learning algorithm.
# It is mainly used for classification, but it can also
# be used for regression.

# Main Idea
# SVM finds the best boundary (hyperplane) that separates
# different classes of data.

# Example:
# Suppose we have two classes:
#
# Class A -> ● ● ●
# Class B -> ▲ ▲ ▲
#
# SVM tries to find a boundary that separates
# Class A and Class B.

# Hyperplane
# A hyperplane is a decision boundary used to separate classes.

# In 2 dimensions:
# Hyperplane -> Line
#
# In 3 dimensions:
# Hyperplane -> Plane
#
# In higher dimensions:
# Hyperplane -> Decision boundary

# Margin
# Margin is the distance between the decision boundary
# and the nearest data points from each class.

# SVM tries to find the hyperplane with the
# maximum possible margin.

# Support Vectors
# Support vectors are the data points closest to
# the decision boundary.

# These points are very important because they help
# determine the position of the decision boundary.

# Maximum Margin
# SVM tries to maximize the margin between classes.

# Large Margin:
# Better separation between classes.

# Small Margin:
# Classes are closer to the decision boundary.

# Classification
# SVM can classify data into different classes.

# Example:
# Email -> Spam / Not Spam
# Tumor -> Benign / Malignant
# Student -> Pass / Fail

# Regression
# SVM can also be used for regression using SVR
# (Support Vector Regression).

print("SVM Basics Completed!")