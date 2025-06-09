def cube_n(n):
    if n<=0:
        return 0
    else:
        total=sum(i**3 for i in range(1, n+1))
        return total
    
n=int(input("Enter a positive integer: "))
if n<0:
    print("Please enter a positive integer.")
else:
    result=cube_n(n)
    print("The sum of the cubes of the first", n, "natural numbers is:", result)