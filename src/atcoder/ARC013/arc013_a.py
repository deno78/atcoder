nml = list(map(int,input('').split()))
pqr = list(map(int,input('').split()))

def chk(a,b,c,x,y,z):
    a1 = int(a/x)
    b1 = int(b/y)
    c1 = int(c/z)
    ans = a1*b1*c1
    return ans

anslist=[]
anslist.append(chk(nml[0],nml[1],nml[2],pqr[0],pqr[1],pqr[2]))
anslist.append(chk(nml[0],nml[1],nml[2],pqr[0],pqr[2],pqr[1]))
anslist.append(chk(nml[0],nml[1],nml[2],pqr[1],pqr[2],pqr[0]))
anslist.append(chk(nml[0],nml[1],nml[2],pqr[1],pqr[0],pqr[2]))
anslist.append(chk(nml[0],nml[1],nml[2],pqr[2],pqr[0],pqr[1]))
anslist.append(chk(nml[0],nml[1],nml[2],pqr[2],pqr[1],pqr[0]))

print(max(anslist))
