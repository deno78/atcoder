# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,k = map(int, input().split())
alist=list(map(int,input().split()))
alist.sort()
alist=list(set(alist))

# solve
ans=-1
for i in range( min(k,len(alist))):
    if alist[i] != i:
        print(i)
        exit()

# answer
print(min(k,len(alist)))