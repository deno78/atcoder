h,w=map(int,input().split())

for i in range(h):
    wk=[]
    for j in range(w):
        a=4
        if i==h-1:
            a-=1
        if i==0:
            a-=1
        if j==0:
            a-=1
        if j==w-1:
            a-=1
        wk.append(str(a))
    print(" ".join(wk))
