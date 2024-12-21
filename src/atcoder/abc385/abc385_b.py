# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
h,w,x,y = map(int, input().split())
smap=[]
for i in range(h):
    smap.append(list(input()))
t=input()

x-=1
y-=1

# solve
ans=0
for i in range(len(t)):
    c=t[i]
    x2=x
    y2=y
    if c=="U":
        x2-=1
    elif c=="D":
        x2+=1
    elif c=="L":
        y2-=1
    elif c=="R":
        y2+=1
    if 0>y2 or y2>=w or 0>x2 or x2>=h or smap[x2][y2]=="#":
        x2=x
        y2=y
    if smap[x2][y2]=="@":
        smap[x2][y2]="."
        ans+=1
    x=x2
    y=y2
#    print("[{}] {} {}".format(c,x,y))


# answer
print("{} {} {}".format(x+1,y+1,ans))
