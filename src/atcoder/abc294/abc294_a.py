n=int(input())
alist=list(map(int,input().split()))

ans=[]
for a in alist:
    if a%2==0:
        ans.append(str(a))

print(" ".join(ans))