# TODO edit the code

# param
n = int(input())
slist = list(input())
wlist=list(map(int,input().split()))

wdic0={}
wdic1={}
for i in range(n):
    w=wlist[i]
    s=slist[i]
    if s=="0":
        if w not in wdic0:
            wdic0[w]=0
        wdic0[w]+=1
    elif s=="1":
        if w not in wdic1:
            wdic1[w]=0
        wdic1[w]+=1

wlist2=list(set(wlist))
wlist2.sort()
#print(wdic0)
#print(wdic1)
w0=0
w1=0
w0_all=slist.count("0")
w1_all=slist.count("1")

ans=max(w0_all,w1_all)
for w in wlist2:
    if w in wdic0.keys():
        w0+=wdic0[w]
    if w in wdic1.keys():
        w1+=wdic1[w]
    ans1=w0+w1_all-w1
#    ans2=w1+w0_all-w0
#    print("[{}] {}/{} {}".format(w,w0,w1,ans1,ans2))
    ans=max(ans,ans1)

# answer
print(ans)


# 30 40 45 60 80
#  0  1  2  2  2
#  3  3  3  2  1

