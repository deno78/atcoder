n = int(input(''))
m = 0
alist = [0]*n
mcnt=0
for i in range(n):
    a = int(input(''))
    alist[i]=a
    if a > m:
        m = a
        mcnt=1
    if a==m:
        mcnt+=1

alist2 = sorted(alist)
for i in range(len(alist)):
    if alist[i] == m:
        print(alist2[-2])
    else:
        print(m)