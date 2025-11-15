#Convert a list of multiple integers into a single integer
digits = [1, 2, 3, 4]
number = 0

for digit in digits:
    number = number * 10 + digit

print("Single integer:", number)