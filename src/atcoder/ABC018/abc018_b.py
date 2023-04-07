s=list(input())
n=int(input())
lr=[]
for i in range(n):
    l,r=map(int,input().split())
    l-=1
    r-=1
    lr.append([l,r])

for l,r in lr:
    s1=s[0:l]
    s2=reversed(s[l:r+1])
    s3=s[r+1:]
    s1.extend(s2)
    s1.extend(s3)
    s=s1
#    print(s)

print("".join(s))