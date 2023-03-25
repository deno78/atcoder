a,b,c=map(int,input().split())

for i in range(a//c-1,b//c+1):
    x=c*i
    if x>=a and x<=b:
        print(x)
        exit()
print(-1)
