end=int(input("Enter the ending number of the interval: "))
sum=0
for n in range(1,end+1):
    sum+=n
print("The sum of natural numbers from 1 to", end, "is", sum)
