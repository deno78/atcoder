import sys

# 再帰上限を引き上げる（念のため）
sys.setrecursionlimit(200000)

def solve():
    # 入力を全て読み込む
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        T_str = next(iterator)
        if not T_str: return
        T = int(T_str)
    except StopIteration:
        return

    results = []

    for _ in range(T):
        try:
            N = int(next(iterator))
            rlist = []
            for _ in range(N):
                rlist.append(int(next(iterator)))
        except StopIteration:
            break

        if N == 0:
            results.append(0)
            continue
            
        # rlist[i] は入力された列iの駒の行番号
        # 操作後の行番号を x[i] とすると
        # 1. x[i] <= rlist[i] (上にしか動かせない)
        # 2. |x[i] - x[i+1]| <= 1 (隣接条件)
        # これを満たす最大の x[i] の和を求め、sum(rlist) - sum(x) が答え
        
        # 貪欲法（2パス）で解ける
        
        # 配列のコピーを作成して変更していく
        current_h = list(rlist)
        
        # 左から右へのパス: x[i] <= x[i-1] + 1
        for i in range(1, N):
            if current_h[i] > current_h[i-1] + 1:
                current_h[i] = current_h[i-1] + 1
        
        # 右から左へのパス: x[i] <= x[i+1] + 1
        for i in range(N - 2, -1, -1):
            if current_h[i] > current_h[i+1] + 1:
                current_h[i] = current_h[i+1] + 1
                
        # 操作回数の計算
        # 元の高さの合計 - 修正後の高さの合計
        ops = sum(rlist) - sum(current_h)
        results.append(ops)

    for res in results:
        print(res)

if __name__ == '__main__':
    solve()

