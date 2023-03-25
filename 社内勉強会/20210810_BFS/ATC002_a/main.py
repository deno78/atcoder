# 入力値受取
r,c=map(int,input().split())
sy,sx=map(int,input().split())
gy,gx=map(int,input().split())
# 索引として使いやすいように1引いておく
sy-=1 
sx-=1
gy-=1
gx-=1

# 
map=[]
for i in range(r):
    map.append(list(input()))

steps=[]
for i in range(r):
    steps.append([-1]*c)

# 開始位置を設定
steps[sy][sx]=0
pos=list()
pos.append([sy,sx])

# 全部の場所を踏むまでループ
while len(pos)>0:
    # キューの先頭を取り出す
    y,x=pos.pop(0)
    d=steps[y][x]
    # 上下左右を調べる
    for dx,dy in [[-1,0],[1,0],[0,-1],[0,1]]:
        x2=x+dx
        y2=y+dy
        # 座標を踏み外しておらず、壁でなく、未踏破であれば、
        if y2>0 and x2>0 and y2<r and x2<c and map[y2][x2]=="." and steps[y2][x2]==-1:
            # 歩数を進めて、次に調べるべき場所とする
            steps[y2][x2]=d+1
            pos.append([y2,x2])
    print("----------------------------")
    for row in steps:
        print(str(row).replace("-1","#"))

print(steps[gy][gx])