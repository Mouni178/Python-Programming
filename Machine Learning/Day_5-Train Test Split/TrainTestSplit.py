"""
Train-Test Split
"""
# What is Train-Test Split?
# Train-Test Split is the process of dividing a dataset into
# two parts: Training Data and Testing Data.

# Why do we split the dataset?
# - To train the model using one part of the data.
# - To test the model on unseen data.
# - To check how well the model performs.

# Types of Data
# 1. Training Data
# - Used to train the machine learning model.
# - The model learns patterns from this data.
# 2. Testing Data
# - Used to evaluate the trained model.
# - It checks the model's performance on new data.

# Common Split Ratios
# - 80% Training : 20% Testing
# - 70% Training : 30% Testing
# - 75% Training : 25% Testing

# Example
# Student Dataset
# Total Records = 100
# Training Data = 80 Records
# Testing Data = 20 Records
# Python Example

from sklearn.model_selection import train_test_split

# X = Features
# y = Target

# X_train, X_test, y_train, y_test = train_test_split(
#     X, y,
#     test_size=0.2,
#     random_state=42
# )

# Parameters
# test_size -> Percentage of testing data
# random_state -> Produces the same split every time

print("Train-Test Split Completed!")