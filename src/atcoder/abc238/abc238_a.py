
# TODO edit the code

# param
n = int(input())

# solve
a1=1
a2=n**2

# answer
for i in range(1,n+1):
    a1*=2
    if a1>a2:
        print('Yes')
        exit()

print('No')