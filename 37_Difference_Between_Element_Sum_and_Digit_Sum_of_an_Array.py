nums = [1,15,6,3]
element_sum=0
for item in nums:
    element_sum+=item
digit_sum=0
for items in nums:
    while items!=0:
        temp=items%10
        digit_sum+=temp
        items=items//10
print(abs(element_sum-digit_sum))