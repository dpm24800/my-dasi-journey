---
layout: post
title:  "NumPy – note plan"
date:   2025-10-31 21:12:45 +0545
categories: jekyll note-plans
---
## 1. Introduction to NumPy
- **What is NumPy?**
  - Stands for Numerical Python.
  - The fundamental package for scientific computing in Python.
  - The fundamental library for numerical computing in Python.
  - Core object: the homogeneous, multidimensional `ndarray`.

- **Why NumPy? The Key Advantages**
  - Why it's used instead of Python lists? (speed, memory efficiency, vectorization)
    - **Performance:** Much faster than native Python lists for numerical operations due to:
        - Contiguous memory allocation.
        - Vectorized operations (written in C/Fortran).
    - **Convenience:** Rich set of built-in functions for linear algebra, Fourier transforms, random number generation, etc.
    - **Interoperability:** The de-facto standard for array exchange in the Python data ecosystem (Pandas, Scikit-learn, Matplotlib all build on it).

- Provides support for large, multi-dimensional arrays and matrices.
- Overview of the ndarray object
- Comparison: Python list vs NumPy array
- Key features and advantages over Python lists

- **The `ndarray` Object** (N-dimensional Array)
    - The core data structure in NumPy.
    - **Homogeneous:** All elements must be of the same data type.
    - **Fixed Size:** The size (total number of elements) is immutable once created.

1. **NumPy Array (`ndarray`) vs. Python List**
    - Homogeneous data types vs. heterogeneous.
    - Fixed size at creation vs. dynamic resizing.
    - Vectorized operations vs. element-wise loops.
    - Memory efficiency.

- **NumPy vs. Python Lists**
    - **Speed:** NumPy is significantly faster due to vectorized operations and being implemented in C.
    - **Memory:** NumPy arrays are more memory-efficient as they store data in a contiguous block of memory.

- Installation (and setup): `pip install numpy`
- Importing NumPy and alias (`import numpy as np`)


## 2. NumPy Arrays
- Array dimensions: 1D, 2D, 3D arrays
- Data types (`dtype`) and type conversion

### Creating Arrays
- **From Python (Data) Structures**
  - `np.array([list/tuple])`: Create an array from a Python list or tuple.
- **Initial Placeholders**
  - `np.zeros(shape)`: Creates an array filled with ZEROS
  - `np.ones(shape)`: Creates an array filled with ONES
  - `np.full(shape, fill_value)`: Creates an array filled with a specific value
  - `np.empty(shape)`: Creates an array with EMPTY (uninitialized) data
  - `np.eye(N)` or `np.identity(N)`: Creates an N times IDENTITY MATRIX: see deepseek

- **Sequences**
  - `np.arange(start, stop, step)`: Creates an array with regularly spaced values (similar to `range`).
  - `np.linspace(start, stop, num)`: Creates an array with a specified number of evenly spaced values over a given interval.

## Copying arrays: 
- `copy()`: 
- shallow vs deep copy

- **Copies vs. Views:**
  - **View:** A new array object that looks at the *same data* (e.g., slicing). Modifying the view changes the original array.
  - **Copy:** A new array object with a *new copy of the data* (e.g., using `arr.copy()`). Modifying the copy does not affect the original.
  - `np.copy()` vs `np.view()`

## Key Array Attributes
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

## Array Indexing
- **Basic Indexing**: Indexing in 1D, 2D, and nD Arrays
  - Accessing individual/single elements: `arr[1]`, `arr[0, 1]`, `arr[0]`, `arr[1, 2]`
  - Multi-dimensional indexing `arr[row, col]`
  - Negative indexing
  - **Integer Array Indexing:** Using an array of indices to select non-contiguous elements (e.g., `arr[[0, 2, 4]]`).
- **Fancy Indexing (Integer Array Indexing)**: (using lists or arrays of indices)
  - Using integer arrays/lists to index.
  - Difference from slicing: *always returns a copy*.
  - Combined indexing (e.g., `arr[[0, 2, 4], 1:]`).
