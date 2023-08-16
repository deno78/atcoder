x,y=map(int,input().split())

z = x
ans=0
while z <= y:
    ans+=1
    z=z*2

print(ans)