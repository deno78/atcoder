# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
s = input()
clist = list(map(int, input().split()))

# solve
ans = float("INF")

for i in range(1,n):
    s1=[]
    s2=[]
    for j in range(n):
        if j<i:
            s1.append(j%2)
            s2.append((j+1)%2)
        elif j==i:
            s1.append((j+1)%2)
            s2.append(j%2)
        elif j>i:
            s1.append((j+1)%2)
            s2.append(j%2)
    # print(s1)
    # print(s2)
    wk1=0
    wk2=0
    for j in range(n):
        if s[j]!=str(s1[j]):
            wk1+=clist[j]
        if s[j]!=str(s2[j]):
            wk2+=clist[j]
    ans=min(ans,wk1,wk2)

# answer
print("{}".format(ans))

