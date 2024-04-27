# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
alist = list(map(int, input().split()))
l=[]
for i in range(n):
    a=alist[i]
    l.append(a)
#    print("#[{}] {} {}".format(i,a,l))
    while True:
        if len(l)<=1:
            break
        if l[-1]!=l[-2]:
            break
        if l[-1]==l[-2]:
            a1=l.pop(-1)
            a2=l.pop(-1)
            l.append((a1+1))
#    print("#[{}] {} {}".format(i,a,l))

# solve
# answer
print("{}".format(len(l)))
