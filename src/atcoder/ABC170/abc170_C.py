xn = input('')
x = int(xn.split(' ')[0])
n = int(xn.split(' ')[1])
ps = list(map(int,input().split()))

max_width = 2*x

result = x
for i in range(max_width):
    x1 = x-i
    x2 = x+i
    if x1 not in ps:
        result = x1
        break
    if x2 not in ps:
        result = x2
        break

print(result)

