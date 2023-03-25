# TODO edit the code

# param
n = int(input())
alist=list(map(int,input().split()))

ans=0
p=0 # 位置
s=0 # 歩数
m=0 # その途中での最大値:


for i in range(n):
    s+=alist[i]
    m=max(m,s)
    ans=max(ans,p+m)
    p+=s
    # print("[{}] step:{} max:{} pos:{}".format(i,s,m,p))


print(ans)
