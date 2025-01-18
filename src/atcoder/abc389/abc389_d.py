# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
r = int(input())

# solve
ans = 0
r2=r**2

x=0
sz=-1
for y in range(-1*r-1,1):
    ok=True
    if x**2+y**2<=r2:
        for dx,dy in [[0.5,0.5],[-0.5,0.5],[0.5,-0.5],[-0.5,-0.5]]:
            x2=x+dx
            y2=y+dy
            if x2**2+y2**2>r2:
                ok=False
                break
        if ok:
            sz=abs(y)
            break
if sz==-1:
    wk=0
else:
    wk=sz+1

wk=(wk-1)*2+1
print(wk)
print(r//2*(1+wk-2)*2)
ans+=wk
ans+=r//2*(1+wk-2)*2
#    print(wk)

# answer
print("{}".format(ans))

