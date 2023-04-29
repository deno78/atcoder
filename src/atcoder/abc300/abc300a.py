n,a,b=map(int,input().split())
clist=list(map(int,input().split()))

for i in range(n):
    if clist[i]== a+b:
        print(i+1)
        exit()

