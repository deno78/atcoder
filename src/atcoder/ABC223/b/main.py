s=input()
l=[]
for i in range(len(s)):
    l.append(s[i:] + s[0:i])
print(min(l))
print(max(l))
