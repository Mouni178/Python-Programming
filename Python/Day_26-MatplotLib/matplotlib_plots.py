import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]
# Line Plot
plt.plot(x, y)
plt.show()
# Scatter Plot
plt.scatter(x, y)
plt.show()
# Bar Plot
plt.bar(x, y)
plt.show()
# Horizontal Bar Plot
plt.barh(x, y)
plt.show()
# Histogram
marks = [70, 75, 80, 85, 90, 90, 95, 100]
plt.hist(marks)
plt.show()
# Pie Chart
subjects = ["Python", "Java", "SQL", "ML"]
students = [30, 20, 25, 25]
plt.pie(students, labels=subjects, autopct="%1.1f%%")
plt.show()