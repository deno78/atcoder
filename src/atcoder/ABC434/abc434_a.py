w,b=map(int,input().split())
ans=0
while True:
    if b*ans>w*1000:
        print(ans)
        exit()
    ans+=1

