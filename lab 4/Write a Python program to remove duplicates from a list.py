#Write a Python program to get the frequency of elements in a list.
from collections import Counter

# Sample list
items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

# Count frequency
frequency = Counter(items)

# Print result
print("Frequency of elements:", frequency)
