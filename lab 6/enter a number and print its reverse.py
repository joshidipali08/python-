def reverse_number(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return reversed_num

# Input from user
number = int(input("Enter a number: "))

# Handle special case for 0
if number == 0:
    print("Reversed number: 0")
else:
    print("Reversed number:", reverse_number(abs(number)))
