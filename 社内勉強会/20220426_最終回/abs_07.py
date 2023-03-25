n=int(input())
alist=list(map(int,input().split()))
a=0
b=0
alist.sort()


for i in range(n):
    if i%2==0:
        a+=alist.pop(-1)
    else:
        b+=alist.pop(-1)
print(a-b)