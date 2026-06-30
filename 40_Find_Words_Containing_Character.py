words = ["leet","code"]
x = "e"
answer=[]
for i in range(len(words)):
    if x in words[i]:
        answer.append(i)
print(answer)