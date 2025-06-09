def lcm(a,b):
    if a>b:
        greater = a
    else:
        greater = b
    while True:
        if((greater%a==0) and (greater%b==0)):
            lcm = greater
            break
        greater+=1
    return lcm

n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
result = lcm(n1, n2)
print("The LCM of", n1, "and", n2, "is", result)