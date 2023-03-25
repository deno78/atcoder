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


n = int(input(''))
cnt=2

sumlist=[]
x=0
for i in range(n):
    x=x+i
    sumlist.append(x)

#
# print(sumlist)
print(cnt)

# n*(n+1)/2
