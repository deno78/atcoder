# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,d,p = map(int, input().split())
flist = list(map(int, input().split()))

# solve
ans=0
flist.sort(reverse=True)
for i in range(n//d+1):
    i1=i*d
    i2=min(n,(i+1)*d)
#    print("{}-{}".format(i1,i2))
    a1=sum(flist[i1:i2])
    a2=p
    ans+=min(a1,a2)

# answer
print("{}".format(ans))
