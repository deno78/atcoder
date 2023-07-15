# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
slist=[]
for i in range(n):
    slist.append(input())

sdict={}
for i in range(n):
    s1=slist[i]
    if s1 in sdict.keys():
        sdict[s1]+=1
    else:
        s2="".join(reversed(list(s1)))
        if s2 in sdict.keys():
            sdict[s2]+=1
        else:
            sdict[s1]=1

# solve
# answer
print(len(sdict.keys()))
