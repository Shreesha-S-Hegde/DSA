moves = "UD"
countL=0
countR=0
countU=0
countD=0
for items in moves:
    if items=='L':
        countL+=1
    if items=='R':
        countR+=1
    if items=='U':
        countU+=1
    if items=='D':
        countD+=1
if countU==countD and countL==countR:
    print(True)
else:
    print(False)