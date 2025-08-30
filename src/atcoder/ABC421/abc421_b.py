def rev(i1):
    s1=reversed(list(str(i1)))
    return int("".join(s1))

x,y=map(int,input().split())

alist=[]
alist.append(x)
alist.append(y)
for i in range(2,10):
    a1=alist[i-2]
    a2=alist[i-1]
    a3=rev(a1+a2)
    alist.append(a3)

print(alist[-1])