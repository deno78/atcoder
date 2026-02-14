n=int(input())
slist=[]
m=0
for i in range(n):
    s=input()
    slist.append(s)
    m=max(m,len(s))

for i in range(n):
    ans=""
    l=m-len(slist[i])
    for j in range(l//2):
        ans+="."
    ans+=slist[i]
    for j in range(l//2):
        ans+="."
    print(ans)