# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())

# solve
x=0
ans=-1
while True:
    k=x**3
    if k > n:
        break
    s=str(k)
    ok=True
    for i in range(len(s)//2):
        if s[i]!=s[-1*(i+1)]:
            ok=False
            break
    if ok:
        ans=k
    x+=1        
# answer
print(ans)