# Program to calculate the Surface Area and Volume of a Cube

# Input: Length of a side
side = float(input("Enter the length of a side of the cube: "))

# Calculations
surface_area = 6 * (side ** 2)
volume = side ** 3

# Output the results
print(f"Surface Area of the cube: {surface_area}")
print(f"Volume of the cube: {volume}")
