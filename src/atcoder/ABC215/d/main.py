
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

n,m=map(int,input().split())
alist=list(map(int,input().split()))

dv1=set([])
for a in alist:
    dv2=make_divisors(a)
    dv1|=set(dv2)
ans=[0]*(m+1)
dv1.remove(1)
for d in dv1:
    for i in range(m//d+1):
        x=i*d
        if x<len(ans):
            ans[x]=1

del ans[0]
cnt=ans.count(0)
print(cnt)
for i in range(len(ans)):
    if ans[i]==0:
        print(i+1)
