import math

def calc(x):
    return math.floor(a*x/b) - a*math.floor(x/b)

a,b,n=map(int,input().split())

# for i in range(n):
#     print(calc(i))

if n>b-1:
    print(calc(b-1))
else:
    print(calc(n))