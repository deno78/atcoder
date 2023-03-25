def check(xlist,n1,n2,c):
    x1=xlist[n1][c]
    x2=xlist[n2][c]
    if x1=='G':
        if x2=='G':
            return 0
        elif x2=='C':
            return 1
        elif x2=='P':
            return -1
    elif x1=='C':
        if x2=='G':
            return -1
        elif x2=='C':
            return 0
        elif x2=='P':
            return 1
    elif x1=='P':
        if x2=='G':
            return 1
        elif x2=='C':
            return -1
        elif x2=='P':
            return 0
            
n,m=map(int,input().split())
alist=[]
adic={}
for i in range(n*2):
    alist.append(list(input()))
    adic[i]=0

for i in range(m):
    wdic={}
    for a,w in adic.items():
        if w not in wdic.keys():
            wdic[w]=[]
        wdic[w].append(a)
    for alist2 in wdic.values():
        alist2.sort()
        for j in range(len(alist2)//2):
            a1=alist2[j*2]
            a2=alist2[j*2+1]
            result=check(alist,a1,a2,i)
            if result==1:
                if a1 not in adic.keys():
                    adic[a1]=0
                adic[a1]+=1
            elif result==-1:
                if a2 not in adic.keys():
                    adic[a2]=0
                adic[a2]+=1

wdic2={}
for a,w in adic.items():
    if w not in wdic2.keys():
        wdic2[w]=[]
    wdic2[w].append(a)
wlist=sorted(wdic2.keys(),reverse=True)
for w in wlist:
    alist2=wdic2[w]
    alist2.sort()
    for a in alist2:
        print(a+1)