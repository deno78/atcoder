# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
s = input()
t = input()

# solve
ok=0
ans=[]
for i in range(len(t)):
    if s[ok]==t[i]:
        ans.append(str(i+1))
        ok+=1

print(" ".join(ans))