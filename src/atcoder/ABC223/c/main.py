n=int(input())
ablist=[]
t=0
for i in range(n):
    a,b=map(int,input().split())
    ablist.append([a,b])
    t+=a/b
t/=2
l=0
for a,b in ablist:
    if t > a/b:
        t-=a/b
        l+=a
    else:
        l+=(b*t)
        print(l)
        exit()


