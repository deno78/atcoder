xab = input().split()
x=int(xab[0])
a=int(xab[1])
b=int(xab[2])

# 賞味期限内
if a >= b:
    print('delicious ')
# 賞味期限は切れているが、消費期限内
elif b-a <= x:
    print('safe ')
else:
# 消費期限を越えたらアウト
    print('dangerous ')
