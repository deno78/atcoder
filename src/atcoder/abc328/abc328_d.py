# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1
from collections import deque

# param
s = input()

# solve

q = deque([])

for i in range(len(s)):
    c=s[i]
    q.append(c)
    if len(q)>=3:
        if q[-1]=="C" and q[-2]=="B" and q[-3]=="A":
            q.pop()
            q.pop()
            q.pop()

# answer
print("".join(list(q)))
