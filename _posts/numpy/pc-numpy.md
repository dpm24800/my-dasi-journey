

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
