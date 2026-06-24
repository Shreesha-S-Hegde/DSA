nums=[0,1,3,4,5]
n=len(nums)
nums.sort()
if nums[0]!=0:
    print(0)
for i in range(1,n):
    if nums[i]!=nums[i-1]+1:
        answer=nums[i-1]+1
        print(answer)