n=int(input())

stlist=[]
for i in range(n):
    stlist.append(input())

if len(set(stlist))!= len(stlist):
    print('Yes')
else:
    print('No')
