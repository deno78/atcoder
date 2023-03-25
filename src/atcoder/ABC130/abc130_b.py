n,x=map(int,input().split())
llist=list(map(int,input().split()))

for i in range(n):
    x-=llist[i]
    if x<0:
        print(i+1)
        exit()

print(n+1)