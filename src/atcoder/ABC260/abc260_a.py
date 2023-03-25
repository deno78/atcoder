s = list(input())
d={}
for c in s:
    if c not in d.keys():
        d[c]=0
    d[c]+=1
for k,v in d.items():
    if v==1:
        print(k)
        exit()
print(-1)
exit()