# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,m = map(int, input().split())
r=[]
for i in range(n):
    r.append([-1,-1])

for i in range(m):
    a,b,c,d=input().split()
    a=int(a)-1
    c=int(c)-1
    if b=="R":
        r[a][0]=c
    else:
        r[a][1]=c
    if d=="R":
        r[c][0]=a
    else:
        r[c][1]=a
# solve
checked=[0]*n
ans1=0
ans2=0
for i in range(n):
    if checked[i]==0:
        g=[i]
        wk=[i]
        chained=True
        while len(wk)>0:
            w=wk.pop(0)
            n1=r[w][0]
            n2=r[w][1]
            if n1==-1 or n2==-1:
                chained=False
            if checked[n1]==0 and n1 != -1:
                checked[n1]=1
                g.append(n1)
                wk.append(n1)
            if checked[n2]==0 and n2 != -1:
                checked[n2]=1
                g.append(n2)
                wk.append(n2)
        if chained:
            ans1+=1
        else:
            ans2+=1
    

# answer
print("{} {}".format(ans1,ans2))