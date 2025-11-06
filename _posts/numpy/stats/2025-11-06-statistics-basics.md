---
layout: post
title:  "Statistics Basics"
date:   2025-11-06 5:12:45 +0545
categories: numpy stats
---
Excellent — let’s turn this into a **structured series** of detailed articles, one for each concept:

- 1️⃣ Mean
- 2️⃣ Median
- 3️⃣ Mode
- 4️⃣ Standard Deviation
- 5️⃣ Covariance
- 6️⃣ Correlation

Each article will have **two major sections**:

* **Mathematical Concept** — with definitions, formulas, intuition, and examples.
* **NumPy Function** — explaining how to compute it programmatically with examples and interpretation.

Let’s begin the series below with **Part 1: Mean**, and I’ll continue the rest one by one afterward.

---

# 📘 Part 1: Mean — Mathematical Concept and NumPy Implementation

---

## 🧮 Mathematical Concept of Mean

### 1. Definition

The **mean**, also known as the **arithmetic average**, is a measure of **central tendency** — a single value that represents the “center” or “typical” value of a dataset.

$$
\text{Mean}(\bar{x})= \frac{\sum_{i=1}^{n} x_i}{n}
$$

Where:

* (x_i) = individual data points
* (n) = total number of observations

It’s simply the **sum of all observations divided by the number of observations**.

---

### 2. Intuitive Understanding

Think of mean as the **balancing point** of your data.
If each data point were a weight on a scale, the mean is where the scale would balance perfectly.

However, it’s **sensitive to extreme values (outliers)** — one unusually high or low number can pull the mean significantly in its direction.

---

### 3. Example

Dataset: [2, 4, 6, 8, 10]

[
\bar{x} = \frac{2 + 4 + 6 + 8 + 10}{5} = 6
]

So, the **mean** is **6**, representing the center of these values.

---

### 4. Types of Mean

There are multiple types of means used in different contexts:

| Type            | Formula                           | Use Case                              |
| --------------- | --------------------------------- | ------------------------------------- |
| Arithmetic Mean | ( \frac{\sum x_i}{n} )            | General average                       |
| Weighted Mean   | ( \frac{\sum w_i x_i}{\sum w_i} ) | When values have different importance |
| Geometric Mean  | ( (\prod x_i)^{1/n} )             | For growth rates, ratios              |
| Harmonic Mean   | ( \frac{n}{\sum \frac{1}{x_i}} )  | For rates and ratios (e.g., speed)    |

For this article, we focus on the **arithmetic mean**, as it’s most common in statistical analysis.

---

### 5. Mathematical Properties

1. **Sum of deviations** from the mean is always **zero**:
   [
   \sum (x_i - \bar{x}) = 0
   ]
2. **Mean minimizes squared deviations**:
   The arithmetic mean is the point where the sum of squared deviations is smallest — the foundation of **least squares regression**.
3. **Linear transformation** property:
   [
   \text{If } y = a + bx, \text{ then } \bar{y} = a + b\bar{x}
   ]

---

## 💻 NumPy Function for Mean

### 1. Function: `numpy.mean()`

**Syntax:**

```python
numpy.mean(a, axis=None, dtype=None, out=None, keepdims=False)
```

### 2. Parameters

| Parameter    | Description                                                               |
| ------------ | ------------------------------------------------------------------------- |
| **a**        | Input array or object containing numerical data                           |
| **axis**     | Axis or axes along which to compute the mean. Default is flattened array. |
| **dtype**    | Data type of the returned array.                                          |
| **out**      | Alternative output array.                                                 |
| **keepdims** | If True, retains reduced dimensions as size 1.                            |

---

### 3. Example 1: Basic Mean

```python
import numpy as np

data = np.array([2, 4, 6, 8, 10])
mean_value = np.mean(data)
print("Mean:", mean_value)
```

**Output:**

```
Mean: 6.0
```

---

### 4. Example 2: Mean Along an Axis

```python
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

mean_row = np.mean(matrix, axis=1)  # Row-wise mean
mean_col = np.mean(matrix, axis=0)  # Column-wise mean

print("Row-wise mean:", mean_row)
print("Column-wise mean:", mean_col)
```

**Output:**

```
Row-wise mean: [2. 5. 8.]
Column-wise mean: [4. 5. 6.]
```

---

### 5. Example 3: Weighted Mean (Manual)

NumPy doesn’t have a built-in weighted mean, but you can compute it easily:

```python
values = np.array([10, 20, 30])
weights = np.array([1, 2, 3])

weighted_mean = np.sum(values * weights) / np.sum(weights)
print("Weighted Mean:", weighted_mean)
```

**Output:**

```
Weighted Mean: 23.333333333333332
```

---

### 6. Numerical Stability Tip

If your data contains very large or very small values, you can use `dtype=np.float64` for precision:

```python
np.mean(data, dtype=np.float64)
```

---

### 7. Applications in Data Science

* Calculating **average performance metrics**
* Summarizing **sensor or time-series data**
* Finding **expected values** in probability distributions
* Normalization and **data preprocessing** (centering data around zero)

---

### 8. Common Mistakes

❌ Confusing mean with median (especially in skewed data)
❌ Ignoring missing values (use `np.nanmean()` for datasets with NaN)
✅ Always check data distribution before relying solely on mean.

---

## 🏁 Summary

| Concept | Formula                          | NumPy Function | Sensitive to Outliers | Common Use             |
| ------- | -------------------------------- | -------------- | --------------------- | ---------------------- |
| Mean    | ( \bar{x} = \frac{\sum x_i}{n} ) | `np.mean()`    | ✅ Yes                 | Average/Expected value |

---

### 👉 Next in Series: **Part 2 — Median: Understanding the Robust Middle**

Would you like me to continue right now with **Part 2 (Median)** in the same detailed style — first mathematically, then with NumPy examples?
