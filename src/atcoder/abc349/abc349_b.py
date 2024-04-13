# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
s = input()

# solve
d={}
for c in s:
    if c not in d.keys():
        d[c]=0
    d[c]+=1

d2={}
for k,v in d.items():
    if v not in d2.keys():
        d2[v]=0
    d2[v]+=1

for k,v in d2.items():
    if v>0 and v!=2:
        print("No")
        exit()

# answer
print("Yes")
