n=int(input())
alist=list(map(int,input().split()))

ans=0
for a in alist:
    if a>10:
        ans+=(a-10)

print(ans)