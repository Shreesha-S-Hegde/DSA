n=int(input("Enter a number:"))
if n<=0:
    print(False)
else:
    while n%4==0:
        n=n//4
    print(n==1)