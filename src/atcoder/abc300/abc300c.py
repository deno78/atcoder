def check(x,y,sz):
    for s in range(sz+1):
        if cmap[x+s][y+s]=="." or cmap[x-s][y+s]=="."  or cmap[x+s][y-s]=="."  or cmap[x-s][y-s]=="." :
            return False
    return True

h,w=map(int,input().split())

cmap=[]
for i in range(h):
    cmap.append(list(input()))

ans=[]
for sz in range(min(h,w)):
    ans.append(0)
for i in range(h):
    for j in range(w):
        for sz in reversed(range(1,min(h,w))):
            if i+sz<h and j+sz<w and cmap[i+sz][j+sz]=="#":
                ok=check(i,j,sz)
                if check(i,j,sz):
#                    print("{},{} {}".format(i,j,sz))
                    ans[sz-1]+=1
                    break

ans2=[]
for a in ans:
    ans2.append(str(a))

print(" ".join(ans2))