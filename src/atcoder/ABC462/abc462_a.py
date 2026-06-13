s=input()
ans=[]
for c in list(s):
    if c in "0123456789":
        ans.append(c)
print("".join(ans))