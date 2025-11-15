# Program to find the longest word in a sentence

# Input from the user
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Find the longest word
longest_word = max(words, key=len)

# Display the result
print("The longest word is:", longest_word)
print("Length of the longest word:", len(longest_word))
