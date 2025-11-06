---
layout: post
title: Some articles are just so short
categories: misc
status: published
---

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.


$$\bar{x} = \sum a$$

---

Perfect ✅ — that’s a **great direction** for your data science blog series, Dipak!
You’ll be covering the **core descriptive statistics** — essential for any beginner in **data analysis, ML, or AI**.

Here’s how we can structure the **series**:

---

## 📘 Series Title: “Descriptive Statistics with NumPy — Step-by-Step Guide”

### Articles Overview:

1. **Mean — The Measure of Central Tendency**
2. **Median — The Middle of Your Data**
3. **Mode — The Most Frequent Value**
4. **Standard Deviation — Measuring Spread**
5. **Covariance — How Two Variables Move Together**
6. **Correlation — Measuring Strength of Relationship**

---

Each article will include:

1. **Conceptual and Mathematical Explanation**
2. **Manual Calculation Example**
3. **NumPy Implementation**
4. **Practical Use Case**
5. **Summary**

---

Let’s begin with **Article 1: Mean** 👇

---

# 🧮 Mean — The Measure of Central Tendency

The **mean** (or **average**) is one of the most fundamental statistical concepts.
It gives us a single number that represents the **center** of a dataset — a way to summarize all values into one representative figure.

---

## 🔹 1. Mathematical Definition

If you have ( n ) data points ( x_1, x_2, x_3, \ldots, x_n ), the **mean** is calculated as:

$$
\bar{X} = \frac{x_1 + x_2 + x_3 + \cdots + x_n}{n}
$$

or simply: 

$$\bar{X} = \frac{\sum_{i=1}^{n} x_i}{n}$$


---

### 🧮 Example:

Let’s say you have the following dataset:
$$
X = [2, 4, 6, 8, 10]
$$

Then:
$$
\bar{X} = \frac{2 + 4 + 6 + 8 + 10}{5} = \frac{30}{5} = 6
$$

✅ The **mean** is **6**, meaning the “center” of this data lies around 6.

---

## 🔹 2. Why Mean Matters

* **Gives overall trend:** Represents the “average” behavior of data.
* **Useful for comparison:** e.g., average income, average temperature, etc.
* **Foundation for other metrics:** Used in calculating variance, standard deviation, covariance, etc.

However, mean is **sensitive to outliers**.
For example, [2, 4, 6, 8, 100] → Mean = 24, which doesn’t represent most data points well.

---

## 🔹 3. Mean in NumPy

NumPy provides multiple ways to compute mean efficiently:

### ✅ Basic Example:

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

### ✅ Mean Across Axes:

If you have a 2D array, you can compute mean across rows or columns.

```python
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print("Mean of all elements:", np.mean(arr))
print("Mean of each column:", np.mean(arr, axis=0))
print("Mean of each row:", np.mean(arr, axis=1))
```

**Output:**

```
Mean of all elements: 5.0
Mean of each column: [4. 5. 6.]
Mean of each row: [2. 5. 8.]
```

---

### ✅ Weighted Mean:

If some data points are more important, use **`np.average()`** with weights.

```python
values = np.array([10, 20, 30])
weights = np.array([1, 2, 3])

weighted_mean = np.average(values, weights=weights)
print("Weighted Mean:", weighted_mean)
```

**Output:**

```
Weighted Mean: 23.333333333333332
```

Here, higher weights make `30` influence the mean more.

---

## 🔹 4. Real-Life Example

Suppose we have student marks from 5 subjects:

```python
marks = np.array([78, 82, 69, 90, 76])
mean_marks = np.mean(marks)
print("Average marks:", mean_marks)
```

**Output:**

```
Average marks: 79.0
```

So the student’s average score across subjects is 79.

---

## 🔹 5. Summary

| Concept                   | Description                              |
| :------------------------ | :--------------------------------------- |
| **Formula**               | $$ \bar{X} = \frac{\sum x_i}{n} $$         |
| **NumPy Function**        | `np.mean()` or `np.average()`            |
| **Sensitive to Outliers** | ✅ Yes                                    |
| **Used in**               | Variance, standard deviation, covariance |

---

### 💡 Tip:

In data analysis, use **median** instead of mean when your data contains **outliers** (e.g., income, house prices).

---

Would you like me to continue with the **next article: “Median — The Middle of the Data”** in the same format (mathematics + NumPy + examples + real-world note)?
