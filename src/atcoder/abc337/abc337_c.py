# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
alist = list(map(int, input().split()))

adict={}
top=-1
# solve
for i in range(n):
    a=alist[i]
    if a==-1:
        top=i+1
    else:
        adict[a]=i+1
# answer
ans=[]
ans.append(top)
while True:
    x=ans[-1]
    if x in adict.keys():
        ans.append(adict[x])
        x=adict[x]
    else:
        break
ans2=[]
for a in ans:
    ans2.append(str(a))
print(" ".join(ans2))
