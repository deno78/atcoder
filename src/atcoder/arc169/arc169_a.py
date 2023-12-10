# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
alist = list(map(int, input().split()))
plist = list(map(int, input().split()))

pdict={}
for i in range(n):
    pdict[i]=[]
for i in range(n-1):
    p=plist[i]
    p-=1
    pdict[p].append(i+1)
ans=0

wk=[]
wk.append(0)
chk=[0]*n

a0=0

while len(wk)>0:
    w=wk.pop(0)
    a0+=alist[w]
    chk[w]=1
    for x in pdict[w]:
        wk.append(x)
    pdict[w]=[]

for k,v in pdict.items():
    if len(v)==0 and chk[k]>0:
#        print("{} {} {}".format(k,v,alist[k]))
        ans+=alist[k]*chk[k]

# answer
if ans>0:
    print("+")
elif ans<0:
    print("-")
else:
    if a0>0:
        print("+")
    elif a0<0:
        print("-")
    else:
        print("0")
