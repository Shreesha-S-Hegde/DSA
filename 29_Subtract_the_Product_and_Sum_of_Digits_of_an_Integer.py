n=int(input("Enter a number:"))
num=n
sum=0
product=1
while n!=0:
    x=n%10
    sum+=x
    product*=x
    n=n//10
print(product-sum)