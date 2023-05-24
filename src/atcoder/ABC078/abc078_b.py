x,y,z=map(int,input().split())

if x%(y+z)==0 or x%(y+z)<z:
    print(x//(y+z)-1)
else:
    print(x//(y+z))
