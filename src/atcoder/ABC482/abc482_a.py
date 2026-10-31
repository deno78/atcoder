s=input()
ans=0
for c in s:
    if c=="o":
        ans+=1
if ans%2==0:
    print("even")
else:
    print("odd")