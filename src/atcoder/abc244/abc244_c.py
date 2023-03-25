# TODO edit the code

# param
n = int(input())

L=2*n+1

a=[]
for i in range(L):
    a.append(i+1)

while len(a)>0:
    print(a.pop())
    y=int(input())
    a.remove(y)
