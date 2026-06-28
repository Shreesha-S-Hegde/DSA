nums = [1,2,3,4,10]
greater=0
smaller=0
for item in nums:
    if item >= 10:
        greater+=item
    else:
        smaller+=item
if greater==smaller:
    print(False)
else:
    print(True)