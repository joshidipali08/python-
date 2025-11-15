# Write a NumPy program to find the memory size of a NumPy array.
import numpy as np

# Define an array
arr = np.array([10, 20, 30, 40, 50])

# Find memory size in bytes
print("Array:", arr)
print("Memory size of array (in bytes):", arr.nbytes)