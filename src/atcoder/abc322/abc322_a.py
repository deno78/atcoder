# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
s = input()

# solve
for i in range(n-2):
#    print(s[i:i+3])
    if s[i:i+3]=="ABC":
        print(i+1)
        exit()
print(-1)