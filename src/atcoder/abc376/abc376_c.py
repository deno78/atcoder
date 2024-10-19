# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
alist = list(map(int, input().split()))
blist = list(map(int, input().split()))

alist.sort(reverse=True)
blist.sort(reverse=True)

# solve
x=-1
for i in range(n):
    a=alist[i]
    if i>=n-1:
        if x==-1:
            x=alist[-1]
            break
        else:
            b=blist[i-1]
    elif x!=-1 and i>0:
        b=blist[i-1]
    else:
        b=blist[i]
    if a>b:
        if x==-1:
            x=a
        else:
            print(-1)
            exit()
#    print("[{}] {}/{} ({})".format(i,a,b,x))

# answer
print("{}".format(x))
