import math
n = int(input(''))
s = input('')

c = 0
r=0
g=0
b=0

for i in range(n):
    if s[i] == 'R':
        r+=1
    if s[i] == 'G':
        g+=1
    if s[i] == 'B':
        b+=1

print(r*g*b)
