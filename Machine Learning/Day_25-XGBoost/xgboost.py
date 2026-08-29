"""
XGBoost
"""

# What is XGBoost?

# XGBoost stands for Extreme Gradient Boosting.

# XGBoost is an optimized and efficient implementation
# of the Gradient Boosting algorithm.

# It is an Ensemble Learning technique.

# XGBoost can be used for:
# 1. Classification
# 2. Regression


# Main Idea

# XGBoost builds multiple weak learners, usually
# Decision Trees, sequentially.

# Each new tree tries to improve the errors
# made by the previous trees.


# Basic Workflow

# Dataset
#    ↓
# First Decision Tree
#    ↓
# Calculate Errors
#    ↓
# Next Decision Tree
#    ↓
# Correct Previous Errors
#    ↓
# Repeat
#    ↓
# Combine Trees
#    ↓
# Final Prediction


# Why "Extreme"?

# XGBoost is designed to be:
# - Fast
# - Efficient
# - Scalable
# - Regularized
# - Suitable for large datasets


# Important Concepts

# 1. Boosting

# XGBoost uses boosting.
# Models are built sequentially and each new model
# tries to improve the previous model.


# 2. Decision Trees

# XGBoost commonly uses decision trees
# as its base learners.


# 3. Gradient Boosting

# XGBoost improves the model by minimizing
# a loss function using gradient-based optimization.


# 4. Regularization

# XGBoost includes regularization to help
# control overfitting.

# Common regularization parameters:
# - reg_alpha
# - reg_lambda


# Important Parameters

# n_estimators
# Number of trees.

# max_depth
# Maximum depth of each tree.

# learning_rate
# Controls how much each new tree contributes
# to the final model.

# A smaller learning rate usually requires
# more trees.

# subsample
# Fraction of training data used for each tree.

# colsample_bytree
# Fraction of features used for each tree.


# Advantages

# - High predictive performance
# - Fast and efficient
# - Handles complex datasets
# - Supports classification and regression
# - Includes regularization
# - Handles missing values in many common workflows
# - Provides feature importance


# Disadvantages

# - More complex than simple algorithms
# - Can overfit if parameters are not controlled
# - Requires parameter tuning
# - Less interpretable than a single Decision Tree


# XGBoost vs Random Forest

# Random Forest:
# - Uses Bagging
# - Trees are generally built independently
# - Reduces variance

# XGBoost:
# - Uses Boosting
# - Trees are built sequentially
# - Each tree improves the previous model


# Applications

# - Fraud Detection
# - Customer Churn Prediction
# - Credit Risk Prediction
# - Sales Prediction
# - Classification
# - Regression
# - Ranking


print("XGBoost Notes Completed!")