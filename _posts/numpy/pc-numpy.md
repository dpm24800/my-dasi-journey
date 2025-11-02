# NumPy Fundamentals  
NumPy (Numerical Python) is one of the most powerful and essential libraries in data
science and machine learning. It provides support for large, multi-dimensional arrays and
matrices, along with a collection of mathematical functions to operate on these arrays

**Why Use NumPy?**  
NumPy is fast and efficient when it comes to handling large datasets and performing
mathematical computations. It provides a solid foundation for working with data in Python,
making it crucial for data analysis, machine learning, and scientific computing.

**Installing NumPy**  
Before you begin using NumPy, you need to install it. If you haven't installed it yet, you can
do so using pip.  
`pip install numpy`  

Once installed, you can import NumPy into your Python script like this:  
`import numpy as np`  

## Creating NumPy Arrays
A NumPy array is similar to a list in Python but offers more functionality and is more
efficient for handling large amounts of data.

**1. Creating a Basic NumPy Array**  
You can create a basic 1D array using the np.array() function.


```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])  # Create a 1D array
print(arr)
```

    [1 2 3 4 5]
    

**2. Creating a Multidimensional Array**  
You can also create 2D, 3D, and higher-dimensional arrays.


```python
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])  # Create a 2D array
print(arr_2d)
```

    [[1 2 3]
     [4 5 6]]
    

**3. Creating Arrays with Built-in Functions**  
NumPy provides functions to create arrays filled with zeros, ones, or random values.


```python
zeros = np.zeros((3, 3))  # Create an array of zeros
print(zeros)
```
    [[0. 0. 0.]
     [0. 0. 0.]
     [0. 0. 0.]]

```python
ones = np.ones((2, 4))  # Create an array of ones
print(ones)
```

    [[1. 1. 1. 1.]
     [1. 1. 1. 1.]]
    


```python
random_arr = np.random.rand(2, 3)  # Create an array with random values
print(random_arr)
```

    [[0.16991609 0.91678049 0.56229448]
     [0.12281604 0.49698982 0.68606174]]
    

## Array Indexing and Slicing
Just like lists in Python, NumPy arrays can be indexed and sliced to extract specific elements or subsets of data.

**1. Indexing a 1D Array**  
You can access elements of a 1D array using their index.


```python
arr = np.array([10, 20, 30, 40, 50])
print(arr[0])  # Access the first element >> Output: 10
print(arr[-1])  # Access the last element >> Output: 50
```
    10
    50

**2. Slicing a 1D Array**  
You can extract a range of elements using slicing.


```python
# Slice the array to get elements from index 1 to 3
print(arr[1:4])  # Output: [20 30 40]
```

    [20 30 40]
    

**3. Indexing a 2D Array**  
You can index a 2D array using two indices (row, column).


```python
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

# Access the element in the first row, second column
print(arr_2d[0, 1]) # Output: 2
```

    2
    

**4. Slicing a 2D Array**  
Slicing works similarly in 2D arrays.


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
    

## Array Operations
NumPy makes it easy to perform various operations on arrays. These operations are
vectorized, meaning they are performed on all elements of the array at once.

**1. Arithmetic Operations** 
You can perform element-wise arithmetic operations on arrays.


```python
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Element-wise addition
print(arr1 + arr2) # Output: [5 7 9]

# Element-wise multiplication
print(arr1 * arr2) # Output: [ 4 10 18]
```

    [5 7 9]
    [ 4 10 18]
    

**2. Mathematical Functions**  
NumPy provides many mathematical functions like square, square root, and exponential.


```python
arr = np.array([1, 4, 9])

# Element-wise square root
print(np.sqrt(arr))  # Output: [1. 2. 3.]

# Element-wise square
print(np.square(arr))  # Output: [1 16 81]
```

    [1. 2. 3.]
    [ 1 16 81]
    

**3. Aggregation Functions**  
NumPy also provides functions for aggregating the data, such as finding the sum, mean, or
maximum.


```python
arr = np.array([1, 2, 3, 4, 5])

# Find the sum of all elements
print(np.sum(arr))  # Output: 15

# Find the mean of the array
print(np.mean(arr))  # Output: 3.0

# Find the maximum element
print(np.max(arr))  # Output: 5
```

    15
    3.0
    5

**Reshaping Arrays**  
You can reshape a NumPy array to change its dimensions.


```python
arr = np.array([1, 2, 3, 4, 5, 6])

# Reshape the array into a 2D array (2 rows, 3 columns)
reshaped_arr = arr.reshape(2, 3)
print(reshaped_arr)
```

    [[1 2 3]
     [4 5 6]]
    

**Broadcasting**
Broadcasting allows NumPy to perform operations on arrays of different shapes. This is
useful when you need to perform operations between arrays with different dimensions.

Example of Broadcasting


```python
arr = np.array([1, 2, 3])

# Add a scalar to the array
print(arr + 10)  # Output: [11 12 13]
```

    [11 12 13]
    
