n,m=map(int,input().split())
s=list(input())
t=list(input())
q=int(input())
wlist=[]
for _ in range(q):
    wlist.append(input())

for w in wlist:
    taka=True
    aoki=True
    for c in w:
        if c not in s:
            taka=False
        if c not in t:
            aoki=False
    if taka==True and aoki==False :
        print("Takahashi")
    elif aoki==True and taka==False:
        print("Aoki")
    else:
        print("Unknown ")
    