# TODO edit the code

# param
n,q = map(int,input().split())
alist=list(map(int,input().split()))
qlist=[]
for _ in range(q):
    qlist.append(list(map(int,input().split())))

# 数字毎の出現位置リストを連想配列で作っておく
ndic={}
for i in range(n):
    a=alist[i]
    if a not in ndic.keys():
        ndic[a]=[]
    ndic[a].append(i)

# solve
for x,k in qlist:
    if x in ndic.keys():
        # 連想配列から出現位置リストを取り出し
        nlist=ndic[x]
        if k<len(nlist)+1:
            # リストから出現位置を取り出して表示
            y=nlist[k-1]
            print(y+1)
        else:
            # k回以上でてこなかったら-1
            print(-1)
    else:
        # 1回も出てきていなければ-1を表示
        print(-1)
