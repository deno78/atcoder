# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
s = input()

# solve
map={}
for c in s:
    if c not in map.keys():
        map[c]=0
    map[c]+=1

# answer
ans=[]
a=max(map.values())

for k,v in map.items():
    if v==a:
        ans.append(k)
ans.sort()

print(ans[0])