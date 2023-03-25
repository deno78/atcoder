n=int(input())

alist=[]


for i in range(n):
    alist.append(int(input()))




# 元リストを重複排除してソートしたリストを作る
aset=list(set(alist))
aset.sort()



# ソート済み＆重複排除したリストに順位を付けて値＆順位の連想配列に格納
adic={}
for i in range(len(aset)):
    key=aset[i]
    adic[key]=i




# 値＆順位の連想配列を調べながら表示していく
for a in alist:
    print(adic[a])
