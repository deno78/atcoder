lrd = input('')
l = int(lrd.split()[0])
r = int(lrd.split()[1])
d = int(lrd.split()[2])

cnt=0
for i in range(l,r+1):
    if i%d==0:
        cnt+=1

print(cnt)