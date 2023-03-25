def get_a(a,ans):
    a2=t[a][0]
    if a2==-1:
        return ans
    else:
        ans.append(str(a2))
        get_a(a2,ans)
        return ans

def get_b(a,ans):
    a2=t[a][1]
    if a2==-1:
        return ans
    else:
        ans.append(str(a2))
        get_b(a2,ans)
        return ans

n,q=map(int,input().split())

t=[]
for i in range(n):
    t.append([-1,-1])

for i in range(q):
    l=input()
    if l.startswith("1"):
        o,x,y=map(int,l.split())
        t[x-1][1]=y-1
        t[y-1][0]=x-1
    elif l.startswith("2"):
        o,x,y=map(int,l.split())
        t[x-1][1]=-1
        t[y-1][0]=-1
    elif l.startswith("3"):
        o,x=map(int,l.split())
        a1=get_a(x-1,[])
        a2=get_b(x-1,[])
        print("#" +  " ".join(a1) + " " +str(x) + " " + " ".join(reversed(a2)))
