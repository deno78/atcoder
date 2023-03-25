def check(x,y,w,h,c,slist):
    print("{}/{} is ok".format(x,y))
    slist[x][y]= c
    if x>0 and slist[x-1][y] == '.':
        slist[x-1][y] = c
        check(x-1,y,w,h,c,slist)
    if x<w-1 and slist[x+1][y] == '.':
        slist[x+1][y] = c
        check(x+1,y,w,h,c,slist)
    if y>0 and slist[x][y-1] == '.':
        slist[x][y-1] = c
        check(x,y-1,w,h,c,slist)
    if y<h-1 and slist[x][y+1] == '.':
        slist[x][y+1] = c
        check(x,y-1,w,h,c,slist)
    if x>0 and y>0 and slist[x-1][y-1] == '.':
        slist[x-1][y-1] = c+1
        check(x-1,y-1,w,h,c+1,slist)
    if x<w-1 and y>0 and slist[x+1][y-1] == '.':
        slist[x+1][y-1] = c+1
        check(x+1,y-1,w,h,c+1,slist)
    if x>w-1 and y>w-1 and slist[x+1][y+1] == '.':
        slist[x+1][y+1] = c+1
        check(x+1,y+1,w,h,c+1,slist)
    if x>0 and y<h-1 and slist[x-1][y+1] == '.':
        slist[x-1][y+1] = c+1
        check(x-1,y+1,w,h,c+1,slist)

hw = input('').split()
h = int(hw[0])
w = int(hw[1])

chw = input('').split()
ch = int(chw[0])
cw = int(chw[1])

dhw = input('').split()
dh = int(dhw[0])
dw = int(dhw[1])

slist=[]
for i in range(h):
    wlist=[]
    line = input('')
    for j in range(w):
        wlist.append(line[j])
    slist.append(wlist)

check(ch-1,cw-1,w,h,0,slist)


