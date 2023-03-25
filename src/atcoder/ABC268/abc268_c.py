n=int(input())
plist=list(map(int,input().split()))

clist=[0]*n

# 1回回すと p+/-1の人が喜ぶ
for i in range(n):
    p=plist[i]
    p1=(p-i-1)%n
    p2=(p-i)%n
    p3=(p-i+1)%n
    clist[p1]+=1
    clist[p2]+=1
    clist[p3]+=1

print(max(clist))