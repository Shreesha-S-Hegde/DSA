n=int(input("Enter a number:"))
count=0
for i in range(n+1):
    if i%3==0 or i%5==0 or i%7==0:
        count+=i
print(count)