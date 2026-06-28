n=int(input("Enter an integer,n:"))
start=int(input("Enter an integer,start:"))
nums=[]
for i in range(n):
    ele=start+2*i
    nums.append(ele)
    answer=0
for j in range(n):
    answer=answer^nums[j]
print(answer)