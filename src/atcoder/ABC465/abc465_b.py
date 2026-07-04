x,y,l,r,a,b=map(int,input().split())

ans=0
for i in range(a,b):
    if l<=i and i<r:
        ans+=x
#        print(i,"#",ans)
    else:
        ans+=y
#        print(i,"$",ans)
    
print(ans)