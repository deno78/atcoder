n=int(input())
for i in range(100):
    if 2**i > n:
        print(2**(i-1))
        exit()

