# TODO edit the code

# param
a,b,k = map(int,input().split())

if a>=b:
    print(0)
    exit()

ans=0
# solve
while True:
    ans+=1
    a*=k
    if a>=b:
        print(ans)
        exit()
