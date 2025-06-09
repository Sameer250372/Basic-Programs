n=int(input("Enter a number: "))
n1=str(n)
n2=len(n1)
sum=0
temp=n
while temp>0:
    digit=temp%10
    sum+=digit**n2
    temp//=10
if sum==n:
    print(n,"is an Armstrong number")
else:
    print(n,"is not an Armstrong number")