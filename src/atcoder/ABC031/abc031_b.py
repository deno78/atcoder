l,h=map(int,input().split())
n=int(input())
alist=[]
for i in range(n):
    alist.append(int(input()))

for a in alist:
    if a>h:
        print(-1)
    else:
        if a<=l:
            print(l-a)
        else:
            print(0)
