n = int(input(''))
s=0

for i in range(1,n+1):
    if i%3==0 and i%5==0:
        pass
    elif i%3==0 and i%5!=0:
        pass
    elif i%5==0 and i%3!=0:
        pass
    else:
        # 上記以外ならカウントアップ
        s+=i
 
print(s)
