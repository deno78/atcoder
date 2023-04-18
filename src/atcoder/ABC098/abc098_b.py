n=int(input())
s=input()

cset=set(list(s))
ans=0
for i in range(1,n):
    x=s[:i]
    y=s[i:]
#    print("{} = {}/{}".format(s,x,y))
    wk=0
    for c in cset:
        if c in x and c in y:
            wk+=1
    ans=max(ans,wk)

print(ans)    
    
