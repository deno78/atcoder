n=int(input())
xy=[]
for i in range(n):
    xy.append(list(map(int,input().split())))

d1=[]
d2=[]
d3=[]
for i in range(n):
    for j in range(n):
        if i!=j:
            xy1=xy[i]
            xy2=xy[j]
            if xy1[0]==xy2[0]:
                d3.append(0)
            elif xy1[1]==xy2[1]:
                d3.append(1)
            else:
                d1.append((xy1[1]-xy2[1])/(xy1[0]-xy2[0]))
                d2.append((xy2[1]-xy1[1])/(xy2[0]-xy1[0]))

d1=list(set(d1))
d2=list(set(d2))
d3=list(set(d3))
#print(d1)
#print(d2)
#print(d3)
print(len(d1)+len(d2)+len(d3)*2)
