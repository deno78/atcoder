# TODO edit the code

# param
n = int(input())
t=input()

N=0
E=1
S=2
W=3

x=0
y=0
r=E
# solve
for c in t:
    if c=='R':
        r=(r+1)%4
    else:
        if r==N:
            y+=1
        elif r==S:
            y-=1
        elif r==E:
            x+=1
        elif r==W:
            x-=1

# answer
print("{} {}".format(x,y))
