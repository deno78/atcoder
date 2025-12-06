n=int(input())
alist=list(map(int,input().split()))

wk=[0]
visited=set()
visited.add(0)
max_reach=alist[0]-1
while len(wk)>0:
    w=wk.pop(0)
    a=alist[w]
    next=min(n-1,w+a-1)
    for i in range(w,min(n,w+a)):
        a2=alist[i]
        next=min(n-1,max(next,a2+i-1))
        if next not in visited:
            visited.add(next)
            wk.append(next)
            max_reach=max(max_reach,next)
#            print(f"w:{w},a:{a},i:{i},a2:{a2},next:{next}")

print(min(n,max_reach+1))