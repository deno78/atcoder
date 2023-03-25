rgbn=list(map(int,input().split()))
r=rgbn[0]
g=rgbn[1]
b=rgbn[2]
n=rgbn[3]

cnt=0
for i in range(0,n//r+1):
    n2=n-r*i
    for j in range(0,n2//g+1):
        n3=n2-j*g
        #print("{}:{}:{} ->{}".format(i,j,n3,n3%b))
        if n3%b==0:
            cnt+=1
print(cnt)