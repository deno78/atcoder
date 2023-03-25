nst = input().split()
n=int(nst[0])
s=int(nst[1])
t=int(nst[2])

cnt=0
w=int(input())
if w >=s and w <= t:
    cnt+=1
for i in range(n-1):
    a = int(input())
    w+=a
    if w >=s and w <= t:
        cnt+=1
print(cnt)
