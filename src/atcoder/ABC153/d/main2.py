h=int(input())

cnt=0
m=1
while h>0:
#    print(m)
    cnt+=m
    m*=2
    h=h//2
print(cnt)