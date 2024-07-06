# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
a,b,c,d,e,f = map(int, input().split())
g,h,i,j,k,l = map(int, input().split())

# solve
x1=min(a,d)
y1=min(b,e)
z1=min(c,f)
x2=max(a,d)
y2=max(b,e)
z2=max(c,f)

for x in range(min(g,j),max(g,j)+1):
    for y in range(min(h,k),max(h,k)+1):
        for z in range(min(i,l),max(i,l)+1):
            if x1<x and x <x2 and y1<y and y<y2 and z1<z and z<z2:
                print("Yes")
                exit()

print("No")