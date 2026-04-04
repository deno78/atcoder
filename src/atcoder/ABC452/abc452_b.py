h,w=map(int,input().split())

for i in range(h):
    l=[]
    for j in range(w):
        if i==0 or i==h-1 or j==0 or j==w-1:
            l.append("#")
        else:
            l.append(".")
    print("".join(l))