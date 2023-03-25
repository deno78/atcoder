n=int(input())
alist=list(map(int,input().split()))
x=int(input())

s=sum(alist)
d=x//s

t=d*s
for i in range(n):
    a=alist[i]
    t+=a
#    print("[{}] {} ->{} / {}".format(i,a,t,x))
    if t>x:
        print(i+1+(d*n))
        exit()

