a = 200
b = 600

print("\n Equation Assignment Operators :\n")

print((a+b)**2 == a**2 + 2*(a+b) + b**2)
print((a-b)**2 == a**2 - 2*(a+b) + b**2)
print((a+b)*(a+b) == 2*(a**2 - b**2))
print((a+b)+(a-b) == a**2 - b**2)
print(a**3 + b**3 == (a+b)*(a**2 - a*b + b**2))


print("\n Bitwise Operations")

print(a | b == (a ^ b) + (a & b))
print(a ^ (a & b) == (a | b) ^ b)
print(b ^ (a & b) == (a | b) ^ a)
print((a & b) ^ (a | b) == a ^ b)


print("\n Addition \n")

print((a+b) == (a | b) + (a & b))
print(a+b == (a ^ b) + 2*(a & b))


print("\n Subtraction \n")

print(a-b == (a ^ (a & b)) - ((a | b) ^ a))
print(a-b == ((a | b) ^ b) - ((a | b) ^ a))
print(a-b == (a ^ (a & b)) - (b ^ (a & b)))
print(a-b == ((a | b) ^ b) - (b ^ (a & b)))
