import copy
hwk = input('')
h = int(hwk.split(' ')[0])
w = int(hwk.split(' ')[1])
k = int(hwk.split(' ')[2])

clist = []
for i in range(h):
    clist.append(input())

cnt_all=0
for i in range(2**(h+w)):
    bag=[]
    clist2 = []
    for line in clist:
        clist2.append(line)
    for j in range(h+w):
        if ((i>>j)&1):
            if j < h:                
                # 行を選ぶ方
                bag.append("Y:{}".format(j))
                clist2[j] = 'R'*w
            else:
                # 列を選ぶ方
                bag.append("X:{}".format(j-h))
                for i2 in range(h):
                    line = list(clist2[i2])
                    line[j-h] ='R'
                    clist2[i2] = "".join(line)
    cnt = 0
    for c in clist2:
        cnt+=c.count('#')
    if cnt==k:
#        print(clist2)
        cnt_all+=1

print(cnt_all)