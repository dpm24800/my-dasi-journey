---
layout: post
title:  "Array Slicing – NumPy"
date:   2025-10-31 21:12:45 +0545
categories: jekyll numpy
---
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

### Slicing 2-D Array

#### Slicing 2-D Array with step
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