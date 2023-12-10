# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
k,g,m = map(int, input().split())
# solve
x=0
y=0
for i in range(k):
    if x==g:
        x=0
    elif y==0:
        y=m
    else:
        z=g-x
        if g >= x+y:
            x+=y
            y=0
        else:
            y-=z
            x=g
     
#    print("{} {}".format(x,y))
        
# answer
print("{} {}".format(x,y))
