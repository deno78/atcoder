n=int(input())
for i in range(int(n**0.5)+2):
    if i**2>n:
        print((i-1)**2)
        exit()