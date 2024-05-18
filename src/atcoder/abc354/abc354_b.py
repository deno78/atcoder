# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
sc=[]
t=0
for i in range(n):
    s, c = input().split()
    sc.append(s)
    t+=int(c)
sc.sort()
# solve
print(sc[t%n])

# answer
