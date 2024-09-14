# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,m = map(int, input().split())
ab={}
for i in range(m):
    a,b=input().split()
    if a not in ab.keys():
        ab[a]=[]
    if b=="F":
        print("No")
    elif len(ab[a])==0:
        print("Yes")
        ab[a].append(b)
    else:
        print("No")


# solve

