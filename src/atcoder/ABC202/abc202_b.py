s=input()

s2=[]
for i in range(len(s)):
    c=s[len(s)-i-1]
    if c=='6':
        c='9'
    elif c=='9':
        c='6'
    s2.append(c)

print("".join(s2))