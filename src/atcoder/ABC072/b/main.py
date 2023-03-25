s=input()

a=[]
for i in range(len(s)):
    if i%2==0:
        a.append(s[i])
print("".join(a))