- **Boolean Indexing/Masking**: (conditional selection)
  - Using a boolean array (a "mask") to select elements that satisfy a condition (e.g., `arr[arr > 5]`)
  - Using boolean arrays to filter data.
  - Example: `arr[arr > 5]`.
  - Combining conditions with `&` (and), `|` (or), `~` (not).

## Array Slicing
- Accessing subarrays using slice notation (`start:stop:step`) along each axis (e.g., `arr[1:3, 0:2]`).
- **Basic Slicing**: 
  - Basic/One-dimensional slicing: `arr[start:stop:step]`
  - The concept of a view vs. a copy.
    - Copy vs View (`arr.copy()` vs slicing behavior)
      - Slicing returns a *view*.
      - Using `.copy()` to create an explicit copy.
- Slicing in 2D and 3D arrays
- Using `np.where()` for conditional filtering

## Iterating/Iteration Over Arrays
  - `for row in arr:` for 2D arrays.
  - `np.nditer()`: for efficient multi-dimensional iteration.
  - `np.ndenumerate()`: to get indices and values.

## Broadcasting Arrays
- Concept and rules of broadcasting
- Examples of compatible and incompatible shapes
- Broadcasting in arithmetic and aggregation
- A set of rules that allows NumPy to work with arrays of different shapes when performing arithmetic operations.
- Understanding the rules for how a smaller array is "stretched" to match the shape of a larger array.
-   **The Rule:** Arrays can be operated on if their dimensions are compatible.
    -   **Rules:** 1) Trailing dimensions equal, or 2) One of them is 1.
    -   Examples: Adding a 1D array to a 2D array, scalar with an array.
    -   Using `np.newaxis`/`None` to reshape arrays for broadcasting.

## 4. Array Operations 
- Element-wise addition, subtraction, multiplication, division


## Array Operations
### 4.1 Arithmetic Operations
## 5. Mathematical Operations and Statistics
- **Element-wise Operations:**
    - Standard arithmetic operators (`+, -, *, /, **`) apply element-wise to arrays.
    - Element-wise operations: addition, subtraction, multiplication, division
    - Scalar operations

## NumPy Universal Functions (ufuncs)
### 1. ufunc Simple Arithmetic/Mathematical Operatiosn
  - `np.add()`: Addition
  - `np.sum([arr1, arr2], axis=1)`: Addition
  - `np.subtract()`: Subtraction
  - `np.multiply()`: Multiplication
  - `np.divide()`: Division
  - `np.pow()`: Power
  - `np.mod()` ??: Modulus
  - `np.remainder()`: Remainder
  - `np.divmod()`: Quotient and Mod
  - `np.absolute(arr)`: Absolute Values

### 2. ufunc Rounding Decimals
  - `np.trunc(arr)`: Truncation (Remove the decimals, and return the float number closest to zero): 
  - `np.fix(arr)`: Fix (Remove the decimals, and return the float number closest to zero): 
  - `np.around(arr)`: Rounding (increments preceding digit or decimal by 1 if >=5 else do nothing)
  - `np.floor(arr)`: Floor (rounds off decimal to nearest lower integer): 
  - `np.ceil(arr)`: Ceil (rounds off decimal to nearest upper integer):

### Exponential and Logarithmic ufunc
  - `np.log(arr)`: Natural Log, or Log at Base e
    - `math.log()`: Log at Any Base
  - `np.log2(arr)`: Log at Base 2
  - `np.log10(arr)`: Log at Base 10

### ufunc Statistical (or what??)
  - `np.sum([arr1, arr2])`: Summations
    - `np.add()` vs `np.sum()`
  - `np.sum([arr1, arr2], axis=1)`: Summation Over an Axis
  - `np.cumsum(arr)`: Cummulative Sum
  - 
  - `np.prod(arr)`: Products
  - `np.prod([arr1, arr2])`: 
  - `np.prod([arr1, arr2], axis=1)`: Product Over an Axis
  - `np.cumprod(arr)`: Cummulative Product
  - `np.prod([arr1, arr2], axis=1)`: Product Over an Axis
  - `np.cumprod(arr)`: Cummulative Product

  - `np.diff(arr)`: Differences
  - `np.diff(arr, n=2)` ?? where it shold be

 - `arr.sum()`: Summations
    - `np.sum(arr, axis=0)`: Summation over an axis
    - `np.sum([arr1, arr2], axis=1)`: summation in the following array over 1st axis:
  - `np.cumsum()`: Cumulative Sum
  - np.prod(): 
  - `np.cumprod()`: Products
