s=input()
k=int(input())

sc=[]
c=0
sc.append(0)
for i in range(len(s)):
    if s[i]==".":
        c+=1
    sc.append(c)

l=0
r=0
ans=0
while r<len(s):
    if s[r]=="X":
        r+=1
    elif sc[r]-sc[l]<k:
        r+=1
    else:
        l+=1
    ans=max(ans,r-l)
#    print("{}-{} [{}] ({})".format(l,r,ans,(sc[r]-sc[l])))

print(ans)