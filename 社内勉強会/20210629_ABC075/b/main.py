hw=input().split()
h=int(hw[0])
w=int(hw[1])

slist=[]
for i in range(h):
    slist.append(list(input()))

# 各マス[i,j]について調べる
for i in range(h):
    for j in range(w):
        # 対象のマスが爆弾でなければ調査
        if slist[i][j]!= '#':
            c=0 # 爆弾の数
            # 周囲8マスを調べる
            for k in range(9):
                x=k%3-1+i # 横方向に調べる座標
                y=k//3-1+j # 縦方向に調べる座標
                #print("{}/{} -> {}/{}".format(i,j,x,y))
                # 調べる座標が0～h/wで、対象のマスが爆弾だったらカウントアップ
                if x>=0 and y>=0 and x<h and y<w and slist[x][y]=='#':
                    c+=1
            # 集計結果をマスに設定
            slist[i][j]=str(c)
            #print("### {}/{} ->{}".format(i,j,c))

for s in slist:
    print("".join(s))
