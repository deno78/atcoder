# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())

# solve
while True:
    s=str(n)
    n1=int(s[0])
    n2=int(s[1])
    n3=int(s[2])
    if n1*n2==n3:
        print(n)
        exit()
    n+=1
