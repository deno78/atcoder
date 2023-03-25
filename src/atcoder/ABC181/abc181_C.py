import itertools

n = int(input(''))

def check(xy1,xy2,xy3):
    ret = (
        ((xy1[0]-xy3[0])*(xy2[1] - xy3[1]))
         - 
        ((xy2[0]-xy3[0])*(xy1[1]-xy3[1]))
        ) / 2
#    print("1:{},2:{},3:{} ret:{}".format(xy1,xy2,xy3,ret))
    return ret

xylist=[]

for i in range(n):
    xy = input('').split()
    x = int(xy[0])
    y = int(xy[1])
    xylist.append([x,y])

alllist = list(itertools.combinations(xylist,3))

allNg = True
for combo in alllist:
    if check(combo[0],combo[1],combo[2]) == 0:
        print('Yes')
        allNg = False
        break
if allNg:
    print('No')

