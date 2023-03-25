
def divisor(n): 
    cnt=0
    i = 1
    while i**2 <= n:
        if n%i == 0:
            if i==n//i:
                cnt+=1
            else:
                cnt+=2
        i += 1
    return cnt



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
result=0
for c in range(1,n):
    n2 = n-c
    div = divisor(n2)
    print("{}->{}".format(n2,div))
    result+=div
#    fact = make_divisors(n2)
#    print(fact)
#    result+=len(fact)

print(result)