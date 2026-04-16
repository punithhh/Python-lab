import re

text = input("Enter email: ")

# match()
m = re.match(r'[A-Za-z]+', text)

# search()
s = re.search(r'@', text)

# findall()
f = re.findall(r'\w+', text)

# split()
sp = re.split(r'@', text)

# sub()
new_text = re.sub(r'\.', '_', text)

print("\nUsing match():")
if m:
    print("Starts with:", m.group())

print("\nUsing search():")
if s:
    print("@ symbol found")
else:
    print("@ symbol not found")

print("\nUsing findall():")
print(f)

print("\nUsing split():")
print(sp)

print("\nUsing sub():")
print(new_text)

print("\nUsing finditer():")
for i in re.finditer(r'\d', text):
    print("Digit", i.group(), "at position", i.start())
