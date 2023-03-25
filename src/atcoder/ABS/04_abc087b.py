a = int(input(''))
b = int(input(''))
c = int(input(''))
x = int(input(''))

cnt=0

for i in range(a+1):
    for j in range(b+1):
        for k in range(c+1):
            money = 500*i + 100*j + k*50
            print("{} + {} + {} = {}".format(i,j,j,money))
            if money == x:
                cnt+=1

print(cnt)
