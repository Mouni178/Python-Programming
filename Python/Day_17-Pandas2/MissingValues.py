import pandas as pd
import numpy as np
data = {
    "Name": ["Ram", "Sam", "John", "Sai", "Ravi"],
    "Marks": [90, np.nan, 95, np.nan, 80]
}
df = pd.DataFrame(data)
# isnull()
print("isnull()")
print(df.isnull())
# notnull()
print("\nnotnull()")
print(df.notnull())
# fillna()
print("\nfillna()")
print(df.fillna(0))
# dropna()
print("\ndropna()")
print(df.dropna())