# TODO edit the code

# param
n,m = map(int,input().split())

n=n%12
a=(n*60+m)*360/(12*60)
b=m*360/60

ans=min(abs(a-b),360-abs((a-b)))
# answer
print(ans)
