---
layout: post
title:  "Slicing Arrays – NumPy"
date:   2025-11-03 21:12:45 +0545
categories: numpy
---
**Table of Contents**:
- [Unfinished](#unfinished)
- [Slicing 1D Array](#slicing-1d-array)
- [Slicing 2-D Array](#slicing-2-d-array)
  - [Slicing 2-D Array with step](#slicing-2-d-array-with-step)
- [Slicing 3-D Array](#slicing-3-d-array)
  - [Slicing 3-D Array with step](#slicing-3-d-array-with-step)

---

## Unfinished


&nbsp;

**Slicing/Subsetting - Array**  
Just like lists in Python, NumPy arrays can be indexed and sliced to extract specific elements or subsets of data.
You can extract a range of elements using slicing.

## Slicing 1D Array
**Syntax**: `arr[start, end, step]`
- start: default=0
- end: exclusive
- step: optional, default=1

**Example**:
```py
# Slicing 1-D Array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

print("Array: ", arr, "\n")
print("array[1:10]:", arr[1:10]) # elements from index 1 to 10 (exclusive)
print("array[1:12:2]:", arr[1:12:2]) # elements from index 1 to 12 (exclusive) with step 2

print()
print("array[:]:", arr[:]) # : all elements
print("array[::2]:", arr[::2]) # all elements with step 2

print()
print("array[3:]:", arr[3:]) # : all elements starting from index 3
print("array[::2]:", arr[:4]) # all elements upto index 4 (exclusive)
```

**Output**,
```
Array:  [ 1  2  3  4  5  6  7  8  9 10 11 12] 

array[1:10]: [ 2  3  4  5  6  7  8  9 10]
array[1:12:2]: [ 2  4  6  8 10 12]

array[:]: [ 1  2  3  4  5  6  7  8  9 10 11 12]
array[::2]: [ 1  3  5  7  9 11]

array[3:]: [ 4  5  6  7  8  9 10 11 12]
array[::2]: [1 2 3 4]
```

## Slicing 2-D Array
Slicing works similarly in 2D arrays.

**Example**:
```python
# Slice the first row
print(arr_2d[0, :])  # Output: [1 2 3]
```

    [1 2 3]
    


```python
# Slice the second column
print(arr_2d[:, 1])  # Output: [2 5]
```

    [2 5]


### Slicing 2-D Array with step
**Syntax**: `arr[start:end:step, start:end:step]`
`

**Example 1**:
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

print("Original Array:\n", arr2d, "\n")
print("Slicing odd columns: array[:, ::2]\n", arr2d[:, ::2], "\n")) # all rows, columns with step 2
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

**Example 2**:
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

## Slicing 3-D Array


### Slicing 3-D Array with step