- 
- **Aggregate functions**: Statistical Functions
- **Aggregation and Statistics (often using the `axis` parameter):**
  - `arr.min()`: 
  - `arr.max()`: 
  - `argmin()`: 
  - `argmax()`: 

  - `arr.mean()`: 
  - `np.median()`:
  - `np.std()`: Standard Deviation
  - `np.var()`: Variance
  - `np.percentile()`: 
- Axis-based operations: `axis=0` vs `axis=1`

### LCM and GCD/HCF
  - `np.lcm(num1, num2)`: LCM of two numners
  - `np.lcm.reduce(arr)`: LCM in Arrays
  - `np.gcd(num1, num2)`: GCD of two numners
  - `np.gcd.reduce(arr)`: GCD in Arrays
### ufunc Trigonometric: incomplete
  - `np.pi`: PI
  - `np.sin(arr)`: Sin
  - `np.cos(arr)`: Cos
  - `np.tan(arr)`: Tan
### ufunc Hyperbolic
  - `np.sinh()`: Hyperbolic Sine
  - `np.cosh()`: Hyperbolic Cos
  - `np.sinh()`: Hyperbolic Tan
- **Finding Angles**:
  - `np.arcsinh()`: Radian value for sinh
  - `np.arcsinh()`: Radian value for cosh
  - `np.arcsinh()`: Radian value for ta

### ufunc Set Operations
  - `np.unique(arr)`: Find unique elements from any 1-D array: 
  - `np.union1d(arr)`: Finding Union: 
  - `np.intersect1d(arr)`: Finding intersection: 
  - `np.setdiff1d(arr)`: Finding difference: 
  - `np.setxor1d(arr)`: Finding Symmetric Differenc

`np.sqrt()`:  
`np.exp()`: 

- **Rounding and truncating**: 
  - `np.round()`: 
  - `np.floor()`: 
  - `np.ceil()`:

## 6. Linear Algebra with NumPy (`numpy.linalg`)
- **Important Functions in `numpy.linalg`**
  - Matrix creation using `np.matrix` or `np.array`
  - Matrix Multiplication: 
    - `@` operator (Python 3.5+) (eg. `a @ b`)
    - `np.dot()` = `np.dot(a, b)`
    - (Preferred for) Matrix Products: `matmul()`
  - Transpose: `.T`
  - Determinant (of a matrix): `np.linalg.det()`
  - Inverse (of a matrix): `np.linalg.inv()`
  - Eigenvalues and eigenvectors: `np.linalg.eig()`
  - Solving linear equations/systems: `np.linalg.solve()`
  - Singular Value Decomposition: `np.linalg.svd()`

2.  **Vector/Matrix Norms**
    -   `np.linalg.norm()`
  
## 7. Array Manipulation
- **Reshaping**: Changing Array Shape
    - `arr.reshape(new_shape)`: Changes the shape of an array without changing its data.
    - `arr.ravel()` or `arr.flatten()`: Flattens/converts a multi-dimensional array into a 1D array. [`arr.ravel()` (1D view), `arr.flatten()` (1D copy).]
- **Transposing**:  ✅
      - `arr.T` or `np.transpose(arr)`: Swaps the rows and columns (or permutes dimensions for N-D arrays).
- **Arrays Concatenation and Stacking**:
  - `np.concatenate((arr1, arr2), axis=0/1)`: Joins a sequence of arrays along an existing axis.
  - 
- **Stacking helpers**:
    - `np.stack()`: joins along a *new* axis.
    - `np.vstack((a1, a2))`: (Vertical Stack): Joins arrays along the first axis (rows)
    - `np.hstack((a1, a2))`: (Horizontal Stack): Joins arrays along the second axis (columns)
    - `np.dstack()`: Stack along height, which is the same as depth: 
    - `np.row_stack()`: 
    - `np.column_stack()`: 
