# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,t = map(int, input().split())
alist = list(map(int, input().split()))


# solve
chk=[0]*(n**2)
for i in range(t):
    a=alist[i]
    a-=1
    x=a%n
    y=a//n
    chk[a]=1
#    print("{} {}".format(i,chk))
    ok1=True
    ok2=True
    ok3=True
    ok4=True
    for j in range(n):
#        print("## 1 {}".format(y*n+j))
        if chk[y*n+j]==0:
            ok1=False
            break
    for j in range(n):
#        print("## 2 {}".format(x+j*n))
        if chk[x+j*n]==0:
            ok2=False
            break
    if ok1==True or ok2==True:
#        print("#1")
        print(i+1)
        exit()
    for j in range(n):
        if chk[(n+1)*j]==0:
            ok3=False
        if chk[n-1+(n-1)*j]==0:
            ok4=False
        if ok3==False and ok4==False:
            break
    if ok3==True or ok4==True:
#        print("#2")
        print(i+1)
        exit()

# answer
print(-1)


# 0  1  2  3
# 4  5  6  7
# 8  9 10 11
#12 13 14 15
