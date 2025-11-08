n=int(input())
whb=[]
for i in range(n):
    w,h,b=map(int,input().split())
    whb.append((w,h,b))

if n==1:
    print(whb[0][2])
    exit()

def enumerate_patterns(whb, limit=None):
    stack = [(0, 0, 0, ())]
    yielded = 0
    while stack:
        i, hw, bw, sel = stack.pop()
        if i == n:
            yield sel
            yielded += 1
            if limit is not None and yielded >= limit:
                return
            continue
        w, h, b = whb[i]

        # 「選ばない」遷移は常に可能
        nbw = bw + w
        stack.append((i+1, hw, nbw, sel))

        # hw + w <= bw のときのみ「選ぶ」遷移を許可
        if hw + w <= bw:
            nhw = hw + w
            # 選択を末尾に追加した新しいタプルを生成してプッシュ
            stack.append((i+1, nhw, bw, sel + (i,)))

# 使用例: 最初の 100 パターンを出力（必要に応じて limit を変更）
for pat in enumerate_patterns(whb, limit=100):
    print(list(pat))

