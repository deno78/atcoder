# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

def check(x):
    ary=list(str(x))
    for i in range(1,len(ary)):
        if ary[i]>=ary[i-1]:
            return False
    return True

# param
k = int(input())

# solve
dp=[0]*9

ans=[]
for i in range(2**10):
    bag=[]
    for j in range(10):
        if i>>j&1:
            bag.append(str(j))
    bag.sort(reverse=True)
    if len(bag)>0:
        ans.append(int("".join(bag)))

ans.sort()

print(ans[k])