---
layout: post
title:  "Key Array Attributes"
date:   2025-10-31 21:12:45 +0545
categories: jekyll note-plans
---
The more important attributes of an ndarray object are:
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



