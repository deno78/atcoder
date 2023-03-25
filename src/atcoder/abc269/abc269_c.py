n=int(input())

n2=list(bin(n)[2:])
n2.reverse()
a=[]
for i in range(len(n2)):
    x=n2[i]
    if x=="1":
        a.append(i)

ans=[]
for i in range(2**len(a)):
    x=0
    for j in range(len(a)):
        if((i>>j) &1):
#            print("[{}] ={}".format(a[j],2**a[j]))
            x+=2**a[j]
#    print("-----------")
    ans.append(x)

for x in ans:
    print(x)