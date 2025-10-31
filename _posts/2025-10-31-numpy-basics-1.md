---
layout: post
title:  "NumPy Basics 1"
date:   2025-10-31 21:12:45 +0545
categories: jekyll numpy
---
## Introduction
- Stands for Numerical Python
- Why Use:
  - powerful numerical computing library
  - faster than Python list
- It has fundamental package, scientific computing, such as:
  - Linear Algebra
  - Matrix, 
  - Statistics
  - Probalbiltiy
  - Trigonometry
  - Image Processing
  - Log etc.
- n-dimentional (nd) array
  - Collection of homogentous data types.

### Installing NumPy
If you haven’t installed NumPy yet, enter this command in your command prompt or terminal:

```
pip install numpy
```

This Python code shows the installed NumPy version:

```py
np.__version__ # to check version
```

### Importing NumPy 
Before you can use any NumPy functions, you need to import NumPy like this:

```py
import numpy as np # import numpy library
```

After importing NumPy, you can use all of its functions:

## Creating NumPy Array 
A NumPy array holds data of the same type, unlike a Python list where elements can have different types. This makes NumPy arrays faster and more efficient than lists.
```py
# Create NumPy array of different data types
arr_int = np.array([1, 2, 3, 4, 5]) # Integer array
arr_float = np.array([1.0, 2.5, 3.9, 4.2, 5.4]) # Float array
arr_str = np.array(['1', '2', '3', '4', '5']) # String array
arr_mixed = np.array([1, 2.0, '3', 4.0, 5]) # Mixed array with string

print("Integer Array:", arr_int)
print("Float Array:", arr_float)
print("String Array:", arr_str)
print("Mixed Array (upcasted to string):", arr_mixed)
```

Output,
```
Integer Array: [1 2 3 4 5]
Float Array: [1.  2.5 3.9 4.2 5.4]
String Array: ['1' '2' '3' '4' '5']
Mixed Array (upcasted to string): ['1' '2.0' '3' '4.0' '5']
```

## Array Dimensions (`array.ndim`) 
- `array.ndim` attribute returns the number of dimensions of an array. 
- It tells you how many axes the array has, which corresponds to the number of nested levels of lists used to create it.

#### 1. Zero Dimensional (0D) Array/Scalar
- A single value (like the number (5)) is a zero-dimensional array, 
- So `array.ndim` would be 0.

```py
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

#### 2. One Dimensional (1D) Array
- 1D Array: A simple list or vector

```py
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

#### 2. Two Dimensional (2D) Array
- 2D Array: A table with rows and columns, like a matrix.

```py
# 2D array of 2 rows and 3 columns
# arr2d = np.array([[1, 2, 3], [4, 5, 6]]])
arr2d = np.array(
    [
        [1, 2, 3], 
        [4, 5, 6]
    ]
)

print("Array Dimension: ", arr2d.ndim, "\n")
print(arr2d)
```

Output,
```
Array Dimension:  2 

[[ 1  2  3]
 [ 4  5  6]]
```
---
```py
# 2D array of 10 rows and 6 columns
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

**Note**: 2D array can be of any number of (rows and columns)

#### 3. Three Dimensional (3D) Array
- 3D Array: A cube, often used for images or other complex data structures.

```py
# 3D array with 1 block, 4 rows and 3 columns
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
```py
# 3D array with 2 blocks, 3 rows and 3 columns
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
# 3D array with 3 blocks, 3 rows and 3 columns

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
# 3D array with 4 blocks, 2 rows and 3 columns
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
## Array Indexing 
### 1D Array Indexing
```py
# Indexing 1-D Array
arr1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

print("1D Array: ", arr1d)

print("\nAccessing elements:")
print("array[0]:", arr1d[0]) # value at index 0
print("array[5]:", arr1d[5]) # value at index 5
print("array[-1]:", arr1d[-1]) # value at index -1
```

Output,
```
1D Array:  [ 1  2  3  4  5  6  7  8  9 10 11 12]

Accessing elements:
array[0]: 1
array[5]: 6
array[-1]: 12
```

### 2D Array Indexing
- In a 2D array indexing (e.g., `arr2d[1, 2]`),
  - The first number specifies the row.
  - The second number specifies the column.

```py
# Indexing 2-D Array
# arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

arr2d = np.array([
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9], 
    [10, 11, 12]
])

