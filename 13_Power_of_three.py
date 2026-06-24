n=int(input("Enter the number:"))
if n<=0:
    print(False)

while n%3==0:
    n=n//3
print(n==1)