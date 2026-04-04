n=int(input())
ab=[]
for i in range(n):
    a,b=map(int,input().split())
    ab.append((a,b))

m=int(input())
slist=[]
for i in range(m):
    s=input().strip()
    slist.append(s)

# 各ルール idx について、条件を満たす文字候補を前計算
possible=[set() for _ in range(n)]
for s in slist:
    ls=len(s)
    for idx,(a,b) in enumerate(ab):
        if ls==a and 1<=b<=ls:
            possible[idx].add(s[b-1])

for i in range(m):
    s1=slist[i]
    if len(s1)!=n:
        print("No")
        continue

    ok=True
    for idx in range(n):
        if s1[idx] not in possible[idx]:
            ok=False
            break

    print("Yes" if ok else "No")
