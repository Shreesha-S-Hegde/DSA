gain= [-5,1,5,0,-7]
n=len(gain)
current_alt=0
max_alt=0
for item in gain:
    current_alt+=item
    if current_alt>=max_alt:
        max_alt=current_alt
    print(max_alt)