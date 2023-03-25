# TODO edit the code

# param
n = int(input())
alist=list(map(int,input().split()))
blist=list(map(int,input().split()))


# solve
ans1 = 0
ans2 = 0

for i in range(n):
    for j in range(n):
        if i!=j:
            if alist[i]==blist[j]:
                ans2+=1
        else:
            if alist[i]==blist[j]:
                ans1+=1
# answer
print(ans1)
print(ans2)