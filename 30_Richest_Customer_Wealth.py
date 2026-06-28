accounts = [[2,8,7],[7,1,3],[1,9,5]]
max=0
for items in accounts:
    current=0
    for ele in items:
        current+=ele
    if current>=max:
        max=current
print(max)