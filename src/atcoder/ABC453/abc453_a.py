n=int(input())
s=input()
ans=[]
head=False
for c in list(s):
    if c!="o":
        ans.append(c)
        head=True
    elif head==True:
        ans.append(c)

print("".join(ans))