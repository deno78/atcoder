n=int(input())
s=input()

ans=-1
if "-" not in s:
    print(-1)
    exit()
if "o" not in s:
    print(-1)
    exit()

r=s.index("o")
l=max(0,r-1)
while r<n and l<n-1:
    if s[r]=="o":
        r+=1
    elif s[l]=="-":
        l+=1
    else:
        ans=max(ans,s[l:r].count("o"))
        l=r
        r=l+1
#    print("[{}-{}]={} => {} =>{}".format(l,r,s[l:r],s[l:r].count("o"),ans))
ans=max(ans,s[l:r].count("o"))

print(ans)