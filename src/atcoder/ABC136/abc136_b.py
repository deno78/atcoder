n=int(input(''))

cnt=0 # 件数
# N以下の正の整数＝1からNまで
for i in range(1,n+1):
    # iを文字列にして、2で割ったあまりが1なら奇数
    if len(str(i))%2==1:
        cnt+=1 # カウントアップ

print(cnt)