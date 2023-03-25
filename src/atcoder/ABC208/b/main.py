import math
p=int(input())

flist=[]
for i in range(p):
    x = math.factorial(i)    
    if x > p:
        break
    else:
        flist.append(x)
#print(flist)
cnt=0
for x in reversed(flist):
    if p>=x:
        y=p//x
#        print("{} p:{} cnt:{}".format(x,p,cnt))
        p-=x*y
        cnt+=y

print(cnt)