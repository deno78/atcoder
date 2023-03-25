import math
alist=[]
for i in range(5):
    alist.append(int(input()))

a2=[]
a3=10
a4=-1
for a in alist:
    a2.append((math.ceil(a/10))*10)
    if a%10 < a3 and a%10>0:
        a3=a%10
        a4=a
#print("{} {}/{}".format(sum(a2),a3,a4))
print(sum(a2)-(10-a3))