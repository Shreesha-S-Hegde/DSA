s = "loveleetcode"
n=len(s)
for i in range(n):
    unique=True
    for j in range(n):
        if i!=j and s[i]==s[j]:
            unique=False
            break
    if unique:
        print(i)
print(-1)