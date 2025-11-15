# Program to solve the equation: z = (x + y)^2 - 2xy

# Input: Values of x and y from the user
x = float(input("Enter the value of x: "))
y = float(input("Enter the value of y: "))

# Calculation using the formula z = (x + y)^2 - 2xy
z = (x + y)**2 - 2 * x * y

# Output the result
print(f"The result of the equation z = (x + y)^2 - 2xy is: {z}")
