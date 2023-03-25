from itertools import groupby

s=input()

ACGT=list('ACGT')

ans=0
a=0
for k,v in groupby(s):
    if k in ACGT:
        a+=len(list(v))
    else:
        ans=max(ans,a)
        a=0
ans=max(ans,a)
print(ans)