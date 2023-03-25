import math
nd = input('').split()
n = int(nd[0])
d = int(nd[1])

xlist = []
for i in range(n):
    xs = list(map(int,input('').split()))
    xlist.append(xs)

# 1件づつ検査する
cnt=0
for i in range(n):
    x1 = xlist[i]
    for j in range(i,n):
        # 全部の組み合わせについて調べる。
        if i!=j:
            x2 = xlist[j]
#            print("{} / {}".format(x1,x2))
            s=0 # 距離
            # 各次元の要素について二乗して加算する
            for k in range(d):
                s+=(x1[k]-x2[k])**2
            # 平方根をとる
            r=math.sqrt(s)
#            print("{}->{}".format(s,r))
            # 整数かどうか、を調べる
            if r.is_integer():
                cnt+=1

print(cnt)