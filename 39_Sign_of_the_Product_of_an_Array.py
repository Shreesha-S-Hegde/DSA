nums = [-1,-2,-3,-4,3,2,1]
product=1
for items in nums:
    product*=items
if product==0:
    print(0)
if product>0:
    print(1)
else:
    print(-1)