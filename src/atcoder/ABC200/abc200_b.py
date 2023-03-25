nk=input().split()
n=int(nk[0])
k=int(nk[1])

for i in range(k):
    if n%200==0:
        n=n//200
    else:
        n=int(str(n)+"200")

print(n)