n=int(input())
plist=[]
for i in range(n):
    plist.append(int(input()))

print(sum(plist)-max(plist)//2)