# TODO edit the code

# param
h,w=map(int,input().split())
r,c=map(int,input().split())

# solve
ans = 4
if h==r:
    ans-=1
if w==c:
    ans-=1
if r==1:
    ans-=1
if c==1:
    ans-=1
    
# answer
print(ans)
