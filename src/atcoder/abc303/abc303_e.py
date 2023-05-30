# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
uv={}
for i in range(n):
    uv[i]=[]

for i in range(n-1):
    u,v = map(int, input().split())
    u-=1
    v-=1
    uv[u].append(v)
    uv[v].append(u)

groups=[]
groups2=[]

for u,v in uv.items():
    if len(v)==2:
        groups2.append(len(v))
    elif len(v)>2:
        groups.append(len(v))
# solve
ans=[]
for i in range((len(groups2)-(len(groups)+1))//2):
    ans.append(2)

for a in groups:
    ans.append(a)

ans.sort()

ans2=[]
for a in ans:
    ans2.append(str(a))

# answer
print(" ".join(ans2))