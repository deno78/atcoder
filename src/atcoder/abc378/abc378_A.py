# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
a = list(map(int, input().split()))
a.sort()

# solve
ans=0
d={}
for i in range(len(a)):
    if a[i] not in d.keys():
        d[a[i]]=0
    d[a[i]]+=1

for k,v in d.items():
    if v==2:
        ans+=1
    elif v==3:
        ans+=1
    elif v==4:
        ans+=2

# answer
print("{}".format(ans))
