n = int(input())

# 今の場所と時間
posT=0
posX=0
posY=0

ng = False
for i in range(n):
    txy = input('')
    t = int(txy.split(' ')[0])
    x = int(txy.split(' ')[1])
    y = int(txy.split(' ')[2])
    
    # pos-xyの距離を測る
    distance = abs(x-posX) + abs(y-posY)

    # 次の場所に到達できなければng
    if (t-posT)<distance:
        ng=True
        break
    # 次の場所に到達できるが、上手に止まれなければng
    if (t-posT - distance)%2 == 1:
        ng = True
        break

    # 次の目標地点を始点とする.
    posT=t
    posX=x
    posY=y
    
if ng:
    print('No')
else:
    print('Yes')
