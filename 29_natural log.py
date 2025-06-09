import math 
n=float(input("Enter a number: "))
if n<=0:
    print("Natural logarithm is not defined for non-positive numbers.")
else:
    natural_log=math.log(n)
    print("The natural logarithm of", n, "is", natural_log) 