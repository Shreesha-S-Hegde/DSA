n=int(input("Enter the number:"))
if n<=0:
    print(False)

while n%2==0:
    n=n//2
print(n==1)