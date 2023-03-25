
def make_divisors(n):
    # 大小2つのリストを作る
    lower_divisors , upper_divisors = [], []

    # i=1からnの平方根までループ
    i = 1
    while i*i <= n:
        # nをiで割り切れたら小リストに追加
        if n % i == 0:
            lower_divisors.append(i)
            # その相方も大リストに追加
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


n=50000

print(make_divisors(n))
