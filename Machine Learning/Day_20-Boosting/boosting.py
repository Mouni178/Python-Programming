"""
Boosting in Machine Learning
"""

# What is Boosting?

# Boosting is an Ensemble Learning technique.
# It combines multiple weak learners to create
# a strong learner.

# Ensemble Learning

# Ensemble Learning means combining multiple models
# to improve the overall prediction.

# Weak Learner

# A weak learner is a model that performs slightly
# better than random guessing.

# In Boosting, weak learners are trained sequentially.


# Main Idea of Boosting

# Model 1
#    ↓
# Find mistakes
#    ↓
# Model 2 focuses more on mistakes
#    ↓
# Find remaining mistakes
#    ↓
# Model 3 focuses on them
#    ↓
# Combine all models
#    ↓
# Final Prediction


# Sequential Learning

# In Bagging:
# Models are generally trained independently.

# In Boosting:
# Models are trained sequentially.
# Each new model tries to improve the mistakes
# made by previous models.


# Example

# Suppose we have 3 weak learners.

# Model 1 makes some incorrect predictions.
# Model 2 gives more attention to those errors.
# Model 3 tries to correct the remaining errors.

# Finally, the predictions of all models
# are combined to produce a stronger prediction.


# Types of Boosting

# 1. AdaBoost
# Adaptive Boosting

# 2. Gradient Boosting

# 3. XGBoost
# Extreme Gradient Boosting

# 4. LightGBM
# Light Gradient Boosting Machine

# 5. CatBoost
# Categorical Boosting


# AdaBoost

# AdaBoost gives more importance to incorrectly
# classified data points.

# The next weak learner focuses more on those
# difficult examples.


# Gradient Boosting

# Gradient Boosting builds models sequentially.
# Each new model tries to reduce the errors
# of the previous models.

# It commonly uses Decision Trees as weak learners.


# XGBoost

# XGBoost stands for Extreme Gradient Boosting.

# It is a highly optimized implementation
# of gradient boosting.

# It is widely used for:
# - Classification
# - Regression
# - Structured/Tabular Data


# Advantages of Boosting

# - Can produce highly accurate models
# - Reduces bias
# - Works well with complex datasets
# - Useful for classification and regression


# Disadvantages of Boosting

# - Can be computationally expensive
# - Training can be slower
# - Can overfit if not properly controlled
# - More difficult to understand than a single Decision Tree


# Bagging vs Boosting

# Bagging:
# - Models are trained independently
# - Mainly reduces variance
# - Example: Random Forest

# Boosting:
# - Models are trained sequentially
# - Each model improves previous mistakes
# - Can reduce bias
# - Examples: AdaBoost, Gradient Boosting, XGBoost


print("Boosting Completed!")