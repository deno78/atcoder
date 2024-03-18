# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
x = int(input())

# solve
if x%10==0:
    ans=x//10
else:
    if x>=0:
        ans=x//10+1
    else:
        ans=x//10+1

# answer
print("{}".format(ans))
