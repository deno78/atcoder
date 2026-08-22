s=input()

ans=[]
for c in list(s):
    if c=="A":
        ans.append(c)
    else:
        ans.append(".")
print("".join(ans))