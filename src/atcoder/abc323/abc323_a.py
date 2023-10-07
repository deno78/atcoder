# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
s = input()

# solve
ok=True
for i in range(1,9):
    x=i*2-1
    if s[x]!="0":
        print("No")
        exit()

print("Yes")
    
