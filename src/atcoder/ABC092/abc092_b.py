n=int(input())
d,x=map(int,input().split())
alist=[]
for i in range(n):
    alist.append(int(input()))

for i in range(d):
    for a in alist:
        if i%a==0:
            x+=1

print(x)