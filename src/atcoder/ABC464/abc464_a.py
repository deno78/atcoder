s=input()
e=0
w=0
for c in s:
    if c=="E":
        e+=1
    elif c=="W":
        w+=1

if e>w:
    print("East")
else:
    print("West")