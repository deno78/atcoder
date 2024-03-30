# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
s = input()

# solve
ans = set([])
for i in range(len(s)):
    for j in range(i,len(s)+1):
        w=s[i:j]
        if len(w)>0:
            ans.add(w)
# answer
print(len(ans))