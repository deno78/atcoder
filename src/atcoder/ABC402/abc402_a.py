s=input()
ans=[]
for c in s:
    if c.isupper():
        ans.append(c)

print("".join(ans))