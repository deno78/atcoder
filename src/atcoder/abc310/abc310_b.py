# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,m = map(int, input().split())
plist=[]
for i in range(n):
    plist.append(list(map(int,input().split())))

# solve
for i in range(n):
    for j in range(n):
        if i!=j:
            p1=plist[i]
            p2=plist[j]
            if p1[0] >= p2[0]:
                ok=True
                for c1 in p1[2:]:
                    if c1 not in p2[2:]:
                        ok=False
                        break
                cnt=0
                for c2 in p2[2:]:
                    if c2 not in p1[2:]:
                        cnt+=1
                if ok and (p1[0] > p2[0] or cnt>0):
                    print("Yes")
                    exit()

print("No")
