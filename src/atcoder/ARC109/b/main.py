
n=int(input())
# あまった長さN+1の棒からどれだけ端材を作れるか、という方向

left=0
right=n
while left<=right:
    mid=(left+right)//2
    # 中央値の長さで作れる丸太の数(1..x)の本数を求める
    mid_value=mid*(1+mid)//2
    #print("l:{}-m:{}-r:{} : v:{}/n:{}".format(left,mid,right,mid_value,n+1))
    if n+1<mid_value:
        right=mid-1
    elif n+1>mid_value:
        left=mid+1
    else:
        break


n1=mid*(1+mid)//2
if n1 > n+1:
    print(n-mid+2)
else:
    print(n-mid+1)


#4 -> 5,4,3 -> [1,2],3,4