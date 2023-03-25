n  = int(input(''))

s = 0
for i in range(n):
    ab = input('').split()
    a = int(ab[0])
    b = int(ab[1])
    s+=int((a+b)*(b-a+1)/2)

print(s)
