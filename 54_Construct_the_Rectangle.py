import math
area=4
w = int(math.sqrt(area))
while area % w != 0:
    w -= 1
print([area // w, w])