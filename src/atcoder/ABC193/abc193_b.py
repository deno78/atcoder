n=int(input())
m=-1
for i in range(n):
    apx=input().split()
    a=int(apx[0])
    p=int(apx[1])
    x=int(apx[2])-a
    if x>0:
        if m==-1 or p<m:
            m=p

print(m)
