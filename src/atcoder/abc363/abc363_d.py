# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
n-=1
# solve
i=0
while n>0:
    i+=1
    x=10**i-1
    if n-x<0:
        print(n)
        exit()
    n-=x


# answer
