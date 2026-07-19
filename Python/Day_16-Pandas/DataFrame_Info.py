import pandas as pd
data={
    "Name":["Ram","Sam","John","Ravi","Sai"],
    "Age":[21,22,23,24,25],
    "Marks":[90,85,95,88,91]
}
df=pd.DataFrame(data)
# head()
print(df.head())
# tail()
print(df.tail())
# shape
print(df.shape)
# size
print(df.size)
# columns
print(df.columns)
# index
print(df.index)
# dtypes
print(df.dtypes)
# info()
df.info()
# describe()
print(df.describe())