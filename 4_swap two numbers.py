
#by using a temporary variable
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print(f"Before swapping: a = {a}, b = {b}")

s = a
a = b
b = s
print(f"After swapping: a = {a}, b = {b}")

#by without using a temporary variable
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print(f"Before swapping: a = {a}, b = {b}")
a,b = b,a
print(f"After swapping: a = {a}, b = {b}")