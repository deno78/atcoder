a,b=map(int,input().split())
x=b-a

y=0
for i in range(1,1000):
    y+=i
    if i==x:
        a2=y-x
        b2=y
        break

print(a2-a)