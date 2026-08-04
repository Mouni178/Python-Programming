import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset("tips")
# Scatter Plot
sns.scatterplot(x="total_bill", y="tip", data=tips)
plt.show()
# Line Plot
sns.lineplot(x="size", y="tip", data=tips)
plt.show()
# Bar Plot
sns.barplot(x="day", y="total_bill", data=tips)
plt.show()
# Count Plot
sns.countplot(x="day", data=tips)
plt.show()
# Histogram
sns.histplot(tips["total_bill"])
plt.show()
# Box Plot
sns.boxplot(x="day", y="total_bill", data=tips)
plt.show()
# Violin Plot
sns.violinplot(x="day", y="total_bill", data=tips)
plt.show()
# Pair Plot
sns.pairplot(tips)
plt.show()
# Heatmap
corr = tips.corr(numeric_only=True)
sns.heatmap(corr, annot=True)
plt.show()