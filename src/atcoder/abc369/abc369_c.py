# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
alist = list(map(int, input().split()))

if n==1:
    print(1)
    exit()

# solve
d=alist[1]-alist[0]
l=0
r=1
ans=n
while l<n and r<n:
    if r+1<n and alist[r+1]==alist[r]+d:
        r+=1
        if r==n:
            x=(r-l)*(r-l+1)//2
            ans+=x
            break
    else:
        x=(r-l)*(r-l+1)//2
        ans+=x
#        print("{}-{} ({}) = {}".format(l+1,r+1,d,x))
        l=r
        r=l+1
        if l<n and r<n:
            d=alist[r]-alist[l]
        else:
            break

# answer
print("{}".format(ans))
