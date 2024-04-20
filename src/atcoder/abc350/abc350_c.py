# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
alist = list(map(int, input().split()))
adict={}
for i in range(n):
    a=alist[i]
    adict[a]=i

# solve
ans=[]
for i in range(n):
    if alist[i]!=i+1:
        x=adict[i+1]
        v=alist[i]
        ans.append([i+1,x+1])
        alist[i]=i+1
        alist[x]=v
        adict[v]=x

# answer
print(len(ans))
for x,y in ans:
    print("{} {}".format(x,y))