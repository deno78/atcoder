f="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

s=input()
ans=0
for i in range(1,len(s)+1):
    c=s[-1*i]
    p=f.index(c)+1
    x=26**(i-1)
    ans+=x*p
#    print("[{}] {} * {} -> {}".format(i,c,p,x,ans))
print(ans)
