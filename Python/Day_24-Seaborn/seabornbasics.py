import seaborn as sns
import matplotlib.pyplot as plt
# Load Dataset
tips = sns.load_dataset("tips")
print(tips.head())
# Dataset Shape
print(tips.shape)
# Dataset Columns
print(tips.columns)
# Dataset Information
print(tips.info())
# Dataset Description
print(tips.describe())
# List of Built-in Datasets
print(sns.get_dataset_names())