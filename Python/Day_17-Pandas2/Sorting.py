import pandas as pd
data = {
    "Name": ["Ram", "Sam", "John", "Sai", "Ravi"],
    "Age": [21, 22, 20, 23, 24],
    "Marks": [90, 85, 95, 80, 75]
}
df = pd.DataFrame(data)
# Ascending
print("Ascending Order")
print(df.sort_values("Marks"))
# Descending
print("\nDescending Order")
print(df.sort_values("Marks", ascending=False))
# Multiple Columns
print("\nSort by Age and Marks")
print(df.sort_values(["Age", "Marks"]))