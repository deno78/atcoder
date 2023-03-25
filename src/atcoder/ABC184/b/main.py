n,x=map(int,input().split())
s=input()

for c in list(s):
    if c=='o':
        x+=1
    elif c=='x':
        x-=1
        x=max(x,0)

print(x)
