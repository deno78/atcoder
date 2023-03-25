r=5
c=5
sx=0
sy=0

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
        # 座標を踏み外しておらず、未踏破であれば、
        if y2>=0 and x2>=0 and y2<r and x2<c and steps[y2][x2]==-1:
            # 歩数を進めて、次に調べるべき場所に追加する
            steps[y2][x2]=d+1
            pos.append([y2,x2])
    print("----------------------------")
    for row in steps:
        print(row)

