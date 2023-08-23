n=int(input())

a=[]
a.append(0)
a.append(0)
a.append(1)

MOD=10007

for i in range(3,n):
    a[i%3]=sum(a)%MOD
#    print("[{}]:{} / {}".format(i,a[i%3],a))

print(a[n%3-1]%MOD)