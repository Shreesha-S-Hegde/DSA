nums=[5,4,2,3]
arr=[]
while len(nums)!=0:
    temp=[]
    smallest=nums[0]
    for item in nums:
        if item<=smallest:
            smallest=item
    temp.append(smallest)
    nums.remove(smallest)
    second_smallest=nums[0]
    for items in nums:
        if items<=second_smallest:
            second_smallest=items
    temp.append(second_smallest)
    nums.remove(second_smallest)
    temporary=temp[::-1]
    arr.extend(temporary)
print(arr)