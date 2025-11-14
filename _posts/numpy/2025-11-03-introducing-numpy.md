---
layout: post
title:  "Introducing NumPy"
date:   2025-11-02 10:12:45 +0545
categories: numpy
---

<center>
    <!-- ![numpy-logo](../../../../assets/numpy-logo.png) -->
    <img src="../../../../assets/images/numpy-logo.png">
</center>

## What is NumPy?
- NumPy (Numerical Python) is a foundational open-source Python library 
  - that provides efficient tools for (working with: creating and manipulating) **large, multi-dimensional arrays and matrices**, 
  - along with a wide collection of high-level **mathematical and logical functions** for working with numerical data, 
  - making it crucial for data science and machine learning and numerical/scientific computing.
- It is designed to handle large numerical datasets more efficiently—faster computation and lower memory usage—than standard Python lists for numerical operations.
- At its core is the homogeneous, multidimensional **ndarray (N-dimensional array)** object — a fast, flexible container for numerical data.

### The ndarray (N-dimensional Array) Object
The `ndarray` is the central/core data structure of NumPy. It is,
- **Homogeneous**: All elements must be of the same data type (e.g., all integers or all floats).  
- **Multidimensional**: Can represent 1D (vector), 2D (matrix), or higher dimensions (tensor).  
- **Fixed Size**: Once created, the ndarray has a fixed/immutable shape and size (total number of elements), means it cannot be changed dynamically like Python lists.

#### NumPy Array (`ndarray`) vs. Python List  
  - Homogeneous data types vs. heterogeneous.
  - Fixed size at creation vs. dynamic resizing.
  - Vectorized operations vs. element-wise loops.
  - Memory efficiency
    - **Memory**: NumPy arrays are more memory-efficient as they store data in a contiguous block of memory.
  - **Speed**: NumPy is significantly faster due to vectorized operations and being implemented in C.

## Why Use NumPy?
Due to following key features, NumPy is widely used:
- **Multi-dimensional/N-D arrays**: 
  - It introduces the **ndarray (N-dimensional array)** object, a homogeneous container capable of storing structured data of the same type, making it ideal for efficiently handling large datasets.

- **High Performance/speed**: 
  - It is much faster than native Python lists for numerical operations due to:
    - Contiguous memory allocation.
      - Arrays are stored in *contiguous memory blocks*, allowing faster access.  
    - Vectorized operations (written in C/Fortran).
      - Core operations are implemented in **C** and **Fortran**, enabling speed through *vectorization* (operations applied to entire arrays, not element by element).
      - It uses optimized C code under the hood, which makes operations like iteration, transposing, and element-wise calculations much faster than with standard Python lists.

- **Memory Efficiency**:
  - When dealing with large datasets, *Python lists* can be slow and memory-hungry.
  - NumPy arrays are more memory-efficient (use **less memory**) than Python lists because, 
    - all elements share the same data type and don't require type-checking for every element.
    - they use contiguous memory.

- **Rich Functionality**: ✅
  - It provides a vast library (of rich functionality) with hundreds of built-in mathematical functions for tasks such as linear algebra, Fourier transforms, random number generation, statistical operations etc.

- **Foundation for other libraries**: ✅
  - As the core library for scientific computing in Python, NumPy serves as the foundation for many popular libraries including Pandas, Matplotlib, Scikit-learn, TensorFlow, PyTorch, and SciPy, all of which rely on its powerful array structure.

- **Interoperability**: The de-facto standard for array exchange in the Python data ecosystem (Pandas, Scikit-learn, Matplotlib all build on it).

- **Ease of use/Convenience**: It offers a simple and expressive way to perform complex numerical operations. For example, multiplying two arrays can be done with a single line of code (c=a*b), whereas it would require a loop in standard Python.

- If you’re planning to work with **data**, **ML models**, or **numerical algorithms**, mastering NumPy is the first big step.

## Installing NumPy
Before you begin using NumPy, you need to install it. If you haven't installed it yet, you can
do so using pip.  
`pip install numpy`  

## Importing NumPy and alias
Once installed, you can import NumPy into your Python script like this:  
`import numpy as np`