# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
s = input()
q = int(input())
f=[0]*n
clist=list(s)
# solve
last=-1
last_idx=0
for i in range(q):
    t,x,c=input().split()
    t=int(t)
    if t==1:
        x=int(x)-1
        clist[x]=c
        f[x]=i
    else:
        last=t
        last_idx=i

# answer
if last==2:
    s=s.lower()
elif last==3:
    s=s.upper()

s2=list(s)
for i in range(n):
    if f[i]>=last_idx:
        s2[i]=clist[i]
    elif last==2:
        s2[i]=clist[i].lower()
    elif last==3:
        s2[i]=clist[i].upper()

print("".join(s2))
