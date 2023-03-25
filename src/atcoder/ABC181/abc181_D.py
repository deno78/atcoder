s = input('')

alist = []
for i in range(13,126):
    s2 = str(8*i)
    if '0' not in s2:
        s2map = {}
        for j in range(0,10):
            s2map[str(j)] = s2.count(str(j))
#        print("[{}]:{}".format(s2,s2map))
        alist.append(s2map)

allNg = True
smap = {}
for j in range(0,10):
    smap[str(j)] = s.count(str(j))

for a in alist:
    ok = True
    for k,v in a.items():
        v2 = smap[k]
        if v2 < v:
            ok = False
    if ok == True:
#        print(a)
        print('Yes')
        allNg = False
        break

if allNg:
    if int(s)%8==0:
        print('Yes')
    else:
        print('No')