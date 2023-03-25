x=int(input())

u=[1000,5]
m=[500,5]
h=0
for i in range(len(m)):
    c=x//m[i]
    h+=u[i]*c
    x-=c*m[i]
print(h)