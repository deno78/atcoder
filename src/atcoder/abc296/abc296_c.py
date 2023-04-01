# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,x = map(int, input().split())
alist=list(map(int,input().split()))

# solve
bdict={}
for i in range(n):
    a=alist[i]
    bdict[a-x]=1

for a in alist:
    if a in bdict.keys():
        print("Yes")
        exit()
print("No")
