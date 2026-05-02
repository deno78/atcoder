s=input()

ans=0
wklist=[]
wk=[]
c1=s[0]
wk.append(c1)
for i in range(1,len(s)):
    c2=s[i]
    if c1==c2:
        ans += len(wk) * (len(wk) + 1) // 2
        ans%=998244353
        wk=[]
    c1=c2
    wk.append(c1)
ans += len(wk) * (len(wk) + 1) // 2
ans%=998244353
 
print(ans)