# 5. Concatinating DataFrames
import numpy as np
import pandas as pd

df1 = pd.DataFrame({'name': ['sachin', 'virat', 'sourav'], 'wickets': [98, 97, 96], 'year': [1990, 2000, 2010]})

df2 = pd.DataFrame({'name': ['jack', 'robert', 'adam'], 'wickets': [90, 95, 92], 'year': [1990, 2000, 2010]})

df3 = pd.concat([df1, df2], axis=0)
df4 = pd.concat([df1, df2], axis=1)

print(df3)

print()
print(df4)