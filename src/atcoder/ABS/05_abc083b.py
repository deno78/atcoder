nab = input('')
n = int(nab.split(' ')[0])
a = int(nab.split(' ')[1])
b = int(nab.split(' ')[2])

total = 0
for i in range(1,n+1):
    istr = str(i)
    s = 0
    for j in range(len(istr)):
        s += int(istr[j])
    if s >= a and s <= b:
        total+=i
print(total)