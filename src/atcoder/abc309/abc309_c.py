# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,k = map(int, input().split())
ab={}
days=[]
all=0
for i in range(n):
    a,b = map(int,input().split())
    if a not in ab.keys():
        ab[a]=0
    ab[a]+=b
    days.append(a)
    all+=b

# solve
days=list(set(days))
days.sort()
if all<=k:
    print(1)
    exit()

#print("{} {}".format(1,all))

for d in days:
    all-=ab[d]
#    print("{} {}".format(d+1,all))
    if all<=k:
        print(d+1)
        exit()

