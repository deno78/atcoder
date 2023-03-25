n=int(input())
slist=[]
for i in range(n):
    slist.append(input())
cnt=0
acnt=0
bcnt=0
for s in slist:
    cnt+=s.count('AB')
    if s.endswith('A'):
        acnt+=1
    if s.startswith('B'):
        bcnt+=1

if acnt==n:
    acnt-=1
if bcnt==n:
    bcnt-=1

print(cnt+(min(acnt,bcnt)))
