# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
x = int(input())

# solve
ans=0
for i in range(1,x+10):
    ans=i
    x//=i
    if x==1:
        break

# answer
if ans==0:
    ans=1
print("{}".format(ans))
