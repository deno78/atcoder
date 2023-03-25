nw = input('').split()
n = int(nw[0])
w = int(nw[1])

wmap = {}

for i in range(n):
    stp = input('').split()
    s=int(stp[0])
    t=int(stp[1])
    p=int(stp[2])
    key = [s,t]
    wmap[key] = p
    for k,v in wmap.items():
        if (s > k[0] and s < k[1]) or (t > k[0] and t < k[1]):
            s2 = max(s,k[0])
            t2 = min(t,k[1])
            key2 = [s2,t2]
            p2 = p + v
            wmap[key2] = p2
            if p2 > w:
                print('No')
                exit(0)

print('Yes')