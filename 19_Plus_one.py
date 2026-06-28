digits = [1,2,3]
n=len(digits)
l=[]
new = ' '
for item in digits:
    new+=str(item)
new=int(new)
new+=1
for items in str(new):
    l.append(int(items))
print("The appended list is",l)