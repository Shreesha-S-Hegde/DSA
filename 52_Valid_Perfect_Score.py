num = 16
for i in range(1, num + 1):
    if i * i == num:
        answer = True
        break
    else:
        answer=False
print(answer)