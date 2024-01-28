# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

def get_len(x,a,b):
    if (a<=x and x<b):
        return n-abs(a-b)
    else:
        return abs(a-b)


# param
n,m = map(int, input().split())
xlist=list(map(int,input().split()))

llist1=[]
llist2=[]

for i in range(m-1):
    x1=xlist[i]
    x2=xlist[i+1]
    l1=abs(x1-x2)
    l2=n-l1
    llist1.append(l1)
    llist2.append(l2)

# solve
ans=float("INF")
p1=min(xlist)
if p1 >1:
    p1-=1
p2=max(xlist)
if p2<n:
    p2+=1
for i in [p1,p2]:
    wk=0
    for j in range(m-1):
        x1=xlist[j]
        x2=xlist[j+1]
        l1=llist1[j]
        l2=llist2[j]
        in_x1_x2=(x1<=i and i <x2)
        if in_x1_x2:
            wk+=l2
        else:
            wk+=l1
#        print("({}:{})[{}] {}->{}".format(i,in_x1_x2,j,x1,x2))
    ans=min(ans,wk)

# answer
print(ans)

