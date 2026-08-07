import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [5, 10, 15, 20, 25]
# Title
plt.title("Student Marks")
# Labels
plt.xlabel("Subjects")
plt.ylabel("Marks")
# Line Plot
plt.plot(x, y)
# Grid
plt.grid()
# Legend
plt.legend(["Marks"])
plt.show()
# Figure Size
plt.figure(figsize=(8, 5))
plt.plot(x, y)
plt.title("Figure Size Example")
plt.show()