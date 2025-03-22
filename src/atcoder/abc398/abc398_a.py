n=int(input())
ans=[]
x=(n-1)//2
ans=["-"]*x
if n%2==0:
    ans.append("==")
else:
    ans.append("=")
ans.extend(["-"]*x)
print("".join(ans))