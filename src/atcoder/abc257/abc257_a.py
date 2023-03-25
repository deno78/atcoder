# TODO edit the code

# param
n,x=map(int,input().split())

# solve
ans=[]
abc=list("abcdefghijklmnopqrstuvwxyz")
for a in abc:
    for i in range(n):
        ans.append(a)

# answer
print(ans[x-1].upper())
