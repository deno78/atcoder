n = int(input(''))

nummap = {}

for i in range(n):
    ab = input('')
    a = int(ab.split(' ')[0])
    b = int(ab.split(' ')[1])
    for j in range(a,b+1):
        if not j in nummap.keys():
            nummap[j] = 0
        nummap[j]=nummap[j]+1

print(nummap)
import statistics
if len(nummap.keys())%2!=0:
    median = statistics.median(nummap.keys())
    print(nummap[median])
else:
    medians = statistics.median(nummap.keys())
    total = 0
    for m in medians:
        total+=nummap[m]

    print(total)