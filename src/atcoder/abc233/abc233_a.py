# TODO edit the code

# param
x,y = map(int,input().split())

if (y-x)%10==0:
    print(max((y-x)//10,0))
else:
    print(max((y-x)//10+1,0))
