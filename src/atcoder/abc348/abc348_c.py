# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
ac={}
for i in range(n):
    a, c = map(int, input().split())
    if c not in ac.keys():
        ac[c]=[]
    ac[c].append(a)

# solve
ans=-1
for c in ac.keys():
    a=min(ac[c])
    ans=max(ans,a)

# answer
print("{}".format(ans))
