n = int(input(''))
alist = list(map(int,input('').split()))

cnt=0
for i in range(1,n+1):
    if alist[i-1]%2!=0 and i%2!=0:
        cnt+=1


print(cnt)