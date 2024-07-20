# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1
import itertools

# param
n,k = map(int, input().split())
s = input()

# solve
ans=set([])
for w in itertools.permutations(s,n):
    ok1=True
    for i in range(n-k+1):
        ok2=True
        for j in range(k//2):
            if w[i+j]!=w[i+k-j-1]:
#                print("{} {}({}/{})=({}/{})".format(w,w[i:i+k],w[i+j],w[i+k-j-1],i+j,i+k-j-1))
                ok2=False
                break
        if ok2==True:
            ok1=False
            break
    if ok1==True:
        ans.add("".join(w))
# answer
print(len(ans))