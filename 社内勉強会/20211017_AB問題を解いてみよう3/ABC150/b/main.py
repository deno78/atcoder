n=int(input())
s=input()

i=0
c=0
while i < n:
    if s.find('ABC',i)>-1:
        i=s.index('ABC',i)
        c+=1
        i+=1
    else:
        break
print(c)
