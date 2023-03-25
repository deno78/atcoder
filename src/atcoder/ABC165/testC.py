nmq = input('')
n=int(nmq.split(' ')[0])
m=int(nmq.split(' ')[1])
q=int(nmq.split(' ')[2])

abcdlist=[]

for i in range(q):
    abcd=input('')
    abcdlist.append(abcd.split(' '))

mx=0

astr=''
for i in range(n):
    astr+='9'

for i in range(int(astr)):
    dx=0
    alist=[]
    for j in range(n):
        alist.append(int(str(i).zfill(n)[j])+1)
    for abcd in abcdlist:
        a=int(abcd[0])
        b=int(abcd[1])
        c=int(abcd[2])
        d=int(abcd[3])
        if alist[b-1]==alist[a-1]+c:
            dx+=d
    if dx > mx:
        mx=dx
print(mx)
