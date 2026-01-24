import math
import sys
from functools import cmp_to_key

def solve():
    # 高速化のため入力を一括で読み込む
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)

    try:
        n = int(next(iterator))
        q = int(next(iterator))
    except StopIteration:
        return

    dir_by_index = []
    dir_counts = {}

    for _ in range(n):
        x = int(next(iterator))
        y = int(next(iterator))
        # 向きを正規化
        g = math.gcd(abs(x), abs(y))
        dx = x // g
        dy = y // g
        key = (dx, dy)
        dir_by_index.append(key)
        if key in dir_counts:
            dir_counts[key] += 1
        else:
            dir_counts[key] = 1

    # 厳密な偏角ソートのための比較関数
    # v1, v2 は (dx, dy) のタプル
    def compare(v1, v2):
        x1, y1 = v1
        x2, y2 = v2
        
        # 領域（象限のようなもの）で大まかに分類
        # Area 0: [0, pi)  -> 上半平面 (y>0) または 正のX軸 (y=0, x>0)
        # Area 1: pi       -> 負のX軸 (y=0, x<0)
        # Area 2: (pi, 2pi) -> 下半平面 (y<0)
        
        # 下半平面なら Area 2
        if y1 < 0: r1 = 2
        # 負のX軸なら Area 1
        elif y1 == 0 and x1 < 0: r1 = 1
        # それ以外は Area 0
        else: r1 = 0
            
        if y2 < 0: r2 = 2
        elif y2 == 0 and x2 < 0: r2 = 1
        else: r2 = 0
        
        if r1 != r2:
            return r1 - r2
        
        # 同じ領域なら外積で比較
        # cross_product = x1*y2 - x2*y1
        # 正なら反時計回り (v1 -> v2)、つまり v1 < v2
        cp = x1 * y2 - x2 * y1
        if cp > 0:
            return -1 # v1 < v2
        if cp < 0:
            return 1  # v1 > v2
        return 0

    # 重複を除いた方向キーのリストを作成し、偏角順にソート
    unique_dirs = list(dir_counts.keys())
    unique_dirs.sort(key=cmp_to_key(compare))

    # 累積和と、各方向がソート済みリストの何番目かのマッピングを作成
    prefix = [0]
    dir_to_idx = {}
    for idx, key in enumerate(unique_dirs):
        prefix.append(prefix[-1] + dir_counts[key])
        dir_to_idx[key] = idx
    
    m = len(unique_dirs)
    res = []
    
    for _ in range(q):
        a = int(next(iterator)) - 1
        b = int(next(iterator)) - 1
        
        key_a = dir_by_index[a]
        key_b = dir_by_index[b]
        
        idx_a = dir_to_idx[key_a]
        idx_b = dir_to_idx[key_b]
        
        # 時計回りなので、インデックスが小さくなる方向へ進む
        if idx_a >= idx_b:
            # 配列上で idx_b ... idx_a の範囲
            cnt = prefix[idx_a+1] - prefix[idx_b]
        else:
            # 配列をまたぐ場合: idx_b ... end と start ... idx_a
            cnt = (prefix[m] - prefix[idx_b]) + prefix[idx_a+1]
        
        res.append(str(cnt))

    sys.stdout.write("\n".join(res) + "\n")

if __name__ == '__main__':
    solve()
