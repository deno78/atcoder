n,a,b=map(int,input().split())

if a==0:
    print(0)
    exit()

x1=n//(a+b)
x2=n%(a+b)
# print(x1*a)
# print(min(a,x2))
print(x1*a+ min(a,x2))
