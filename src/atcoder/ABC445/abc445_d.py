H,W,N=map(int,input().split())
hw=[]
wdict={}
hdict={}

h_start=-1
w_start=-1
for i in range(N):
    a,b=map(int,input().split())
    hw.append((a,b))
    if a not in hdict.keys():
        hdict[a]=[]
    hdict[a].append(i)
    if b not in wdict.keys():
        wdict[b]=[]
    wdict[b].append(i)
    if a==H:
        h_start=i
    if b==W:
        w_start=i

wk=[]
wk.append([0,0])
ans=[]
while len(wk)>0:
    x,y=wk.pop(0)
    ans.append([x+1,y+1])
    a=H-y
    b=W-x
    if a in hdict.keys() and len(hdict[a])>0:
        next_index=hdict[a].pop(0)
        next_hw=hw[next_index]
        wdict[next_hw[1]].remove(next_index)
        wk.append([x+next_hw[1],y])
    elif b in wdict.keys() and len(wdict[b])>0:
        next_index=wdict[b].pop(0)
        next_hw=hw[next_index]
        hdict[next_hw[0]].remove(next_index)
        wk.append([x,y+next_hw[0]])

for i in range(len(ans)-1):
    print(ans[i][0],ans[i][1])