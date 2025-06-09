a=float(input("Enter first number: "))
b=float(input("Enter second number: "))
addition=a+b
subtraction=a-b
multiplication=a*b
if b==0:
    division="undefined (cannot divide by zero)"
else:
    division=a/b
print(f"Addition:{a} + {b} = {addition}")
print(f"Subtraction: {a} - {b} = {subtraction}")
print(f"Multiplication: {a} * {b} = {multiplication}")
print(f"Division: {a} / {b} = {division}")