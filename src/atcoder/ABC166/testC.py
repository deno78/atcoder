nm = input('')
n=int(nm.split(' ')[0])
m=int(nm.split(' ')[1])
hs = input('').split(' ')

abmap = {}
for i in range(m):
    ab = input('')
    a = int(ab.split(' ')[0])
    b = int(ab.split(' ')[1])
    if a in abmap.keys():
        abmap[a].append(b)
    else:
        abmap[a] = [b]
    if b in abmap.keys():
        abmap[b].append(a)
    else:
        abmap[b] = [a]

ytb_cnt=0
for a,b in abmap.items():
    ah = int(hs[a-1])
    ytb = 1
    for bn in b:
        bh = int(hs[bn-1])
#        print("{}[{}]->{}[{}]".format(a,ah,b,bh))
        if ah <= bh:
            ytb=0
    if ytb == 1:
        ytb_cnt+=1
for h in range(len(hs)):
    if not (h+1) in abmap.keys():
#        print("{} is no root".format(h+1))
        ytb_cnt+=1
print(ytb_cnt)