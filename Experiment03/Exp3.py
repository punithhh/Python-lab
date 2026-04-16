# Taking input from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Case conversion
print("\nUppercase:", string1.upper())
print("Lowercase:", string1.lower())

# Capitalize and Title
print("Capitalized:", string1.capitalize())
print("Title Case:", string2.title())

# Concatenation
concat = string1 + " " + string2
print("Concatenated String:", concat)

# String slicing
print("First three characters:", string1[0:3])

# Replace characters
print("Replace 'r' with 'R':", string1.replace("r", "R"))

# Splitting
print("Split string1 using 'f':", string1.split("f"))

# Length of string
print("Length of string1:", len(string1))
print("Length of string2:", len(string2))

# Find position of character
print("Position of 'b' in string2:", string2.find("b"))

# Count occurrences
print("Count of 'a' in string1:", string1.count("a"))

# Swap case
print("Swapcase:", string1.swapcase())

# Accessing characters
print("First character of string1:", string1[0])
print("Last character of string1:", string1[-1])

# Strip spaces
print("After strip:", string1.strip())

# Check start and end
print("Starts with 'a':", string1.startswith("a"))
print("Ends with 'z':", string1.endswith("z"))

# Check string types
print("Is alphabet:", string1.isalpha())
print("Is digit:", string1.isdigit())

# Join example
words = [string1, string2]
print("Joined with hyphen:", "-".join(words))

# Searching word
search = input("\nEnter a word to search in the string: ")

if search in string1:
    print("Word found in string 1")
elif search in string2:
    print("Word found in string 2")
else:
    print("Word not found in string ")
