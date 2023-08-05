# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
p=list(map(int,input().split()))

if len(p)==1:
    print(0)
else:
    print(max(0,max(p[1:])-p[0]+1))