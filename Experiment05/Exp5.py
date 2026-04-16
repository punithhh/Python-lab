# Input number of elements
n = int(input("Enter number of elements: "))

# Temporary list to store elements
temp_list = []

# Reading elements
for i in range(n):
    value = int(input("Enter element: "))
    temp_list.append(value)

# Convert list to tuple
t = tuple(temp_list)

print("\nTuple elements:", t)

# Length of tuple
print("Length of tuple:", len(t))

# Access elements
print("First element:", t[0])
print("Last element:", t[-1])

# Slicing
print("Tuple slice (first three elements):", t[0:3])

# Count occurrences
x = int(input("Enter element to count: "))
print("Count of element:", t.count(x))

# Index of element
y = int(input("Enter element to find index: "))
if y in t:
    print("Index of element:", t.index(y))
else:
    print("Element not found in tuple")

# Maximum and Minimum
print("Maximum element:", max(t))
print("Minimum element:", min(t))

# Sum of elements
print("Sum of elements:", sum(t))

# Sorting tuple
sorted_tuple = tuple(sorted(t))
print("Sorted tuple:", sorted_tuple)

# Tuple concatenation
t2 = (100, 200)
print("Tuple after concatenation:", t + t2)

# Tuple repetition
print("Tuple after repetition:", t * 2)
