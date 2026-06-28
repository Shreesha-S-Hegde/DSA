nums = [3,4,6]
if nums[0]+nums[1]<=nums[2] or nums[0]+nums[2]<=nums[1] or nums[1]+nums[2]<=nums[0]:
    print("none")
elif nums[0]==nums[1] and nums[1]==nums[2]:
    print("equilateral")
elif nums[0]!=nums[1] and nums[0]!=nums[2] and nums[1]!=nums[2]:
    print("scalene")
else:
    print("isosceles")