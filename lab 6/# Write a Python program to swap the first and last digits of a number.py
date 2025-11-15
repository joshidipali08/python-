# Write a Python program to swap the first and last digits of a number.
def swap_first_last_digits(num):
    num_str = str(num)
    if len(num_str) <= 1:
        return num # No swap needed for single-digit numbers

    # Swap first and last digits
    swapped = num_str[-1] + num_str[1:-1] + num_str[0]
    return int(swapped)

# Input from user
number = int(input("Enter a number: "))
swapped_number = swap_first_last_digits(number)
print("Number after swapping first and last digits:", swapped_number)