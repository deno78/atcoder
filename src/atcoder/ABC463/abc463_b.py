n,x=input().split()
n=int(n)
slist=[]
for i in range(n):
    slist.append(input())

idx="ABCDE".index(x)

for i in range(n):
    s=slist[i]
    if s[idx]=="o":
        print("Yes")
        exit()
print("No")