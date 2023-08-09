n=int(input())
alist=[]
for i in range(n):
    alist.append(int(input()))

alist=list(set(alist))
alist.sort()
print(alist[-2])
