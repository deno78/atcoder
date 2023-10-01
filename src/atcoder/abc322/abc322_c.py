# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,m = map(int, input().split())
alist=list(map(int,input().split()))

# solve
d=0
for i in range(1,n+1):
#    print("[{}] {}".format(i,alist[d]))
    if alist[d]>i:
        print(alist[d]-i)
    else:
        print(0)
        d+=1
