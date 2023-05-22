n=int(input())

n2=0
for c in list(str(n)):
    n2+=int(c)

if n%n2==0:
    print("Yes")
else:
    print("No")