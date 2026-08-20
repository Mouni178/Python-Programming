"""
Information Gain in Machine Learning
"""

# What is Gain?

# In Decision Trees, Gain usually refers to
# Information Gain.

# What is Information Gain?

# Information Gain is a measure used to determine
# how much uncertainty or impurity is reduced after
# splitting a dataset based on a particular feature.

# Simple Definition:
# Information Gain tells us how useful a feature is
# for splitting the data.

# Information Gain is mainly used in:
# Decision Tree algorithms


# Relationship between Entropy and Information Gain

# Entropy measures:
# How impure or uncertain the data is.

# Information Gain measures:
# How much that impurity is reduced after a split.


# Information Gain Formula

# Information Gain =
# Entropy of Parent
# -
# Weighted Average Entropy of Children


# Formula:
#
# IG(S, A) = Entropy(S) - Σ (|Sv| / |S|) × Entropy(Sv)
#
# S  = Parent dataset
# A  = Feature used for splitting
# Sv = Subset created after the split
#
# |Sv| = Number of samples in the subset
# |S|  = Total number of samples


# Example

# Suppose we have 10 students.

# Parent Dataset:
#
# Pass = 5
# Fail = 5
#
# Entropy of Parent = 1
#
# Now we split the students based on
# "Study Hours".


# After splitting:

# Group 1:
# Pass = 4
# Fail = 1

# Group 2:
# Pass = 1
# Fail = 4


# Each group is still mixed.
# Therefore, each group has some entropy.


# Weighted Entropy

# We calculate the entropy of each child group
# and then calculate their weighted average.

# Weighted Entropy =
# (Size of Group 1 / Total Size) × Entropy(Group 1)
# +
# (Size of Group 2 / Total Size) × Entropy(Group 2)


# Finally:

# Information Gain =
# Parent Entropy - Weighted Child Entropy


# If:
# Parent Entropy = 1
# Weighted Child Entropy = 0.72
#
# Information Gain = 1 - 0.72
# Information Gain = 0.28


# Interpretation

# High Information Gain:
# The feature creates a good split.
# It reduces uncertainty significantly.

# Low Information Gain:
# The feature does not create a very useful split.


# Information Gain in Decision Trees

# A Decision Tree can have multiple features.

# Example:

# Features:
# - Age
# - Income
# - Education
# - Experience

# The algorithm calculates Information Gain
# for each feature.

# Example:

# Age       -> IG = 0.10
# Income    -> IG = 0.35
# Education -> IG = 0.20
# Experience-> IG = 0.15

# Income has the highest Information Gain.

# Therefore:
# Income can be selected as the splitting feature.


# Important Points

# 1. Information Gain is used in Decision Trees.
# 2. It is calculated using Entropy.
# 3. It measures the reduction in uncertainty.
# 4. Higher Information Gain means a better split.
# 5. The feature with the highest Information Gain
#    can be selected for splitting.
# 6. Entropy and Information Gain are closely related.


# Entropy vs Information Gain

# Entropy:
# Measures impurity or uncertainty.

# Information Gain:
# Measures the reduction in impurity after splitting.
print("Information Gain Topic Completed!")