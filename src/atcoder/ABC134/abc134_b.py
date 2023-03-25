import math
nd = input('').split()
n = int(nd[0])
d = int(nd[1])
# 監視員は自分のいる場所と前後dの範囲だけカバーできる
print(math.ceil(n/(d*2+1)))