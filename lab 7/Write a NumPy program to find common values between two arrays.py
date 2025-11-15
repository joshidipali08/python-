#c. Write a NumPy program to find common values between two arrays
import numpy as np

# Define two arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([4, 5, 6, 7, 8])

# Find common values
common_values = np.intersect1d(arr1, arr2)

print("Array 1:", arr1)
print("Array 2:", arr2)
print("Common values:", common_values)
