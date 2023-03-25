from itertools import groupby

n=int(input())
s=input()

ans=0
for k,v in groupby(list(s)):
    ans+=1
print(ans)
