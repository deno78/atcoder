s=input()

abc=list('abcdefghijklmnopqrstuvwxyz')

for c in list(s):
    abc.remove(c)

if len(abc)==0:
    ans=""
    for i in range(len(s)):
        c=s[i]
        if c not in s[:i] and 
    print(-1)    
else:
    print(s+abc[0])