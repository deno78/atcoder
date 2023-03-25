n,k=map(int,input().split())

while True:
    n=min(n,abs(n-k))
    if n-k <0:
        n=min(n,abs(n-k))
        break

print(n)