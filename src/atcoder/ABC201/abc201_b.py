n=int(input())

ts=[]
d={}
for i in range(n):
    st=input().split()
    s=st[0]
    t=int(st[1])
    d[t]=s
    ts.append(t)

ts.sort(reverse=True)
t2=ts[1]
#print(ts)
print(d[t2])