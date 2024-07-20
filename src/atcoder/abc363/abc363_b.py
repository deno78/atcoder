# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,t,p = map(int, input().split())
llist = list(map(int, input().split()))

# solve
c=0
ans=0
for i in range(n):
    if llist[i]>=t:
        c+=1

while c<p:
    c=0
    for i in range(n):
        llist[i]+=1
        if llist[i]>=t:
            c+=1
    ans+=1
# answer
print("{}".format(ans))
