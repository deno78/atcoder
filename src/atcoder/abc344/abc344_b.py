# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
alist=[]
while True:
    a = int(input())
    alist.append(a)
    if a==0:
        break

# solve

# answer
for i in range(1,len(alist)+1):
    print(alist[-1*i])
