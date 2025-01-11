# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
alist = list(map(int, input().split()))

# solve
d=0
dlist=[0]*n
for i in range(n):
    a=alist[i]
    a+=i
    a-=(n-i-1)
#    print("[{}] {}".format(i,a))
#    print(dlist)
    d-=dlist[i]
    a-=d
    if a<0:
        dlist[n-(-1*a)]-=1
        a=0
#    print(a)
    alist[i]=a
# answer
alist2=[]
for a in alist:
    alist2.append(str(a))
print(" ".join(alist2))
