n,a,b=map(int,input().split())
sd=[]
for i in range(n):
    s,d=input().split()
    sd.append([s,int(d)])

ans=0
for s,d in sd:
    l=1
    if s=="West":
        l=-1
    if d<a:
        ans+=l*a
    elif a<=d and d<=b:
        ans+=l*d
    else:
        ans+=l*b

if ans>0:
    print("East {}".format(ans))
elif ans<0:
    print("West {}".format(-1*ans))
else:
    print(0)
