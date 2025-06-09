start=int(input("Enter the starting number of the interval: "))
end=int(input("Enter the ending number of the interval: "))
for n in range(start,end+1):
    order=len(str(n))
    temp=n
    sum=0
    while temp>0:
        digit=temp%10
        sum+=digit**order
        temp//=10
    if sum==n:
        print(n)