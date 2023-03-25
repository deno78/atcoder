# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
alist=list(map(int,input().split()))
blist=[0]*n

# solve
for i in range(n):
    if blist[i]==0:
        a=alist[i]-1
        blist[a]=1

# answer
ans=[]
for i in range(n):
    b=blist[i]
    if b==0:
        ans.append(str(i+1))
print(len(ans))
print(" ".join(ans))
