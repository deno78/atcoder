# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1
import itertools

# param
a,b, C = map(int, input().split())
cnt=bin(C).count("1")
if (a+b)<cnt:
    print(-1)
    exit()
if (a+b-cnt)%2!=0:
    print(-1)
    exit()

w=(a+b-cnt)//2
alist=[]
blist=[]
for i in range(a-w):
    alist.append(1)
    blist.append(0)
for i in range(b-w):
    blist.append(1)
    alist.append(0)
for i in range(w):
    alist.append(1)
    blist.append(1)
# print(list(reversed(alist)))
# print(list(reversed(blist)))

x=0
for i in range(len(alist)):
    if alist[i]==1:
        x+=2**i
y=0
for i in range(len(blist)):
    if blist[i]==1:
        y+=2**i
print("{} {}".format(x,y))