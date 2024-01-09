# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,m = map(int, input().split())
alist=list(map(int,input().split()))
uv={}
for i in range(n):
    uv[i]=[]
for i in range(m):
    u,v=map(int,input().split())
    u-=1
    v-=1
    uv[u].append(v)
    uv[v].append(u)
# solve
ans=0
wk=[]
blist=[0]*n
blist[0]=alist[0]
wk.append([0,blist])
while len(wk)>0:
    w=wk.pop(0)
    u=w[0]
    blist=w[1]
    if u==n-1:
        bset=set(blist)
        bset.remove(0)  
#        print(bset)      
        ans=max(len(bset),ans)
    else:
        a=alist[u]
        for v in uv[u]:
#            print("{} -> {} ({}/{})".format(u,v2,a,alist[v2]))
            if alist[v]>=a and blist[v]==0:
                blist2=blist.copy()
                blist2[v]=alist[v]                
                wk.append([v,blist2])
#    print(wk)

# answer
print(ans)