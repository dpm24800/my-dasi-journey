---
layout: post
title: "Array Manipulation – NumPy"
date: 2025-11-01 05:12:45 +0545
categories: jekyll numpy
---

## 7. Array Manipulation
### Reshaping Array: Changing Array Shape
**Reshaping Arrays**  
You can reshape a NumPy array to change its dimensions.


```python
arr = np.array([1, 2, 3, 4, 5, 6])

# Reshape the array into a 2D array (2 rows, 3 columns)
reshaped_arr = arr.reshape(2, 3)
print(reshaped_arr)
```

    [[1 2 3]
     [4 5 6]]

### Transposing Array
`arr.T` or `np.transpose(arr)`: Swaps the rows and columns (or permutes dimensions for N-D arrays).

#### Transposing 2-D Array
During the transpose of a 2D NumPy array:
- The number of columns becomes the number of rows.
- The number of rows becomes the number of columns.
  - Thus, a 2D array with shape `(3, 4)` becomes `(4, 3)` after transposition.

```python
# Transposing 2-D array

import numpy as np
arr2d = np.array([
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18]
])

arr2d_t = arr2d.T

print("Original Array:\n", arr2d, "\n")
print("Original Array Shape:", arr2d.shape)

print()
print("Transposed Array:\n", arr2d_t, "\n")
print("Transposed Array (shape):", arr2d_t.shape)
```

Output,
```
Original Array:
 [[ 1  2  3  4  5  6]
 [ 7  8  9 10 11 12]
 [13 14 15 16 17 18]] 

Original Array Shape: (3, 6)

Transposed Array:
 [[ 1  7 13]
 [ 2  8 14]
 [ 3  9 15]
 [ 4 10 16]
 [ 5 11 17]
 [ 6 12 18]] 

Transposed Array (shape): (6, 3)
```
**Note**: `np.transpose(arr)` also does the same thing as `arr.T` does, (i.e. transposition of array).

```python
# Transposing 2-D array

import numpy as np
arr2d = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
    [130, 140, 150, 160],
    [170, 180, 190, 200]
])

arr2d_t = np.transpose(arr2d)

print("Original Array:\n", arr2d, "\n")
print("Original Array Shape:", arr2d.shape)

print()
print("Transposed Array:\n", arr_trans, "\n")
print("Transposed Array (shape):", arr_trans.shape)
```

Output,
```
Original Array:
 [[ 10  20  30  40]
 [ 50  60  70  80]
 [ 90 100 110 120]
 [130 140 150 160]
 [170 180 190 200]] 

Original Array Shape: (5, 4)

Transposed Array:
 [[ 10  50  90 130 170]
 [ 20  60 100 140 180]
 [ 30  70 110 150 190]
 [ 40  80 120 160 200]] 

Transposed Array (shape): (4, 5)
```

#### Transposing 3-D Array
During the transpose of a 3D NumPy array:
  - The number of **columns** becomes the number of **blocks** (or depth).
  - The number of **rows** becomes the number of **columns**.
  - The number of **blocks** becomes the number of **rows**.
    - Thus, a 3D array with shape `(2, 3, 4)` becomes `(4, 3, 2)` after transposition.

**Explanation:**  
In a 3D array, the dimensions are typically represented as `(depth, rows, columns)`.
When you apply a transpose operation, NumPy rearranges these axes — by default, it reverses them (e.g., `(2, 3, 4)` becomes `(4, 3, 2)`).

So, if you want to describe it conceptually:
> Transposing a 3D array swaps the roles of blocks, rows, and columns — the structure is reoriented along different axes.

```python
# Transposing a 3-D array

import numpy as np
arr3d = np.array([
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
])

arr3d_t = arr3d.T

print("Original 3-D Array:\n", arr3d, "\n")
print("Original Array Shape:", arr3d.shape)

print()
print("Transposed 3-D Array:\n", arr3d_t, "\n")
print("Transposed Array Shape:", arr3d_t.shape)
```

Output,
```
Original 3-D Array:
 [[[ 1  2  3  4]
  [ 5  6  7  8]
  [ 9 10 11 12]]] 

Original Array Shape: (1, 3, 4)

Transposed 3-D Array:
 [[[ 1]
  [ 5]
  [ 9]]

 [[ 2]
  [ 6]
  [10]]

 [[ 3]
  [ 7]
  [11]]

 [[ 4]
  [ 8]
  [12]]] 

Transposed Array Shape: (4, 3, 1)
```

```py
# Transposing a 3-D array

import numpy as np
arr3d = np.array([
    [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]
    ], 
    [
        [21, 22, 23, 24, 25],
        [26, 27, 28, 29, 30],
        [31, 32, 33, 34, 35],
        [36, 37, 38, 39, 40]
    ],
    [
        [41, 42, 43, 44, 45],
        [46, 47, 48, 49, 50],
        [51, 52, 53, 54, 55],
        [56, 57, 58, 59, 50]
    ]
])

arr3d_t = np.transpose(arr3d)

print("Original 3-D Array:\n", arr3d, "\n")
print("Original Array Shape:", arr3d.shape)

print()
print("Transposed 3-D Array:\n", arr3d_t, "\n")
print("Transposed Array Shape:", arr3d_t.shape)
```

Output,
```
Original 3-D Array:
 [[[ 1  2  3  4  5]
  [ 6  7  8  9 10]
  [11 12 13 14 15]
  [16 17 18 19 20]]

 [[21 22 23 24 25]
  [26 27 28 29 30]
  [31 32 33 34 35]
  [36 37 38 39 40]]

 [[41 42 43 44 45]
  [46 47 48 49 50]
  [51 52 53 54 55]
  [56 57 58 59 50]]] 

Original Array Shape: (3, 4, 5)

Transposed 3-D Array:
 [[[ 1 21 41]
  [ 6 26 46]
  [11 31 51]
  [16 36 56]]

 [[ 2 22 42]
  [ 7 27 47]
  [12 32 52]
  [17 37 57]]

 [[ 3 23 43]
  [ 8 28 48]
  [13 33 53]
  [18 38 58]]

 [[ 4 24 44]
  [ 9 29 49]
  [14 34 54]
  [19 39 59]]

 [[ 5 25 45]
  [10 30 50]
  [15 35 55]
  [20 40 50]]] 

Transposed Array Shape: (5, 4, 3)
```


- **Arrays Concatenation and Stacking**:
  - `np.concatenate((arr1, arr2), axis=0/1)`: Joins a sequence of arrays along an existing axis.
  - 
- **Stacking helpers**:
    - `np.stack()`: joins along a *new* axis.
    - `np.vstack((a1, a2))`: (Vertical Stack): Joins arrays along the first axis (rows)
    - `np.hstack((a1, a2))`: (Horizontal Stack): Joins arrays along the second axis (columns)
    - `np.dstack()`: Stack along height, which is the same as depth: 
    - `np.row_stack()`: 
    - `np.column_stack()`: 
- **Splitting Arrays:**
    - `np.split()`: Split an array into multiple smaller arrays
    - `np.hsplit()`: 
    - `np.vsplit()`: 
    - `np.array_split()`: (allows uneven splits).