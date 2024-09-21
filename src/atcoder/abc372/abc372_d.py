# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
hlist = list(map(int, input().split()))

# solve
ans = []

for i in range(n):
    a=0
    for j in range(n):
        if i!=j:
            ok=True
            i1=i
            i2=j
            if i>j:
                i1=j
                i2=i
            for k in range(i1,i2):
                if k!=i and hlist[k]>hlist[j]:
                    ok=False
                    print("[{}-{}]/{}".format(i,j,k))
                    break
            if ok:
                a+=1
    ans.append(str(a))
# answer
print(" ".join(ans))
