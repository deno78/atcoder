n,y=map(int,input().split())

a=y//10000
for i in reversed(range(a+1)):
    b=(y-i*10000)//5000
    for j in reversed(range(b+1)):
        k=n-i-j
        if (i*10000+j*5000+k*1000)==y and k>=0:
            print("{} {} {}".format(i,j,k))
            exit()

print("-1 -1 -1")