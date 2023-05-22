# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
alist = list(map(int, input().split()))

# solve
add={}
for i in range(1,n):
    if abs(alist[i]-alist[i-1])!=1:
        add[i]=[alist[i-1],alist[i]]

if len(add)==0:
    alists = [str(n) for n in alist]
    print(" ".join(alists))
    exit()

add2={}
for k in add.keys():
    a1,a2=add[k]
    a=[]
    if a1 < a2:
        for i in range(1,a2-a1+1):
            a.append(a1+i)
    else:
        for i in range(1,a1-a2+1):
            a.append(a1-i)
    add2[k]=a


idx=0
ans=[]
for k in add2.keys():
    ans.extend(alist[idx:k])
    ans.extend(add2[k])
    idx=k+1
ans.extend(alist[idx:])
# answer
alists = [str(n) for n in ans]
print(" ".join(alists))
