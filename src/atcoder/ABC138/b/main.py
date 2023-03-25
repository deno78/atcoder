n=int(input())
alist=list(map(int,input().split()))

t=0
for i in range(n):
    t+=1/alist[i]

print(1/t)