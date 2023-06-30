o=input()
e=input()

ans=[]
for i in range(len(o)+len(e)):
    if i%2==0:
        c=o[i//2]
    else:
        c=e[i//2]
    ans.append(c)

print("".join(ans))