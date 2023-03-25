n=int(input())

l=[]
l.append(2)
l.append(1)
for i in range(2,90):
    l.append(l[i-1]+l[i-2])

print(l[n])