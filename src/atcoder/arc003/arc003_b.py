n=int(input())
slist=[]
sdic={}
for i in range(n):
    s1=input()
    s2="".join(reversed(list(s1)))
    slist.append(s2)
    sdic[s2]=s1

slist.sort()
for s in slist:
    print(sdic[s])
