def ccw(ax, ay, bx, by, cx, cy):
    # 3点が反時計回りならTrue
    return (cy - ay) * (bx - ax) > (by - ay) * (cx - ax)

def is_intersect(a1, b1, a2, b2, c1, d1, c2, d2):
    # 線分(a1,b1)-(a2,b2)と(c1,d1)-(c2,d2)が交差するか判定
    return (ccw(a1, b1, c1, d1, c2, d2) != ccw(a2, b2, c1, d1, c2, d2)) and \
           (ccw(a1, b1, a2, b2, c1, d1) != ccw(a1, b1, a2, b2, c2, d2))


rt,ct,ra,ca=map(int,input().split())
n,m,l=map(int,input().split())
slist=[]
tlist=[]
seq=[]
u=0
for i in range(m):
    s,a=input().split()
    a=int(a)
    slist.append([s,a])
    u+=a
    seq.append(u)
u=0
for i in range(l):
    t,b=input().split()
    b=int(b)
    tlist.append([t,b])
    u+=b
    seq.append(u)

seq=sorted(list(set(seq)))
seq.insert(0,0)
ans=0
s,a=slist[0]
t,b=tlist[0]
d={"U":(-1,0),"D":(1,0),"R":(0,1),"L":(0,-1)}
idx1=0
idx2=0
for i in range(1,len(seq)):
    u=seq[i]
    mv=seq[i]-seq[i-1]
    a-=u
    b-=u
    if a<=0:
        s,a=slist[idx1]
        idx1+=1
    if b<=0:
        t,b=tlist[idx2]
        idx2+=1
    rt0=rt
    ct0=ct
    ra0=ra
    ca0=ca
    rt+=d[s][0]*mv
    ct+=d[s][1]*mv
    ra+=d[t][0]*mv
    ca+=d[t][1]*mv
#    print("[{}] {}({})({},{})->({},{}) {}({})({},{})->({},{})".format(u,s,a,rt0,ct0,rt,ct,t,b,ra0,ca0,ra,ca))
    if rt0==ra0 and ct0 == ca0 and s==t:
        ans+=mv
    else:
        if is_intersect(rt0,ct0,rt,ct,ra0,ca0,ra,ca):
            ans+=1
        elif rt==ra and ct==ca:
            ans+=1

print(ans)
