# 12.1 Create two 2D Numpy arrays with random numbers and concatenate them using the
# Numpy library. After Concatenation, reshape the resulting Numpy array such that the number
# of rows and columns is reversed.

import numpy as np

# create two 2D numpy arrays with random numbers
arr1 = np.random.rand(2, 3)
arr2 = np.random.rand(2, 4)

print("Array 1:\n", arr1)
print("Array 2:\n", arr2)

# concatenate the two arrays
concatenated = np.concatenate((arr1, arr2), axis=1)

print("Concatenated array:\n", concatenated)

# reshape the concatenated array
reshaped = concatenated.reshape(concatenated.shape[1], concatenated.shape[0])

print("Reshaped array:\n", reshaped)
print("\nID: 21DCE042\nAuthor: Jash Karangiya")