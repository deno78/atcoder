s=input()
n=int(s)

sn=0
for c in list(s):
    sn+=int(c)

if n%sn==0:
    print("Yes")
else:
    print("No")
