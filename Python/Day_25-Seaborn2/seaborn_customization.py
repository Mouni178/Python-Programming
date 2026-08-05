import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset("tips")
# Title
sns.scatterplot(x="total_bill", y="tip", data=tips)
plt.title("Total Bill vs Tip")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.show()
# Style
sns.set_style("darkgrid")
sns.barplot(x="day", y="total_bill", data=tips)
plt.show()
# Color
sns.barplot(x="day", y="tip", data=tips, color="green")
plt.show()
# Palette
sns.countplot(x="day", data=tips, palette="Set2")
plt.show()
# Figure Size
plt.figure(figsize=(8,5))
sns.boxplot(x="day", y="tip", data=tips)
plt.show()