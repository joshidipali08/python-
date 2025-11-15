# Write a Python program to print all odd numbers between 1 to 100 using a while loop.

# Initialize the counter
num = 1

# Loop from 1 to 100
while num <= 100:
    if num % 2 != 0:
        print(num, end=' ')
    num += 1