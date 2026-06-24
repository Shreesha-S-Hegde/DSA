n=17
if n<=0:
    print(False)
else:
    for i in [2,3,5]:
        while n%i==0:
            n=n//i
    print(n==1)