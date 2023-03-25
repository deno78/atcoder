import math
n=int(input())
xy1=input().split()
xy2=input().split()
x1=int(xy1[0])
y1=int(xy1[1])
x2=int(xy2[0])
y2=int(xy2[1])
xc=(x1+x2)/2
yc=(y1+y2)/2

# 1つの頂点を移動するときの中心から移動する角度を求める（ラジアン）
rad=math.radians(360/n)
# 始点が中心の直上
rad1=math.radians(90)
# 始点が中心の直下
if yc < y1:
    rad1=math.radians(270)
# 始点が中心の直下／直上以外の場合はatanで中心から始点角度を求める
if xc-x1!=0:
    # ※atanだと、-90～+90度の範囲しか求められないので、atan2を使う
    rad1=math.atan2(yc-y1,xc-x1)

# 中心から第2点の角度を求める
rad2=rad1+rad

# 中心から始点の距離＝半径を求める
r=math.sqrt((xc-x1)**2 + (yc-y1)**2)

# 斜辺＝半径と、回転角から、第2点のx/y軸移動距離を求める
dx=int(math.cos(rad2)*r*100000)/100000
dy=int(math.sin(rad2)*r*100000)/100000

#print("{} {}".format(xc,yc))
#print("{} {}".format(dx,dy))
print("{} {}".format(xc-dx,yc-dy))
