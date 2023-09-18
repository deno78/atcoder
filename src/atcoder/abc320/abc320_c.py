# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1
import itertools

# param
m = int(input())
s1 = input()
s2 = input()
s3 = input()

ss=[]
ss.append(s1+s1)
ss.append(s2+s2)
ss.append(s3+s3)

# solve
d1={}
d2={}
d3={}

for i in range(10):
    d1[i]=[]
    d2[i]=[]
    d3[i]=[]

for i in range(m):
    c1=int(s1[i])
    c2=int(s2[i])
    c3=int(s3[i])
    d1[c1].append(i)
    d2[c2].append(i)
    d3[c3].append(i)

chk=[]
for i in range(10):
    if len(d1[i])>0 and len(d2[i])>0 and len(d3[i])>0:
        chk.append(str(i))

ans = float("INF")

for c in chk:
    for l in list(itertools.permutations([0,1,2])):
        t=0
        p=0
        for i in l:
            p2=ss[i].index(c,p)
            t+=(p2-p)+1
            p=p2+1
            p%=m
        ans=min(ans,t-1)


        



# answer
if ans==float("INF"):
    ans=-1
print("{}".format(ans))
