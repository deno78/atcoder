n = int(input(''))
k = int(input(''))

x=1
for i in range(n):
    x1 = x*2
    x2 = x+k
    x=min(x1,x2)

print(x)
