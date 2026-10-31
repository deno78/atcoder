import sys
from bisect import bisect_left, bisect_right

# 高速に入力を読み込む
input = sys.stdin.read

def main():
    data = input().split()
    if not data:
        return
    
    h = int(data[0])
    w = int(data[1])
    n = int(data[2])
    q = int(data[3])
    
    idx = 4
    rows = []
    cols = []
    for _ in range(n):
        rows.append(int(data[idx]))
        cols.append(int(data[idx + 1]))
        idx += 2
        
    # それぞれ昇順ソート
    rows.sort()
    cols.sort()
    
    ans = []
    for _ in range(q):
        s = int(data[idx])
        p1 = int(data[idx + 1])
        p2 = int(data[idx + 2])
        idx += 3
        
        if s == 1:
            # p1 <= r <= p2 を満たす点の個数
            cnt = bisect_right(rows, p2) - bisect_left(rows, p1)
            ans.append(str(cnt))
        elif s == 2:
            # p1 <= c <= p2 を満たす点の個数
            cnt = bisect_right(cols, p2) - bisect_left(cols, p1)
            ans.append(str(cnt))
            
    print('\n'.join(ans))

if __name__ == '__main__':
    main()