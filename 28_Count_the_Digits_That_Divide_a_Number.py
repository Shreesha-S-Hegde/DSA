num=121
count=0
actual_num=num
while num!=0:
    x=num%10
    if actual_num%x==0:
        count+=1
    num=num//10
print(count)