---
layout: post
title:  "Array Attributes – NumPy"
date:   2025-11-03 21:12:45 +0545
categories: numpy
---

**Table of Contents**:
- [Array Dimensions (array.ndim)](#array-dimensions-arrayndim)
- [Array Shape (array.shape)](#array-shape-arrayshape)
- [Array Size (array.size)](#array-size-arraysize)
- [Examples:](#examples)
    - [1. Zero Dimensional (0-D) Array](#1-zero-dimensional-0-d-array)
    - [2. One Dimensional (1-D) Array](#2-one-dimensional-1-d-array)
    - [2. Two Dimensional (2-D) Array](#2-two-dimensional-2-d-array)
    - [3. Three Dimensional (3-D) Array](#3-three-dimensional-3-d-array)
- [Array Data Type (array.dtype)](#array-data-type-arraydtype)
 
---
&nbsp;
<center>
    <!-- ![numpy-logo](../../../../assets/numpy-logo.png) -->
    <img src="../../../../assets/numpy-logo.png">
</center>

Here are key/important attributes/properties of an ndarray object:
- `array.ndim` – the number of dimensions (axes) of the array.
- `array.shape` – dimensions of the array; A tuple of integers indicating the size of the array in each dimension (e.g., `(rows, columns)`).
- `array.size` – total number of elements
- `array.dtype` – data type of elements (e.g., `np.int64`, `np.float32`, `bool_`, `'<U10'` for string)
- `array.itemsize` – size of each element (in bytes)
- `array.nbytes` – total memory consumed // total size in bytes (`.size * .itemsize`)
- `array.data`: 

<!-- - **Data Types (`dtype`)**
 - Importance of `dtype` for memory and precision.
    - Common types: `int8/16/32/64`, `uint8/16/32/64`, `float16/32/64`, `complex64/128`, `bool_`, `object_`, `string_`.
    - Specifying and converting dtypes: `dtype` parameter, `.astype()` method. -->

If you have not read this post yet, please consider reading this post - [Array Creation](#), as current post builds upon [Array Creation](#).

---

## Array Dimensions (array.ndim) 
- The `array.ndim` attribute returns the number of dimensions of an array. 
- It tells you how many axes the array has, which corresponds to the number of nested levels of lists used to create it.

## Array Shape (array.shape) 
- The `array.shape` attribute returns the dimensions (shape) of a NumPy array as a tuple.
- It shows how many elements are present along each axis (rows, columns, etc.).
- The shape of an array looks like:
  - 0-D Array: ()
  - 1-D Array: (n,): (5,)
  - 2-D Array: (2, 5), (5, 2)
  - 3-D Array: (2, 3, 4), (3, 5, 7)

## Array Size (array.size) 
- The `array.size` attribute returns the total number of elements in the array.
- It counts all items, regardless of the shape.

**shape vs. size**:
the total number of elements in the array.

## Examples:
Here are examples of `array.ndim()`, `array.shape` and `array.size()`.

#### 1. Zero Dimensional (0-D) Array
- 0-D Array: Scalar or a single value (like the number (5)) is a zero-dimensional (0-D) array, 
- So its `array.ndim` would be 0.

**Example**:
```python
# Zero-dimensional array
arr0d = np.array(5)

print("Array Dimension: ", arr0d.ndim)
print("Array Shape: ", arr0d.shape)
print("Array Size: ", arr0d.size)
print(arr0d)
```
**Output**, 
```
Array Dimension:  0
Array Shape:  ()
Array Size:  1
5
```

#### 2. One Dimensional (1-D) Array
- 1D Array: A simple list/tuple or vector is an one-dimensional (1-D) array.

**Example**:
```python
# One-dimensional array
arr1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

print("Array Dimension: ", arr1d.ndim)
print("Array Shape: ", arr1d.shape)
print("Array Size: ", arr1d.size)
print(arr1d)
```
**Output**,
```
Array Dimension:  1
Array Shape:  (12,)
Array Size:  12
[ 1  2  3  4  5  6  7  8  9 10 11 12]
```

#### 2. Two Dimensional (2-D) Array
- 2-D Array: A table with rows and columns, like a matrix is a two-dimensional (2-D) array.
  
**Example 1**:
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

print("Array Dimension: ", arr2d.ndim)
print("Array Shape: ", arr2d.shape)
print("Array Size: ", arr2d.size, "\n")
print("Array Items:\n", arr2d)
```

**Output**,
```
Array Dimension:  2
Array Shape:  (4, 3)
Array Size:  12 

Array Items:
 [[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]
```

**Example 2**:
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
print("Array Shape: ", arr2d.shape)
print("Array Size: ", arr2d.size)
print(arr2d)
```
**Output**,
```

 ```

**Note**: 2-D array can be of any number of (rows and columns)

#### 3. Three Dimensional (3-D) Array
- 3-D Array: A cube, often used for images or other complex data structures is a three-dimensional (3-D) array.

**Example 1**:
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
print("Array Shape: ", arr3d1b.shape)
print("Array Size: ", arr3d1b.size)
print(arr3d1b)
```

**Output**,
```

```

**Example 2**:
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
print("Array Shape: ", arr3d2b.shape)
print("Array Size: ", arr3d2b.size)
print(arr3d2b)
```

**Output**,
```

```
**Note**: Each block should have equal number of rows and columns.

**Example 3**:
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
print("Array Shape: ", arr3d3b.shape)
print("Array Size: ", arr3d3b.size)
print(arr3d3b)
```

**Output**,
```

```

**Example 4**:
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
print("Array Shape: ", arr3d4b.shape)
print("Array Size: ", arr3d4b.size)
print(arr3d4b)
```

**Output**,
```

```

## Array Data Type (array.dtype) 
The `array.dtype` attribute returns the data type of an array. 

**Example**:
```py
# Demonstrate array.dtype attribute
import numpy as np

arrInt = np.arange(1, 6, dtype=int)
arrFlt = np.arange(1, 6, dtype=float)
arrStr = np.array(("Nepal", "India", "China", "Iran"))
arrBool = np.array([True, False, False, True, False, True])

print("arrInt.dtype:", arrInt.dtype, "\n", arrInt, "\n")
print("arrFlt.dtype:", arrFlt.dtype, "\n", arrFlt, "\n")
print("arrStr.dtype:", arrStr.dtype, "\n", arrStr, "\n")
print("arrBool.dtype:", arrBool.dtype, "\n", arrBool, "\n")
```
**Output**,
```
arrInt.dtype: int64 
 [1 2 3 4 5] 

arrFlt.dtype: float64 
 [1. 2. 3. 4. 5.] 

arrStr.dtype: <U5 
 ['Nepal' 'India' 'China' 'Iran'] 

arrBool.dtype: bool 
 [ True False False  True False  True] 
```
<!-- 
## Array Itemsize (array.itemsize) 
- `array.itemsize` – size of each element (in bytes)


## Array nytes (array.nbytes) 
The **`array.nbytes`** attribute returns the total memory consumed // total size in bytes (`.size * .itemsize`)

## Array Data (array.data) 

-  – 
- `array.data`:  -->