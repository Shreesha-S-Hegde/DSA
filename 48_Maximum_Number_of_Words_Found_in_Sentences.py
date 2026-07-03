sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
answer=0
for items in sentences:
    words=len(items.split())
    if words>answer:
        answer=words
print(answer)