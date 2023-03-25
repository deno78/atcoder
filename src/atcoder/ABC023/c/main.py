rck=input().split()
r=int(rck[0])
c=int(rck[1])
k=int(rck[2])
n=int(input())
rclist=[] # 飴リスト
rlist=[0]*r # 縦方向のどの位置に飴がいくつあるか 
clist=[0]*c # 横方向のどの位置に飴がいくつあるか

for i in range(n):
    xy=list(map(int,input().split()))
    x=xy[0]-1
    y=xy[1]-1
    # それぞれのカウンタに記録していく
    rclist.append([x,y])
    rlist[x]+=1
    clist[y]+=1

cnt=0 # 件数

# 縦方向の件数が分かったら、
# 横方向の件数を求めやすいように連想配列に変換
# ここで計算量は O(c)
cdic={}
for i in range(len(clist)):
    y=clist[i]
    if y not in cdic.keys():
        cdic[y]=0
    cdic[y]+=1

# 縦の飴がある列全件に対して、件数を索引にチェック
# ここで計算量は O(X)
for x in rlist:
    if k-x in cdic.keys():
        cnt+=cdic[k-x]

# 飴がある位置について、個別チェック
# ここで計算量は、O(n)
for x,y in rclist:
    # 飴がある位置の件数を求める
    ame=rlist[x]+clist[y]
    if ame==k:
        # 一致してたら足し過ぎ（実際は-1）なので引く
        cnt-=1
    if ame==k+1:
        # 1つ多ければ、先の全件チェックに引っかかっていなかったので足す
        cnt+=1
print(cnt)