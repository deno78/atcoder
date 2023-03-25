H,W=map(int,input().split())
h,w=map(int,input().split())

ans=H*W
ans-=H*w
ans-=h*W
ans+=h*w
print(ans)