nw = input('').split()
n = int(nw[0])
w = int(nw[1])

wmap = {}

for i in range(n):
    stp = input('').split()
    s=int(stp[0])
    t=int(stp[1])
    p=int(stp[2])
    if s not in wmap.keys():
        wmap[s] = 0
    if t not in wmap.keys():
        wmap[t] = 0
    
    wmap[s] += p
    wmap[t] += -1*p

wmap2 = sorted(wmap.items())
hm=0
for k,v in wmap2:
    hm += v
    #print("[{}]:{} -> {}".format(k,v,hm))
    if hm > w:
        print('No')
        exit(0)


print('Yes')