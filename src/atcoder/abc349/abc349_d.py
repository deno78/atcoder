# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
l,r = map(int, input().split())

# solve
ans=[]
wk=[]
wk.append(l)
while len(wk)>0:
    l1=wk.pop(0)
    i=0
    while l1%2==0:
        r2=2**(i+1)*(l1//2+1)
        if r2>r:
            break
        i+=1
        l1=l1//2
    l2=2**i*l1
    r2=2**i*(l1+1)
#    print("# {} {}".format(l2,r2))
    ans.append([l2,r2])
    if r2>=r:
        break
    wk.append(r2)

# answer
print(len(ans))
for l1,r1 in ans:
    print("{} {}".format(l1,r1))