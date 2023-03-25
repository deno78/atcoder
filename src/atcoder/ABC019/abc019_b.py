s=input()

ans=[]
p=s[0]
cnt=0
for c in s:
    if p==c:
        cnt+=1
    else:
        ans.append(p)
        ans.append(str(cnt))
        cnt=1
        p=c

ans.append(p)
ans.append(str(cnt))

print("".join(ans))