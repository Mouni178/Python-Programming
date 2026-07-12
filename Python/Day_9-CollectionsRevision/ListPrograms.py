numbers=[10, 40, 20, 50, 30]
print("Original List:", numbers)
# Append
numbers.append(60)
print("After Append:", numbers)
# Insert
numbers.insert(2, 25)
print("After Insert:", numbers)
# Remove
numbers.remove(40)
print("After Remove:", numbers)
# Pop
numbers.pop()
print("After Pop:", numbers)
# Count
print("Count of 20:", numbers.count(20))
# Index
print("Index of 25:", numbers.index(25))
# Sort
numbers.sort()
print("Sorted:", numbers)
# Reverse
numbers.reverse()
print("Reversed:", numbers)
# Functions
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))
print("Average:", sum(numbers)/len(numbers))
# Membership
print(30 in numbers)
# Copy
copy_list = numbers.copy()
print("Copied List:", copy_list)