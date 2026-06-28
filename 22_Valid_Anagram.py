s="anagram"
t="nagaram"
if len(s)!=len(t):
    print(False)
first=sorted(s)
second=sorted(t)
if first==second:
    print(True)
else:
    print(False)