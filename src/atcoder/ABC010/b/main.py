n=int(input())
alist=list(map(int,input().split()))

b=0
for a in alist:
    i=0
    for i in range(a):
        a2=a-i
        if a2%2!=0 and a2%3!=2:
            break
    b+=i
print(b)