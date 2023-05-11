import math
a=int(input().replace(" ",""))
for i in range(100*100+1):
    if a==i**2:
        print("Yes")
        exit()
print("No")
