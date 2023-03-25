nk = input('')
n = int(nk.split(' ')[0])
k = int(nk.split(' ')[1])

alist = input('').split(' ')
alist2 = []

next=1
loop_end=0
alist2.append(1)
for i in range(len(alist)):
    next = int(alist[next-1])
    if next in alist2:
        loop_end=next
        break
    else:
        alist2.append(next)

head_size=alist2.index(loop_end)
loop_size=len(alist2) - head_size

k2=(k-head_size)%loop_size+head_size
#print(alist2)
#print(k2)
pos=alist2[k2]

print(pos)
