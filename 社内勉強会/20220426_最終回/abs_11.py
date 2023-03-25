n=int(input())
px=0
py=0
pt=0

for i in range(n):
    t,x,y=map(int,input().split())
    d=abs(px-x) + abs(py-y)
    if (t-pt)<d or (d-(t-pt))%2==1:
        print("No")
        exit()
    pt=t
    px=x
    py=y
print("Yes")