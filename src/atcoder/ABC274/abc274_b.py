h,w=map(int,input().split())

c=[]
for i in range(h):
    c.append(list(input()))

ans=[]
for i in range(w):
    a=0
    for j in range(h):
        if c[j][i]=="#":
            a+=1
    ans.append(str(a))

print(" ".join(ans))