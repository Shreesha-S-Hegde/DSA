nums=[1,3,5,6]
target=5
n=len(nums)
if target in nums:
    for i in range(n):
        if target==nums[i]:
            answer=i
else:
    nums.append(target)
    nums.sort()
    result=nums.index(target)
print(result)