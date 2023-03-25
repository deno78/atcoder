def make_divisors2(n):
    cnt=1
    for i in range(1,n):
        if n%i==0:
            cnt+=1
    return n*cnt

n = int(input())

result = 0
for i in range(1, n+1):
    result += make_divisors2(i)
print(result)
