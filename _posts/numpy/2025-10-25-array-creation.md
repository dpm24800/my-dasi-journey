---
layout: post
title:  "Array Creation – NumPy"
date:   2025-11-02 20:40:45 +0545
categories: jekyll numpy
---
## Table of Contents
- [Table of Contents](#table-of-contents)
- [1. From Python (Data) Structures: np.array(\[list/tuple\])](#1-from-python-data-structures-nparraylisttuple)
- [2. Initial Placeholders](#2-initial-placeholders)
  - [2.1 np.zeros(shape) ✅](#21-npzerosshape-)
  - [2.2. np.ones(shape) ✅](#22-nponesshape-)
  - [2.3. np.full(shape, fill\_value) ✅](#23-npfullshape-fill_value-)
  - [2.4. np.empty(shape)](#24-npemptyshape)
  - [2.5. np.eye(N) or np.identity(N)](#25-npeyen-or-npidentityn)
    - [np.eye()](#npeye)
    - [np.identity()](#npidentity)
- [3. Array Range: np.arange()](#3-array-range-nparange)
  - [3.1. 1-D Sequence](#31-1-d-sequence)
  - [3.2. N-D Sequence: using reshape() with arange()](#32-n-d-sequence-using-reshape-with-arange)
    - [2-D Sequence](#2-d-sequence)
    - [3-D Sequence](#3-d-sequence)
    - [4-D Sequence](#4-d-sequence)
- [4. Linearly spaced values: np.linspace()](#4-linearly-spaced-values-nplinspace)

---

## 1. From Python (Data) Structures: np.array([list/tuple])
- Create an array from a Python list or tuple.

## 2. Initial Placeholders
### 2.1 np.zeros(shape) ✅
The `np.zeros()` function creates an array of a specified **shape** filled entirely with **zeros**.

* **Syntax:** `np.zeros(shape, dtype=None)`
  * The `shape` parameter defines the dimensions of the array.
  * The optional `dtype` argument specifies the data type (default is `float`).

**1-D array of zeros**: 
```py
# Create 1-D array with zeros (placeholder)
import numpy as np
arr1 = np.zeros(5) # default data type: float
arr1i = np.zeros(5, dtype=int) # change data type into int with `dtype` parameter

print(arr1)
print(arr1i)
```
Output,
```
[0. 0. 0. 0. 0.]
[0 0 0 0 0]
```

**2-D array of zeros**: 
```py
# Create 2-D array with zeros (placeholder)
import numpy as np
arr2 = np.zeros((4, 5), dtype=int)
print(arr2)
```
Output,
```
[[0 0 0 0 0]
 [0 0 0 0 0]
 [0 0 0 0 0]
 [0 0 0 0 0]]
```
**3-D array of zeros**: 
```py
# Create 3-D array with zeros (placeholder)
import numpy as np
arr3 = np.zeros((3, 4, 5), dtype=int)
print(arr3)
```

Output,
```
[[[0 0 0 0 0]
  [0 0 0 0 0]
  [0 0 0 0 0]
  [0 0 0 0 0]]

 [[0 0 0 0 0]
  [0 0 0 0 0]
  [0 0 0 0 0]
  [0 0 0 0 0]]

 [[0 0 0 0 0]
  [0 0 0 0 0]
  [0 0 0 0 0]
  [0 0 0 0 0]]]
```

**4-D array of zeros**: 
```py
# Create 4-D array with zeros (placeholder)
import numpy as np
arr4 = np.zeros((2, 3, 4, 5), dtype=int)
print(arr4)
```

Output,
```
[[[[0 0 0 0 0]
   [0 0 0 0 0]
   [0 0 0 0 0]
   [0 0 0 0 0]]

  [[0 0 0 0 0]
   [0 0 0 0 0]
   [0 0 0 0 0]
   [0 0 0 0 0]]

  [[0 0 0 0 0]
   [0 0 0 0 0]
   [0 0 0 0 0]
   [0 0 0 0 0]]]


 [[[0 0 0 0 0]
   [0 0 0 0 0]
   [0 0 0 0 0]
   [0 0 0 0 0]]

  [[0 0 0 0 0]
   [0 0 0 0 0]
   [0 0 0 0 0]
   [0 0 0 0 0]]

  [[0 0 0 0 0]
   [0 0 0 0 0]
   [0 0 0 0 0]
   [0 0 0 0 0]]]]
```

### 2.2. np.ones(shape) ✅
The `np.ones()` function creates an array of a specified **shape** filled entirely with **ones**.

* **Syntax:** `np.ones(shape, dtype=None)`
  * The `shape` parameter defines the dimensions of the array.
  * The optional `dtype` argument specifies the data type (default is `float`).

**1-D array of ones**: 
```py
import numpy as np
arr1 = np.ones(5) # 1-D 
arr1i = np.ones(5, dtype=int) # 

print(arr1)
print(arr1i)
```
Output,
```
[1. 1. 1. 1. 1.]
[1 1 1 1 1]
```

**2-D array of ones**: 
```py
import numpy as np
arr2 = np.ones((4, 5), dtype=int) # 2-D
print(arr2)
```
Output,
```
[[1 1 1 1 1]
 [1 1 1 1 1]
 [1 1 1 1 1]
 [1 1 1 1 1]]
```
**3-D array of ones**: 
```py
import numpy as np
arr3 = np.ones((3, 4, 5), dtype=int) # 3-D 
print(arr3)
```

Output,
```
[[[1 1 1 1 1]
  [1 1 1 1 1]
  [1 1 1 1 1]
  [1 1 1 1 1]]

 [[1 1 1 1 1]
  [1 1 1 1 1]
  [1 1 1 1 1]
  [1 1 1 1 1]]

 [[1 1 1 1 1]
  [1 1 1 1 1]
  [1 1 1 1 1]
  [1 1 1 1 1]]]
```

**4-D array of ones**: 
```py
import numpy as np
arr4 = np.ones((2, 3, 4, 5), dtype=int) # 4-D
print(arr4)
```

Output,
```
[[[[1 1 1 1 1]
   [1 1 1 1 1]
   [1 1 1 1 1]
   [1 1 1 1 1]]

  [[1 1 1 1 1]
   [1 1 1 1 1]
   [1 1 1 1 1]
   [1 1 1 1 1]]

  [[1 1 1 1 1]
   [1 1 1 1 1]
   [1 1 1 1 1]
   [1 1 1 1 1]]]


 [[[1 1 1 1 1]
   [1 1 1 1 1]
   [1 1 1 1 1]
   [1 1 1 1 1]]

  [[1 1 1 1 1]
   [1 1 1 1 1]
   [1 1 1 1 1]
   [1 1 1 1 1]]

  [[1 1 1 1 1]
   [1 1 1 1 1]
   [1 1 1 1 1]
   [1 1 1 1 1]]]]
```
### 2.3. np.full(shape, fill_value) ✅
The `np.full()` function creates an array of a given *shape* and fills it with a *specified constant value*.
- **Syntax**: `np.full(shape, fill_value, dtype=None)`
  - The `shape` defines the dimensions of the array.
  - The `fill_value` specifies the value to fill the array with.
  - The optional `dtype` argument sets the data type (default is `float`).

```py
# Create a 2D array of shape (4, 4) filled with 5
import numpy as np
arr24 = np.full((4, 4), 5)

print("np.full((4, 4), 5):\n", arr24)
```
Output,
```
np.full((4, 4), 5):
 [[5 5 5 5]
 [5 5 5 5]
 [5 5 5 5]
 [5 5 5 5]]
```

```py
# Create a 3-D array of shape (2, 4, 4) filled with 10
import numpy as np
arr25 = np.full((2, 4, 4), 10)

print("np.full((2, 4, 4), 10):\n", arr25)
```

Output,
```
np.full((2, 4, 4), 10):
 [[[10 10 10 10]
  [10 10 10 10]
  [10 10 10 10]
  [10 10 10 10]]

 [[10 10 10 10]
  [10 10 10 10]
  [10 10 10 10]
  [10 10 10 10]]]
```

### 2.4. np.empty(shape)
The `np.empty()` function creates an array of a specified **shape** without initializing its values — that is, the array contains **EMPTY/random or uninitialized values** already present at that memory location.

* **Syntax:** `np.empty(shape, dtype=float)`
  * The `shape` parameter defines the dimensions of the array.
  * The optional `dtype` argument specifies the data type (default is `float`).



### 2.5. np.eye(N) or np.identity(N)
Creates an N times IDENTITY MATRIX:  
Both `np.eye()` and `np.identity()` functions create a **2-D identity matrix**, where all diagonal elements are **1** and all other elements are **0**.

#### np.eye()
* **Syntax:** `np.eye(N, M=None, k=0, dtype=float)`
  * `N` → number of rows
  * `M` → number of columns (defaults to `N` for a square matrix)
  * `k` → index of the diagonal (0 is main diagonal)

```python
import numpy as np
arr = np.eye(3)
print(arr)
```

Output,
```
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
```

#### np.identity()
* **Syntax:** `np.identity(n, dtype=None)`
  * Always creates a **square identity matrix** of size `n x n`.

```python
arr = np.identity(4)
print(arr)
```

Output,
```
[[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]]
```

> Use `np.eye()` for more control (e.g., non-square matrices or shifted diagonals),
> and `np.identity()` for simple square identity matrices.

## 3. Array Range: np.arange()
The term arange comes from “array” + “range.”
It means “create an array within a range of values.”

In Python, the built-in range() function generates a sequence of numbers — but it doesn’t return an array.  
NumPy’s np.arange() does the same thing, except it returns a NumPy array instead of a Python range object.

The `arange()` function creates a **1-D array** of numbers within a specified range.
* With **one argument** → interpreted as `end` (exclusive).
* With **two arguments** → interpreted as `start` and `end` (exclusive).
* With **three arguments** → interpreted as `start`, `end` (exclusive), and `step`.

The **default step size** is `1`, and a **negative step (-1)** generates a decreasing sequence.

### 3.1. 1-D Sequence
```py
import numpy as np
arr1 = np.arange(10)        # start=0, end=10 (exclusive), step=1
arr2 = np.arange(2, 15)     # start=2, end=15 (exclusive), step=1
arr3 = np.arange(1, 20, 2)  # start=1, end=20 (exclusive), step=2

print("np.arange(10):\n", arr1, "\n")
print("np.arange(2, 15):\n", arr2, "\n")
print("np.arange(1, 20, 2):\n", arr3, "\n")
```

Output,
```
np.arange(10):
 [0 1 2 3 4 5 6 7 8 9] 

np.arange(2, 15):
 [ 2  3  4  5  6  7  8  9 10 11 12 13 14] 

np.arange(1, 20, 2):
 [ 1  3  5  7  9 11 13 15 17 19] 

```

```py
import numpy as np
arr4 = np.arange(20, 10, -1)    # start=20, end=10 (exclusive), step=-1
arr5 = np.arange(-10, 1)        # start=-10, end=1 (exclusive), step=1
arr6 = np.arange(-10, 1, 2)     # start=-10, end=1 (exclusive), step=2

print("np.arange(20, 10, -1):\n", arr4, "\n")
print("np.arange(-10, 1):\n", arr5, "\n")
print("np.arange(-10, 1, 2):\n", arr6, "\n")
```

Output,
```
np.arange(20, 10, -1):
 [20 19 18 17 16 15 14 13 12 11] 

np.arange(-10, 1):
 [-10  -9  -8  -7  -6  -5  -4  -3  -2  -1   0] 

np.arange(-10, 1, 2):
 [-10  -8  -6  -4  -2   0] 
```
### 3.2. N-D Sequence: using reshape() with arange()  
If you want to create a range of numbers in **multiple dimensions**, you can use the `reshape()` function to specify the desired shape.  

However, ensure that the **total number of elements** in the new shape matches the number of elements generated by `arange()`. 

Otherwise, it will raise an error such as: `ValueError: cannot reshape array of size 20 into shape (5,6)` with `np.arange(1, 21).reshape(5, 6)`

#### 2-D Sequence
```py
import numpy as np
# Create a 2D array (5x6) with numbers from 1 to 30
arr2d = np.arange(1, 31).reshape(5, 6)
print("np.arange(1, 31).reshape(5, 6):\n", arr2d)
```
Output,
```
np.arange(1, 31).reshape(5, 6):
 [[ 1  2  3  4  5  6]
 [ 7  8  9 10 11 12]
 [13 14 15 16 17 18]
 [19 20 21 22 23 24]
 [25 26 27 28 29 30]]
```
#### 3-D Sequence
```py
import numpy as np
# Create a 3D array sized (3, 5, 4) with numbers from 1 to 60
arr3d = np.arange(1, 61).reshape(3, 5, 4)
print("np.arange(1, 61).reshape(3, 5, 4):\n", arr3d)
```
Output,
```
np.arange(1, 61).reshape(3, 5, 4):
 [[[ 1  2  3  4]
  [ 5  6  7  8]
  [ 9 10 11 12]
  [13 14 15 16]
  [17 18 19 20]]

 [[21 22 23 24]
  [25 26 27 28]
  [29 30 31 32]
  [33 34 35 36]
  [37 38 39 40]]

 [[41 42 43 44]
  [45 46 47 48]
  [49 50 51 52]
  [53 54 55 56]
  [57 58 59 60]]]
```
#### 4-D Sequence
```py
import numpy as np
# Create a 4D array sized (2, 3, 4, 5) with numbers from 1 to 120
arr4d = np.arange(1, 121).reshape(2, 3, 4, 5)
print("np.arange(1, 121).reshape(2, 3, 4, 5):\n", arr4d)
```
Output,
```
np.arange(1, 121).reshape(2, 3, 4, 5):
 [[[[  1   2   3   4   5]
   [  6   7   8   9  10]
   [ 11  12  13  14  15]
   [ 16  17  18  19  20]]

  [[ 21  22  23  24  25]
   [ 26  27  28  29  30]
   [ 31  32  33  34  35]
   [ 36  37  38  39  40]]

  [[ 41  42  43  44  45]
   [ 46  47  48  49  50]
   [ 51  52  53  54  55]
   [ 56  57  58  59  60]]]


 [[[ 61  62  63  64  65]
   [ 66  67  68  69  70]
   [ 71  72  73  74  75]
   [ 76  77  78  79  80]]

  [[ 81  82  83  84  85]
   [ 86  87  88  89  90]
   [ 91  92  93  94  95]
   [ 96  97  98  99 100]]

  [[101 102 103 104 105]
   [106 107 108 109 110]
   [111 112 113 114 115]
   [116 117 118 119 120]]]]
```

## 4. Linearly spaced values: np.linspace()
The `np.linspace()` function creates an array with a **specified number of evenly spaced values** between a **start** and **stop** value (inclusive by default).

* **Syntax:** `np.linspace(start, stop, num=50, endpoint=True, dtype=None)`
  * `start` → starting value of the sequence
  * `stop` → ending value of the sequence
  * `num` → number of samples to generate (default is 50)
  * `endpoint` → if `True`, the stop value is included in the range
  * `dtype` → optional data type of the output array

**Example:**

```python
import numpy as np
arr = np.linspace(0, 10, 5)
print(arr)
```

Output,
```
[ 0.   2.5  5.   7.5 10. ]
```

> Use `np.linspace()` when you need a specific number of equally spaced values within a range (useful in plotting and mathematical computations).
