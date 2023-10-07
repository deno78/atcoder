# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,m = map(int, input().split())
alist=list(map(int,input().split()))
slist=[]
for i in range(n):
    s = input()
    slist.append(s)

ALL=sum(alist)
wk={}
g=0
for i in range(n):
    s=slist[i]
    w=[]
    c=ALL+i+1
    for j in range(m):
        a=alist[j]
        if s[j]=="x":
            w.append(a)
            c-=a
    w.sort(reverse=True)
    wk[i]=[c,w]
    g=max(g,c)
    w.insert(0,0)
# solve
for x in wk.values():
    c=x[0]
    w=x[1]
    for i in range(len(w)):
        c+=w[i]
        if c>=g:
            print(i)
            break

# answer
