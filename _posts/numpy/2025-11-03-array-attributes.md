---
layout: post
title:  "Array Attributes – NumPy"
date:   2025-11-03 21:12:45 +0545
categories: numpy
---

**Table of Contents**:
- [Array Dimensions (`array.ndim`)](#array-dimensions-arrayndim)
    - [1. Zero Dimensional (0-D) Array/Scalar](#1-zero-dimensional-0-d-arrayscalar)
    - [2. One Dimensional (1-D) Array](#2-one-dimensional-1-d-array)
    - [2. Two Dimensional (2-D) Array](#2-two-dimensional-2-d-array)
    - [3. Three Dimensional (3-D) Array](#3-three-dimensional-3-d-array)
 
---

&nbsp;

Here are key/important ndarray object attributes/properties:
- `array.ndim` – the number of dimensions (axes) of the array.
- `array.shape` – dimensions of the array; A tuple of integers indicating the size of the array in each dimension (e.g., `(rows, columns)`).
- `array.size` – total number of elements
- `array.dtype` – data type of elements (e.g., `np.int64`, `np.float32`, `bool_`, `'<U10'` for string)
- `array.itemsize` – size of each element (in bytes)
- `array.nbytes` – total memory consumed // total size in bytes (`.size * .itemsize`)
- `array.data`: 

- **Data Types (`dtype`)**
 - Importance of `dtype` for memory and precision.
    - Common types: `int8/16/32/64`, `uint8/16/32/64`, `float16/32/64`, `complex64/128`, `bool_`, `object_`, `string_`.
    - Specifying and converting dtypes: `dtype` parameter, `.astype()` method.

If you have not read this post yet, please consider reading this post - [Array Creation](#), as current post builds upon [Array Creation](#).



## Array Dimensions (`array.ndim`) 
- `array.ndim` attribute returns the number of dimensions of an array. 
- It tells you how many axes the array has, which corresponds to the number of nested levels of lists used to create it.

#### 1. Zero Dimensional (0-D) Array/Scalar
- A single value (like the number (5)) is a zero-dimensional array, 
- So `array.ndim` would be 0.

```python
# Zero-dimensional array
arr0d = np.array(5)
print("Array Dimension: ", arr0d.ndim)
print(arr0d)
```
Output, 
```
Array Dimension:  0
5
```

#### 2. One Dimensional (1-D) Array
- 1D Array: A simple list or vector

```python
# One-dimensional array
arr1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

print("Array Dimension: ", arr1d.ndim)
print(arr1d)
```

Output,
```
Array Dimension:  1
[ 1  2  3  4  5  6  7  8  9 10 11 12]
```

#### 2. Two Dimensional (2-D) Array
- 2-D Array: A table with rows and columns, like a matrix.

```python
# 2-D array of 4 rows and 3 columns
# arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

arr2d = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9], 
        [10, 11, 12]
    ]
)

print("Array Dimension: ", arr2d.ndim, "\n")
print(arr2d)
```

Output,
```
Array Dimension:  2 

[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]
```

```python
# 2-D array of 10 rows and 6 columns
# arr2d = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36], [37, 38, 39, 40, 41, 42], [43, 44, 45, 46, 47, 48], [49, 50, 51, 52, 53, 54], [55, 56, 57, 58, 59, 60]])
arr2d = np.array(
    [
        [1, 2, 3, 4, 5, 6],
        [7, 8, 9, 10, 11, 12],
        [13, 14, 15, 16, 17, 18],
        [19, 20, 21, 22, 23, 24],
        [25, 26, 27, 28, 29, 30],
        [31, 32, 33, 34, 35, 36],
        [37, 38, 39, 40, 41, 42],
        [43, 44, 45, 46, 47, 48],
        [49, 50, 51, 52, 53, 54],
        [55, 56, 57, 58, 59, 60]
    ]
)

print("Array Dimension: ", arr2d.ndim, "\n")
print(arr2d)
```
Output,
```
Array Dimension:  2 

[[ 1  2  3  4  5  6]
 [ 7  8  9 10 11 12]
 [13 14 15 16 17 18]
 [19 20 21 22 23 24]
 [25 26 27 28 29 30]
 [31 32 33 34 35 36]
 [37 38 39 40 41 42]
 [43 44 45 46 47 48]
 [49 50 51 52 53 54]
 [55 56 57 58 59 60]]
 ```

**Note**: 2-D array can be of any number of (rows and columns)

#### 3. Three Dimensional (3-D) Array
- 3-D Array: A cube, often used for images or other complex data structures.

```python
# 3-D array with 1 block, 4 rows and 3 columns
# arr3d1b = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]])

arr3d1b = np.array([
    [ # block 0
        [1, 2, 3],
        [4, 5, 6], 
        [7, 8, 9],
        [10, 11, 12]
    ]
])

print("Array Dimension:", arr3d1b.ndim, "\n")
print(arr3d1b)
```
Output,
```
Array Dimension: 3 

[[[ 1  2  3]
  [ 4  5  6]
  [ 7  8  9]
  [10 11 12]]]
```
---
```python
# 3-D array with 2 blocks, 3 rows and 3 columns
# arr3d2b = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]])

arr3d2b = np.array([
    [ # block 0
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ],
    [ # block 1
        [10, 11, 12],
        [13, 14, 15],
        [16, 17, 18]
    ]
])

print("Array Dimension: ", arr3d2b.ndim, "\n")
print(arr3d2b)
```

Output,
```
Array Dimension:  3 

[[[ 1  2  3]
  [ 4  5  6]
  [ 7  8  9]]

 [[10 11 12]
  [13 14 15]
  [16 17 18]]]
```
**Note**: Each block should have equal number of rows and columns.

---

```py
# 3-D array with 3 blocks, 3 rows and 3 columns

# arr3d3b = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]], [[19, 20, 21], [22, 23, 24], [25, 26, 27]]])


arr3d3b = np.array([
    [ # block 0
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ],
    [ # block 1
        [10, 11, 12],
        [13, 14, 15],
        [16, 17, 18]
    ],
    [ # block 2
        [19, 20, 21],
        [22, 23, 24], 
        [25, 26, 27]
    ]
])

print("Array Dimension: ", arr3d3b.ndim, "\n")
print(arr3d3b)
```

Output,
```
Array Dimension:  3 

[[[ 1  2  3]
  [ 4  5  6]
  [ 7  8  9]]

 [[10 11 12]
  [13 14 15]
  [16 17 18]]

 [[19 20 21]
  [22 23 24]
  [25 26 27]]]
```

---

```py
# 3-D array with 4 blocks, 2 rows and 3 columns
# arr3d4b = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]], [[13, 14, 15], [16, 17, 18]], [[19, 20, 21], [22, 23, 24]]])

arr3d4b = np.array([
    [ # block 0
        [1, 2, 3],
        [4, 5, 6]
    ],
    [ # block 1
        [7, 8, 9],
        [10, 11, 12]
    ],
    [ # block 2
        [13, 14, 15],
        [16, 17, 18]
    ],
    [ # block 3
        [19, 20, 21],
        [22, 23, 24]
    ]
])

print("Array Dimension: ", arr3d4b.ndim, "\n")
print(arr3d4b)
```

Output,
```
Array Dimension:  3 

[[[ 1  2  3]
  [ 4  5  6]]

 [[ 7  8  9]
  [10 11 12]]

 [[13 14 15]
  [16 17 18]]

 [[19 20 21]
  [22 23 24]]]
```
---