---
layout: post
title:  "Broadcasting Arrays – NumPy"
date:   2025-11-05 12:12:45 +0545
categories: numpy
---
<center>
<!-- ![numpy-logo](../../../../assets/numpy-logo.png) -->
<img src="../../../../assets/numpy-logo.png">
</center>

## What Is Broadcasting?
**Broadcasting** is a mechanism that allows NumPy to apply operations (like addition, subtraction, multiplication, etc.) on arrays of **different shapes** by **automatically expanding** the smaller array so that both arrays have compatible shapes.

In simple terms:
> Broadcasting lets NumPy “stretch” smaller arrays across larger ones without making actual copies, so operations can be performed element-wise.

### Example: Without Broadcasting

Let’s start with a simple example.

```python
import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

print(a + b)
```

**Output**,

```
[11 22 33 44]
```

Here, both arrays `a` and `b` have the same shape `(4,)`, so NumPy performs **element-wise addition** — this is straightforward.

### Example: With Broadcasting
Now suppose you have a **1D array** and want to add it to a **2D array**.

```python
A = np.array([[1, 2, 3],
              [4, 5, 6]])

b = np.array([10, 20, 30])

print(A + b)
```

**Output:**

```
[[11 22 33]
 [14 25 36]]
```

Here, `A` has shape `(2, 3)` and `b` has shape `(3,)`.

NumPy **broadcasts** `b` to match the shape of `A`:

```
b → [[10, 20, 30],
     [10, 20, 30]]
```
Then, it performs element-wise addition.


### Broadcasting Rules
To understand how broadcasting works behind the scenes, NumPy follows a set of **broadcasting rules** to align array dimensions.

**Rule 1:** Compare shapes from right to left.
- Start comparing each dimension of both arrays from the **trailing (rightmost)** side.

**Rule 2:** Dimensions must be either equal or one of them must be 1.
- If the sizes match, or one of them is **1**, NumPy can stretch (broadcast) that dimension.
- If neither condition is met → **broadcasting error** occurs.

**Rule 3:** If one array has fewer dimensions, pad its shape with ones on the left.

### Example: Different Shapes
Let’s visualize with an example:

```python
A = np.array([[1],
              [2],
              [3]])   # Shape: (3, 1)

B = np.array([10, 20, 30])  # Shape: (3,)
```

Now let’s see what happens if we try:

```python
A + B
```

**Step 1:** Adjust shapes:

```
A → (3, 1)
B → (1, 3)
```

**Step 2:** Broadcasting expands both arrays to shape `(3, 3)`.

```
A → [[1, 1, 1],
     [2, 2, 2],
     [3, 3, 3]]

B → [[10, 20, 30],
     [10, 20, 30],
     [10, 20, 30]]
```

**Result:**

```
[[11 21 31]
 [12 22 32]
 [13 23 33]]
```

### When Broadcasting Fails
If dimensions are **incompatible**, NumPy raises a `ValueError`.

```python
A = np.array([[1, 2, 3],
              [4, 5, 6]])   # Shape: (2, 3)

B = np.array([1, 2])        # Shape: (2,)

A + B
```

**Error:**

```
ValueError: operands could not be broadcast together with shapes (2,3) (2,)
```

Why?
* Comparing from right to left:

  * `3` (A) ≠ `2` (B)
  * Shapes don’t match, and none of them is `1`.


### Real-Life Use Cases

#### 1. **Adding Constants to Arrays**

```python
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print(arr + 10)
```

**Output**,
```
[[11 12 13]
 [14 15 16]]
```

Here, the scalar `10` is **broadcast** to match the shape of `arr`.

---

#### 2. **Row or Column Operations**

Add a 1D array (row) to every row of a 2D matrix:

```python
A = np.array([[1, 2, 3],
              [4, 5, 6]])
b = np.array([10, 20, 30])
print(A + b)
```

Add a column vector to each column:

```python
A = np.array([[1, 2, 3],
              [4, 5, 6]])
b = np.array([[10],
              [20]])
print(A + b)
```

### Visual Summary

| Example  | Shape 1 | Shape 2 | Result | Broadcasted      |
| -------- | ------- | ------- | ------ | ---------------- |
| `A + 10` | (2, 3)  | ()      | (2, 3) | Scalar → All     |
| `A + b`  | (2, 3)  | (3,)    | (2, 3) | Row broadcast    |
| `A + c`  | (2, 3)  | (2, 1)  | (2, 3) | Column broadcast |

### Behind the Scenes: Memory Efficiency
Broadcasting **does not create new copies** of data. Instead, NumPy uses **virtual expansion** — it behaves as if data were duplicated but avoids the actual memory cost. This makes broadcasting extremely **fast and memory-efficient**.

### Summary

- **Definition**: Automatic alignment of arrays with different shapes for element-wise operations.
- **When it works**: Shapes match or one of the dimensions is 1.
- **When it fails**: Incompatible dimensions that cannot be aligned.
- **Benefit**: Reduces code, avoids loops, increases speed and efficiency


### Key Takeaways
* Broadcasting enables **vectorized operations** without explicit looping.
* NumPy automatically expands smaller arrays to perform element-wise arithmetic.
* Use broadcasting wisely for **cleaner and faster** numerical computations.
* Always check array **shapes** before applying broadcasting.

### Final Example
```python
# Multiply a 3x3 matrix by a 1D array
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
b = np.array([1, 0, -1])

print(A * b)
```

**Output:**

```
[[ 1  0 -3]
 [ 4  0 -6]
 [ 7  0 -9]]
```

Here, the array `b` is broadcast across every row of `A`, giving an elegant, efficient operation — all thanks to **NumPy broadcasting**.