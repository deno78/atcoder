import math
n=int(input())
xlist=list(map(int,input().split()))

ans1=0
ans2=0
ans3=0
for x in xlist:
    ax=abs(x)
    ans1+=ax
    ans2+=ax**2
    ans3=max(ans3,ax)

print(ans1)
print(math.sqrt(ans2))
print(ans3)
