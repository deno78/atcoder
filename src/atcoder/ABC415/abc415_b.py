s=input()
ans=[]
for i in range(len(s)):
    if s[i]=="#":
        ans.append(str(i+1))
    if len(ans)==2:
        print(",".join(ans))
        ans=[]
