# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
h,w = map(int, input().split())
slist=[]
for i in range(h):
    slist.append(input())

# solve
for s in slist:
    ans=list(s)
    for i in range(w-1):
        if ans[i]=="T" and ans[i+1]=="T":
            ans[i]="P"
            ans[i+1]="C"
    print("".join(ans))
