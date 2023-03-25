# TODO edit the code

def check(i):
    return 10**(i+1) - 10**(i)

# param
n = int(input())

MOD=998244353

# solve
ans=0
x2=0
for i in range(len(str(n))-1):
    x1=10**i
    x2=10**(i+1)-1
    ans+=(1+(x2-x1)+1)*(x2-x1+1)//2
    ans%=MOD
#print(ans)
x1=x2+1
x2=n
#print("{}-{}".format(x1,x2))
ans+=(1+(x2-x1)+1)*(x2-x1+1)//2
ans%=MOD

# 1-9 1+2+...9
# 10-16 1+2+3+...6
# 10-99 1+2+...99
# 100-999 1+2+...999
# 10-1 11-2 12-3 13-4 14-5 15-6 16-7

# answer
print(ans)