print("2D Array:\n", arr2d)
print("\nAccessing elements:")
print("array[0, 0]:", arr2d[0, 0]) # value at row 0, column 0
print("array[1, 1]:", arr2d[1, 1]) # value at row 1, column 1
print("array[-2, -1]:", arr2d[-2, -1]) # value at second last row, last column
```

Output,
```
2D Array:
 [[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]

Accessing elements:
array[0, 0]: 1
array[1, 1]: 5
array[-2, -1]: 9
```

### 3D Array Indexing
- In a 3D array indexing (e.g., `arr3d[0, 1, 2]`),
  - The first number specifies the block.
  - The second number specifies row.
  - The third number specifies column.

```py
# Indexing 3-D Array
arr3d = np.array([
    [ # Block 0
        [1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9], 
        [10, 11, 12]
    ],
    [ # Block 1
        [13, 14, 15],
        [16, 17, 18],
        [19, 20, 21],
        [22, 23, 24]
    ],
    [ # Block 2
        [25, 26, 27],
        [28, 29, 30],
        [31, 32, 33],
        [34, 35, 36]
    ]
])
print("3D Array:\n", arr3d)

print("\nAccessing elements:")
print("array[0, 0, 0]:", arr3d[0, 0, 0]) # value at block 0, row 0, column 0
print("array[0, 1, 1]:", arr3d[0, 1, 1]) # value at block 0, row 1, column 1

print("array[1, 3, 2]:", arr3d[1, 3, 2]) # value at block 1, row 3, column 2
print("array[1, 0, 2]:", arr3d[1, 0, 2]) # value at block 1, row 0, column 2

print("array[2, -2, 2]:", arr3d[2, -2, 2]) # value at block 2, second last row, column 2
print("array[2, -1, -2]:", arr3d[2, -1, -2]) # value at block 2, last row, second last column
```

Output,
```
3D Array:
 [[[ 1  2  3]
  [ 4  5  6]
  [ 7  8  9]
  [10 11 12]]

 [[13 14 15]
  [16 17 18]
  [19 20 21]
  [22 23 24]]

 [[25 26 27]
  [28 29 30]
  [31 32 33]
  [34 35 36]]]

Accessing elements:
array[0, 0, 0]: 1
array[0, 1, 1]: 5
array[1, 3, 2]: 24
array[1, 0, 2]: 15
array[2, -2, 2]: 33
array[2, -1, -2]: 35
```

## Array Slicing
### Slicing 1D Array

```py
# Slicing 1-D Array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

print("Array: ", arr, "\n")
print("array[1:10]:", arr[1:10]) # elements from index 1 to 9
print("array[1:12:2]:", arr[1:12:2]) # elements from index 1 to 9 with step 2
```

Output,
```
Array:  [ 1  2  3  4  5  6  7  8  9 10 11 12] 

array[1:10]: [ 2  3  4  5  6  7  8  9 10]
array[1:12:2]: [ 2  4  6  8 10 12]
```

### Slicing 2D Array

#### Slicing 2D Array with step
```py
# Slicing 2-D Array with step
arr2d = np.array([
    [1, 2, 3, 4, 5, 6], 
    [7, 8, 9, 10, 11, 12], 
    [13, 14, 15, 16, 17, 18], 
    [19, 20, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35, 36]
])

print("Original Array:\n", arr2d)

print()
print("Slicing odd columns: array[:, ::2]\n", arr2d[:, ::2]) # all rows, columns with step 2
print()

print("Slicing even columns: array[:, 1::2]\n", arr2d[:, 1::2]) # all rows, columns with step 2 (starting from index 1)
```

Output,
```
Original Array:
 [[ 1  2  3  4  5  6]
 [ 7  8  9 10 11 12]
 [13 14 15 16 17 18]
 [19 20 21 22 23 24]
 [25 26 27 28 29 30]
 [31 32 33 34 35 36]]

Slicing odd columns: array[:, ::2]
 [[ 1  3  5]
 [ 7  9 11]
 [13 15 17]
 [19 21 23]
 [25 27 29]
 [31 33 35]]

Slicing even columns: array[:, 1::2]
 [[ 2  4  6]
 [ 8 10 12]
 [14 16 18]
 [20 22 24]
 [26 28 30]
 [32 34 36]]
```

```py
 # Slicing 2-D Array with step
arr2d = np.array([
    [1, 2, 3, 4, 5, 6], 
    [7, 8, 9, 10, 11, 12], 
    [13, 14, 15, 16, 17, 18], 
    [19, 20, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35, 36]
])

print("Original Array:\n", arr2d)

print()
print("Slicing odd rows: array[::2, :]\n", arr2d[::2,:]) # rows with step 2, all columns

print()
print("Slicing even rows: array[1::2, :]\n", arr2d[1::2,:]) # rows with step 2 (starting from index 1), all columns
```

Output,
```
Original Array:
 [[ 1  2  3  4  5  6]
 [ 7  8  9 10 11 12]
 [13 14 15 16 17 18]
 [19 20 21 22 23 24]
 [25 26 27 28 29 30]
 [31 32 33 34 35 36]]

Slicing odd rows: array[::2, :]
 [[ 1  2  3  4  5  6]
 [13 14 15 16 17 18]
 [25 26 27 28 29 30]]

Slicing even rows: array[1::2, :]
 [[ 7  8  9 10 11 12]
 [19 20 21 22 23 24]
 [31 32 33 34 35 36]]
```