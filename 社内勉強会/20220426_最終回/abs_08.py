n=int(input())
dlist=[]
for i in range(n):
    dlist.append(int(input()))

print(len(list(set(dlist))))