#Write a Python program to find the sum of all natural numbers between 1 to n.
# Input from the user
n = int(input("Enter a number: "))

# Initialize sum
total = 0
i = 1

# Loop to calculate sum
while i <= n:
    total += i
    i += 1

# Output the result
print("Sum of natural numbers from 1 to", n, "is:", total)
