---
layout: post
title:  Data Analysis Basics
description: 
# thumbnail: ../../../../../assets/Correl.png
author: Dipak Pulami Magar
date:   2025-11-12 10:12:45 +0545
categories: pandas
status: published
---

- [Group By and Aggregate Functions in Pandas | Python Pandas Tutorials](https://www.youtube.com/watch?v=VRmXto2YA2I)
- [How to use Pandas Groupby Like a Pro!](https://www.youtube.com/watch?v=CCTXOVCr9us)

- [Summarizing data using Group by in PYTHON PANDAS | HINDI TUTORIAL](https://www.youtube.com/watch?v=fQIuHkDRiek)
- [How to handle Missing data in PYTHON PANDAS | HINDI TUTOTIAL](https://www.youtube.com/watch?v=rsxMYBTUHVo)
- [How to Remove duplicates from dataset in PYTHON PANDAS | HINDI TUTORIAL ](https://www.youtube.com/watch?v=IkeIeCUxhwA)


df.drop_duplicates(subset='brand', keep='last')
df.drop_duplicates() ---> checks duplicates in all columns.

df[df.col1.notnull()]

- Detecting missing values
df.isnull().sum()
df.isnull().sum().sort_values(ascending=False)

- Dropping missing values
df.dropna(how='all', axis=1)  ---> delete the entire column, if there's missing values in its all rows
df.dropna(how='all') ---> default axis=0
df.dropna() ---> delete the entire row, if there is missing value in any of its column

- Filling missing values
df.fillna(0) ---> fills 0 in the missing values of entire dataset
df['col1'] = df['col1'].fillna(0) ---> fills 0 in the missing values of col1
df[['col1', 'col2']] = df[['col1', 'col2']].fillna(0) ---> fills the missing values of two columns with 0

df['col3'] = df['col3'].fillna(method='ffill') ---> fills the missing value with its previous data
df['col3'] = df['col3'].fillna(method='bfill') ---> fills the missing value with its successive data
df['col1'] = df['col1'].fillna(df['col1'].mean() ---> fills the missing value with its(column's) mean
df['col2'] = df['col2'].fillna(df['col2'].median() ---> fills the missing value with its(column's) mean



df.head()
df.tail()
df.col1.head()
df[['col1', 'col2']].head()

df.shape
df.size
df.columns
df.index
df.axes
df.dtypes

df.select_dtypes(include=np.number)
df.select_dtypes(include=np.object)

---

# x. Adding Index to a DataFrame: [done]
```py
import numpy as np
import pandas as pd

df = pd.DataFrame({'name':['a','b','c'], 'score':[20, 30,40]})
indexes = ['row1', 'row2', 'row3']

print("df without index:"); print(df); print()
df.index = indexes; 

print("df with index added:"); print(df); print()
```
Output,

```
df without index:
  name  score
0    a     20
1    b     30
2    c     40

df with index added:
     name  score
row1    a     20
row2    b     30
row3    c     40
```

---

# 4. Dropping columns
df1 = df[['col1', 'col2']] # making new dataset from selected columns
df = df.drop(['col2'], axis=1) # drop column 
df = df.drop(['col1', ''col2'], axis=1) # drop two columns from dataframe

---

# 5. Renaming columns: 
df1 = df.rename(columns={'col1':'cola','col2':'colb'})
df1.columns = df1.columns + '_n'

---

# 6. Transposing a DataFrame: [done]
```py
import numpy as np
import pandas as pd

df = pd.DataFrame({
     'name':['a','b','c'], 
     'score':[20, 30,40]}, 
     index=['row1', 'row2', 'row3'])

df1 = df.T # transposed: changed rows to column and vice versa
df2 = df1.transpose() # transposed back to original form

print("original df:"); print(df); print()
print("df transposed: (df1 = df.T)"); print(df1); print()
print("df2 transposed back to original: (df3 = df2.transpose())"); print(df2)
```

**Output**:
```
original df:
     name  score
row1    a     20
row2    b     30
row3    c     40

df transposed: (df1 = df.T)
      row1 row2 row3
name     a    b    c
score   20   30   40

df2 transposed back to original: (df3 = df2.transpose())
     name score
row1    a    20
row2    b    30
row3    c    40
```
---

# 7. Concatinating DataFrames: [done]
```py
import pandas as pd

df1 = pd.DataFrame({'name': ['sachin', 'virat', 'sourav'], 
                    'wickets': [98, 97, 96], 
                    'year': [1990, 2000, 2010]})

df2 = pd.DataFrame({'name': ['mark', 'robert', 'adam'], 
                    'wickets': [90, 95, 92], 
                    'year': [1990, 2000, 2010]})

df3 = pd.concat([df1, df2], axis=0)
df4 = pd.concat([df1, df2], axis=1)

print("df1:\n", df1, "\n")
print("df2:\n", df2, "\n")

print("pd.concat([df1, df2], axis=0):")
print(df3, "\n")

print("pd.concat([df1, df2], axis=1):")
print(df4)
```

**Output**:
```
df1:
      name  wickets  year
0  sachin       98  1990
1   virat       97  2000
2  sourav       96  2010

 df2:
      name  wickets  year
0    mark       90  1990
1  robert       95  2000
2    adam       92  2010 

pd.concat([df1, df2], axis=0):
     name  wickets  year
0  sachin       98  1990
1   virat       97  2000
2  sourav       96  2010
0    mark       90  1990
1  robert       95  2000
2    adam       92  2010

pd.concat([df1, df2], axis=1):
     name  wickets  year    name  wickets  year
0  sachin       98  1990    mark       90  1990
1   virat       97  2000  robert       95  2000
2  sourav       96  2010    adam       92  2010
```


