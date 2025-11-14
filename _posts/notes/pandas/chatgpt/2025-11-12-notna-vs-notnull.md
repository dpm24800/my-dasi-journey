---
layout: post
title:  .notna() vs .notnull()
author: Dipak Pulami Magar
date: 2025-11-12 10:12:45 +0545
categories: pandas extra
status: draft
---
## `.notna()` vs `.notnull()` in pandas

Just like before, **these two are also identical** — both check for **non-missing values** (i.e., values that are *not* `NaN`, `None`, or `NaT`).

---

### 1. **Purpose**

They return `True` where the data **exists** (not missing).

Let’s use the same example:

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

### 2. **Using `notna()`**

```python
print(df.notna())
```

**Output:**

```
    name    age
0   True   True
1   True  False
2   True   True
3  False   True
```

---

### 3. **Using `notnull()`**

```python
print(df.notnull())
```

**Output (identical to `notna()`):**

```
    name    age
0   True   True
1   True  False
2   True   True
3  False   True
```

---

### **Comparison Table**

| Function  | Meaning        | Returns `True` When             | Same As     | Use For                |
| --------- | -------------- | ------------------------------- | ----------- | ---------------------- |
| `isna()`  | is missing     | Value is `NaN` / `None` / `NaT` | `isnull()`  | Finding missing values |
| `notna()` | is not missing | Value exists                    | `notnull()` | Keeping valid values   |

---

### **Quick Summary**

| Missing? | Function                | Returns |
| -------- | ----------------------- | ------- |
| Yes      | `isna()` / `isnull()`   | `True`  |
| No       | `notna()` / `notnull()` | `True`  |

---

### **Practical Examples**
#### Select only rows with missing data

```python
df[df.isna().any(axis=1)]
```

#### Select only rows with valid (non-missing) data

```python
df[df.notna().all(axis=1)]
```

#### Count missing values

```python
df.isna().sum()
```

---

### **Conclusion**

* `isna()` ≡ `isnull()` → detect missing values
* `notna()` ≡ `notnull()` → detect non-missing values
* Prefer `isna()` and `notna()` (modern naming, consistent with NumPy)

---
