n=int(input())
alist=list(map(int,input().split()))

total=n*n/2
nmap={}

for a in alist:
    if a not in nmap.keys():
        nmap[a]=0
    nmap[a]+=1

for k,v in nmap.items():
    total-= v*v/2
print(int(total))
