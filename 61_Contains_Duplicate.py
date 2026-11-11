nums = [1,1,1,3,3,4,3,2,4,2]
noduplicates=set(nums)
if len(nums)==len(noduplicates):
    print(False)
else:
    print(True)