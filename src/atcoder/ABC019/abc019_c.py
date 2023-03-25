n=int(input())

alist=set(map(int,input().split()))
c=0
s=set()
for a in alist:
    c+=1
    while a%2==0:
        a//=2
    s.add(a)
print(len(s))