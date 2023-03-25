# shine
# stone

# 辞書ファイルを読み込む
dic=[]
with open('ejdict-hand-utf8.txt',mode='r',encoding='UTF-8') as f:
    dic=f.readlines()

# 出現順と重みづけのスコアファイルを読み込む
scores={}
with open('words.csv',mode='r',encoding='UTF-8') as f:
    for l in f.readlines():
        row=l.split(',')
        for i in range(5):
            c1=i*2
            c2=i*2+1
            c=row[c1]
            if c not in scores.keys():
                scores[c]=[]
            scores[c].append(int(row[c2]))

# 入力値をファイルから受け取ってリストに格納する
matches=[]
includes=[]
missed=[]
with open('input.txt',mode='r',encoding='UTF-8') as f:
    lines=f.readlines()
    matches=list(lines[0].strip())  # 1行目はマッチした文字列
    missed=list(lines[1].strip())   # 2行目は空振りした文字列
    for i in range(2,len(lines)):   # 3行目以降は黄色文字列
        l=lines[i].strip()
        if len(l)==5:
            includes.append(list(l))
ans={}  # 回答
for l in dic:
    # 辞書文字列を分解して調べていく
    w=l.split('\t')[0].split(',')[0].lower().replace("\n","")
    # 初期検査、5文字で、記号を含まないこと
    if len(w)==5 and '.' not in w and '-' not in w and '\''not in w:
        ok = True   # 検査OKフラグ
        for m in missed:    # 空振り文字列が含まれていれば除外
            if m in w:
                ok = False
        for i in range(5):  # マッチ文字列とマッチしなかったら除外
            if matches[i] != '-' and w[i]!=matches[i]:
                ok = False
        for i in range(5):  # 黄色文字列を1個づつ調べていく
            for inc in includes:
                # 黄色文字を一つでも含んでいるか検査
                if inc[i]!='-' and inc[i] not in w:
                    ok = False
                # 黄色文字列の位置が誤っていないか検査
                if inc[i]!='-' and inc[i] == w[i]:
                    ok = False
        if ok:
            # OKなら出現頻度から得点を更新して回答候補に追加
            ans[w]=0
            for i in range(5):
                if w[i] in scores.keys():
                    ans[w]+=scores[w[i]][i]

# 回答候補を得点順にソート
ans_sorted = sorted(ans.items(), key=lambda x:x[1],reverse=True)

# 候補からスコアのトップ10を表示
for i in range(min(10,len(ans_sorted))):
    print(ans_sorted[i])


