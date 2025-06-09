terms=int(input("Enter the number of terms in the Fibonacci sequence: "))
a,b=0,1
count=0
if terms<=0:
    print("Please enter a positive integer.")
elif terms==1:
    print(f"Fibonacci sequence up to {terms} term: {a}")
else:
    print(f"Fibonacci sequence up to {terms} terms:")
    while count < terms:
        print(a,end=' ')
        nth=a+b
        a=b
        b=nth
        count += 1