- **Splitting Arrays:**
    - `np.split()`: Split an array into multiple smaller arrays
    - `np.hsplit()`: 
    - `np.vsplit()`: 
    - `np.array_split()`: (allows uneven splits).

- **Adding/Removing Elements**
    - `np.insert()`: 
    - `np.append()`: 
    - `np.delete()`: 
    - *Note: These are not in-place; they return new arrays.*

- `np.newaxis` and `reshape()` for dimensional expansion

## Searching Arrays
- `np.where(condition, value_if_true, value_if_false)`: Conditional replacement: 
- `np.searchsorted()`: 

## Sorting Array
  - `np.sort()`: 
  - `np.argsort()`: 
  - `np.lexsort()`: 

## Filtering Array
- dsfs
- dfsdf

## 🧰 8. Array Manipulation and Utilities
- `np.unique()` – unique elements
- `np.clip()` – limit values within a range
- `np.any()`: logical checks
- `np.all()` – logical checks
- `np.isnan()`: 
- `np.isinf()`: 
- `np.isfinite()`: 

## Random Arrays
- Random Module in NumPy (`numpy.random`)
- Functions for generating random numbers from Random Module
- Generating random numbers: 
  - `np.random.rand()`: random float from 0 to 1
  - `np.random.randn()`: 
  - `random.rand()`: Random floats: `yes`, 
  - `randn()` ?? # returns a random float between 0 and 1.
  - `np.random.randint(range)`: Random integers in a range
  - `random.randint(100, size=(5))`: Random Array: 
    - `random.randint(100, size=(3, 5))`: Random Array: 
  - `np.random.normal()`: 

- Random samples/sampling: 
  - `random.random_sample()`
  - `random.choice()`
  - `random.shuffle()`
- `np.random.seed()`: Seeding for reproducibility/Setting seed
- Permutations and shuffling: 
  - `np.random.permutation()`: 
  - `np.random.shuffle()`: 

- Probability distributions:
  - `np.random.normal()` – Normal distribution
  - `np.random.uniform()` – Uniform distribution
  - `np.random.binomial()` – Binomial distribution

## 10. File Input and Output (I/O)
- Saving and loading arrays:
  - `np.save()` / `np.load()` (binary .npy format)
- Working with text files: 
  - `np.savetxt()`: (text files, CSVs)
  - `np.loadtxt()`: (text files, CSVs)
  - `np.genfromtxt()`: for complex CSVs
  - `np.savez()`: for multiple arrays
- Working with binary files (`.npy` and `.npz` formats): (most efficient)
    -   `np.save('file.npy', arr)`: 
    -   `np.load('file.npy')`: 
    -   `np.savez('file.npz', a=arr1, b=arr2)`: for multiple arrays.

## 11. Performance and Memory Optimization
- Vectorization vs loops performance
- Avoiding Python loops using NumPy operations
- Broadcasting instead of `for` loops
- Using `np.vectorize()`
- In-place operations to save memory
- Memory views (`arr.view()`) and slicing behavior

## 12. Advanced Topics
- Structured arrays and record arrays
- Masked arrays (`np.ma`)
- Memory layout: C-contiguous vs Fortran-contiguous arrays
- Strides and slicing performance
- NumPy’s internal data buffer and alignment
- Integration with C/C++ and Fortran (brief overview)
- Interoperability with Pandas and Matplotlib

## 13. Practical Applications
- Data normalization and scaling
- Statistical summaries and matrix operations in data science
- Implementing mean normalization and z-score standardization
- Image manipulation using NumPy arrays
- Vectorized implementations of mathematical functions (e.g., sigmoid, softmax)
- Using NumPy as a backend for ML preprocessing

## 14. Common Interview/Exam Topics
- Difference between array and list
- View vs Copy
- Broadcasting rules
- Memory layout (C-order vs F-order)
- Vectorization examples
- Axis explanation in aggregation functions
- Random seeding and reproducibility