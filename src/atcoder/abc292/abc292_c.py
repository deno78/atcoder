# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

# param
n = int(input())

# solve
ans=0

cache={}

for ab in range(1,n//2+1):
    cd = n-ab
    p1=-1
    p2=-1    
    if ab in cache.keys():
        p1=cache[ab]
    else:
        p1=len(make_divisors(ab))
    if cd in cache.keys():
        p2=cache[ab]
    else:
        p2=len(make_divisors(cd))
    #print("{}[{}]+{}[{}]".format(ab,p1,cd,p2))
    if ab==cd:
        ans+=(p1*p2) 
    else:
        ans+=(p1*p2)*2
# answer
print(ans)