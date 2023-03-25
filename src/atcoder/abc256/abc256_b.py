# TODO edit the code

# param
n = int(input())
alist=list(map(int,input().split()))

p=0
rlist=[0]*4
# solve
for i in range(n):
    rlist[0]=1
    for j in reversed(range(len(rlist))):
        if rlist[j]==1 and j+alist[i]>3:
            p+=1
            rlist[j]=0
        elif rlist[j]==1 and j+alist[i]<=3:
            rlist[j]=0
            rlist[j+alist[i]]=1

# answer
print(p)
