def binary_search_find_closest(data, target):
    left=0
    right=len(data)
    mid=(left+right)//2
    while right-left>1:
        mid=(left+right)//2
        mid_val=data[mid]
        if target >= mid_val:
            left=mid
        else:
            right=mid
    return right

l,q=map(int,input().split())

xlist=[]
xlist.append(0)
ans=[]
for i in range(q):
    c,x=map(int,input().split())
    if c==1:
        idx=binary_search_find_closest(xlist,x)
        xlist.insert(idx,x)
    elif c==2:
        idx=binary_search_find_closest(xlist,x)
        if idx==len(xlist) and idx>0:
            x1=xlist[0]
        else:
            x1=xlist[idx-1]
        if idx>len(xlist)-1:
            x2=l
        else:
            x2=xlist[idx]
        print("chk:{}/{}".format(x2,x1))
        print(xlist)
        ans.append(x2-x1)

print(ans) 
for a in ans:
    print(a)
