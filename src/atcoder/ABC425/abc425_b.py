n=int(input())
alist=list(map(int,input().split()))

wk=[]
wk2=[]
for a in alist:
    if a!=-1:
        if a in wk:
            print("No")
            exit()
        wk.append(a)
for i in range(1,n+1):
    if i not in wk:
        wk2.append(i)

ans=[]
for i in range(n):
    if alist[i]==-1:
        ans.append(str(wk2.pop(0)))
    else:
        ans.append(str(alist[i]))
print("Yes")
print(" ".join(ans))

