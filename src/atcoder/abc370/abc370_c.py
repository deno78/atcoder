# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
s = input()
t = input()

# solve
ans=[]
while s!=t:
    wk1=[]
    wk2={}
    for j in range(len(s)):
        if s[j]!=t[j]:
            w=s[:j]+t[j:]
            wk1.append(w)
            wk2[w]=j
    wk1.sort()
    w2=wk1.pop(0)
    idx=wk2[w2]
    s=s[:idx]+t[idx]+s[idx+1:]
    ans.append(s)
    if s==t:
        break

# answer
print(len(ans))
for a in ans:
    print(a)
