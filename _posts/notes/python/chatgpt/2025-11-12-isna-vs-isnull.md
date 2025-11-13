---
layout: post
title:  .isna() vs .isnull()
author: Dipak Pulami Magar
date: 2025-11-12 10:12:45 +0545
categories: pandas extra
status: draft
---

### Short Answer
- `isna()` and `isnull()` in pandas are **identical**.
- They both check for **missing (NaN)** values in a DataFrame or Series.

---

### Detailed Explanation

#### 1. Purpose

Both functions detect **missing data** (`NaN`, `None`, or `NaT`).

```python
import pandas as pd
import numpy as np

data = {
    'name': ['Dipak', 'Sita', 'Ram', None],
    'age': [25, np.nan, 30, 28]
}

df = pd.DataFrame(data)
print(df)
```

**Output:**

```
    name   age
0  Dipak  25.0
1   Sita   NaN
2    Ram  30.0
3   None  28.0
```

---

#### 2. **Using `isna()`**

```python
print(df.isna())
```

**Output:**

```
    name    age
0  False  False
1  False   True
2  False  False
3   True  False
```

---

#### 3. **Using `isnull()`**

```python
print(df.isnull())
```

**Output:** identical to `isna()`

```
    name    age
0  False  False
1  False   True
2  False  False
3   True  False
```

---

#### 4. **They return the same result**
In fact, pandas defines them like this in the source code:

```python
pd.isnull  = pd.isna
```

That means both functions **point to the same underlying implementation**.

---

### **Comparison Table**

| Feature                    | `isna()`  | `isnull()` | Same? |
| -------------------------- | --------- | ---------- | ----- |
| Detects NaN / None / NaT   | ✅         | ✅          | ✅     |
| Works on Series            | ✅         | ✅          | ✅     |
| Works on DataFrame         | ✅         | ✅          | ✅     |
| Introduced for readability | ✅ (newer) | Legacy     | ✅     |
| Preferred in documentation | ✅         |            |       |

---

### **Conclusion**

* ✅ `isna()` = `isnull()`
* ✅ Both detect missing values.
* ✅ Use `isna()` for modern, clean, and consistent code.

---

**Bonus Tip:**
To remove missing values:

```python
df.dropna(inplace=True)
```

To fill missing values:

```python
df.fillna(0, inplace=True)
```