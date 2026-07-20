import pandas as pd
data = {
    "Name": ["Mounika", "Shiva", "Jayanth", "Sai", "Raju"],
    "Age": [21, 22, 20, 23, 24],
    "Marks": [90, 85, 95, 80, 75]
}
df = pd.DataFrame(data)
# Single Column
print("Name Column")
print(df["Name"])
# Multiple Columns
print("\nName and Marks")
print(df[["Name", "Marks"]])
# loc[]
print("\nloc[]")
print(df.loc[2])
print("\nloc() Multiple Rows")
print(df.loc[1:3])
# iloc[]
print("\niloc[]")
print(df.iloc[2])
print("\niloc() Multiple Rows")
print(df.iloc[1:4])
print("\nSpecific Row and Column")
print(df.iloc[2, 1])
print("\nMultiple Rows and Columns")
print(df.iloc[0:3, 0:2])