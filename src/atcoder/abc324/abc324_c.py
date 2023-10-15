# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,t = input().split()
n=int(n)
slist=[]
for i in range(n):
    s=input()
    slist.append(s)

# solve
ans=[]
for j in range(n):
    s=slist[j]
    l1=len(s)
    l2=len(t)
    if abs(l1-l2)<2:
        d=0
        i1=0
        i2=0
        while i1<l1 and i2<l2:
#            print("[{}] {} {} {}".format(j,s[i1],t[i2],d))
            if s[i1]==t[i2]:
                i1+=1
                i2+=1
            else:
                if l1>l2:
                    i1+=1
                elif l1<l2:
                    i2+=1
                else:
                    i1+=1
                    i2+=1
                d+=1
        if d<=1:
            ans.append(str(j+1))

print(len(ans))
print(" ".join(ans))