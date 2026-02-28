s=input()
t=input()

ans=0
i1=0
i2=0
while i1<=len(s) and i2<=len(t):
    c1=""
    c2=""
    if i1<len(s):
        c1=s[i1]
    if i2<len(t):
        c2=t[i2]
#    print(i1,c1,i2,c2)
    if c1==c2:
        i1+=1
        i2+=1
        continue
    elif c1=="A":
        i1+=1
        ans+=1
    elif c2=="A":
        i2+=1
        ans+=1
    else:
        print(-1)
        exit()

print(ans)

