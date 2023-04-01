n,x,y=map(int,input().split())

lv_a=n
lv_b=n-1
cnt_a=1
cnt_b=0

while lv_b!=1:
    lv_b=lv_a
    cnt_a+=x
    cnt_a-=1
    lv_a-=1
    lv_b-=1
    cnt_b+=cnt_a*y

print(cnt_b)
