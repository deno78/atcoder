abck = input('')
a = int(abck.split(' ')[0])
b = int(abck.split(' ')[1])
c = int(abck.split(' ')[2])
k = int(abck.split(' ')[3])

cnt=0
left=k

#A
if a > k:
    left=0
    cnt=k
else:
    left=k-a
    cnt=a

if left>0:
    left-=b

if left>0:
    cnt-=left

print(cnt)

