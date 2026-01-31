n,t=map(int,input().split())
# nはalistの数、tは最終時間
alist=list(map(int,input().split()))

if n==0:
    print(t)
    exit()

ans=0

# 差分リストを作る
blist=[]
wk=0
for i in range(n):
    blist.append(alist[i]-wk)
    wk=alist[i]
# 最後の時間を調整
if t!=alist[-1]:
    blist.append(t-alist[-1])
print(blist)
stop=-1
for i in range(len(blist)):
    b=blist[i]
    if stop>0:
        # 停止中
        if b>stop:
            # そのターム中に起動する
            play=b-stop
            stop=0
            ans+=play
        else:
            # まだ停止中
            stop-=b
    elif stop==-1:
        # 起動直後
        play=b
        ans+=play
        stop=0
    else:
        # 停止から起動
        if b > 100:
            play = b - 100
            stop = 0
            ans += play
        else:
            play = 0
            stop = 100 - b
    print(i,b,stop,play,ans)

print(ans)