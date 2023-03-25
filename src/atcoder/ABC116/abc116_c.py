# 貪欲法
# 出来る限り広い範囲で水やりを試行していき回数を求める。

n=int(input())
hlist=list(map(int,input().split()))

# 試行回数
cnt=0

# 目標達成するまで無限ループ
while max(hlist)>0:
    cnt=cnt+1
    l=0 # 左端のデフォルト値は0
    # 左端から1以上の部分＝水やり必要な場所を求める
    for i in range(len(hlist)):
        if hlist[i]>0:
            l=i
            break

    r=len(hlist) # 右端のデフォルト値は列末
    # 左端から列末に向けて0を探す
    if 0 in hlist[l:]:
        r = hlist.index(0,l)

    # 水やりして、リストを更新する
    for i in range(l,r):
        hlist[i]=hlist[i]-1
    print("[{}-{}] {}".format(l,r,hlist))

print(cnt)
