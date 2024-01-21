# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
h,w,k = map(int, input().split())
slist=[]
for i in range(h):
    s = input()
    slist.append(s)
# slist2=list(zip(*slist))

# solve
ans=float("INF")

for x in range(w):
    for y in range(h):
#        print("[{} {}]".format(x,y))
        a1=0
        a2=0
        if x+k<=w:
            for i in range(k):
                p=slist[y][x+i]
                if p=="x":
                    a1=float("INF")
                    break
                elif p==".":
                    a1+=1
        else:
            a1=float("INF")
        if y+k<=h:
            for i in range(k):
                p=slist[y+i][x]
                if p=="x":
                    a2=float("INF")
                    break
                elif p==".":
                    a2+=1
        else:
            a2=float("INF")
        ans=min(ans,a1,a2)

# answer
if ans ==float("INF"):
    ans=-1
print(ans)
