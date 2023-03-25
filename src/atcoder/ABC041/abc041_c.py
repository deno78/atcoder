n=int(input())
a=list(map(int,input().split()))
d=dict()
for i in range(len(a)):
    d[i]=a[i]
d2=sorted(d.items(),key=lambda x:x[1],reverse=True)

for p in d2:
    print(p[0]+1)