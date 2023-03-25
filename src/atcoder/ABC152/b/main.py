a,b=map(int,input().split())

l1=[]
for i in range(b):
    l1.append(str(a))
l2=[]
for i in range(a):
    l2.append(str(b))

s1="".join(l1)
s2="".join(l2)
print(min(s1,s2))