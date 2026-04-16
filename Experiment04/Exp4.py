# Create empty list
numbers = []

# Input number of elements
n = int(input("Enter number of elements: "))

# Add elements to list
for i in range(n):
    value = int(input("Enter element: "))
    numbers.append(value)

print("\nOriginal List:", numbers)

# Insert element
numbers.insert(1, 50)
print("After inserting 50 at position 1:", numbers)

# Append element
numbers.append(100)
print("After appending 100:", numbers)

# Remove element
if numbers:
    numbers.remove(numbers[0])
    print("After removing first element:", numbers)

# Pop element
popped = numbers.pop()
print("Popped element:", popped)
print("List after pop:", numbers)

# Length of list
print("Length of list:", len(numbers))

# Sort list
numbers.sort()
print("Sorted list:", numbers)

# Reverse list
numbers.reverse()
print("Reversed list:", numbers)

# Maximum and minimum
print("Maximum element:", max(numbers))
print("Minimum element:", min(numbers))

# Count occurrences
element = int(input("Enter element to count: "))
print("Count of element:", numbers.count(element))

# Find index
element2 = int(input("Enter element to find index: "))
if element2 in numbers:
    print("Index of element:", numbers.index(element2))
else:
    print("Element not found")

# Copy list
copy_list = numbers.copy()
print("Copied list:", copy_list)

# Clear list
numbers.clear()
print("List after clear:", numbers)
