# TODO edit the code

# param
n = int(input())
alist=list(map(int,input().split()))

# solve
ans = 0
for i in range(3000):
    if i not in alist:
        print(i)
        exit()

