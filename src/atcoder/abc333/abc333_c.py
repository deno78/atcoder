# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1
import itertools


# param
n = int(input())

# solve
wk=[]
for i in range(1,16):
    x= int("".join(["1"]*i))
    wk.append(x)

ans=[]
for x in itertools.combinations_with_replacement(wk,3):
    ans.append(sum(x))

ans.sort()
# print(len(ans))

# answer
print(ans[n-1])

# 4->10  2x5
# 5->20  2x2x5
# 6 ->35 5x7
# 7->56  2x2x2x7
# 8->84  2x2x3x7
# 19->1140