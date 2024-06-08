# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

def paint(x,y,lv):
    if lv==1:
        blocksize=1
    else:
        blocksize=3**(lv-1)
    for i in range(9):
        dx=i%3*blocksize
        dy=i//3*blocksize
#        print("LV:{} dx:{} dy:{}".format(lv,dx,dy))
        if i==4:
            for j in range(blocksize):
                for k in range(blocksize):
                    grid[y+1+blocksize+j][x+1+blocksize+k]="."
        else:
            if lv==1:
                grid[y+dy][x+dx]="#"
            else:
                paint(x+dx,y+dy,lv-1)


# param
n = int(input())
if n==0:
    print("#")
    exit()

# solve
sz=3**n
grid=[]
for i in range(sz):
    grid.append(["."]*sz)

paint(0,0,n)

# answer
for i in range(sz):
    print("".join(grid[i]))