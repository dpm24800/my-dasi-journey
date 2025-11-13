# 6. Transposing DataFrame
import numpy as np
import pandas as pd

df = pd.DataFrame({'name':['a','b','c'], 'score':[20, 30,40]})

indexes = ['row1', 'row2', 'row3']
df.index = indexes

df1 = df.T
df2 = df.transpose()

print(df1, "\n")
print(df2)