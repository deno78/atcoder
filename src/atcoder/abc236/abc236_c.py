# TODO edit the code

# param
n,m = map(int,input().split())

slist=input().split()
tlist=input().split()


# solve
ans = [False]*n

j=0
for i in range(n):
    if slist[i]==tlist[j]:
        ans[i] = True
        j+=1

# answer
for a in ans:
    if a==True:
        print('Yes')
    else:
        print('No')
