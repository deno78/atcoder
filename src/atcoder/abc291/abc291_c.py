# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
s = list(input())
x=0
y=0
# solve
hist={}
hist["0/0"]=1
for i in range(n):
    c=s[i]
    if c=="R":
        x+=1
    elif c=="L":
        x-=1
    elif c=="U":
        y+=1
    elif c=="D":
        y-=1
    key="{}/{}".format(x,y)
    if key in hist.keys():
        print("Yes")
        exit()
    hist[key]=1

print("No")
