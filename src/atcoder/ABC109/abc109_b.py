n=int(input())
wlist=[]
for i in range(n):
    wlist.append(input())

cache=[wlist[0]]
last=wlist[0]
for i in range(1,n):
    w=wlist[i]
    if w in cache:
        print("No")
        exit()
    cache.append(w)
    if w[0]!=last[-1]:
        print("No")
        exit()
    last=w

print("Yes")