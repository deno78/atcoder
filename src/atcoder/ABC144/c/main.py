
n=int(input())

ans=float('INF')
for i in range(1,int(n**0.5)+1):
    if n%i==0:
        j=n//i
        #print("[{} * {}] = {}".format(i,j,i+j-2))
        ans=min(i+j-2,ans)

print(ans)