s=input()
ans=len(s)
for i in range(len(s)-1):
    c1=int(s[i])
    c2=int(s[i+1])
    if c1>c2:
        ans+=(c1-c2)
    elif c1<c2:
        ans+=(10-c2+c1)

ans+=int(s[-1])
print(ans)