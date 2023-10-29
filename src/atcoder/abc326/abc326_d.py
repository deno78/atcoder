# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1
import itertools

# param
n = int(input())
r = input()
c = input()

# solve
ans=[]
alist=list(itertools.permutations(range(n),n))
blist=list(itertools.permutations(range(n),n))
clist=list(itertools.permutations(range(n),n))
for a in alist:
    for b in blist:
        for c in clist:
            ok=True
            for i in range(n):
                if a[i]==b[i] or a[i]==b[i] or b[i]==c[i]:
                    ok=False
            if ok:
                m=[]
                for i in range(n):
                    m.append(["."]*n)
                for i in range(n):
                    m[i][a[i]]="A"
                    m[i][b[i]]="B"
                    m[i][c[i]]="C"
                ans=m

# answer
print(ans)