height = [1,8,6,2,5,4,8,3,7]
maximum=0
for i in range(len(height)):
    for j in range(i+1,len(height)):
        area=(min(height[i],height[j]))*(j-i)
        maximum=max(maximum,area)
print(maximum)