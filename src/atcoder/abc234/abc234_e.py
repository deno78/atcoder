def check(alist,d):
    t=alist[0]
    w=[]
    w.append(t)
    for i in range(1,len(alist)):
        t+=d
        w.append(t)
        print(w)
        if alist[i]>=t:
            return False
        if t>10 or t<0:
            return False
    print(w)
    return True


# param
x = int(input())
xlist=list(map(int,list(str(x))))

d=10
x1=xlist[0]
xlist.pop(0)
x=x1
ok=False
for a in range(x1,10):
    xlist.insert(0,a)
    for d in range(-9,10):
        print("[{}]:[{}]".format(a,d))
        if check(xlist,d) == True:
            x=a
            ok=True
            break
    if ok==True:
        print("{} {}".format(a,d))
        break
    xlist.pop(0)

ans=[]
ans.append(x)
for i in range(1,len(xlist)):
    x+=d
    ans.append(x)

s=""
for a in ans:
    s+=str(a)
print(s)