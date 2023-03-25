a,b=map(int,input().split())
x=0
t=1
while t<b:
    x+=1
    t=t+(a-1)
print(x)