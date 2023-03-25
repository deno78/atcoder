nk = input('')
n = int(nk.split(' ')[0])
k = int(nk.split(' ')[1])

sunukes = [0]*n
for i in range(k):
    d = int(input(''))
    a = input('').split(' ')
    for j in a:
        no = int(j)-1
        sunukes[no] = 1

cnt=0
for s in sunukes:
    if s == 0:
        cnt+=1
print(cnt)

