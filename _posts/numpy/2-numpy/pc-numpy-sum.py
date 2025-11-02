# pre-course summary: NumPy
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])  # Creating a 1D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])  # Creating a 2D array
zeros = np.zeros((3, 3))  # Creating an array of zeros
ones = np.ones((2, 4))  # Creating an array of ones
random_arr = np.random.rand(2, 3)  # Creating an array with random values

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = np.array([1, 4, 9])

print(arr)  # Output: [1 2 3 4 5 6]
print(arr_2d)  # Output: [[1 2 3] [4 5 6]]
print(zeros)  # Output: [[0. 0. 0.] [0. 0. 0.] [0. 0. 0.]]
print(ones)  # Output: [[1. 1. 1. 1.] [1. 1. 1. 1.]]
print(random_arr)  # Output: Random values in a 2D array

print(arr[0])  # Accessing the first element >> # Output: 1
print(arr[-1])  # Accessing the last element >> # Output: 6
print(arr[1:4])  # Slicing the Arrray >> # Output: [2 3 4]

print(arr_2d[0, 1])  # Indexing an element from 2D Array >> # Output: 2
print(arr_2d[0, :])  # Slicing 2D Array >> # Output: [1 2 3]
print(arr_2d[:, 1])  # Slicing 2D Array >> # Output: [2 5]

print(arr1 + arr2)  # Element-wise addition >> # Output: [5 7 9]
print(arr1 * arr2)  # Element-wise multiplication >> # Output: [ 4 10 18]

print(np.sqrt(arr3))   # Element-wise square root >> # Output: [1. 2. 3.]
print(np.square(arr3))  # Element-wise square >> # Output: [1 16 81]

print(np.sum(arr))  # Find the sum of all elements >> # Output: 21
print(np.mean(arr))  # Find the mean of the array >> # Output: 3.5
print(np.max(arr))  # Find the maximum element >> # Output: 6

# Reshape the array into a 2D array (2 rows, 3 columns)
print(arr.reshape(2, 3))  # Output: [[1 2 3] [4 5 6]]

print(arr + 10)  # Add a scalar to the array >> # Output: [11 12 13 14 15 16]
