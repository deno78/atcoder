n=int(input())
a=0
for i in range(1,n+1):
    if i%2==1:
        c=0
        for j in range(1,i+1):
            if i%j==0:
                c=c+1
        if c==8:
            a=a+1
print(a)