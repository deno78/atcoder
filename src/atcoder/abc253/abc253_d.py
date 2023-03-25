# TODO edit the code
import math

# param
n,a,b=map(int,input().split())

# solve
all=n*(1+n)//2

ab=a*b//math.gcd(a,b)

an=n//a
bn=n//b
abn=n//ab
al=an*a
bl=bn*b
abl=abn*ab

a_all=an*(a+al)//2
b_all=bn*(b+bl)//2
ab_all=abn*(ab+abl)//2

# answer
#print(all)
print(all-a_all-b_all+ab_all)


# 9 2 4
# 1 2 3 4 5 6 7 8 9
# 1   3   5   7   9