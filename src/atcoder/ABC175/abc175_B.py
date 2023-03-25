
n = int(input(''))
l = list(map((int),input('').split()))

cnt=0
for i in range(n):
    for j in range(i,n):
        for k in range(j,n):
            l1 = l[i]
            l2 = l[j]
            l3 = l[k]
            if (l1 != l2 and l2 != l3 and l1 != l3) and (l1+l2 >l3 and l2+l3 > l1 and l1+l3 > l2):
               # print("{}[{}]/{}[{}]/{}[{}]".format(i,l1,j,l2,k,l3))
                cnt+=1
print(cnt)

            
