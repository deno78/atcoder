n,m=map(int,input().split())
cs={}
for i in range(n):
    c,s=map(int,input().split())
    if c not in cs.keys():
        cs[c]=[]
    cs[c].append(s)

ans=[]
for i in range(1,m+1):
    if i not in cs.keys():
        ans.append(-1)
    else:
        ans.append(max(cs[i]))

print(" ".join(map(str,ans)))