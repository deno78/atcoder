x,y,z=map(int,input().split())

if x*y<0:
    print(abs(x))
else:
    if abs(x) < abs(y):
        print(abs(x))
    else:
        if z*y < 0:
            print(abs(x)+abs(z)*2)
        else:
            if abs(z) > abs(y):
                print(-1)
            else:
                print(abs(x))
