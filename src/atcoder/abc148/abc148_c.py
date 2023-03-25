import math
# TODO edit the code

# param
a,b = map(int,input().split())


# answer
print(a*b//math.gcd(a,b))
