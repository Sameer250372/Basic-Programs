import math
a=float(input("Enter coefficient a: "))
b=float(input("Enter coefficient b: "))     
c=float(input("Enter coefficient c: "))

d=(b**2)-(4*a*c)

if d > 0:
    r1=(-b+math.sqrt(d))/(2*a)
    r2=(-b-math.sqrt(d))/(2*a)
    print(f"The roots are real and different: {r1} and {r2}")
elif d == 0:
    r1=r2=-b/(2*a)
    print(f"The roots are real and the same: {r1}")
else:
    real_part=-b/(2*a)
    imaginary_part=math.sqrt(-d) / (2 * a)
    print(f"The roots are complex and different: {real_part}+{imaginary_part}i and {real_part}-{imaginary_part}i")