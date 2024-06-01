# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

def popcount(x):
    '''xの立っているビット数をカウントする関数
    (xは64bit整数)'''

    # 2bitごとの組に分け、立っているビット数を2bitで表現する
    x = x - ((x >> 1) & 0x5555555555555555)

    # 4bit整数に 上位2bit + 下位2bit を計算した値を入れる
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)

    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f # 8bitごと
    x = x + (x >> 8) # 16bitごと
    x = x + (x >> 16) # 32bitごと
    x = x + (x >> 32) # 64bitごと = 全部の合計
    return x & 0x0000007f

# param
MOD=998244353
n,m = map(int, input().split())

# solve
x=0
for i in range(61):
    if m>>i&1:
        x=i+1
ans1=[]
ans2=0
for i in range(2**x):
    ret=popcount(i&m)
    ans2+=ret
    ans2%=MOD
    ans1.append(ret)
    print("[{}/{}] {} {}".format(i,2**x,m,ret))
print(ans2)
cnt=n//(2**x)
# print(cnt)
ans=ans2*cnt
ans%=MOD
d=n%(len(ans1))
for i in range(d):
#    print("[{}]+={}".format(i,ans1[i]))
    ans+=ans1[i]
    ans%=MOD
# answer
print("{}".format(ans))
