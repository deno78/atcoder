# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
wxs=[]
for i in range(n):
    w,x = map(int, input().split())
    wxs.append([w,x])

# solve
ans=0
for s in range(0,50):
    wk=0
    for j in range(n):
        w,x=wxs[j]
        s2=(s+x)%24
        t2=s2+1
        if 9<=s2 and t2<=18:
            wk+=w
#        print("\t[{}-{}] [{}-{}] {}".format(s,s+1,s2,t2,wk))
#    print("[{}-{}] {}".format(s,s+1,s2,t2,wk))
    ans=max(ans,wk)
# answer
print("{}".format(ans))
