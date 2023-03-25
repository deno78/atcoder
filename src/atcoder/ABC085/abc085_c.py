ny = input('').split()
n = int(ny[0])
y = int(ny[1])


for i in range(n+1):
    for j in range(n-i+1):
        k = (n-i-j)
        y2 = 10000*i+5000*j+1000*k
        if y2 == y:
            print("{} {} {}".format(i,j,k))
            exit()

print("-1 -1 -1")