n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))

for i in range(1,n):
    if a[i]>a[i-1]:
        print("up {}".format(a[i]-a[i-1]))
    elif a[i] <a[i-1]:
        print("down {}".format(a[i-1]-a[i]))
    else:
        print("stay")

