s = "A man, a plan, a canal: Panama"
s=s.lower()
new=""
for items in s:
    if items.isalnum():
        new+=items
if new==new[::-1]:
    print(True)
else:
    print(False)