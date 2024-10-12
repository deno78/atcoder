# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
s = input()

# solve
ans = 0
for i in range(n-2):
    if s[i]=="#" and s[i+1]=="." and s[i+2]=="#":
        ans+=1

# answer
print("{}".format(ans))
