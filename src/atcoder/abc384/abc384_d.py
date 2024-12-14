# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,s = map(int, input().split())
alist = list(map(int, input().split()))

sum_alist=sum(alist)
s2=s%sum_alist
d2=s//sum_alist
#print("{}={}*{}+{}".format(s,d2,sum_alist,s2))
# solve
blist=[]
b=0
blist.append(0)
for i in range(n):
    b+=alist[i]
    blist.append(b)
for i in range(n):
    b+=alist[i]
    blist.append(b)
#print(blist)
f=0
t=1
while t<len(blist) and f<len(blist)-1:
    wk=blist[t]-blist[f]
    wk+=d2*sum_alist
#    print("{}-{}={} [{}]".format(f,t,wk,n))
    if wk==s:
        print("Yes")
        exit()
    elif wk>s:
        f+=1
    elif wk<s:
        t+=1

# answer
print("No")