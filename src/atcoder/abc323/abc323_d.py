# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1
import heapq

# param
n = int(input())
sc={}
keys=[]
for i in range(n):
    s,c = map(int, input().split())
    sc[s]=c
    keys.append(s)

# solve
ans=0
heapq.heapify(keys)

while len(keys)>0:
    s=heapq.heappop(keys)
    c=sc.pop(s)
    if c>1:
        s2=s*2
        if s2 not in sc.keys():
            sc[s2]=0
            heapq.heappush(keys,s2)
        sc[s2]+=c//2
    if c%2==1:
        ans+=1

# answer
print(ans)
