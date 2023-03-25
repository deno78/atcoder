n = int(input(''))

# A,Bのインデクス＋値をそれぞれ作成して入力
amap = {}
bmap = {}
for i in range(n):
    ab = input('').split()
    amap[i] = int(ab[0])
    bmap[i] = int(ab[1])
c=0 # 現在日付=current

# bmapを納期順に並べる
bmap2 = sorted(bmap.items(),key=lambda x:x[1])

# 納期順に日付を進めていく
for i,b in bmap2:
    a=amap[i] # コストをamapから取得
    c+=a # 日付をコスト分進める
    print("limit:{} / current:{} [{}] cost:{} ".format(b,c,i,a))
    if c > b:
        print("No")
        exit(0)
print("Yes")