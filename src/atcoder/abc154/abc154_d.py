# TODO edit the code

# param
n,k = map(int,input().split())
p=list(map(int,input().split()))

# solve
a = sum(p[0:k])
ans=a
for i in range(n-k):
    a-=p[i]
    a+=p[k+i]
    ans=max(ans,a)

# answer
print((ans+k)/2)
