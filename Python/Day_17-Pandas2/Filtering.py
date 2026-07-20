import pandas as pd
data = {
    "Name": ["Ram", "Sam", "John", "Sai", "Ravi"],
    "Age": [21, 22, 20, 23, 24],
    "Marks": [90, 85, 95, 80, 75]
}
df = pd.DataFrame(data)
# Marks > 80
print("Marks > 80")
print(df[df["Marks"] > 80])
# Age >= 22
print("\nAge >= 22")
print(df[df["Age"] >= 22])
# AND Condition
print("\nMarks > 80 AND Age > 20")
print(df[(df["Marks"] > 80) & (df["Age"] > 20)])
# OR Condition
print("\nMarks > 90 OR Age > 23")
print(df[(df["Marks"] > 90) | (df["Age"] > 23)])