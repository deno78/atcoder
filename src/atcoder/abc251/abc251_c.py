# TODO edit the code

# param
n = int(input())
si={}
ts={}
for i in range(n):
    s,ti=input().split()
    t=int(ti)
    if s not in si.keys():
        si[s]=i+1
        if t not in ts.keys():
            ts[t]=s

m=max(ts.keys())
sa=ts[m]

# solve
ans = si[sa]

# answer
print(ans)
