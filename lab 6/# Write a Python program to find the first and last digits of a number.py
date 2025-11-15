# Write a Python program to find the first and last digits of a number

# Input from user
num = int(input("Enter a number: "))

# Get last digit
last_digit = num % 10

# Get first digit
first_digit = num
while first_digit>= 10:
    first_digit//= 10   # keep dividing until one digit is left

# Display result
print("First digit:", first_digit)
print("Last digit:", last_digit)
