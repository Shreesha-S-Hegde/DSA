nums = [2,2,1,1,1,2,2]
n=len(nums)
sorted_nums=list(set(nums))
for i in sorted_nums:
    answer=nums.count(i)
    if answer>(n/2):
        answer=i
print(answer)