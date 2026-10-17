import sys
import math

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    Q = int(input_data[1])
    
    A = [int(x) for x in input_data[2:2+N]]
    
    # P: A の累積和 (1-indexed, P[0] = 0)
    P = [0] * (N + 1)
    for i in range(N):
        P[i + 1] = P[i] + A[i]
        
    # PP: P の累積和 (1-indexed, PP[0] = 0)
    PP = [0] * (N + 1)
    for i in range(N):
        PP[i + 1] = PP[i] + P[i + 1]
        
    def get_sum(K):
        if K <= 0:
            return 0
        # m*(m+1)//2 <= K を満たす最大の m
        m = (math.isqrt(8 * K + 1) - 1) // 2
        r = K - m * (m + 1) // 2
        return PP[m] + P[r]

    idx = 2 + N
    out = []
    for _ in range(Q):
        L = int(input_data[idx])
        R = int(input_data[idx + 1])
        idx += 2
        ans = get_sum(R) - get_sum(L - 1)
        out.append(str(ans))
        
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    solve()
