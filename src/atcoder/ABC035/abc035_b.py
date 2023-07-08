s=input()
t=input()

x=0
y=0
w=0
for i in range(len(s)):
    c=s[i]
    if c=="U":
        y+=1
    elif c=="D":
        y-=1
    elif c=="L":
        x-=1
    elif c=="R":
        x+=1
    elif c=="?":
        w+=1

b=abs(x)+abs(y)
if t=="1":
    print(b+w)
else:
    if (b-w)%2==0:
        print(max(b-w,0))
    else:
        print(max(b-w,1))
