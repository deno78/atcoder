def cmb(a,mod):
    x=1
    # 組合せの数を1個づつ減らして乗算
    # その時に、10**9+7で割って数字を小さくしながら進める
    for i in range(a):
        x=x*(a-i)%mod
    return x

nm = input().split()
n=int(nm[0])
m=int(nm[1])

# 差が1より大きい場合は交互に並べられない
if abs(n-m)>1:
    print(0)
    exit(0)

# 割る数
MOD=10**9+7

c1 =cmb(n,MOD) # 犬の組合せ数
c2 =cmb(m,MOD) # 猿の組合せ数
if n==m:
    # 同数の場合はひっくり返しても可
    # ABAB ←→ BABA
    print((c1*c2*2)%MOD)
else:
    # 1つ多い場合は、多い方が両端で固定される。
    # ABABA
    print((c1*c2)%MOD)
