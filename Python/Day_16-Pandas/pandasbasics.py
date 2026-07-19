import pandas as pd
print(pd.__version__)# Create Series
#Create series
s = pd.Series([10,20,30,40,50])
print(s)
# Custom Index
s = pd.Series([90,80,70],index=["Math","Science","English"])
print(s)
# Access Elements
print(s["Math"])
# Name
s.name="Marks"
print(s)