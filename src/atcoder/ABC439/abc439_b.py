n=int(input())
history=set()
history.add(n)
while True:
    x=0
    for c in str(n):
        x+=int(c)**2
    n=x
    if n==1:
        break
    if n in history:
        break
    history.add(n)
#print(history)
if n==1:
    print("Yes")
else:
    print("No")