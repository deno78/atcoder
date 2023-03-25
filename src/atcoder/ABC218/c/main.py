n=int(input())
smap=[]
tmap=[]
for i in range(n):
    smap.append(input())
for i in range(n):
    tmap.append(input())

spoints=[]
for i in range(n):
    for j in range(n):
        if smap[i][j]=="#":
            spoints.append([i,j])
tpoints=[]
for i in range(n):
    for j in range(n):
        if tmap[i][j]=="#":
            tpoints.append([i,j])

sminx=n
sminy=n
tminx=n
tminy=n
for sp in spoints:
    sminy=min(sminy,sp[0])
    sminx=min(sminx,sp[1])
for tp in tpoints:
    tminy=min(tminy,tp[0])
    tminx=min(tminx,tp[1])
print("{}/{} {}/{}".format(sminy,sminx,tminy,tminx))
print("--------------")
for i in range(n-sminy):
    print(smap[i+sminy][sminx:])
print("--------------")
for i in range(n-tminy):
    print(tmap[i+tminy][tminx:])

ok=True
for i in range(n):
    for j in range(n):
        if i+sminy<n and j+tminy<n and j+sminx<n and i+tminx<n:
            print("[{}/{}] s:{} t:{}".format(i,j,smap[i+sminy][j+sminx],tmap[j+tminy][i+tminx]))
            if smap[i+sminy][j+sminx]!=tmap[j+tminy][i+tminx]:            
                ok=False

if ok:
    print('Yes')
else:
    print('No')