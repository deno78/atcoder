nm = input('').split()
n = int(nm[0])
m = int(nm[1])
results = [0]*(n+1)
results[0]=1
results[1]=1

for i in range(m):
    a = int(input(''))
    results[a]-=1

MOD=1000000007


for i in range(2,n+1):
    if results[i]==-1:
        results[i] = 0
    else:
        results[i] = results[i-1] + results[i-2]

#print(results)
print(results[-1]%MOD)