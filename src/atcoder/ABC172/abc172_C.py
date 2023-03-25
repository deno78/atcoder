nmk = input('')
n = int(nmk.split(' ')[0])
m = int(nmk.split(' ')[1])
k = int(nmk.split(' ')[2])

alist = list(map(int,input().split()))
blist = list(map(int,input().split()))

l = (n+m)
t =k

max_read=0

for i in range(2**l):
    bag = ['A']*l
    bcount=0
    a=0
    b=0
    time=0
    read=0

    for j in range(l):
        if ((i>>j)&1):
            bag[l-1-j]='B'
            bcount+=1
            if bcount == m:
                break
    if bag.count('A')==n:
        for item in bag:
            t=0
            if item=='A':
                t = alist[a]
                a+=1
            else:
                t = blist[b]
                b+=1
            time+=t
            if k>=time:
                read+=1
            else:
                break
        if max_read < read:
            max_read = read
#        print("{} {}/{} {}".format(i,time,k,bag))

print(max_read)

