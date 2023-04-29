import bisect
import math
def prime(n):
    ret=[]
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(2 * i, n + 1, i):
                is_prime[j] = False
    for i in range(n):
        if is_prime[i]:
            ret.append(i)
    return ret


n=int(input())

primes=prime(int(n**0.5))

ans=0
for i in range(len(primes)-2):
    for j in range(i+1,len(primes)):
        if primes[i]**2*primes[j]*primes[i+1]**2 > n:
            break
        for k in range(j+1,len(primes)):
            if primes[i]**2*primes[j]*primes[k]**2 > n:
                break
            else:
                ans+=1
print(ans)
