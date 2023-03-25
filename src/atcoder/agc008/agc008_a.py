import sys
x,y=map(int,input().split())

if x==y:
    print(0)
    exit()

ans=abs(abs(x)-abs(y))

if x>0:
    if y>0:
        print("a",file=sys.stderr)
        if x>y:
            ans+=2
    elif y<0:
        print("b",file=sys.stderr)
        ans+=1
        if x<y:
            ans+=1
    elif y==0:
        ans+=1
elif x<0:
    if y>0:
        print("c",file=sys.stderr)
        if x<y:
            ans+=1
    elif y<0:
        if x>y:
            print("d1",file=sys.stderr)
            ans+=2
    elif y==0:
        pass
elif x==0:
    if y>0:
        print("z2",file=sys.stderr)
        pass
    elif y<0:
        print("z2",file=sys.stderr)
        ans+=1
    elif y==0:
        pass

print(ans)