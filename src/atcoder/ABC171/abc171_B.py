nk = input('')
n = int(nk.split(' ')[0])
k = int(nk.split(' ')[1])

plist = list(map(int,input().split()))

plist.sort()

m=0
for i in range(k):
    m+=plist[i]

print(m)