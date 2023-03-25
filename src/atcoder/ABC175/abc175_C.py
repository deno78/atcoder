xkd = input('').split()
x = int(xkd[0])
k = int(xkd[1])
d = int(xkd[2])

if x > k*d:
    # 届かない場合は極力近づく
    print(x-(k*d))
elif x < k*d and x > (k-1)*d:
    # ぎりぎり０をまたげるパターン
    x1 = x - k*d
    x2 = x - (k-2)*d
    # またぐか、2つ前か、の2択
    if abs(x1) > abs(x2):
        print(abs(x2))
    else:
        print(abs(x1))
else:
    # それ以降
    # 目的地を求める
    step1 = int(x//d) # 目的地までのステップ数
    a1 = x - step1*d # 目的地
#    print("step1:{} a1:{}".format(step1,a1))
    # 0を突き抜けたほうが目的地のケース
    if abs(a1) > abs(a1-d):
        a1 = a1-d
        step1 +=1
#        print("step1:{} a1:{}".format(step1,a1))
    if (k-step1)%2 == 0:
        # 残ステップが偶数ならぴったり
        a2 = a1
    else:
        # 残ステップが奇数なら1個余分に移動
        if abs(a1-d) > abs(a1+d):
            a2 = a1+d
        else:
            a2 = a1-d
    print(abs(a2))
