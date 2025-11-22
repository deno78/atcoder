s=input()
sz=len(s)
ans=0
for i in range(len(s)-1):
    if int(s[i])+1==int(s[i+1]):
        mx=min(i+1, sz-i-1)   
#        print("#",i,mx)
        for j in range(mx):
            if s[i-j]==s[i] and s[i+j+1]==s[i+1]:
                ans+=1
#                print(i-j,i+j+1)
            else:
                break

print(ans)
