arr = [2,6,4,1]
n=len(arr)
for i in range(2,n):
    if arr[i]%2!=0 and arr[i-1]%2!=0 and arr[i-2]%2!=0:
        answer=True
    else:
        answer=False
print(answer)