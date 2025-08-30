n=int(input())
slist=[]
for i in range(n):
    slist.append(input())
x,y=input().split()
if slist[int(x)-1]==y:
    print("Yes")
else:
    print("No")