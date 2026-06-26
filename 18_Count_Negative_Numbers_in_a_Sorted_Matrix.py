grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
count=0
m=len(grid)
for items in grid:
    for ele in items:
        if ele<0:
            count+=1
print("Number of negative integers is",count)