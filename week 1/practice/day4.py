# DAY4

# Task 1: The "Sub-Matrix" Challenge
# Create a 5x5 matrix with values from 1 to 25.
# Extract the middle 3x3 sub-matrix.
# Set all values in that sub-matrix to 0.
# Check the original 5x5 matrix—did it change? (This tests your understanding of "Views").

# Task 2: Feature Selection (Slicing)
# Imagine a 10x4 matrix where the first 3 columns are "Features" and the last column is the "Target".
# Create a random 10x4 array.
# Slice it to create X (all rows, first 3 columns).
# Slice it to create y (all rows, only the last column).

# Task 3: Axis-based Analytics
# Create a 4x4 matrix of random floats.
# Calculate the mean of each column.
# Calculate the sum of each row.
# Find the index of the maximum value in each row using np.argmax(axis=1).


# task1
import numpy as np
arr = np.arange(1,26).reshape(5,5)
print(arr)
subarr = arr[1:4 , 1:4]
print(subarr)
subarr[:] = 0
print(subarr)
print (arr)

# task2
data = np.random.rand(10,4)
print(data)
x = data[ : , :3]
y = data[ : , 3:4]
print(x.shape)
print(y.shape)

# task3
flt = np.random.rand(4,4)
print(flt)
meancol = np.mean(flt,axis = 0)
print(meancol)
sumrow = np.sum(flt,axis = 0)
print(sumrow)
maxrrow = np.argmax(flt , axis=1)
print(maxrrow)