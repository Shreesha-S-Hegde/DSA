num=28
total=0
for i in range(1,num):
    if num%i==0:
        total+=i
print(total==num)