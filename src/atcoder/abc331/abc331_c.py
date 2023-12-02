# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
alist = list(map(int, input().split()))

# solve
adict={}
alist2=sorted(alist)
w=0
s=sum(alist)
for i in range(n):
    a=alist2[i]
    if a not in adict.keys():
        adict[a]=s
    adict[a]-=a
    s-=a

# answer
ans=[]
for i in range(n):
    a=alist[i]
    ans.append(str(adict[a]))
print(" ".join(ans))
