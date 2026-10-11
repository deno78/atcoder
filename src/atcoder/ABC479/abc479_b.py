n=int(input())
s=input()
wk=0
ans=0
for i in range(n):
    if s[i]=="S":
        wk=0
    elif s[i]=="R":
        wk+=1
        ans=max(ans,wk)
print(ans)