---
layout: post
title:  "Iterating (over) Arrays – NumPy"
date:   2025-11-03 20:40:45 +0545
categories: numpy
---
**Table of Contents**:

- [for row in arr:](#for-row-in-arr)
- [np.nditer()](#npnditer)
- [np.ndenumerate()](#npndenumerate)

---

Here are common ways of **Array Iteration** in NumPy,
- `for row in arr:` for 2D arrays.
- `np.nditer()`: for efficient multi-dimensional iteration.
- `np.ndenumerate()`: to get indices and values.

## for row in arr:

## np.nditer()


## np.ndenumerate()
The **`np.ndenumerate()`** function returns the indices and values of an array.


**Example 1**:
```py
# Enumerating 1-D Array
import numpy as np

arr = np.arange(1, 11)

print("Index: value")
for idx, val in np.ndenumerate(arr):
    print(idx, ":", val)
```
**Output**,
```
Index: value
(0,) : 1
(1,) : 2
(2,) : 3
(3,) : 4
(4,) : 5
(5,) : 6
(6,) : 7
(7,) : 8
(8,) : 9
(9,) : 10
```

**Example 2**:
```py
# Enumerating 2-D Array
import numpy as np

arr = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

print("Index: Value")
for idx, val in np.ndenumerate(arr):
    print(idx, ":", val)
```
**Output**,
```
Index: Value
(0, 0) : 1
(0, 1) : 2
(0, 2) : 3
(1, 0) : 4
(1, 1) : 5
(1, 2) : 6
(2, 0) : 7
(2, 1) : 8
(2, 2) : 9
```

**Example 3**:
```py
# Enumerating 3-D Array
import numpy as np

arr = np.array([
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ],
    [
        [10, 11, 12],
        [13, 14, 15],
        [16, 17, 18],
    ], 
    [
        [19, 20, 21],
        [22, 23, 24],
        [25, 26, 27]
    ]
])

print("Index: value")
for idx, val in np.ndenumerate(arr):
    print(idx, ":", val)
```

**Output**,
```
Index: value
(0, 0, 0) : 1
(0, 0, 1) : 2
(0, 0, 2) : 3
(0, 1, 0) : 4
(0, 1, 1) : 5
(0, 1, 2) : 6
(0, 2, 0) : 7
(0, 2, 1) : 8
(0, 2, 2) : 9
(1, 0, 0) : 10
(1, 0, 1) : 11
(1, 0, 2) : 12
(1, 1, 0) : 13
(1, 1, 1) : 14
(1, 1, 2) : 15
(1, 2, 0) : 16
(1, 2, 1) : 17
(1, 2, 2) : 18
(2, 0, 0) : 19
(2, 0, 1) : 20
(2, 0, 2) : 21
(2, 1, 0) : 22
(2, 1, 1) : 23
(2, 1, 2) : 24
(2, 2, 0) : 25
(2, 2, 1) : 26
(2, 2, 2) : 27
```