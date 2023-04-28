a,b=map(int,input().split())

ans=0
for i in range(a,b+1):
    s=str(i)
    ok=True
    for j in range(len(s)//2):
        if s[j]!=s[-1*(j+1)]:
            ok=False
            break
    if ok:
        ans+=1
print(ans)