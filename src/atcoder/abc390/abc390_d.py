# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1
import copy

def calc(lst):
    if lst.count(0)==len(lst):
        return
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i==j:
                continue
            l1=lst[i]
            l2=lst[j]
            lst[i]+=l1+l2
            lst[j]=0
            val=0
            for a in lst:
                val^=a
            ans.add(val)
            calc(lst)
            lst[i]+=l1
            lst[j]+=l2
            
# param
n = int(input())
alist = list(map(int, input().split()))

# solve
ans = set([])

wk=[]
wk.append(alist)
val=0
for a in alist:
    val^=a
ans.add(val)
#print("{} => {}".format(alist,val))

while len(wk)>0:
    w=wk.pop(0)
    for i in range(len(w)):
        for j in range(len(w)):
            w2=copy.deepcopy(w)
            if i==j:
                continue
            w2[i]+=w2[j]
            w2.pop(j)
            val=0
            for a in w2:
                val^=a
            ans.add(val)
#W            print("{} => {}".format(w2,val))
            if len(w2)>2:
                wk.append(w2)

# answer
print("{}".format(len(ans)))
