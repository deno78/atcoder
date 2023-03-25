hmk = input('')

h1 = int(hmk.split(' ')[0])
m1 = int(hmk.split(' ')[1])
h2 = int(hmk.split(' ')[2])
m2 = int(hmk.split(' ')[3])
k = int(hmk.split(' ')[4])

min1 = h1*60 + m1
min2 = h2*60 + m2

if min1 > min2:
    min2+=60*24

a = min2 - min1 - k
print(a)