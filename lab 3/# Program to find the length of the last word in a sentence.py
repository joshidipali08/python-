# Program to find the length of the last word in a sentence

# Input from the user
sentence = input("Enter a sentence: ")

# Remove any trailing spaces and split the sentence into words
words = sentence.strip().split()

# Check if the sentence has any words
if words:
    last_word = words[-1]
    print("The last word is:", last_word)
    print("Length of the last word:", len(last_word))
else:
    print("The sentence has no words.")