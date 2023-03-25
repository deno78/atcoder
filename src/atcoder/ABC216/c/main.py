n=int(input())

a=0
alist=[]
if n%2==1:
    alist.append('A')
    n-=1
for i in range(120):
    if n%2==0:
        n=n//2
        alist.append('B')
    else:
        n-=1
        alist.append('A')
    if n==0:
        break

print("".join(reversed(alist)))