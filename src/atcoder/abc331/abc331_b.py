# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,s,m,l = map(int, input().split())

# solve
ans=float("INF")
for i in range(n//12+2):
    for j in range(n//8+2):
        for k in range(n//6+2):
            if i*12+j*8+k*6>=n:
        #        print("{} {} {}".format(i,j,k))
                ans=min(ans,i*l+j*m+k*s)

# answer
print("{}".format(ans))
