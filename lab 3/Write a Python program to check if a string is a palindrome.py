# Program to check if a string is a palindrome

# Input from the user
string = input("Enter a string: ")

# Remove spaces and convert to lowercase for accurate comparison
cleaned_string = string.replace(" ", "").lower()

# Check if the string is equal to its reverse
if cleaned_string == cleaned_string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

