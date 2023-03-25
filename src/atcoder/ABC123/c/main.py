n=int(input())
tlist=[]
for i in range(5):
    tlist.append(int(input()))
if n%min(tlist)==0:
    print(n//min(tlist)+4)
else:
    print(n//min(tlist)+1+4)