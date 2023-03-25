s=input()

m={"S":0,"N":0,"E":0,"W":0}

for c in s:
    m[c]+=1

for k,v in m.items():
    m[k]=min(v,1)

x=m["E"]-m["W"]
y=m["N"]-m["S"]

if x==0 and y==0:
    print('Yes')
else:
    print('No')

