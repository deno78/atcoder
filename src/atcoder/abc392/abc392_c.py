# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
plist = list(map(int, input().split()))
qlist = list(map(int, input().split()))

# solve
pdict={}
qdict={}
for i in range(n):
    p=plist[i]
    q=qlist[i]
    pdict[i+1]=p
    qdict[q]=i+1

#print(pdict)
#print(qdict)
ans=[]
for i in range(1,n+1):
    x=qdict[i]
    p=pdict[x]
    q=qlist[p-1]
#    print("[{}] {}->{}->{}".format(i,x,p,q))
    ans.append(str(q))

# answer
print(" ".join(ans))