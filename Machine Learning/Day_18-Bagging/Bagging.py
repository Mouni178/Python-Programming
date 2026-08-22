"""
Bagging - Bootstrap Aggregating
"""

# What is Bagging?

# Bagging stands for Bootstrap Aggregating.
# It is an Ensemble Learning technique used to improve
# the stability and performance of Machine Learning models.

# Ensemble Learning

# Ensemble Learning means combining multiple models
# to make a better prediction than a single model.

# Basic Idea of Bagging

# Instead of training one model on the entire dataset,
# Bagging creates multiple samples from the original dataset
# and trains separate models on those samples.

# The predictions from all models are then combined.


# Bootstrap Sampling

# Bootstrap sampling means creating multiple datasets
# by randomly selecting samples from the original dataset
# with replacement.

# "With replacement" means the same data point can appear
# more than once in a bootstrap sample.


# Example

# Original Dataset:

# A B C D E

# Bootstrap Sample 1:
# A C C D E

# Bootstrap Sample 2:
# B B C D A

# Bootstrap Sample 3:
# E A B B D

# Each sample is used to train a separate model.


# Aggregation

# After training multiple models, their predictions
# are combined.

# Classification:
# Majority Voting is commonly used.

# Example:

# Model 1 -> Cat
# Model 2 -> Dog
# Model 3 -> Dog
# Model 4 -> Dog
# Model 5 -> Cat

# Final Prediction -> Dog
# Because Dog received the majority of votes.


# Regression:

# Predictions are usually averaged.

# Model 1 -> 100
# Model 2 -> 110
# Model 3 -> 120

# Final Prediction:
# (100 + 110 + 120) / 3
# = 110


# How Bagging Works

# Step 1:
# Start with the original dataset.

# Step 2:
# Create multiple bootstrap samples.

# Step 3:
# Train a separate model on each sample.

# Step 4:
# Make predictions using all models.

# Step 5:
# Combine the predictions.

# Step 6:
# Produce the final prediction.


# Why Use Bagging?

# - Reduces overfitting
# - Reduces variance
# - Improves model stability
# - Can improve prediction performance


# Bagging and Decision Trees

# Decision Trees can easily overfit the training data.

# Bagging can reduce this problem by training
# multiple Decision Trees on different bootstrap samples.


# Random Forest

# Random Forest is an important example of
# an ensemble method based on multiple Decision Trees.

# It combines multiple decision trees and uses
# aggregation to make the final prediction.


# Advantages of Bagging

# - Reduces variance
# - Helps reduce overfitting
# - More stable than a single model
# - Can work well with Decision Trees


# Disadvantages of Bagging

# - Requires multiple models
# - Can require more computational resources
# - The final model can be harder to interpret


print("Bagging Completed!")