# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
s = input()

# solve
ans=-1
for i in reversed(range(len(s)+1)):
    for j in range(len(s)-i+1):
        s2=s[j:j+i]
        ok=True
        for k in range(len(s2)//2):
            if s2[k]!=s2[-1*(k+1)]:
                ok=False
                break
        if ok:
            ans=max(ans,len(s2))

# answer
print(ans)