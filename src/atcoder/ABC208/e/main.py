n,k=map(int,input().split())

x=1
for i in range(len(str(n))):
    x*=9
    if x>k:        
        break

print(x)
for i in range(1,9):
    if x*i>k:
        break
    else:
        x*=i
print(x)
