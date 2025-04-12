from collections import deque

n,k=map(int,input().split())

DIV=10**9

aist=[1]*k

if n<=k:
    print(1)
    exit()

ans=0
for i in range(0,n-k+1):
  ans+=(i+1)
  print("[{}] {}".format(i,ans))

print(ans%DIV)

#a4=a3+a2
#  =a1+a2+a0+a1
#  =+a0+a0+a1+a1+a1 2/3 

#a5=a4+a3
#  =a3+a2+a1
#  =a1+a2+a0+a1+a1
#  =+a0+a0+a1+a1+a1+a1 2/4

#a6=a5+a4
#  =+a0+a0+a1+a1+a1+a1 2/4
#  =+a0+a0+a1+a1+a1 2/3 
#  =4/7