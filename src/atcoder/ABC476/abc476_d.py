n,m,k=map(int,input().split())
x,y=map(int,input().split())
alist=list(map(int,input().split()))
blist=list(map(int,input().split()))

import bisect

# 同じ個数を選ぶなら、価格の安い商品を選ぶのが最適
alist.sort()
blist.sort()

# デザートの累積価格を作る
aprefix = [0]
for price in alist:
	aprefix.append(aprefix[-1] + price)

# ドリンクの累積価格と、必要なK円紙幣の累積枚数を作る
bprefix = [0]
kcoin_prefix = [0]
for price in blist:
	bprefix.append(bprefix[-1] + price)
	kcoin_prefix.append(kcoin_prefix[-1] + (price + k - 1) // k)

total_money = x + k * y
answer = 0
# ドリンクを安い順に何個買うかを全探索する
for drink_count in range(m + 1):
	if kcoin_prefix[drink_count] > y:
		break

	remaining_money = total_money - bprefix[drink_count]
	# 残った予算で買えるデザート数を二分探索する
	dessert_count = bisect.bisect_right(aprefix, remaining_money) - 1
	answer = max(answer, drink_count + dessert_count)

print(answer)

