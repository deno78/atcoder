n=int(input())

a=[0]*n
for i in range(n):
    j=int(input())-1
    a[j]=a[j]+1

if 0 not in a:
    print("Correct")
else:
    x=a.index(0)+1
    y=a.index(2)+1
    print("{} {}".format(y,x))