nums = [12,345,2,6,7896]
n=len(nums)
total=0
for i in range(n):
    num=nums[i]
    count=0
    while num>0:
        count+=1
        num=num//10
    if count%2==0:
        total+=1
print(total)