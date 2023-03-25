s=list(input())
n=len(s)

ans=0
for i in range(n):
    if s[i]=='D':
        ans+= 2*(n-i-1)+(i)
    elif s[i]=='U':
        ans+= 2*(i)+(n-i-1)
print(ans)