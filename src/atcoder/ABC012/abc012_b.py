n=int(input())

# 時間=60分 x 60秒で割って、引く
h=n//(60*60)
n-=h*60*60
# 分=60秒で割って、引く
m=n//60
n-=m*60
# 残りを秒として表示、先頭ゼロ埋め書式に注意
print("{:0>2}:{:0>2}:{:0>2}".format(h,m,n))
