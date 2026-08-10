"""
Entropy in Machine Learning
"""

# What is Entropy?

# Entropy is a measure of impurity, disorder, or uncertainty
# in a dataset.

# In Machine Learning, Entropy is mainly used in
# Decision Trees to decide how pure or impure a node is.

# Pure Node:
# A node is pure when all data points belong to the same class.

# Example:
# [Yes, Yes, Yes, Yes]
# Entropy = 0
# There is no uncertainty.

# Impure Node:
# A node is impure when data points belong to different classes.

# Example:
# [Yes, Yes, No, No]
# There is uncertainty about the class.

# Entropy Formula:
#
# Entropy = -Σ p(x) * log2(p(x))
#
# p(x) = Probability of a particular class


# Example 1: Completely Pure Dataset

# Dataset:
# Yes = 4
# No = 0

# Probability of Yes:
# P(Yes) = 4/4 = 1

# Probability of No:
# P(No) = 0/4 = 0

# Entropy = 0

# Therefore:
# Completely Pure Dataset -> Entropy = 0


# Example 2: Completely Mixed Dataset

# Dataset:
# Yes = 2
# No = 2

# Probability of Yes:
# P(Yes) = 2/4 = 0.5

# Probability of No:
# P(No) = 2/4 = 0.5

# Entropy:
# = -(0.5 * log2(0.5) + 0.5 * log2(0.5))
# = 1

# Therefore:
# Completely Mixed Binary Dataset -> Entropy = 1


# Entropy Range

# For Binary Classification:
# Minimum Entropy = 0
# Maximum Entropy = 1

# Entropy = 0
# -> Completely Pure

# Entropy = 1
# -> Maximum Uncertainty for a binary split


# Interpretation

# Low Entropy:
# Low uncertainty
# High purity

# High Entropy:
# High uncertainty
# Low purity


# Why is Entropy used in Decision Trees?

# Decision Trees use Entropy to measure the impurity
# of a node.

# A good split should reduce impurity.

# Entropy helps us measure this impurity.

# Information Gain is later used to calculate
# how much the entropy decreases after a split.


# Important Points

# 1. Entropy measures impurity or uncertainty.
# 2. Entropy is used in Decision Trees.
# 3. Lower entropy means greater purity.
# 4. Higher entropy means greater uncertainty.
# 5. For binary classification, entropy ranges from 0 to 1.
# 6. Entropy of a completely pure node is 0.
# 7. Information Gain is related to Entropy.


print("Entropy Topic Completed!")