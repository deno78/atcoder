def chk(w,d):
    if d==n:
        print(w)
    else:
        for c in abc:
            chk(w+c,d+1)

n=int(input())

abc=["a","b","c"]

chk("",0)