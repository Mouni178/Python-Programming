"""
Decision Tree in Machine Learning
"""

# What is a Decision Tree?

# A Decision Tree is a supervised Machine Learning algorithm
# used for both Classification and Regression.

# It makes decisions using a tree-like structure.

# Example:
#
#             Weather
#            /       \
#         Sunny      Rainy
#          /           \
#       Play?         Play?
#
# The model makes decisions by following a path
# from the root to a leaf node.


# Important Terms

# 1. Root Node
# The first and topmost node of the tree.
# It represents the most important feature used
# for the first split.


# 2. Decision Node
# A node where a decision or condition is made.

# Example:
# Age > 18?


# 3. Branch
# A branch represents the result of a decision.

# Example:
# Yes
# No


# 4. Leaf Node
# The final node of the tree.
# It contains the final prediction.

# Example:
# Pass
# Fail


# 5. Splitting
# Splitting means dividing the dataset into
# smaller groups based on a feature.


# Example:
# Feature = Study Hours

# Study Hours > 5?
#
# Yes -> Group 1
# No  -> Group 2


# How Does a Decision Tree Work?

# Step 1:
# Start with the complete dataset.

# Step 2:
# Select the best feature for splitting.

# Step 3:
# Split the dataset.

# Step 4:
# Repeat the process for the child nodes.

# Step 5:
# Stop when a stopping condition is reached.

# Step 6:
# The leaf node gives the final prediction.


# How is the Best Feature Selected?

# Decision Trees can use different criteria
# to select the best split.

# Common criteria:
#
# 1. Entropy
# 2. Information Gain
# 3. Gini Impurity


# Entropy

# Entropy measures the impurity or uncertainty
# in a dataset.

# Lower Entropy -> More Pure
# Higher Entropy -> More Uncertain


# Information Gain

# Information Gain measures how much impurity
# is reduced after splitting the data.

# Higher Information Gain -> Better Split


# Gini Impurity

# Gini Impurity is another measure used to determine
# the impurity of a node.

# Lower Gini -> More Pure


# Decision Tree for Classification

# Example:
#
# Input Features:
# - Study Hours
# - Attendance
#
# Output:
# - Pass
# - Fail


# Decision Tree for Regression

# Example:
#
# Input Features:
# - Area
# - Bedrooms
# - Location
#
# Output:
# - House Price


# Advantages

# - Easy to understand
# - Easy to visualize
# - Can handle numerical data
# - Can handle categorical data
# - Can be used for classification and regression
# - Does not require feature scaling in the same way
#   as distance-based algorithms


# Disadvantages

# - Can easily overfit
# - Small changes in data can change the tree
# - Very deep trees can become complex


# Overfitting

# When a Decision Tree learns the training data
# too closely and performs poorly on new data,
# it is called overfitting.


# Controlling Overfitting

# Important parameters:
#
# max_depth
# min_samples_split
# min_samples_leaf
#
# These parameters help control the size
# and complexity of the tree.


print("Decision Tree Notes Completed!")