num=38
while num>=10:
    sum=0
    for item in str(num):
        sum+=int(item)
        num=sum
print(num)