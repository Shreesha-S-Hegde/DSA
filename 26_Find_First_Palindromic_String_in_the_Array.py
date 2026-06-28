words = ["abc","car","ada","racecar","cool"]
for item in words:
    if item==item[::-1]:
        print(item)