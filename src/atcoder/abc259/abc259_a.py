# TODO edit the code

# param

n,m,x,t,d=map(int,input().split())

# solve
if m >= x:
    ans=t
else:
    ans=t-(x-m)*d

# answer
print(ans)
