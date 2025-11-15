#d. Write a NumPy program to repeat array elements.
import numpy as np

# Define an array
arr = np.array([1, 2, 3])

# Repeat each element 3 times
repeated_arr = np.repeat(arr, 3)

print("Original Array:", arr)
print("Repeated Array:", repeated_arr)
