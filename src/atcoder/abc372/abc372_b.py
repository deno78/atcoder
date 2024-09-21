# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
m = int(input())

# solve
ans=[]
for i in range(21):
    x=1
    j=0
    while x<=m:
        x=3**j
        j+=1
    j-=2
    x=3**j
    ans.append(str(j))
    m-=3**j
#    print("j:{} ans:{} m:{} x:{}".format(j,ans,m,x))
    if m==0:
        break
# answer
print(len(ans))
print(" ".join(ans))
