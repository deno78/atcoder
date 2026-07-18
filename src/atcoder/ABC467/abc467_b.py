n=int(input())
abslist=[]
for i in range(n):
    a,b,s=input().split()
    a=int(a)
    b=int(b)
    abslist.append((a,b,s))

ans1=10000
ans2=10000
for a,b,s in abslist:
    if s=="keep":
        ans1-=a
        ans2-=b
    else:
        ans1-=a
        ans2-=a
#    print(ans1,ans2)
print(ans1-ans2)