#b.	Write a NumPy program to reverse an array (the first element becomes the last).
import numpy as np

# Create an array
arr = np.array([10, 20, 30, 40, 50])

# Reverse the array
reversed_arr = arr[::-1]

print("Original Array:", arr)
print("Reversed Array:", reversed_arr)
