from itertools import combinations

n = int(input(''))
xylist=[]

for i in range(n):
    xylist.append(list(map(int,input().split())))

# 各町間の距離の合計
ans=0
# xylistから2つ取る組合せ
for a,b in combinations(xylist,2):
    # a,b間の距離を足す
    ans+=((abs(a[0]-b[0]))**2 + (abs(a[1]-b[1])**2) )**0.5

# 距離の合計を往復分でx2して、町の数で割る
print(float(2*ans/n))