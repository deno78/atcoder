from collections import Counter

s = '1234'
cnt = Counter(s)
for i in range(112,1000,8):
    print("[{}]:{} -> {}".format(i,Counter(str(i)),Counter(str(i)) - cnt) )
    if not Counter(str(i)) - cnt:
        print('Yes')
