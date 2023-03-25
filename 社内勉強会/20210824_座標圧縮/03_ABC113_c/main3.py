n,m=map(int,input().split())
pylist=[]
ydic1={} # 年→市の変換用辞書
for i in range(m):
    p,y=map(int,input().split())
    ydic1[y]=p
    pylist.append([p,y])






# 市毎にカウントアップするシーケンスを作っておく
seqlist=[1]*(n+1)
ydic2={} # 年→市毎の順番を保存する辞書
# 年毎にソートして調べていく
for y in sorted(ydic1.keys()):
    p=ydic1[y]
    ydic2[y]=seqlist[p]
    seqlist[p]+=1






# 値＆順位の連想配列を調べながら表示していく
for p,y in pylist:
    print("{:0>6}{:0>6}".format(p,ydic2[y]))
