import math
n = input()
ni = int(n)
l=math.floor(len(n)/2)
l2=math.ceil(len(n)/2)

if len(n)==1:
    print(0)
    exit(0)

n1=int(n[:l])
n2=int(n[l:])
if n2 ==0:
    n1=n1-1
    n2=int('1' + n[l:])-1
n3=int(n[:l2])
n4=int(n[l2:])
if n4 ==0:
    n3=n3-1
    n4=int('1' + n[l2:])-1

#print("{} -> {} / {} ->{}".format(n,n1,n2,max(n1,n2)))
#print("{} -> {} / {} ->{}".format(n,n3,n4,max(n3,n4)))

cnt=0
for i in range(1,max(n1,n2,n3,n4)+1):
    x = int(str(i) + str(i))
    if x<=ni:
#        print(x)
        cnt=cnt+1

print(cnt)