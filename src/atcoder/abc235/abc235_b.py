# TODO edit the code

# param
n = int(input())
hlist=list(map(int,input().split()))

ans=-1
for h in hlist:
    if h>ans:
        ans=h
    else:
        break


# answer
print(ans)
