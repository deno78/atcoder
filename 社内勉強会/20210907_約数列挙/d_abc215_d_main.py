
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

n,m=map(int,input().split())
alist=list(map(int,input().split()))

# リストの各値に対して、約数を記録していく
divs=[]
for a in alist:
    divs.extend(make_divisors(a))

# 約数リストから重複を排除する
divs=list(set(divs))

# 約数リストの1個目は1なので消す
divs.remove(1)

# 答えとなる1からMまでのリストを作る
ans=[0]*(m+1)
ans[0]=1

# 約数をNを越えるまで倍々していく
for d in divs:
    for i in range(1,m//d+1):
        # 約数の倍数だったらフラグを立てていく
        ans[i*d]=1

# 答えリストでフラグが立っていない件数を数えて表示
print(ans.count(0))

# 答えリストでフラグが立っていない数を表示
for i in range(len(ans)):
    if ans[i]==0:
        print(i)
