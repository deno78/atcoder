def chk(a,b,slist):
    s = slist[a][b]
#    print("[{},{}] ={}".format(a,b,s))
    if s == '#':
        return 0
    else:
        return 1

hwxy=list(map(int,input().split()))
h=hwxy[0]
w=hwxy[1]
x=hwxy[2]-1
y=hwxy[3]-1

slist=[]
xline = []
for i in range(h):
    s=input()
    slist.append(s)
    xline.append(s[y])

cnt=1
# left
#print('left')
for i in range(1,y+1):
    if chk(x,y-i,slist) ==0:
        break
    else:
        cnt+=1
# right
#print('right')
for i in range(1,w-y):
    if chk(x,y+i,slist) ==0:
        break
    else:
        cnt+=1
# up
#print('up')
for i in range(1,x+1):
    if chk(x-i,y,slist) ==0:
        break
    else:
        cnt+=1
# down
#print('down')
for i in range(1,h-x):
    if chk(x+i,y,slist) ==0:
        break
    else:
        cnt+=1

print(cnt)