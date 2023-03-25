# 深さ優先探索（DFS）を使う

# 再帰呼び出しする走査関数
# s : 検索対象の文字列
# n : 判定するしきい値
def check(s,n):
    print("{}+ -> start.".format(s))
    cnt=0
    # 引数の文字列に 3,5,7のいずれかを順にくっつける
    for c in ['3','5','7']:
        s2 = s+c
        # 結合した後の数字がしきい値より小さいか判定
        if int(s2) <= n:
            # 753数判定
            if '3' in s2 and '5' in s2 and '7' in s2:
                cnt+=1 # 条件を満たしていたらカウントアップ
                print("\t[{}] {} OK".format(cnt,s2))
            # しきい値より小さいなら、その文字列に対して更に深堀りしていく。
            cnt+=check(s2,n)
    print("{}+ -> end [{}]".format(s,cnt))
    return cnt


n = int(input(''))
cnt=check('',n)
print(cnt)
