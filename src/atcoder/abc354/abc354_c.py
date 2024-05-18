# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1
import bisect

# param
n = int(input())
cdict={}
clist=[]
for i in range(n):
    a, c = map(int, input().split())
    cdict[c]=[i,a]
    clist.append(c)

clist.sort()
ans=[]
min_a=-1
# solve
for i in range(n):
    c=clist[i]
    j,a=cdict[c]
#    print("[{}] c:{} a:{} min:{}".format(j,c,a,min_a))
    if min_a<a:
        ans.append(str(j+1))
    min_a=max(a,min_a)

ans.sort()

# answer
print(len(ans))
print(" ".join(ans))