# DAY 3
# Task 1: Array Creation & Inspection
# Create a 1D array of 20 random integers between 1 and 100.
# Reshape that array into a 4x5 matrix (2D array).
# Check and print its shape, number of dimensions, and data type.

# Task 2: Scalar Operations (Vectorization)
# Create a 3x3 matrix filled with the number 5.
# Multiply the entire matrix by 10 without using a loop.
# Subtract 2 from every element in the resulting matrix.
# Square every element.

# Task 3: Boolean Indexing (The Filter)
# Create an array: arr = np.array([10, -5, 20, -15, 30, 0]).
# Use a boolean mask to create a new array that only contains positive numbers.
# Replace all negative numbers in the original array with 0.


# task1
import numpy as np
arr = np.random.randint(1 , 101 , 20) 
arr = arr.reshape(4,5)  
print(arr)
print(arr.shape)
print(arr.ndim)
print(arr.dtype)

#task2
mat1 = np.full((3,3) , 5)
print(mat1)
mat3 = np.full((3,3), 10)
print(mat3 * mat1)
mat2 = mat1 * 10
print(mat2)
mat4 = mat2 - 2
print(mat4)
mat5 = mat4 ** 2
print(mat5)

# task3
arrNew = np.array([10, -5, 20, -15, 30, 0])
posNUm = arrNew[arrNew > 0]
print(posNUm)
arrNew[arrNew < 0] = 0
print(arrNew)