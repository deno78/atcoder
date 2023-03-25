def check(a,n):
    b=2
    cnt=0
    while a**b <=n:
        ans.add(a**b)
        b+=1
    return cnt

n=int(input())
ans=set()
a=2
while a**2 <=n:
    check(a,n)
    a+=1
#print(ans)
print(n-len(ans))