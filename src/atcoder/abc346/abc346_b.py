# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
w,b = map(int, input().split())

# solve
a="wbwbwwbwbwbw"
for i in range((w+b)//len(a)+2):
    a+=a

for i in range(len(a)-(w+b)):
    wk=a[i:i+(w+b)]
    wc=wk.count("w")
    if wc==w:
        print("Yes")
        exit(0)
print("No")