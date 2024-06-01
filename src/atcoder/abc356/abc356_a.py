# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,l,r = map(int, input().split())
l-=1
r-=1

# solve
ans=[]
for i in range(n):
    ans.append(i+1)

ans1=ans[:l]
ans2=ans[l:r+1]
ans3=ans[r+1:]
ans2.reverse()
ans=[]
for a in ans1:
    ans.append(str(a))
for a in ans2:
    ans.append(str(a))
for a in ans3:
    ans.append(str(a))
# answer
print(" ".join(ans))