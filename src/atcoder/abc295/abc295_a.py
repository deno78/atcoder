# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
wlist = input().split()
check=["and","not","that","the","you"]

# solve
ok=False
for w in wlist:
    for c in check:
        if w==c:
            ok=True
            break
if ok:
    print("Yes")
else:
    print("No")
