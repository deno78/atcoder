x,y=map(int,input().split())

ans=0
for i in range(1,7):
    for j in range(1,7):
        if i+j<x and abs(i-j)<y:
            ans+=1

print(1-ans/36)