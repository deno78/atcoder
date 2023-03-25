# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
alist = list(map(int, input().split()))
alist.sort()

# solve

ans=[]
for i in range(n+1):
    ans.append([0,0])
rest=0
for i in range(n):
    a=alist[i]
    if a < len(ans):
        if ans[a][0]==1:
            rest+=1
        else:
            ans[a][0]=1
    else:
        rest+=1            

print(rest)
for i in range(1,n+1):
    print(ans)
    if ans[i][0]==0:
        ans[i][1]=ans[i-1][1]
        rest-=2
        if rest<0:
            print(i-1)
            exit()
    else:
        rest-=1
