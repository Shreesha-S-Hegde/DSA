n=int(input("Enter an integer:"))
m=int(input("Enter another integer:"))
num1=0
num2=0
for i in range(n+1):
    if i%m==0:
        num2+=i
    else:
        num1+=i
print(num1-num2)