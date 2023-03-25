s1=input()
s2=input()
s3=input()
t=input()

ans=""
for c in list(t):
    if c=='1':
        ans+=s1
    elif c=='2':
        ans+=s2
    elif c=='3':
        ans+=s3

print(ans)