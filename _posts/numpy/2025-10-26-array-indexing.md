---
layout: post
title:  "Array Indexing – NumPy"
date:   2025-10-31 21:12:45 +0545
categories: jekyll numpy
---
### 1-D Array Indexing
```py
# Indexing 1-D Array
arr1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

print("1-D Array: ", arr1d)

print("\nAccessing elements:")
print("array[0]:", arr1d[0]) # value at index 0
print("array[5]:", arr1d[5]) # value at index 5
print("array[-1]:", arr1d[-1]) # value at index -1
```

Output,
```
1-D Array:  [ 1  2  3  4  5  6  7  8  9 10 11 12]

Accessing elements:
array[0]: 1
array[5]: 6
array[-1]: 12
```

### 2-D Array Indexing
- In a 2-D array indexing (e.g., `arr2d[1, 2]`),
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

print("2-D Array:\n", arr2d)
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

### 3-D Array Indexing
- In a 3-D array indexing (e.g., `arr3d[0, 1, 2]`),
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
print("3-D Array:\n", arr3d)

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