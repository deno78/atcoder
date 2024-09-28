# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
s = input()

keys="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# solve
ans = 0
p=s.index("A")
for c in list(keys):
    idx=s.index(c)
    ans+=abs(idx-p)
    p=idx

# answer
print("{}".format(ans))
