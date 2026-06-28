n=5
if n==0:
    print("The complement of 0 is 1")
k=n.bit_length()
answer=2**k-n-1
print("the complement of the number is",answer)