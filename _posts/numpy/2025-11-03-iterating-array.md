---
layout: post
title:  "Iterating over Array – NumPy"
date:   2025-11-02 20:40:45 +0545
categories: numpy
---
## Table of Contents

## Iterating Over Arrays: Array Iteration
  - `for row in arr:` for 2D arrays.
  - `np.nditer()`: for efficient multi-dimensional iteration.
  - `np.ndenumerate()`: to get indices and values.




## np.ndenumerate()



**Example**: 
```py
import numpy as np

arr7 = np.array([
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

print("Array Index: value")
for idx, val in np.ndenumerate(arr7):
    print(idx, ":", val)
```