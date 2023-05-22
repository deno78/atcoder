# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
s = input()
n = int(input())

# solve
elist=[]

l=0
sz1=len(s)
while s.find("?",l)!=-1:
    idx=s.index("?",l)
    val=2**(sz1-idx-1)
    elist.append(val)
    l=idx+1
sz=len(elist)
#print(edict)

a=int(s.replace("?","0"),2)
elist.sort(reverse=True)
for v in elist:
    if (a+v)<=n:
        a+=v
# answer
if a>n:
    print(-1)
else:
    print(a)