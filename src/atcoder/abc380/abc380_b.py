# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
s = input()

# solve
ans=[]
wk=0
for i in range(1,len(s)):
    c=s[i]
    if c=="-":
        wk+=1
    else:
        ans.append(str(wk))
        wk=0

# answer
print(" ".join(ans))