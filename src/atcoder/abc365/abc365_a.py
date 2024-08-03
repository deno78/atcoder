# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
y = int(input())

# solve
ans=365
if y%4==0 and y%100!=0:
    if y%100==0 and y%400!=0:
        ans=365
    else:
        ans=366
elif y%400==0:
    ans=366

# answer
print("{}".format(ans))
