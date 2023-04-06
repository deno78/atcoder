# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,m = map(int, input().split())

if n**2<m:
#    print("{} > {}".format(n**2,m))
    print(-1)
    exit()

# solve
ans = float('INF')

for a in range(1,min(n,int(m**0.5)+1)+1):
    b1=m//a
    b2=b1+1
    b3=b1-1
    for b in [b1,b2,b3]:
        if a<=n and b<=n and a*b>=m:
#            print("{}x{}={}".format(a,b,a*b))
            ans=min(ans,a*b)

# answer
if ans==float('INF'):
    print(-1)
else:
    print(ans)