#Find common items from two lists
# Two sample lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Find common items
common_items = list(set(list1) & set(list2))

# Print result
print("Common items:", common_items)
