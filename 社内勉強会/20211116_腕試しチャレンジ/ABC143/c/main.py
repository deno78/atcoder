n=int(input())
s=input()

a=[s[0]]
c=s[0]
for i in range(1,n):
    if s[i]!=c:
        c=s[i]
        a.append(c)

print(len(a))

