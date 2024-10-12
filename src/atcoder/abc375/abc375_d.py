# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
s = input()

# solve
l=len(s)
ans = 0

wdict={}
for i in range(l):
    c=s[i]
    if c not in wdict.keys():
        wdict[c]=[]
    wdict[c].append(i)

for c in wdict.keys():
    if len(wdict[c])>1:
        w=wdict[c]
        for i in range(len(w)-1):
            for j in range(i+1,len(w)):
                ans+=(w[j]-w[i]-1)

# answer
print("{}".format(ans))
