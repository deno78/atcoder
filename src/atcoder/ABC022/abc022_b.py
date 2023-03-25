n=int(input())
alist=set([])
cnt=0
for i in range(n):
    a=int(input())
    if a in alist:
        cnt+=1
    alist.add(a)
print(cnt)