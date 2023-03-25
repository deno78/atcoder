s=input()
t=input()

c=0
for i in range(len(s)):
    if s[i]!=t[i]:
        if c==0 and s[i+1]==t[i] and s[i]==t[i+1]:
            c=1
        elif c==1 and s[i-1]==t[i] and s[i]==t[i-1]:
            c=1
        else:
            print('No')
            exit()

print('Yes')
