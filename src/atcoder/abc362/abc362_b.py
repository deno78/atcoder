# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
xa,ya = map(int, input().split())
xb,yb = map(int, input().split())
xc,yc = map(int, input().split())

# solve
a=(xa-xb)**2+(ya-yb)**2
b=(xb-xc)**2+(yb-yc)**2
c=(xc-xa)**2+(yc-ya)**2

if max(a,b,c)==a:
    if a==b+c:
        print("Yes")
    else:
        print("No")
elif max(a,b,c)==b:
    if b==a+c:
        print("Yes")
    else:
        print("No")
elif max(a,b,c)==c:
    if c==b+a:
        print("Yes")
    else:
        print("No")

# answer
