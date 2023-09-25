
# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = input()

if len(n)==1:
    print("Yes")
    exit()

for i in range(1,len(n)):
    if int(n[i]) >= int(n[i-1]):
        print("No")
        exit()
print("Yes")