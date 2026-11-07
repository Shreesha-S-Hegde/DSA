n=int(input("Enter a number: "))
count=0
answer=bin(n)
result=answer[2:]
for item in result:
    if item=='1':
        count+=1
print(count)