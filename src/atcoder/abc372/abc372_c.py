# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,q = map(int, input().split())
s = input()
xc=[]
for i in range(q):
    x,c=input().split()
    x=int(x)
    x-=1
    xc.append([x,c])

# solve
ans=s.count("ABC")
s=list(s)
for i in range(q):
    x=xc[i][0]
    c=xc[i][1]
    wk1=0
    for j in range(3):
        if x-j+2<len(s) and x-j>=0:
#            print("{} {} {}".format(s[x-j],s[x-j+1],s[x-j+2]))
            if s[x-j]=="A" and s[x-j+1]=="B" and s[x-j+2]=="C":
                wk1+=1
    s[x]=c
    wk2=0
    for j in range(3):
        if x-j+2<len(s) and x-j>=0:
#            print("{} {} {}".format(s[x-j],s[x-j+1],s[x-j+2]))
            if s[x-j]=="A" and s[x-j+1]=="B" and s[x-j+2]=="C":
                wk2+=1
    ans-=wk1
    ans+=wk2
    print(ans)

# answer
