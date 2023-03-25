# TODO edit the code

# param
s=input().split()
t=input().split()

c=0
for i in range(3):
    if s[i]!=t[i]:
        c+=1

ans=-1
if c==0:
    ans=0
elif c==2:
    ans=1
elif c==3:
    ans=2

# answer
if ans%2==0:
    print("Yes")
else:
    print('No')

# R G B
# 2 R B G -> R G B[1]
# 3 G B R -> R B G R[1] -> R G B[2]